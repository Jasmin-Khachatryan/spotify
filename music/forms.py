from django import forms
from .models import Music, Category, Album
from artist.models import Artist


class MusicAddForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    album = forms.ModelChoiceField(queryset=Album.objects.all(), required=False)

    class Meta:
        model = Music
        fields = ("name", "category", "artist", "album", "image", "cover_image", "description",
                  "year", "duration", "file")


