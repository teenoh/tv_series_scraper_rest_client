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