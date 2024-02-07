from django.contrib import admin
from django.utils.html import format_html
from music.models import Music, Category, Album, PlaylistSong, LikedSong
from django.templatetags.static import static


class MusicAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "duration")
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "listens", "thumbnail")
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name", "year", "file", "duration", "category")},
        ),
        (
            "INFO",
            {
                "fields": (
                    "description",
                    ("image", "cover_image", "thumbnail"),
                    "created_at",
                    "is_published",
                    "listens",

                )
            },
        ),
    )

    @staticmethod
    def thumbnail(obj):
        return format_html(
            "<img src='{}' class='thumbnail'>",
            obj.image.url if obj.image else static("img/no_image.jpeg"),
        )


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    readonly_fields = ("thumbnail",)
    fieldsets = (

        (
            "GENERAL",
            {"fields": ("name", "category", "music")},
        ),
        (
            "INFO",
            {
                "fields": (
                    "description",
                    ("image", "thumbnail"),


                )
            },
        ),
    )

    @staticmethod
    def thumbnail(obj):
        return format_html(
            "<img src='{}' class='thumbnail'>",
            obj.image.url if obj.image else static("img/no_image.jpeg"),
        )


class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name",)
    readonly_fields = ("thumbnail",)
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name", "user", "music")},
        ),
        (
            "INFO",
            {
                "fields": (
                    ("image", "thumbnail"),
                )
            },
        ),
    )

    @staticmethod
    def thumbnail(obj):
        return format_html(
            "<img src='{}' class='thumbnail'>",
            obj.image.url if obj.image else static("img/no_image.jpeg"),
        )


admin.site.register(Music, MusicAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(PlaylistSong, PlaylistSongAdmin)
admin.site.register(Category)
admin.site.register(LikedSong)
