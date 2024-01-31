from django.urls import path

from artist.api.views import ArtistListCreateAPIView

urlpatterns = [
    path("", ArtistListCreateAPIView.as_view()),
]
