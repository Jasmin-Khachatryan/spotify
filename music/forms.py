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
                  "year", "duration", "file", "listens")

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter music name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'size': '50'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control',  'size': '50'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter music description', 'size': '50'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'listens': forms.NumberInput(attrs={'class': 'form-control'}),
        }
