from .views import MusicDetailView
from django.urls import path


app_name = "music"

urlpatterns = [
    path("detail/<int:pk>/", MusicDetailView.as_view(), name="detail"),

]
