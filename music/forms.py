from django import forms
from .models import Music, Category


class MusicAddForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    artist = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Music
        fields = ("name", "category", "image", "cover_image", "description",
                  "year", "duration", "file")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist'].widget.attrs['readonly'] = True
