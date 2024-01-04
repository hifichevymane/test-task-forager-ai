# noqa: D100 F401
from django.contrib import admin
from songs.models import Album, Author, MusicLabel, Song


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """`SongAdmin`.

    Defines parameters for displaying `Django Admin` panel
    """

    readonly_fields = ('author', 'music_label', 'release_date')


admin.site.register(Author)
admin.site.register(MusicLabel)
admin.site.register(Album)
