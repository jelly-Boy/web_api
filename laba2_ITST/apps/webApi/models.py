from django.db import models

class Performer(models.Model):
    performer_name = models.CharField(max_length=50, unique=True)
    birthday = models.DateField()

    def __str__(self):
        return self.performer_name

class Album(models.Model):
    album_name = models.CharField(max_length=40, unique=True)
    release_day = models.DateField()
    performer = models.ForeignKey(Performer, models.SET_NULL, to_field='performer_name', default='No performer', null=True)

    def __str__(self):
        return self.album_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.genre_name

class MusicService(models.Model):
    music_service_name = models.CharField(max_length=40, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.music_service_name

class Track(models.Model):
    track_name = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, related_name='g_tracks', null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL,related_name='a_tracks', null=True)
    music_service = models.ManyToManyField(MusicService, related_name='ms_tracks', blank=True)

    def __str__(self):
        return self.track_name
