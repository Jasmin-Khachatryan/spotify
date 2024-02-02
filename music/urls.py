from .views import MusicDetailView, LikedMusicView, AlbumDetailView, PlayListView, AddMusicView, UpdateMusicView, \
    AddToPlaylist, RemoveFromPlaylistView, AddToLikedSongView, RemoveFromLikedSongView, playlist_searchBar, DeleteMusicView
from django.urls import path
app_name = "music"
urlpatterns = [
    path("detail/<int:pk>/", MusicDetailView.as_view(), name="detail"),
    path("liked/<int:pk>/", LikedMusicView.as_view(), name="liked_songs"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("playlists/<int:pk>/", PlayListView.as_view(), name="playlist"),
    path("add-music/", AddMusicView.as_view(), name="add_music"),
    path("edit-music/<int:pk>/", UpdateMusicView.as_view(), name="edit_music"),
    path("add-to-playlist/<int:music_id>/", AddToPlaylist.as_view(), name="add_to_playlist"),
    path("remove-from-playlist/<int:song_id>/", RemoveFromPlaylistView.as_view(), name="remove_from_playlist"),
    path("add-to-liked-song/<int:music_id>/", AddToLikedSongView.as_view(), name="add_to_likedsongs"),
    path("remove-from-liked-song/<int:song_id>/", RemoveFromLikedSongView.as_view(), name="remove_from_likedsongs"),
    path("playlist_search/", playlist_searchBar, name="playlist_search"),
    path("delete_song/<int:pk>/", DeleteMusicView.as_view(), name="delete_song"),

]
