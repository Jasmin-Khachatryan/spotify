# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, FormView, UpdateView
from django.views import View
from artist.models import Artist
from .models import Music, Album, PlaylistSong
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

    def get_queryset(self):
        return Album.objects.select_related("category").prefetch_related("music__artists").order_by("pk")


class AddToPlaylist(LoginRequiredMixin, View):
    def post(self, request, music_id):
        music = Music.objects.get(id=music_id)
        if not request.user.playlistsong_set.exists():
            PlaylistSong.objects.create(name="Best Playlist", user=request.user)
        playlist = request.user.playlistsong_set.first()
        playlist.music.add(music)
        return redirect("music:playlist")

class PlayListView(ListView):
    model = PlaylistSong
    template_name = "music/playlist.html"
    context_object_name = "user_musics"

    def get_queryset(self):
        return PlaylistSong.objects.select_related("user").prefetch_related("music__artists").order_by("pk")


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



class UpdateMusicView(UpdateView):
    model = Music
    form_class = MusicAddForm
    template_name = "music/edit_music.html"
    success_url = reverse_lazy("home:home")

    def get_object(self, queryset=None):
        # Retrieve the Music instance to be updated
        return get_object_or_404(Music, pk=self.kwargs['pk'])

    def get_initial(self):
        initial = super().get_initial()

        # Populate initial values for artists, albums, and categories
        initial['category'] = self.object.category.all()
        initial['album'] = self.object.album_music.all()  # Assuming related name is 'album_music'
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

# class UpdatePizzaView(UpdateView):
#     model = Music
#     form_class = PizzaForm
#     template_name = "pizza/update_pizza.html"
#     context_object_name = "form"
#     pk_url_kwarg = "pk"
#
#     def form_valid(self, form):
#         form.save(commit=True)
#         messages.info(self.request, "Pizza was updated successfully!")
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse("pizza_info", kwargs={"pk": self.object.pk})
#
#     def get_queryset(self):
#         return Pizza.objects.all()


# class DeletePizzaView(DeleteView):
#     model = Pizza
#     template_name = "pizza/delete_pizza.html"
#     context_object_name = "pizza"
#     success_url = reverse_lazy("pizzas")
#     pk_url_kwarg = "pk"
#
#     def delete(self, request, *args, **kwargs):
#         messages.error(request, "pizza was deleted successfully!")
#         return super().delete(request, *args, **kwargs)