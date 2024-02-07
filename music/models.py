from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from helpers.upload_image import upload_music_image, upload_music_cover_image, upload_album_image, upload_playlist_image
from users.models import User


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
    category = models.ManyToManyField(Category, related_name="music")
    is_published = models.BooleanField(default=True)
    duration = models.DurationField()
    listens = models.IntegerField(default=0)
    file = models.FileField(upload_to="music/", null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(upload_to=upload_playlist_image, null=True, blank=True)
    music = models.ManyToManyField(Music, related_name="playlist_music")

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_playlist_song(sender, instance, created, **kwargs):
        if created:
            PlaylistSong.objects.create(user=instance, name="My Playlist")

    @receiver(post_save, sender=User)
    def save_playlist_song(sender, instance, **kwargs):
        instance.playlistsong.save()


class LikedSong(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    music = models.ManyToManyField(Music, related_name="liked_songs")

    def __str__(self):
        return self.user.first_name + "'s Liked Songs"

    @receiver(post_save, sender=User)
    def create_or_update_likedsong(sender, instance, created, **kwargs):
        if created:
            LikedSong.objects.create(user=instance)
        else:
            instance.likedsong.save()


class Album(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    music = models.ManyToManyField(Music, related_name="album_music")
    image = models.ImageField(upload_to=upload_album_image, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
