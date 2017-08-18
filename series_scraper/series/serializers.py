from .models import Seasons, Series, Episodes
from rest_framework import serializers, viewsets

class SeriesSerializer(serializers.HyperlinkedModel):
    class Meta:
        model = Series
        fields = ('name', '')

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

