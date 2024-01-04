# noqa: D100
from rest_framework.viewsets import ModelViewSet
from songs.models import Album, Author, MusicLabel, Song
from songs.serializers import (
    AlbumSerializer, 
    AuthorSerializer, 
    MusicLabelSerializer, 
    SongDetailSerializer, 
    SongCreateSerializer,
)


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
    serializer_class = SongDetailSerializer

    def get_serializer_class(self) -> SongDetailSerializer | SongCreateSerializer:  # noqa: WPS615
        """`get_serializer_class` method.

        When request type is `POST` it returns `SongCreateSerializer` instead of `SongDetailSerializer`
        """
        if self.action == 'create':
            self.serializer_class = SongCreateSerializer

        return super().get_serializer_class()
