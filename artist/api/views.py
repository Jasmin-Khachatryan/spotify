from rest_framework.generics import ListCreateAPIView
from artist.api.serializers import ArtistSerializer
from artist.models import Artist


class ArtistListCreateAPIView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

