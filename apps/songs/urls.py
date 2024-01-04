# noqa: D100
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from songs.views import AlbumModelViewSet, AuthorModelViewSet, MusicLabelModelViewSet, SongModelViewSet

router: SimpleRouter = SimpleRouter()
router.register('songs', SongModelViewSet)
router.register('albums', AlbumModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('music-labels', MusicLabelModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
