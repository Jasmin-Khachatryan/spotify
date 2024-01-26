from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path("user/", include("users.urls", namespace="user")),
    path("music/", include("music.urls", namespace="music")),
    path("artist/", include("artist.urls", namespace="artist")),
    path("premium/", include("payment.urls", namespace="payments")),
    path("__debug__/", include("debug_toolbar.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
