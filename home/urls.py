from .views import HomeView, AboutUsView
from django.urls import path


app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about-us/", AboutUsView.as_view(), name="about_us")
]
