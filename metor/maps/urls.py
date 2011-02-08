from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from metor.maps.models import Station

urlpatterns = patterns('maps.views',
    (r'^$', 'index'),
    (r'^comparacion/?$', 'station_comparison'),
    url(r'^estacion/(?P<slug>\w+)/rosa_viento\.png$', 'windrose', name="windrose"),
    url(r'^estacion/(?P<object_id>\d+)/grid/(?P<parameter>[a-z_]+)/', 'grid', name="grid"),
    url(r'^estacion/(?P<object_id>\d+)/csv/(?P<parameter>[a-z_]+)/', 'csv', name="grid"),
    url(r'^json/stations/$', 'json_stations', name="json_stations"),
    url(r'^json/stations/(?P<station_id>-?\d+)/$', 'json_stations', name="json_station"),
    url(r'^json/stations/(?P<station_id>-?\d+)/values/$', 'json_station_values', name="json_station_values"),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^download/$', 'direct_to_template', {"template": "maps/download.html"}),
    url(r'^download/rdf/$', 'direct_to_template', {"template": "maps/download-rdf.html"}),
    url(r'^download/csv/$', 'direct_to_template', {"template": "maps/download-select.html",
                                                   "extra_context": {
                                                          "type": "csv",
                                                          "stations":  Station.objects.all()
                                                          }
                                                   }),
    url(r'^download/grid/$', 'direct_to_template', {"template": "maps/download-select.html",
                                                   "extra_context": {
                                                          "type": "csv",
                                                          "stations":  Station.objects.all()
                                                          }
                                                   }),
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
