from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())


class RegistrationForm(UserCreationForm):
    is_artist = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "is_artist")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_artist = self.cleaned_data['is_artist']

        if commit:
            user.save()
        return user
