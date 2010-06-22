from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    (r'^$', 'index'),
    (r'^estacion/(?P<station_name>\w+)/rosa_viento$', 'windrose'),
    url(r'^json/stations/$', 'json_stations', name="json_stations"),
    url(r'^json/stations/(?P<station_id>\d+)$', 'json_stations', name="json_station"),
)
