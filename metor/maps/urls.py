from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    (r'^$', 'index'),
    (r'^estacion/(?P<station_name>\w+)/rosa_viento', 'windrose'),
)
