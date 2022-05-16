from rest_framework import serializers
from .models import Track, Artist, Genre
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested import UniqueFieldsMixin


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['artistId', 'artist_name', 'artist_url']


class GenreSerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['genreId', 'name', 'genre_url']


class SongSerializer(UniqueFieldsMixin, WritableNestedModelSerializer, serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Track
        fields = ['name', 'track_id', 'release_date', 'kind', 'content_advisory_rat',
                  'artwork_url100', 'artist', 'genres']


class GroupByGenreSerializer(serializers.ModelSerializer):
    genre_track = TrackSerializer(many=True)

    class Meta:
        model = Genre
        fields = ['genreId', 'name', 'genre_url', 'genre_track']












