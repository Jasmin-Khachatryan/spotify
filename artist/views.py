# from django.shortcuts import render
from .models import Artist
from django.views.generic import DetailView


class ArtistDetailView(DetailView):
    model = Artist
    template_name = "artist/artist.html"
    context_object_name = "artists"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        return Artist.objects.select_related("user").prefetch_related("music").order_by("pk")



