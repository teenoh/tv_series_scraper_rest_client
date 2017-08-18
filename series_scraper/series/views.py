from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .serializers import SeriesSerializer
from .models import Series, Seasons, Episodes
# Create your views here.

class SeriesViewSet(viewsets.ModelViewSet):
    '''
    This si the viewset for the Series model
    '''
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

