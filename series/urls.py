from django.conf.urls import url, include

from rest_framework import routers
from .views import SeriesViewSet, SeasonViewSet, EpisodeViewSet, index, all_series_view, series_view

router = routers.DefaultRouter()
router.register(r'series', SeriesViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^all_series/$', SeriesViewSet.as_view({'get': 'list'}), name="detail"),
    #url(r'^all_series/(?P<series_name>.+)/$', SeasonViewSet.as_view({'get': 'list'})),
     url(r'^all_series/$', all_series_view),
     url(r'^(?P<series_name>.+)/(?P<season_name>.+)/(?P<episode_name>.+)/$', index),
     url(r'^(?P<series_name>.+)/$', series_view),
    #url('^series/(?P<series_name>.+)', SeriesList.as_view(), name="series_list"),
    # url('^series/(?P<series_name>.+)/(?P<season_name>.+)/$', SeasonList.as_view(), name="season_list")
]
