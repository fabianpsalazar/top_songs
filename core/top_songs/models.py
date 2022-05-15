
from django.db import models

# Create your models here.


class Track(models.Model):

    track = models.IntegerField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    kind = models.CharField(max_length=5)
    content_advisory_rat = models.CharField(max_length=255)
    artwork_url100 = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_track = models.ManyToManyField(Track, related_name='genres')
    genreId = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    genre_url = models.URLField()

    def __str__(self):
        return self.genreId


class Artist(models.Model):
    artist_track = models.ManyToManyField(Track, related_name='artist')
    artistId = models.CharField(max_length=255,  unique=True)
    artist_name = models.CharField(max_length=255)
    artist_url = models.URLField()

    def __str__(self):
        return self.artist_name

