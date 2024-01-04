# noqa: D100 F401
from django.contrib import admin
from songs.models import Album, Author, MusicLabel, Song

# Register your models here.
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(MusicLabel)
admin.site.register(Album)
