from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields= ('name', 'download_link')

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Seasons
        fields = ('name', 'episodes')


class SeriesSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)

    class Meta:
        model = Series
        fields = ('name', 'seasons')


