from .views import HomeView, AboutUsView, FAQView, searchBar
from django.urls import path


app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about-us/", AboutUsView.as_view(), name="about_us"),
    path("FAQ/", FAQView.as_view(), name="FAQ"),
    path("search/", searchBar, name="search"),


]
