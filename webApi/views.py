from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['GET'])
def apiOverview(request):
    api_Urls = {
        'List': '/genre-list/',
        'Detail View': '/genre-detail/<str:pk>/',
        'Create': '/genre-create/',
        'Update': '/genre-update/<str:pk>/',
        'Delete': '/genre-delete/<str:pk>/',
    }
    return Response(api_Urls)

@api_view(['GET'])
def genreList(request):
    genres = Genre.objects.all().order_by('-id')
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genreDetail(request, pk):
    genres = Genre.objects.get(id=pk)
    serializer = GenreSerializer(genres, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def genreCreate(request):

    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def genreUpdate(request, pk):
    genre = Genre.objects.get(id=pk)
    serializer = GenreSerializer(instance=genre, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def genreDelete(request, pk):
    genre = Genre.objects.get(id=pk)
    genre.delete()
    return Response('Item was successfully delete!')

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
