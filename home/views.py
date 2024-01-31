from django.views.generic import TemplateView, ListView
from music.models import Album


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
        albums = Album.objects.prefetch_related("category").all()
        chunked_albums = [albums[i:i + 6] for i in range(0, len(albums), 6)]
        context["chunked_albums"] = chunked_albums
        return context
