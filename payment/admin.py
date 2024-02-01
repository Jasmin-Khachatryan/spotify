from django.contrib import admin
<<<<<<< Updated upstream
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name",)
    readonly_fields = ("stripe_id",)
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name", "description")},
        ),
        (
            "INFO",
            {
                "fields": (
                    "price",
                    "stripe_id",

                )
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
=======

from .models import Account

admin.site.register(Account)

>>>>>>> Stashed changes
