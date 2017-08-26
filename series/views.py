from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .serializers import SeriesSerializer, SeasonSerializer, EpisodeSerializer
from .models import Series, Seasons, Episodes
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