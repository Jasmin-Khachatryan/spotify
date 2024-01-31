from django.contrib import admin
from .models import Artist
from django.utils.html import format_html
from django.templatetags.static import static


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("pseudonym", "first_name", "last_name")
    search_fields = ("pseudonym",)
    list_filter = ("followers",)
    readonly_fields = ("followers", "user", "thumbnail")
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("pseudonym", "first_name", "last_name", "date_of_birth", "gender")},
        ),
        (
            "INFO",
            {
                "fields": (
                    "music",
                    ("image", "cover_image", "thumbnail"),
                    "followers",
                    "user",

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


admin.site.register(Artist, ArtistAdmin)
