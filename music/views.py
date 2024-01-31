# from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from artist.models import Artist
from .models import Music, Album, PlaylistSong
from django.views.generic import DetailView, ListView, FormView
from .forms import MusicAddForm


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "music"


class LikedMusicView(ListView):
    model = Music
    template_name = "music/likedsong.html"
    context_object_name = "musics"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "albums"


class PlayListView(ListView):
    model = PlaylistSong
    template_name = "music/playlist.html"
    context_object_name = "user_musics"


class AddMusicView(FormView):
    form_class = MusicAddForm
    template_name = "music/add_music.html"
    context_object_name = "form"
    success_url = reverse_lazy("home:home")



# class UpdateMusicView(FormView):
#     template_name = "music/update_music.html"
#     form_class = MusicAddForm
#     success_url = reverse_lazy("home:home")
#
#     def get_form(self, form_class=None):
#         music_id = self.kwargs['pk']  # Assuming your URL includes the music ID as 'pk'
#         music_instance = get_object_or_404(Music, id=music_id)
#         return self.form_class(instance=music_instance, **self.get_form_kwargs())
#
#     def form_valid(self, form):
#         music_id = self.kwargs['pk']
#         music_instance = get_object_or_404(Music, id=music_id)
#
#         # Update the Music instance with the new form data
#         music_instance.name = form.cleaned_data['name']
#         music_instance.category.set(form.cleaned_data['category'])
#         music_instance.artist = form.cleaned_data['artist']
#         music_instance.album = form.cleaned_data['album']
#         music_instance.image = form.cleaned_data['image']
#         music_instance.cover_image = form.cleaned_data['cover_image']
#         music_instance.description = form.cleaned_data['description']
#         music_instance.year = form.cleaned_data['year']
#         music_instance.duration = form.cleaned_data['duration']
#         music_instance.file = form.cleaned_data['file']
#         music_instance.listens = form.cleaned_data['listens']
#
#         music_instance.save()
#
#         return super().form_valid(form)
