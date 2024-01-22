from .views import ArtistDetailView
from django.urls import path


app_name = "artist"

urlpatterns = [
    path("", ArtistDetailView.as_view(), name="artist_detail"),

]
