from django.views import View
from django.db.models import Q
from .models import Music, Album, PlaylistSong, LikedSong
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, UpdateView,DeleteView
from artist.models import Artist
from .forms import MusicAddForm
from users.models import User


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "music"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.select_related("category").prefetch_related("music__artists").order_by("pk")


class AddMusicView(FormView):
    form_class = MusicAddForm
    template_name = "music/add_music.html"
    context_object_name = "form"
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        music_instance = form.save()

        artist_id = self.request.POST.get('artist', None)
        if artist_id:
            artist_instance = get_object_or_404(Artist, id=artist_id)
            artist_instance.music.add(music_instance)

        album_id = self.request.POST.get('album', None)
        if album_id:
            album_instance = get_object_or_404(Album, id=album_id)
            album_instance.music.add(music_instance)

        return super().form_valid(form)


def playlist_searchBar(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            playlists = Music.objects.filter(
                Q(name__icontains=query) |
                Q(year__icontains=query)|
                Q(description__icontains=query)
                )
            return render(request, "music/playlist_search.html", {'songs': playlists})
        else:
            return render(request, "music/playlist_search.html", {})


class UpdateMusicView(UpdateView):
    model = Music
    form_class = MusicAddForm
    template_name = "music/edit_music.html"
    success_url = reverse_lazy("user:profile pk=user.id ")

    def get_object(self, queryset=None):

        return get_object_or_404(Music, pk=self.kwargs['pk'])

    def get_initial(self):
        initial = super().get_initial()
        initial['category'] = self.object.category.all()
        initial['album'] = self.object.album_music.all()
        initial['artist'] = self.object.artists.all()

        return initial

    def form_valid(self, form):
        music_instance = form.save()

        artist_id = self.request.POST.get('artist', None)
        if artist_id:
            artist_instance = get_object_or_404(Artist, id=artist_id)
            artist_instance.music.add(music_instance)

        album_id = self.request.POST.get('album', None)
        if album_id:
            album_instance = get_object_or_404(Album, id=album_id)
            album_instance.music.add(music_instance)

        return super().form_valid(form)

class DeleteMusicView(DeleteView):
    model = Music
    success_url = reverse_lazy("user:profile pk=user.id ")
    template_name = "music/confirm_delete.html"

class AddToPlaylist(LoginRequiredMixin, View):
    def post(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        playlist, created = PlaylistSong.objects.get_or_create(user=request.user, defaults={'name': 'Default Playlist'})
        playlist.music.add(music)
        return redirect("music:playlist", pk=request.user.pk)
class RemoveFromPlaylistView(LoginRequiredMixin, View):
    def post(self, request, song_id):
        music = get_object_or_404(Music, id=song_id)
        playlist, created = PlaylistSong.objects.get_or_create(user=request.user)
        if music in playlist.music.all():
            playlist.music.remove(music)
        return redirect("music:playlist", pk=request.user.pk)
class AddToLikedSongView(DetailView):
    def post(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        liked_songs, created = LikedSong.objects.get_or_create(user=request.user,)
        liked_songs.music.add(music)
        return redirect("music:liked_songs", pk=request.user.pk)
class RemoveFromLikedSongView(LoginRequiredMixin, View):
    def post(self, request, song_id):
        music = get_object_or_404(Music, id=song_id)
        liked_songs, created = LikedSong.objects.get_or_create(user=request.user)
        if music in liked_songs.music.all():
            liked_songs.music.remove(music)
        return redirect("music:liked_songs", pk=request.user.pk)


class LikedMusicView(DetailView):
    model = LikedSong
    template_name = "music/likedsong.html"
    context_object_name = "musics"
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        liked_song, created = LikedSong.objects.get_or_create(user=user,)
        return liked_song


class PlayListView(DetailView):
    model = PlaylistSong
    template_name = "music/playlist.html"
    context_object_name = "user_musics"
    pk_url_kwarg = "pk"
    def get_object(self, queryset=None):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        playlist, created = PlaylistSong.objects.get_or_create(user=user, defaults={'name': 'Default Playlist'})
        return playlist