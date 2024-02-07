from django.contrib import admin
from .views import User
from django.utils.html import format_html
from django.templatetags.static import static


class UserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name")
    search_fields = ("pseudonym",)
    readonly_fields = ("email", "is_artist", "thumbnail", "account", "is_premium_user")
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("email", "password", "first_name", "last_name")},
        ),
        (
            "INFO",
            {
                "fields": (
                    "is_staff",
                    ("image", "thumbnail"),
                    "is_active",
                    "is_artist",
                    "is_premium_user",
                    "account",

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


admin.site.register(User, UserAdmin)
