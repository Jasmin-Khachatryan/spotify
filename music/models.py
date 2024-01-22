from django.db import models
from helpers.upload_image import upload_music_image, upload_music_cover_image


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to=upload_music_image, null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_music_cover_image, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name="music")
    is_published = models.BooleanField(default=True)
    duration = models.DurationField()
    listens = models.IntegerField(default=0)
    file = models.FileField(upload_to="music/", null=True, blank=True)

    def __str__(self):
        return self.name
