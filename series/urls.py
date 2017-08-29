from django.conf.urls import url, include

from rest_framework import routers
from .views import SeriesViewSet, SeasonViewSet, EpisodeViewSet, index

router = routers.DefaultRouter()
router.register(r'series', SeriesViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^all_series/$', SeriesViewSet.as_view({'get': 'list'}), name="detail"),
    url(r'^all_series/(?P<series_name>.+)/$', SeasonViewSet.as_view({'get': 'list'})),
    url(r'^all_series/(?P<series_name>.+)/(?P<season_name>.+)/', SeasonViewSet.as_view({'get': 'detail'}))
    url(r'^(?P<series>.+)/(?P<season>.+)/(?P<episode>.+)/', index)
    #url('^series/(?P<series_name>.+)', SeriesList.as_view(), name="series_list"),
    # url('^series/(?P<series_name>.+)/(?P<season_name>.+)/$', SeasonList.as_view(), name="season_list")
]
