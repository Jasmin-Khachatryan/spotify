from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MusicSerializer, AlbumSerializer
from music.models import Music, Album
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MusicBase64View(APIView):
    def get(self, request, pk):
        try:
            music = Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            return Response({"error": "Music not found"}, status=status.HTTP_404_NOT_FOUND)

        if not music.file:
            return Response({"error": "Music file not found"}, status=status.HTTP_404_NOT_FOUND)

        encoded_music = MusicSerializer().encode_file(music)

        return Response({"encoded_music": encoded_music}, status=status.HTTP_200_OK)


class MusicDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    lookup_field = "pk"


class MusicListAPIView(ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class AlbumListAPIView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
