from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('name', '')

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields= ('name', 'download_link')


