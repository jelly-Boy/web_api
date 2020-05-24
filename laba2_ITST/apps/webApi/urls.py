from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Routers provide an easy way of automatically determining the URL conf.

router = DefaultRouter()
router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/performers', PerformerGenericAPIView, basename='performer')
router.register(r'api/tracks', TrackGenericAPIView, basename='track')
router.register(r'api/albums', AlbumGenericAPIView, basename='album')
router.register(r'api/music_services', MusicServiceGenericAPIView, basename='music_service')
router.register(r'api/genres', GenreGenericAPIView, basename='genre')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'webApi'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generic/track/<int:id>', TrackGenericAPIView.as_view()),
    path('generic/music_service/<int:id>', MusicServiceGenericAPIView.as_view()),
    path('generic/performer/<int:id>', PerformerGenericAPIView.as_view()),
    path('generic/genre/<int:id>', GenreGenericAPIView.as_view()),
    path('generic/album/<int:id>', AlbumGenericAPIView.as_view()),

]
"""
   """