"""`songs` app serializers."""

from typing import Any

from rest_framework import serializers
from songs.models import Album, Author, MusicLabel, Song


class MusicLabelSerializer(serializers.ModelSerializer):
    """`MusicLabel` model serializer.

    Serializer that represents JSON representation of `MusicLabel` model.
    """

    class Meta:  # noqa: WPS306,D106
        model: type[MusicLabel] = MusicLabel
        fields: str | list[str] = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """`Author` model serializer.

    Serializer that represents JSON representation of `Author` model.
    """

    class Meta:  # noqa: WPS306,D106
        model: type[Author] = Author
        fields: str | list[str] = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """`Album` model serializer.

    Serializer that represents JSON representation of `Album` model.
    """

    class Meta:  # noqa: WPS306,D106
        model: type[Album] = Album
        fields: str | list[str] = '__all__'


class SongCreateSerializer(serializers.ModelSerializer):
    """Serializer for `POST` requests to create `Song` instance.

    Serializer that represents JSON representation of `Song` model when create `Song instance`.
    """

    class Meta:  # noqa: WPS306,D106
        model: type[Song] = Song
        fields: str | list[str] = '__all__'


class SongDetailSerializer(SongCreateSerializer):
    """`Song` model serializer.

    Serializer that represents JSON representation of `Song` model.
    """

    author: serializers.ListSerializer | Any | AuthorSerializer = AuthorSerializer()
    music_label: serializers.ListSerializer | Any | MusicLabelSerializer = MusicLabelSerializer()
    album: serializers.ListSerializer | Any | AlbumSerializer = AlbumSerializer()
    release_date: serializers.ReadOnlyField = serializers.ReadOnlyField()
