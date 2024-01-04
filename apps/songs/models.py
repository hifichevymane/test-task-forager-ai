from datetime import datetime  # noqa: D100

from core.models import TimeStampedModel
from django.db import models
from songs.enums import AlbumType


# Create your models here.
class MusicLabel(TimeStampedModel):
    """`MusicLabel` model.

    This model represents a music label instance.

    Arguments
    ---------
    name: `models.CharField`
        Name of music label
    """

    name = models.CharField(max_length=128, blank=False, null=False)  # noqa: WPS432

    def __str__(self) -> str:
        """`__str__` func.

        String representation of a model instance.
        """
        return self.name


class Author(TimeStampedModel):
    """`Author` model.

    This model represents an author instance

    Arguments
    ---------
    name: `models.CharField`
        Author's name

    description: `models.TextField`
        Author's description
    """

    name = models.CharField(max_length=128, blank=False, null=False)  # noqa: WPS432
    description = models.TextField()

    def __str__(self) -> str:
        """`__str__` func.

        String representation of a model instance.
        """
        return self.name


class Album(TimeStampedModel):
    """`Album` model.

    This model represents album instance.

    Arguments
    ---------
    name: `models.CharField`
        The name of an album

    author: `models.ForeignKey`
        Author's id(`Author` model)

    release_date: `models.DateTimeField`
        The date, when an album was released

    album_type: `models.CharField`
        Type of albums. There are 4 types of albums:
        `ALBUM`, `EP`, `SINGLE`, `COMPILATION`.
        All these values stores in `songs.enums.AlbumType` enum.

    music_label: `models.ForeignKey`
        Music label id(`MusicLabel` model)
    """

    name = models.CharField(max_length=128, blank=False, null=False)  # noqa: WPS432
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_date = models.DateTimeField(blank=False, null=False)
    album_type = models.CharField(
        blank=False,
        null=False,
        default=AlbumType.ALBUM.value,
        choices=AlbumType.choices(),
    )
    music_label = models.ForeignKey(MusicLabel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """`__str__` func.

        String representation of a model instance.
        """
        return f'{self.name} - {self.author}'  # noqa: WPS305


class Song(TimeStampedModel):
    """`Song` model.

    This model represents a song

    Arguments
    ---------
    name: `models.CharField`
        The name of a song

    album: `models.ForeignKey`
        Album id(`Album` model)

    Properties
    ----------
    author: `songs.models.Author`
        Returns the author of a song

    release_date: `datetime`
        Returns the release date of a song

    music_label: `songs.models.MusicLabel`
        Returns the music label of a song
    """

    name = models.CharField(max_length=128, blank=False, null=False)  # noqa: WPS432
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    @property
    def author(self) -> Author:  # noqa: D102
        return self.album.author

    @property
    def release_date(self) -> datetime:  # noqa: D102
        return self.album.release_date

    @property
    def music_label(self) -> MusicLabel:  # noqa: D102
        return self.album.music_label

    def __str__(self) -> str:
        """`__str__` func.

        String representation of a model instance.
        """
        return f'{self.author} - {self.name}'  # noqa: WPS305
