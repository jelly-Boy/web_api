from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'performers', PerformerViewSet, basename='performer')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'music_services', MusicServiceViewSet, basename='music_service')
router.register(r'tracks', TrackViewSet, basename='track')

urlpatterns = [
    path('admin', admin.site.urls)
] + router.urls
