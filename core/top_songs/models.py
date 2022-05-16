
from django.db import models

# Create your models here.


class Track(models.Model):

    registry = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    kind = models.CharField(max_length=5)
    content_advisory_rat = models.CharField(max_length=255)
    artwork_url100 = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    track = models.ManyToManyField(Track, related_name='genre')
    registry = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.gen


class Artist(models.Model):
    track = models.ManyToManyField(Track, related_name='artist')
    registry = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.artist_name

