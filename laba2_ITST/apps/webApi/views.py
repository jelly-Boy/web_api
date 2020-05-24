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
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PerformerGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id =None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id =None):
        return self.update(request, id)

    def delete(self, request, id =None):
        self.destroy(request, id)

class GenreGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        self.destroy(request, id)

class AlbumGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        self.destroy(request, id)


class MusicServiceGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MusicServiceSerializer
    queryset = MusicService.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        self.destroy(request, id)

class TrackGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        self.destroy(request, id)
"""
class PerformerViewSet(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['performer_name']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['genre_name']


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['year_of_release']

class MusicServiceViewSet(viewsets.ModelViewSet):
    queryset = MusicService.objects.all()
    serializer_class = MusicServiceSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['track_name']
"""
# Create your views here.
