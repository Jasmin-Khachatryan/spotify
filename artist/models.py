from django.db import models
from helpers.choices import GenderChoice
from helpers.upload_image import upload_artist_image
from music.models import Music


class Artist(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=8, choices=GenderChoice.choices, default="Male")
    image = models.ImageField(upload_to=upload_artist_image, null=True, blank=True)
    music = models.ForeignKey(Music, related_name="artist", on_delete=models.PROTECT)
    followers = models.IntegerField(default=0)
