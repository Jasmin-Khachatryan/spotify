from django import forms
from .models import Music, Category
from users.models import UserProfile

class MusicAddForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    artist = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Music
        fields = ("name", "category", "image", "cover_image", "description",
                  "year", "duration", "file")


