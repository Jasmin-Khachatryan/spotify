from django import forms
from .models import Music, Category
from users.models import UserProfile

class MusicAddForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    artist = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Music
<<<<<<< HEAD
        fields = ("name", "category", "image", "cover_image", "description",
=======
        fields = ("name", "category", "artist", "album", "image", "cover_image", "description",
>>>>>>> 09e45ad298ffa38e89027e6750a60b24c1d09cda
                  "year", "duration", "file")


