"""`songs` app views."""

from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from songs.models import Album, Author, MusicLabel, Song
from songs.serializers import (
    AlbumSerializer,
    AuthorSerializer,
    MusicLabelSerializer,
    SongCreateSerializer,
    SongDetailSerializer,
)


# Create your views here.
class MusicLabelModelViewSet(ModelViewSet):
    """`MusicLabelModelViewSet`."""

    queryset: QuerySet[MusicLabel] = MusicLabel.objects.all()
    serializer_class: type[MusicLabelSerializer] = MusicLabelSerializer


class AuthorModelViewSet(ModelViewSet):
    """`AuthorModelViewSet`."""

    queryset: QuerySet[Author] = Author.objects.all()
    serializer_class: type[AuthorSerializer] = AuthorSerializer


class AlbumModelViewSet(ModelViewSet):
    """`AlbumModelViewSet`."""

    queryset: QuerySet[Album] = Album.objects.all()
    serializer_class: type[AlbumSerializer] = AlbumSerializer


class SongModelViewSet(ModelViewSet):
    """`SongModelViewSet`."""

    queryset: QuerySet[Song] = Song.objects.all()
    serializer_class: type[SongDetailSerializer] = SongDetailSerializer

    def get_serializer_class(  # noqa: WPS615
        self,
    ) -> SongDetailSerializer | SongCreateSerializer:
        """`get_serializer_class` method.

        When request type is `POST` it returns `SongCreateSerializer` instead of `SongDetailSerializer`
        """
        if self.action == 'create':
            self.serializer_class = SongCreateSerializer

        return super().get_serializer_class()
