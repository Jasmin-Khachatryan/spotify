from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())


class RegistrationForm(UserCreationForm):
    CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    is_artist = forms.BooleanField(initial=False, required=False, widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2", "is_artist")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_artist = self.cleaned_data['is_artist']

        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name",
                  "email", "image")


class FollowForm(forms.Form):
    artist_id = forms.IntegerField(widget=forms.HiddenInput())


class ArtistProfileForm(ProfileForm):
    cover_photo = forms.ImageField(required=False)
    pseudonym = forms.CharField(max_length=255, required=False)

    class Meta(ProfileForm.Meta):
        fields = ProfileForm.Meta.fields + ("cover_photo", "pseudonym")
