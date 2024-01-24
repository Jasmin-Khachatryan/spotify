from django.contrib import admin

from music.models import Music, Category, Album

admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Album)
