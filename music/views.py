# from django.shortcuts import render
from .models import Music, Album, PlaylistSong
from django.views.generic import DetailView, ListView

from django.http import JsonResponse

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



