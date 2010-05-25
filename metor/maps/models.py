from django.db import models

class Station(models.Model):
    class Meta:
        db_table = u'station'

    codStation = models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.CharField(max_length=150)
    idContact = models.CharField(max_length=90)

    def _get_current_sensor(self, type):
        return self.sensor_set.filter(parameterType = type).order_by('-dateBegin')[0]

    def _get_last_measurement(self, type):
        return self._get_current_sensor(type).last_measurement

    def _get_last_temperature(self):
        return self._get_last_measurement('temperature')

    def _get_last_windspeed(self):
        return self._get_last_measurement('windspeed')

    last_temperature = property(_get_last_temperature)
    last_windspeed = property(_get_last_windspeed)

class Sensor(models.Model):
    class Meta:
        db_table = u'sensor'

    codSensor = models.IntegerField(primary_key=True)

    dateBegin = models.DateTimeField() # Field name made lowercase.
    dateend = models.DateTimeField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    granularity = models.IntegerField()
    meditiontype = models.CharField(max_length=9, db_column='meditionType') # Field name made lowercase.
    parameterType = models.CharField(max_length=90)
    unit = models.CharField(max_length=30)

    codStation = models.ForeignKey(Station, db_column='codStation')

    def _get_last_measurement(self):
        measures_set = getattr(self, "%s_set" % self.parameterType)
        last_measure = measures_set.order_by('-measureDate')[0]
        return (last_measure.valor, self.unit)

    last_measurement = property(_get_last_measurement)

class Contact(models.Model):
    class Meta:
        db_table = u'contact'

    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.CharField(max_length=90)

class MeditionsToSensors(models.Model):
    codsensormonitored = models.IntegerField(db_column='codSensorMonitored') # Field name made lowercase.
    codsensormonitor = models.IntegerField(db_column='codSensorMonitor') # Field name made lowercase.
    class Meta:
        db_table = u'meditions_to_sensors'

# Mediciones

# TODO en la BD, todos los measurements deben tener campo id

class Measurement(models.Model):
    class Meta:
        abstract = True

    measureDate = models.DateTimeField()
    valor = models.FloatField()

    codSensor = models.ForeignKey(Sensor, db_column='codSensor')

class Temperature(Measurement):
    class Meta:
        db_table = u'temperature'

class WindSpeed(Measurement):
    class Meta:
        db_table = u'wind_speed'

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

class Uv(Measurement):
    class Meta:
        db_table = u'uv'

class WindDirection(Measurement):
    class Meta:
        db_table = u'wind_direction'

class WindGust(Measurement):
    class Meta:
        db_table = u'wind_gust'

class WindGustDir(Measurement):
    class Meta:
        db_table = u'wind_gust_dir'

class Windchill(Measurement):
    class Meta:
        db_table = u'windchill'
