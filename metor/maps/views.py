from tempfile import NamedTemporaryFile

from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

import rpy2.robjects as robjects

from models import Station


def index(request):
    stations = Station.objects.all()

    return render_to_response('maps/index.html', {'stations' : stations})

def windrose(request, station_name = None):
    if not station_name:
        #TODO error
        return "error"

    #from rpy2.robjects.packages import importr

    station = get_object_or_404(Station, name = station_name)

    table_file = NamedTemporaryFile(prefix="windrose.", suffix=".dat.tmp")
    table_file.write(station.windfreqstmp)
    table_file.flush()

    png_file = NamedTemporaryFile(prefix="windrose.", suffix=".png.tmp")

    # TODO ver si se puede hacer el library(climatol) una sola vez por ejecucion
    # del servidor, porque es lento
    robjects.r('''
         library(climatol)
         library(grDevices)
         png(file='%s', width=512, height=512)
         table <- read.table('%s')
         rosavent(table, 4, 4)
         dev.off()
     ''' % (png_file.name, table_file.name))

    table_file.close()

    response = HttpResponse(mimetype='image/png')
    #response['Content-Disposition'] = 'attachment; filename=windrose_%s.png' % station_name
    response.write(png_file.read())

    png_file.close()

    return response
