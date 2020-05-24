from django.contrib.auth.models import User, Group, Permission
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['track_name', 'album', 'genre', 'music_service_t']
        extra_kwargs = {'music_service_t': {'required': False}, 'album': {'required': False},
                        'genre': {'required': False}}

class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ['performer_name', 'albums']
        extra_kwargs = {'albums': {'required': False}}

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['album_name', 'performer', 'year_of_release', 'tracks']
        extra_kwargs = {'tracks': {'required': False}}

class MusicServiceSerializer(serializers.ModelSerializer):
    ms_tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = MusicService
        fields = ['music_service_name', 'music_service_url', 'ms_tracks']
        extra_kwargs = {'ms_tracks': {'required': False}}

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name', 'g_tracks']
        extra_kwargs = {'g_tracks': {'required': False}}
