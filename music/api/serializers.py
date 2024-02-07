import base64
from rest_framework import serializers
from music.models import Music, Category, Album, PlaylistSong, LikedSong


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ["name"]


class MusicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    encoded_file = serializers.SerializerMethodField()

    class Meta:
        model = Music
        exclude = ("image", "cover_image", "created_at", "file")

    def get_encoded_file(self, obj):
        if isinstance(obj, list):

            return [self.encode_file(instance) for instance in obj]
        else:
            return self.encode_file(obj)

    def encode_file(self, music_instance):
        if music_instance.file:
            with open(music_instance.file.path, "rb") as file:
                encoded_music = base64.b64encode(file.read()).decode('utf-8')
                return encoded_music
        return None


class AlbumSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Album
        exclude = ("image",)


class PlaylistSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many=True)

    class Meta:
        model = PlaylistSong
        exclude = ("image", "user")


class LikedSongserializer(serializers.ModelSerializer):
    music = MusicSerializer

    class Meta:
        model = LikedSong
        exclude = ("user",)
