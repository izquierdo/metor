from django.db import models

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
    name = models.CharField(max_length=30,db_column='stationName')
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    # altitude y latitude son muy parecidos. Se suele usar elevation
    # para evitar confusion
    elevation = models.FloatField(db_column='altitude') 
    location = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, db_column='contactId')

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

    def get_wind_freqs(self):
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
                if fabs(h-degrees) < 11.25:
                    return name

            assert False # we should always return a heading

        def get_speed_range(speed):
            for (name, lo, hi) in speed_ranges:
                if (speed >= lo and speed <= hi) or (speed >= lo and hi == -1):
                    return name

            assert False # incorrect speed_ranges or speed

        #TODO definir bien el rango a buscar
        speeds = {}
        directions = {}

        for sensor in self.sensor_set.filter(parameter_type = 'wind_speed').all():
            for ws in sensor.windspeed_set.all():
                speeds[ws.date] = ws.value

        for sensor in self.sensor_set.filter(parameter_type = 'wind_direction').all():
            for wd in sensor.winddirection_set.all():
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

    def __unicode__(self):
        return u"%s %s"%(self.parameter_type, self.station.name)

    def is_active(self):
        return self.end == None
    is_active.boolean = True

    def _get_last_measurement(self):
        measures_set_name = "%s_set" % (self.parameter_type.replace('_', ''))
        measures_set = getattr(self, measures_set_name)
        last_measure = measures_set.order_by('-date')[0]
        return (last_measure.value, self.unit)

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
