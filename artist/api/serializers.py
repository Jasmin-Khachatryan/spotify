from rest_framework import serializers
from artist.models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        exclude = ("image", "cover_image", "music", "user")
