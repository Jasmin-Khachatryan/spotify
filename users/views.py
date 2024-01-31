from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.views.generic import FormView, DetailView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView as Login, LogoutView as Logout
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.conf import settings
from helpers.mixins import OwnProFileMixin
from artist.models import Artist

from .forms import RegistrationForm, ProfileForm, ArtistProfileForm, EmailForm
from .tasks import send_simple_email
from .generate_token import account_activation_token

User = get_user_model()


class EmailView(FormView):
    template_name = "users/send_simple_email.html"
    form_class = EmailForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        body = form.cleaned_data["body"]

        send_simple_email.apply_async(kwargs={"body": body, "subject": subject,
                                              "email": email, "count": 10})
        return response


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = "users/registration.html"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        is_artist = form.cleaned_data.get('is_artist', False)

        if is_artist:
            Artist.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name
            )

        subject = "Authenticate your Profile"
        user.is_active = False
        user.save()
        token = account_activation_token.make_token(user)
        message = render_to_string("users/authentication.html",
                                   {"user": user,
                                    "domain": get_current_site(self.request),
                                    "token": token})
        email = EmailMessage(subject=subject, body=message,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[user.email])
        email.send(fail_silently=False)

        return response


class ValidateUserLink(TemplateView):

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        pk = kwargs.get("pk")
        user = User.objects.get(pk=pk)
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("user:login")
        return HttpResponse("Your token is invalid")


class LoginView(Login):
    template_name = "users/login.html"


class LogoutView(Logout):
    pass


class UserProfileView(DetailView):
    model = User
    context_object_name = "user"

    def get_template_names(self):
        user = self.get_object()
        if user.is_artist:
            return ["users/artist_profile.html"]
        else:
            return ["users/profile.html"]


class UserUpdateView(OwnProFileMixin, UpdateView):
    model = User

    def get_form_class(self):

        if self.request.user.is_artist:
            return ArtistProfileForm
        else:
            return ProfileForm

    def get_initial(self):
        initial = {
            "image": self.object.image
        }

        if self.object.is_artist:
            initial["pseudonym"] = self.object.artist.pseudonym
            initial["cover_photo"] = self.object.artist.cover_image

        return initial

    def form_valid(self, form):
        user_instance = form.save(commit=False)
        user_instance.save()

        if user_instance.is_artist:

            artist_instance, created = Artist.objects.get_or_create(user=user_instance)
            artist_instance.pseudonym = form.cleaned_data.get('pseudonym')
            artist_instance.cover_image = form.cleaned_data.get('cover_photo')
            artist_instance.first_name = form.cleaned_data.get('first_name')
            artist_instance.last_name = form.cleaned_data.get('last_name')
            artist_instance.image = form.cleaned_data.get('image')
            artist_instance.save()

        return super().form_valid(form)

    def get_template_names(self):
        user = self.get_object()
        if user.is_artist:
            return ["users/edit_artist_profile.html"]
        else:
            return ["users/edit_profile.html"]

    def get_success_url(self):
        return reverse("user:profile", kwargs={"pk": self.object.pk})
