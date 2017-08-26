from django.conf.urls import url, include

from rest_framework import routers
from .views import SeriesViewSet, SeasonViewSet

router = routers.DefaultRouter()
router.register(r'series', SeriesViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'Episode', SeasonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^series/(?P<series>.+)/(?P<season>.+)/(?P<episode>.+)/', episodes)
    #url('^series/(?P<series_name>.+)', SeriesList.as_view(), name="series_list"),
    # url('^series/(?P<series_name>.+)/(?P<season_name>.+)/$', SeasonList.as_view(), name="season_list")
]
