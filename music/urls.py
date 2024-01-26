from .views import MusicDetailView, LikedMusicView, AlbumDetailView, PlayListView, AddMusicView
from django.urls import path


app_name = "music"

urlpatterns = [
    path("detail/<int:pk>/", MusicDetailView.as_view(), name="detail"),
    path("liked/", LikedMusicView.as_view(), name="liked_songs"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("playlists/", PlayListView.as_view(), name="playlist"),
    path("add-music/", AddMusicView.as_view(), name="add_music")
]


