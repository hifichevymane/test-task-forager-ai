"""`Songs` app enums.

Stores all enums, models from `Songs` app use
"""

from enum import StrEnum, auto
from typing import Literal


class AlbumType(StrEnum):
    """`AlbumType` enum.

    Represents all types of `Album` model
    """

    ALBUM = auto()  # noqa: WPS115
    EP = auto()  # noqa: WPS115
    SINGLE = auto()  # noqa: WPS115
    COMPILATION = auto()  # noqa: WPS115

    @classmethod
    def choices(cls) -> list[tuple[str, Literal['ALBUM', 'EP', 'SINGLE', 'COMPILATION']]]:  # noqa: WPS234
        """`choices` classmethod.

        Returns `list` of the `AlbumType` enum values
        """
        return [(key.value, key.name) for key in cls]
