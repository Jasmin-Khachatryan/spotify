# from django.shortcuts import render
from .models import Music, Album
from django.views.generic import DetailView, ListView


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
