# from django.shortcuts import render
from .models import Music
from django.views.generic import DetailView


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "music"
