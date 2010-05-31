from django.db import models

class Station(models.Model):
    class Meta:
        db_table = u'station'

    stationId = models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.CharField(max_length=150)
    contactId = models.CharField(max_length=90)

    def _get_current_sensor(self, type):
        return self.sensor_set.filter(parameterType = type).order_by('-dateBegin')[0]

    def _get_last_measurement(self, type):
        return self._get_current_sensor(type).last_measurement

    def _get_last_temperature(self):
        return self._get_last_measurement('temperature')

    def _get_last_windspeed(self):
        return self._get_last_measurement('wind_speed')

    last_temperature = property(_get_last_temperature)
    last_windspeed = property(_get_last_windspeed)

class Sensor(models.Model):
    class Meta:
        db_table = u'sensor'

    sensorId = models.IntegerField(primary_key=True)

    dateBegin = models.DateTimeField() # Field name made lowercase.
    dateend = models.DateTimeField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    granularity = models.IntegerField()
    meditiontype = models.CharField(max_length=9, db_column='meditionType') # Field name made lowercase.
    parameterType = models.CharField(max_length=90)
    unit = models.CharField(max_length=30)

    stationId = models.ForeignKey(Station, db_column='stationId')

    def _get_last_measurement(self):
        measures_set = getattr(self, "%s_set" % self.parameterType)
        last_measure = measures_set.order_by('-measureDate')[0]
        return (last_measure.value, self.unit)

    last_measurement = property(_get_last_measurement)

class Contact(models.Model):
    class Meta:
        db_table = u'contact'

    contactId = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.CharField(max_length=90)

class MeditionsToSensors(models.Model):
    class Meta:
        db_table = u'meditions_to_sensors'

    sensorMonitorId = models.IntegerField()
    sensorMonitoredId = models.IntegerField()

# Mediciones

# TODO en la BD, todos los measurements deben tener campo id

class Measurement(models.Model):
    class Meta:
        abstract = True

    measureDate = models.DateTimeField()
    value = models.FloatField()

    sensorId = models.ForeignKey(Sensor, db_column='sensorId')

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
