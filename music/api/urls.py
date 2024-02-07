from django.urls import path
from .views import MusicBase64View, MusicDetailAPIView, MusicListAPIView, AlbumListAPIView, AlbumDetailAPIView

urlpatterns = [
    path("", MusicListAPIView.as_view()),
    path("<int:pk>/base64/", MusicBase64View.as_view()),
    path("<int:pk>/", MusicDetailAPIView.as_view()),
    path("album/", AlbumListAPIView.as_view()),
    path("album/<int:pk>", AlbumDetailAPIView.as_view())
]
