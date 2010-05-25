from django.shortcuts import render_to_response
from models import Station

def index(request):
    stations = Station.objects.all()

    return render_to_response('maps/index.html', {'stations' : stations})
