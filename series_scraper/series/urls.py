from django.conf.urls import url, include

from rest_framework import routers
from .serializers import SeriesViewSet

router = routers.DefaultRouter()
router.register(r'series', SeriesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
