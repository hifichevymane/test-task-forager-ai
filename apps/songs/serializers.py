# noqa: D100,D106
from rest_framework import serializers
from songs.models import Album, Author, MusicLabel, Song


class SongSerializer(serializers.ModelSerializer):
    """`Song` model serializer.

    Serializer that represents JSON representation of `Song` model.
    """

    class Meta:  # noqa: WPS306,D106
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """`Album` model serializer.

    Serializer that represents JSON representation of `Album` model.
    """

    class Meta:  # noqa: WPS306,D106
        model = Album
        fields = '__all__'


class MusicLabelSerializer(serializers.ModelSerializer):
    """`MusicLabel` model serializer.

    Serializer that represents JSON representation of `MusicLabel` model.
    """

    class Meta:  # noqa: WPS306,D106
        model = MusicLabel
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """`Author` model serializer.

    Serializer that represents JSON representation of `Author` model.
    """

    class Meta:  # noqa: WPS306,D106
        model = Author
        fields = '__all__'
