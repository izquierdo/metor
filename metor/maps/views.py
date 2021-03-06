from tempfile import NamedTemporaryFile
import json

from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext

import rpy2.robjects as robjects

from models import Station, parameter2model
from datetime import datetime

def index(request):
    stations = Station.objects.all()
    return render_to_response('maps/index.html', {'stations' : stations},
                              context_instance=RequestContext(request))

def station_comparison(request):
    stations = Station.objects.all()
    return render_to_response(
            'maps/comparison.html',
            {'stations' : stations, 'display_ids' : xrange(2)},
            context_instance=RequestContext(request))

def json_station_values(request, station_id):
    station = get_object_or_404(Station, stationId = station_id)
    parameter = request.GET.get("parameter")
    unit = request.GET.get("unit")

    if 'begin' in request.GET and request.GET.get('begin'):
        begin = datetime.strptime(request.GET['begin'], "%Y-%m-%d")
    else:
        begin = datetime(1900, 1, 1)

    if 'end' in request.GET and request.GET.get('end'):
        end = datetime.strptime(request.GET['end'], "%Y-%m-%d")
    else:
        end = datetime(9900, 12, 31)

    result = {}
    all_values = station.values_in_range(parameter, begin, end, unit=unit)

    if len(all_values) < 2000:
        values = all_values
    else:
        values = all_values[len(all_values)-2000:]

    result["values"] = [(x.date.year, x.date.month, x.date.day,
                          x.date.hour, x.date.minute, x.date.second,
                          x.value) for x in values]

    return HttpResponse(json.dumps(result), mimetype='application/json')

def json_stations(request, station_id=None):
    if station_id is None:
        stations = []
        attrs = ["stationId", "name", "longitude", "latitude"]
        for station in Station.objects.all():
            s = dict((att, getattr(station, att)) for att in attrs)
            s["status_url"] = reverse('json_station_values', args=[station.stationId])
            s["windrose_url"] = reverse('windrose', kwargs={'slug': station.slug})
            stations.append(s)
        return HttpResponse(json.dumps(stations), mimetype='application/json')
    else:
        station = get_object_or_404(Station, stationId = station_id)
        attrs = ["stationId", "name", "longitude", "latitude"]

        s = dict((att, getattr(station, att)) for att in attrs)
        s["status_url"] = reverse('json_station_values', args=[station.stationId])
        s["windrose_url"] = reverse('windrose', kwargs={'slug': station.slug})

        return HttpResponse(json.dumps(s), mimetype='application/json')

def windrose(request, slug = None):
    if not slug:
        #TODO error
        return "error"

    station = get_object_or_404(Station, slug = slug)

    from datetime import datetime

    if 'begin' in request.GET and request.GET.get('begin'):
        begin = datetime.strptime(request.GET['begin'], "%Y-%m-%d")
    else:
        begin = datetime(1900, 1, 1)

    if 'end' in request.GET and request.GET.get('end'):
        end = datetime.strptime(request.GET['end'], "%Y-%m-%d")
    else:
        end = datetime(9900, 12, 31)

    if 'granularity' in request.GET:
        granularity = int(request.GET['granularity'])
    else:
        granularity = 86400 # one day in seconds

    table_file = NamedTemporaryFile(prefix="windrose.", suffix=".dat.tmp")
    table_file.write(station.get_wind_freqs(begin, end, granularity))
    table_file.flush()

    png_file = NamedTemporaryFile(prefix="windrose.", suffix=".png.tmp")

    # TODO ver si se puede hacer el library(climatol) una sola vez por ejecucion
    # del servidor, porque es lento
    robjects.r('''
         library(climatol)
         library(grDevices)
         png(file='%s', width=512, height=512)
         table <- read.table('%s')
         rosavent(table, 7, 4)
         dev.off()
     ''' % (png_file.name, table_file.name))

    table_file.close()

    response = HttpResponse(mimetype='image/png')
    #response['Content-Disposition'] = 'attachment; filename=windrose_%s.png' % station_name
    response.write(png_file.read())

    png_file.close()

    return response

def grid(request, object_id, parameter):
    station = get_object_or_404(Station, stationId = object_id)
    #result = station.name + " " + parameter

    if 'granularity' in request.GET:
        granularity = int(request.GET['granularity'])
    else:
        granularity = 86400 # one day in seconds

    if 'start' in request.GET:
        start = datetime.strptime(request.GET['start'], "%Y-%m-%d")
    else:
        start = datetime(1900, 1, 1)

    if 'end' in request.GET:
        end = datetime.strptime(request.GET['end'], "%Y-%m-%d")
    else:
        end = datetime(9900, 12, 31)

    if end < start:
        start, end = end, start

    results = station.values_in_range(parameter, start, end, granularity)
    results = "\n".join([str(x.date) + " " + str(x.value) for x in results])
    return HttpResponse(results, mimetype='text/plain')

def csv(request, object_id, parameter):
    station = get_object_or_404(Station, stationId = object_id)
    #result = station.name + " " + parameter

    if 'granularity' in request.GET:
        granularity = int(request.GET['granularity'])
    else:
        granularity = 86400 # one day in seconds

    if 'start' in request.GET:
        start = datetime.strptime(request.GET['start'], "%Y-%m-%d")
    else:
        start = datetime(1900, 1, 1)

    if 'end' in request.GET:
        end = datetime.strptime(request.GET['end'], "%Y-%m-%d")
    else:
        end = datetime(9900, 12, 31)

    if end < start:
        start, end = end, start

    results = station.values_in_range(parameter, start, end, granularity)
    results = "\n".join(str(x.date) + "," + str(x.value) for x in results)
    r = HttpResponse(results, mimetype='text/plain')
    r['Content-Disposition'] = "attachment; filename=%s-%s.csv" % (station.name, parameter)
    return r
