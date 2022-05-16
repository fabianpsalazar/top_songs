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
        fields = ['registry', 'name', 'url']


class GenreSerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['registry', 'name', 'url']


class SongSerializer(UniqueFieldsMixin, WritableNestedModelSerializer, serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Track
        fields = ['name', 'registry', 'release_date', 'kind', 'content_advisory_rat',
                  'artwork_url100', 'artist', 'genre']


class GroupByGenreSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True)

    class Meta:
        model = Genre
        fields = ['registry', 'name', 'url', 'track']












