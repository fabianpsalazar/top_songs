from rest_framework import viewsets
from rest_framework.response import Response
from .models import Track, Artist, Genre
from rest_framework import status
from .serializers import TrackSerializer, SongSerializer, GroupByGenreSerializer
from rest_framework.decorators import action
from .json_variables import song_example_format, track_example_format
from rest_framework.permissions import IsAuthenticated


class SongViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = SongSerializer

    @action(detail=True, methods=['get'])
    def get_song(self, request, pk=None):
        song_name = self.queryset.filter(name__icontains=pk)
        if song_name:
            track_serialized = self.serializer_class(song_name, many=True)
            return Response(track_serialized.data, status=status.HTTP_200_OK)
        return Response({
            'Message': 'That song name does not exist dude!'
        }, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False)
    def get_top_50(self, request):
        top_50 = self.queryset[:50]
        top_50_serialized = TrackSerializer(top_50, many=True)
        return Response(top_50_serialized.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post', 'get'])
    def create_song(self, request):
        if request.method == 'POST':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Message': 'Song successfully registered'
                }, status=status.HTTP_201_CREATED)
            return Response({
                'Message': 'Invalid data input'
            }, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            return Response({
                'Message': 'Here you can add an entire new song with new artist and genres!',
                'Example': song_example_format
            }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post', 'get'])
    def create_track(self, request):
        if request.method == 'POST':
            serializer = TrackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Message': 'Track successfully registered'
                }, status=status.HTTP_201_CREATED)
            return Response({
                'Message': 'Invalid data input'
            }, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            return Response({
                'Message': 'Here you can add your track!',
                'Example': track_example_format
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'Message': 'Try with method Get or Post!'
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete_track(self, request, pk=None):
        try:
            track_to_dlt = self.queryset.get(registry=pk).delete()
        except:
            return Response({
                    'Message': 'Enter a valid registry'
                }, status=status.HTTP_204_NO_CONTENT)
        return Response({
            'Message': 'Track Deleted!'
        }, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def get_song_genre(self, request):
        queryset = Genre.objects.all()
        serializer = GroupByGenreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_group_genre(self, request, pk=None):
        queryset = Genre.objects.all().filter(name__icontains=pk)
        serializer = GroupByGenreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
















