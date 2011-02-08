from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from metor.maps.models import Station

urlpatterns = patterns('maps.views',
    (r'^$', 'index'),
    url(r'^estacion/(?P<slug>\w+)/rosa_viento\.png$', 'windrose', name="windrose"),
    url(r'^json/stations/$', 'json_stations', name="json_stations"),
    url(r'^json/stations/(?P<station_id>-?\d+)/values/$', 'json_station_values', name="json_station_values"),
)

# Station CRUD
station_list = {
    'queryset': Station.objects.all(),
    'paginate_by': 10,
    'template_object_name': 'station',
}
station_detail = {
    'queryset': Station.objects.all(),
    'template_object_name': 'station',
}
station_form = {
    'model': Station,
    'template_object_name': 'station',
}
station_delete = {
    'model': Station,
    'template_object_name': 'station',
    'post_delete_redirect': '/estaciones/',
}
urlpatterns += patterns('django.views.generic.create_update',
    url('^estaciones/$', object_list, station_list, name='station_list'),
    url('^estaciones/(?P<object_id>\d+)/$', object_detail, station_detail, name='station_detail'),
    url('^estaciones/editar/(?P<object_id>\d+)/$', 'update_object', station_form, name='station_update'),
    url('^estaciones/crear/$', 'create_object', {'model': Station}, name='station_create'),
    url('^estaciones/borrar/(?P<object_id>\d+)/$', 'delete_object', station_delete, name='station_delete'),
)
