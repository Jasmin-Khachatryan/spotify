# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from music.models import Music


class HomeView(ListView):
    template_name = "home/home.html"
    model = Music
    context_object_name = "musics"
    paginate_by = 6


class AboutUsView(TemplateView):
    template_name = "home/about_us.html"


class FAQView(TemplateView):
    template_name = "home/FAQ.html"


