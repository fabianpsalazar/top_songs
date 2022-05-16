import json
from pathlib import Path
from top_songs.models import Track, Artist, Genre
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        Track.objects.all().delete()
        Artist.objects.all().delete()
        Genre.objects.all().delete()
