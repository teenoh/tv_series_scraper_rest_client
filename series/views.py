from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .serializers import SeriesSerializer, SeasonSerializer, EpisodeSerializer
from .models import Series, Seasons, Episodes
from django.http import JsonResponse

# Create your views here.

class SeriesViewSet(viewsets.ModelViewSet):
    '''
    This is the viewset for the Series model
    '''
    queryset = Series.objects.all().order_by('name')
    serializer_class = SeriesSerializer
    
    

class SeasonViewSet(viewsets.ModelViewSet):
    '''
    This is the viewset for the Season model
    '''
    queryset = Seasons.objects.all().order_by('name')
    serializer_class = SeasonSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    '''
    This is the viewset for the Episode model
    '''
    queryset = Episodes.objects.all().order_by('name')
    serializer_class = EpisodeSerializer

def index(request, series_name, season_name, episode_name):
    
    series = Series.objects.get(name=series_name.replace("-", " "))
    season = Seasons.objects.get(name=season_name.replace("-", " "), series=series)
    episode = Episodes.objects.get(name=episode_name.replace("-", " "), season = season)
    key = series_name + ' ' + season_name + ' ' + episode_name 
    return JsonResponse({str(episode): episode.download_link})

def all_series_view(request):
    series = {x.name: x.image_url for x in Series.objects.all()}
    return JsonResponse({'result': series})

def series_view(request, series_name):
    '''
        Returns basic data for each series 
        eg
        {
            name: arrow,
            season_count: 5,
            episodes_count: {
                season 01: 20,
                season 02: 23
                ...
                season 05: 30
            }
        }
    '''
    series_name = series_name
    
    series_object = Series.objects.get(name=series_name)
    season_count = series_object.seasons.count()
    episode_count = {season.name: season.episodes.count() for season in Seasons.objects.filter(series=series_object)}
    return JsonResponse({'name': series_name,
                         'season_count': season_count,
                         'episodes_count': episode_count  })
    

