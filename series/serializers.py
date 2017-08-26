from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields= ('name', 'download_link')

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = ('name', 'episodes')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('name', 'seasons')


