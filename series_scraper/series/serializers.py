from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('name', '')

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Seasons
        fields = ('name', 'episodes')

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields= ('name', 'download_link')

