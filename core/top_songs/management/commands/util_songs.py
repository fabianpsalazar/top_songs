import json
from pathlib import Path
from top_songs.models import Track, Artist, Genre
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import time


class Command(BaseCommand):
    help = 'Fill data base'

    def handle(self, *args, **options):
        print('Minions are working on, keep calm while they finish it ')
        try:
            with open(Path(__file__).parent / 'songs.json') as file:
                data = json.load(file)

            songs = data["feed"]["results"]
            track = Track()

            for song in songs:
                new_track = Track.objects.create(
                    track_id=song["id"],
                    name=song["name"],
                    release_date=song["releaseDate"],
                    kind='songs',
                    content_advisory_rat=song["contentAdvisoryRating"] if "contentAdvisoryRating" in song else 'nan',
                    artwork_url100=song["artworkUrl100"]
                )
            print('Track table filled!')

            artist_list = []
            for song in songs:
                new_song = Track.objects.get(track_id=song["id"])
                if song["artistName"] not in artist_list:
                    new_artist = Artist.objects.create(
                        artistId=song["artistId"],
                        artist_name=song["artistName"],
                        artist_url=song["artistUrl"])
                    artist_list.append(song["artistName"])
                    new_artist.artist_track.add(new_song)
                else:
                    artist_old = Artist.objects.get(artist_name=song["artistName"])
                    artist_old.artist_track.add(new_song)
            print('Artist table filled!')


            genres_list = []
            for song in songs:
                new_song = Track.objects.get(track_id=song["id"])
                for genre in song["genres"]:
                    if genre["genreId"] not in genres_list:
                        new_genre = Genre.objects.create(
                            genreId=genre["genreId"],
                            name=genre["name"],
                            genre_url=genre["url"])
                        genres_list.append(genre["genreId"])
                        new_genre.genre_track.add(new_song)
                    else:
                        genre_old = Genre.objects.get(genreId=genre["genreId"])
                        genre_old.genre_track.add(new_song)

            print('Opps Fatal error ... deleting database')
            time.sleep(3)
            print('Nahh im just kidding, Genre table filled!')

            if User.objects.get(username='admin'):
                print('username:admin exists!, password: admin')
            else:
                User.objects.create_superuser(username='admin', password='admin')
                print('username: admin, password: admin')
        except:
            print('Delete tables first with: manage.py delete_songs')



