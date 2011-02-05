from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    (r'^$', 'index'),
    (r'^comparacion/?$', 'station_comparison'),
    url(r'^estacion/(?P<slug>\w+)/rosa_viento\.png$', 'windrose', name="windrose"),
    url(r'^json/stations/$', 'json_stations', name="json_stations"),
    url(r'^json/stations/(?P<station_id>-?\d+)/$', 'json_stations', name="json_station"),
    url(r'^json/stations/(?P<station_id>-?\d+)/values/$', 'json_station_values', name="json_station_values"),
)
