# noqa: D100
from rest_framework.viewsets import ModelViewSet
from songs.models import Album, Author, MusicLabel, Song
from songs.serializers import AlbumSerializer, AuthorSerializer, MusicLabelSerializer, SongSerializer


# Create your views here.
class MusicLabelModelViewSet(ModelViewSet):
    """`MusicLabelModelViewSet`."""

    queryset = MusicLabel.objects.all()
    serializer_class = MusicLabelSerializer


class AuthorModelViewSet(ModelViewSet):
    """`AuthorModelViewSet`."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AlbumModelViewSet(ModelViewSet):
    """`AlbumModelViewSet`."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongModelViewSet(ModelViewSet):
    """`SongModelViewSet`."""

    queryset = Song.objects.all()
    serializer_class = SongSerializer
