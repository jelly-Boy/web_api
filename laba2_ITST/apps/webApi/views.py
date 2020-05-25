from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import *
from rest_framework import filters
from rest_framework import routers, serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PerformerViewSet(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MusicServiceViewSet(viewsets.ModelViewSet):
    queryset = MusicService.objects.all()
    serializer_class = MusicServiceSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
