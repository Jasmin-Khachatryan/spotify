from .views import ArtistDetailView
from django.urls import path


app_name = "artist"

urlpatterns = [
    path("<int:pk>/", ArtistDetailView.as_view(), name="artist_detail"),

]
