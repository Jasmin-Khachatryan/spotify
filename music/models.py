from django.db import models
from helpers.upload_image import upload_music_image, upload_music_cover_image, upload_album_image
from users.models import User
# from artist.models import Artist


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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_youtube_id = models.CharField(max_length=20)
    song_albums = models.CharField(max_length=255)
    song_dur = models.CharField(max_length=7)
    song_channel = models.CharField(max_length=100)
    song_date_added = models.CharField(max_length=12)

    def __str__(self):
        return f"Title = {self.song_title}, Date = {self.song_date_added}"


class Album(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    music = models.ManyToManyField(Music, related_name="album_music")
    image = models.ImageField(upload_to=upload_album_image, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
