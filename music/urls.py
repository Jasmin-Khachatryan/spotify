from .views import MusicDetailView, LikedMusicView
from django.urls import path


app_name = "music"

urlpatterns = [
    path("detail/<int:pk>/", MusicDetailView.as_view(), name="detail"),
    path("liked/", LikedMusicView.as_view(), name="liked_songs"),

]
