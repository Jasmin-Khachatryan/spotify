# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.views import LoginView as Login
from django.contrib.auth.views import LogoutView as Logout
from django.conf import settings
from .forms import EmailForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, ProfileForm
from .models import UserProfile
from helpers.mixins import OwnProFileMixin


# from .generate_token import account_activation_token

User = get_user_model()


class EmailView(FormView):
    template_name = "users/send_simple_email.html"
    form_class = EmailForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        send_mail(subject, body, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email])
        return response

# class RegistrationView(CreateView):
#     form_class = RegistrationForm
#     model = User
#     success_url = '/'
#     template_name = "users/registration.html"
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         subject = "Authenticate your Profile"
#         user = self.object
#         user.is_active = False
#         token = account_activation_token.make_token(user)
#         message = render_to_string("users/authentication.html",
#                                    {"user": user,
#                                     "domain": get_current_site(self.request),
#                                     "token": token})
#         email = EmailMessage(subject=subject, body=message,
#                              from_email=settings.EMAIL_HOST_USER,
#                              to=[user.email])
#         email.send(fail_silently=False)
#
#         return response


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)

        return response


class LoginView(Login):
    template_name = "users/login.html"


class LogoutView(Logout):
    pass


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "user"


class UserUpdateView(OwnProFileMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "users/edit_profile.html"

    def get_initial(self):
        return {
                "image": self.object.image}

    def get_success_url(self):

        return reverse("user:profile", kwargs={"pk": self.object.pk})


