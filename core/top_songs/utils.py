from .models import Track, Artist, Genre
import json
from pathlib import Path

with open(Path(__file__).parent/'songs.json') as file:
    data = json.load(file)


songs = data["feed"]["results"]
track = Track()
artist = Artist()


def save_song():
    for song in songs:
        track.track = song["id"]
        track.name = song["name"]
        track.release_date = song["releaseDate"]
        track.kind = 'songs'
        if "contentAdvisoryRating" in song:
            track.content_advisory_rat = song["contentAdvisoryRating"]
        else:
            track.content_advisory_rat = 'nan'
        track.artwork_url100 = song["artworkUrl100"]
        track.save()


def save_artist():
    artist_list = []
    for song in songs:
        new_song = Track.objects.get(track=int(song["id"]))
        if song["artistName"] not in artist_list:
            new_artist = Artist.objects.create(
                artistId=song["artistId"],
                artist_name=song["artistName"],
                artist_url=song["artistUrl"])
            artist_list.append(song["artistName"])
            new_artist.save()
            new_artist.artist_track.add(new_song)
        else:
            artist_old = Artist.objects.get(artist_name=song["artistName"])
            artist_old.artist_track.add(new_song)
            artist.save()


def save_genres():
    genres_list = []
    for song in songs:
        new_song = Track.objects.get(track=int(song["id"]))
        for genre in song["genres"]:
            if genre["genreId"] not in genres_list:
                new_genre = Genre.objects.create(
                    genreId=genre["genreId"],
                    name=genre["name"],
                    genre_url=genre["url"])
                genres_list.append(genre["genreId"])
                new_genre.save()
                new_genre.genre_track.add(new_song)
            else:
                genre_old = Genre.objects.get(genreId=genre["genreId"])
                genre_old.genre_track.add(new_song)
                Genre().save()