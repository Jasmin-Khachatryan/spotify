# from django.shortcuts import render

from django.views.generic import TemplateView


class ArtistDetailView(TemplateView):

    template_name = "artist/artist.html"
