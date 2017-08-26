from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episodes
        fields= ('name', 'download_link', 'season')

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seasons
        fields = ('name', 'episodes', 'series')


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('name', 'seasons')


