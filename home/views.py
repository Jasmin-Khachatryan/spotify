# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from music.models import Album
from django.core.paginator import Paginator
from django.db.models import Prefetch


# class HomeView(ListView):
#     template_name = "home/home.html"
#     model = Music
#     context_object_name = "musics"
#     paginate_by = 6


class AboutUsView(TemplateView):
    template_name = "home/about_us.html"


class FAQView(TemplateView):
    template_name = "home/FAQ.html"


class HomeView(ListView):
    template_name = "home/home.html"
    model = Album
    context_object_name = "albums"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all albums with related category
        albums = Album.objects.prefetch_related('category').all()

        # Organize albums into chunks of 6
        chunked_albums = [albums[i:i + 6] for i in range(0, len(albums), 6)]

        context['chunked_albums'] = chunked_albums
        return context