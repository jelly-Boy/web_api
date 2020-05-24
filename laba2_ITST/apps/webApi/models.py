from django.db import models

class Performer(models.Model):
    performer_name = models.CharField(max_length=50)

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    performer = models.ForeignKey(Performer, related_name='albums', on_delete=models.CASCADE, blank=True)
    year_of_release = models.DateField()

class MusicService(models.Model):
    music_service_name = models.CharField(max_length=30)
    music_service_url = models.URLField()

class Track(models.Model):
    track_name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.DO_NOTHING, null=True)
    genre = models.ForeignKey(Genre, related_name='g_tracks', on_delete=models.DO_NOTHING, null=True)
    music_service_t = models.ManyToManyField(MusicService, related_name='ms_tracks', null=True)
# Create your models here.
