from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from metor.maps.models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'email')
    
admin.site.register(Contact, ContactAdmin)


# # esto es para mostrar inline solo los sesonres activos, pero no lo he
# # probado -- jcc
# class ActiveSensorFormSet(BaseInlineFormSet):
#     def get_queryset(self):
#         if not hasattr(self, '_queryset'):
#             qs = super(ActiveSensorFormSet, self).get_queryset().filter(end=None)
#             self._queryset = qs
#         return self._queryset


class SensorInline(admin.TabularInline):
    model = Sensor
    # formset = ActiveSensorFormSet

class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'location', 'contact')
    inlines = [SensorInline]

admin.site.register(Station, StationAdmin)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'begin', 'end', 'granularity', 'is_active')
    # FIXME: no funciona 'station'
    list_filter = ('parameter_type', 'station')

    def sensor_name(self, obj):
        return "%s @ %s" % (obj.parameter_type, obj.station.name)
    sensor_name.short_description = 'Sensor'

admin.site.register(Sensor, SensorAdmin)
