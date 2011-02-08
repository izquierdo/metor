# coding: utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.fields import AutoSlugField

# imports para migrations
import django_extensions.db.fields
from south.modelsinspector import add_introspection_rules

class Contact(models.Model):
    class Meta:
        db_table = u'contact'

    contactId = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s <%s>" % (self.firstname, self.lastname, self.email)

class Station(models.Model):
    class Meta:
        db_table = u'station'

    stationId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,db_column='stationName', verbose_name="Nombre")
    longitude = models.FloatField("Longitud")
    latitude = models.FloatField("Latitud")

    # altitude y latitude son muy parecidos. Se suele usar elevation
    # para evitar confusion
    elevation = models.FloatField(db_column='altitude', verbose_name=u"Elevación")
    location = models.CharField(max_length=50, verbose_name="Localidad")
    contact = models.ForeignKey(Contact, db_column='contactId', verbose_name="Contacto")

    # debe haber un default para que south no se queje
    # el separator es _ ya que - no funciona con la funcion reverse() de Django
    slug = AutoSlugField(max_length=100, populate_from='name', default="slug", separator="_")

    def __unicode__(self):
        return self.name

    def _get_current_sensor(self, type):
        return self.sensor_set.filter(parameter_type = type).order_by('-begin')[0]

    def _get_last_measurement(self, type):
        return self._get_current_sensor(type).last_measurement

    def _get_last_temperature(self):
        return self._get_last_measurement('temperature')

    def _get_last_windspeed(self):
        return self._get_last_measurement('wind_speed')

    last_temperature = property(_get_last_temperature)
    last_windspeed = property(_get_last_windspeed)

    def get_absolute_url(self):
        return reverse('station_detail', args=[self.stationId])

    def get_wind_freqs(self, begin=None, end=None, granularity=None):
        headings = [
            ("N", 0.00),
            ("N", 360.00),
            ("NNE", 22.50),
            ("NE", 45.00),
            ("ENE", 67.50),
            ("E", 90.00),
            ("ESE", 112.50),
            ("SE", 135.00),
            ("SSE", 157.50),
            ("S", 180.00),
            ("SSW", 202.50),
            ("SW", 225.00),
            ("WSW", 247.50),
            ("W", 270.00),
            ("WNW", 292.50),
            ("NW", 315.00),
            ("NNW", 337.50),
        ]

        speed_ranges = [
            ("0-3", 0, 3),
            ("3-6", 3, 6),
            ("6-9", 6, 9),
            ("\"> 9\"", 9, -1),
        ]

        def get_heading(degrees):
            from math import fabs

            for (name, h) in headings:
                if fabs(h-degrees) <= 11.25:
                    return name

            assert False # we should always return a heading

        def get_speed_range(speed):
            for (name, lo, hi) in speed_ranges:
                if (speed >= lo and speed <= hi) or (speed >= lo and hi == -1):
                    return name

            assert False # incorrect speed_ranges or speed

        speeds = {}
        directions = {}

        for ws in self.values_in_range('wind_speed', begin, end, granularity):
            speeds[ws.date] = ws.value

        for wd in self.values_in_range('wind_direction', begin, end, granularity):
            directions[wd.date] = wd.value

        (small,big) = (speeds,directions) if len(speeds) <= len(directions) else (directions,speeds)

        freq_table = {}

        for date in small:
            if date not in big:
                continue

            key = (get_speed_range(speeds[date]), get_heading(directions[date]))

            if key in freq_table:
                freq_table[key] += 1
            else:
                freq_table[key] = 0

        #TODO mejorar esto
        tablestr = " ".join([name for name, h in headings[1:]]) + "\n" # don't display N twice

        for (spdname,lo,hi) in speed_ranges:
            tablestr += spdname + " "
            for (hdname, heading) in headings[1:]: # don't display N twice
                tablestr += (str(freq_table.get((spdname, hdname), 0)) + " ")

            tablestr += "\n"

        return tablestr

    windfreqstmp = property(get_wind_freqs)

    @property
    def active_sensors(self):
        return self.sensors.filter(end=None)

    def values_in_range(self, type, begin_date, end_date, granularity=None, unit=None):
        from fractions import gcd
        from datetime import timedelta

        def convert_unit(measurement, current_unit):
            # TODO hacer esto de otra forma
            if not unit:
                return measurement

            if unit == "celsius":
                if current_unit == "F":
                    measurement.value = (measurement.value-32.0)*(5.0/9.0)
            elif unit == "fahrenheit":
                if current_unit == "C":
                    measurement.value = (measurement.value*(9.0/5.0))+32.0

            return measurement

        sensors = []

        for sensor in self.sensor_set.filter(parameter_type = type).order_by('begin'):
            if sensor.begin <= end_date and (sensor.end is None or sensor.end >= begin_date):
                sensors.append(sensor)

        values = []

        if granularity:
            onemin = timedelta(seconds=granularity)

        for sensor in sensors:
            qs = sensor.values().filter(date__gte=begin_date, date__lte=end_date).order_by('date')
            sensor_values_count = qs.count()
            first_time_through = True

            converted_measures = map(lambda m : convert_unit(m, sensor.unit), qs)

            for idx, measure in enumerate(converted_measures):
                if idx + 1 == sensor_values_count:
                    break

                idx_next, next_measure = idx + 1, qs[idx+1]

                if first_time_through:
                    if measure.date >= begin_date and measure.date <= end_date:
                        values.append(measure)
                        first_time_through = False

                if granularity:
                    current_date = measure.date + onemin

                    while current_date < next_measure.date:
                        if current_date >= begin_date and current_date <= end_date:
                            avg_measure = measure
                            avg_measure.date = current_date

                            # TODO lo que en verdad hay que revisar es que sea una unidad numerica
                            if sensor.unit == '?':
                                values.append(avg_measure)
                            else:
                                avg_measure.value = (measure.value + next_measure.value) / 2.0
                                values.append(avg_measure)

                        current_date = current_date + onemin

                if next_measure.date >= begin_date and next_measure.date <= end_date:
                    # Si es el ultimo valor no vamos a entrar en el ciclo otra
                    # vez. Si no es el ultimo entonces lo agregaremos en el
                    # proximo ciclo si no hemos agregado antes
                    if idx + 1 == sensor_values_count or not first_time_through:
                        values.append(next_measure)


        return values

class Sensor(models.Model):
    class Meta:
        db_table = u'sensor'
        unique_together = (('sensorId', 'begin', 'end'),)

    sensorId = models.AutoField(primary_key=True)

    begin = models.DateTimeField(db_column='dateBegin') # Field name made lowercase.
    end = models.DateTimeField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    granularity = models.IntegerField()
    medition_type = models.CharField(max_length=3, db_column='meditionType') # Field name made lowercase.
    parameter_type = models.CharField(max_length=30)
    unit = models.CharField(max_length=10)

    station = models.ForeignKey(Station, db_column='stationId')

    def values(self):
        measures_set_name = "%s_set" % (self.parameter_type.replace('_', ''))
        measures_set = getattr(self, measures_set_name)
        return measures_set

    def __unicode__(self):
        return u"%s %s"%(self.parameter_type, self.station.name)

    def is_active(self):
        return self.end == None
    is_active.boolean = True

    def _get_last_measurement(self):
        return self.values().order_by('-date')[0]

    last_measurement = property(_get_last_measurement)



class SyncTime(models.Model):
    class Meta:
        db_table = 'sync_times'
    station = models.ForeignKey(Station)
    date = models.DateTimeField()

    def __unicode__(self):
        return "%s@%s" % (station.name, date)


# No entiendo esta tabla -- jcc
class MeditionsToSensors(models.Model):
    class Meta:
        db_table = u'meditions_to_sensors'
        unique_together = (('sensorMonitorId', 'sensorMonitoredId'),)

    sensorMonitorId = models.IntegerField()
    sensorMonitoredId = models.IntegerField()

# Mediciones

class Measurement(models.Model):
    class Meta:
        abstract = True

    date = models.DateTimeField(db_column='measureDate')
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, db_column='sensorId')

    def __unicode__(self):
        return "%s %s (%s %s)" % (self.date, self.value, self.sensor.parameter_type, self.sensor.station.name)

class Barometer(Measurement):
    class Meta:
        db_table = u'barometer'

class Dewpoint(Measurement):
    class Meta:
        db_table = u'dewpoint'

class Et(Measurement):
    class Meta:
        db_table = u'et'

class HeatIndex(Measurement):
    class Meta:
        db_table = u'heat_index'

class Humidity(Measurement):
    class Meta:
        db_table = u'humidity'

class Pressure(Measurement):
    class Meta:
        db_table = u'pressure'

class Radiation(Measurement):
    class Meta:
        db_table = u'radiation'

class Rain(Measurement):
    class Meta:
        db_table = u'rain'

class RainRate(Measurement):
    class Meta:
        db_table = u'rain_rate'

class Temperature(Measurement):
    class Meta:
        db_table = u'temperature'

class Uv(Measurement):
    class Meta:
        db_table = u'uv'

class Windchill(Measurement):
    class Meta:
        db_table = u'windchill'

class WindDirection(Measurement):
    class Meta:
        db_table = u'wind_direction'

class WindGust(Measurement):
    class Meta:
        db_table = u'wind_gust'

class WindGustDir(Measurement):
    class Meta:
        db_table = u'wind_gust_dir'

class WindSpeed(Measurement):
    class Meta:
        db_table = u'wind_speed'


def parameter2model(parameter_type):
    return {"barometer": Barometer,
            "dewpoint": Dewpoint,
            "et": Et,
            "heat_index": HeatIndex,
            "humidity": Humidity,
            "pressure": Pressure,
            "radiation": Radiation,
            "rain": Rain,
            "rain_rate": RainRate,
            "temperature": Temperature,
            "uv": Uv,
            "windchill": Windchill,
            "wind_direction": WindDirection,
            "wind_gust": WindGust,
            "wind_gust_dir": WindGustDir,
            "wind_speed": WindSpeed}[parameter_type]


# South rules

_south_station_rules = [
  (
    [django_extensions.db.fields.AutoSlugField],
    [],
    {
        "max_length": ["max_length", {"default" : True}],
        "blank": ["blank", {"default" : True}],
        "editable": ["editable", {"default" : False}],
        "populate_from": ["_populate_from", {}],
        "separator": ["separator", {"default" : u'-'}],
        "overwrite": ["overwrite", {"default" : False}],
    },
  )
]

add_introspection_rules(_south_station_rules, ["^django_extensions\.db\.fields\.AutoSlugField"])
