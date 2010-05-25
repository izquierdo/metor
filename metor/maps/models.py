# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Barometer(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'barometer'

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.CharField(max_length=90)
    class Meta:
        db_table = u'contact'

class Dewpoint(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'dewpoint'

class Et(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'et'

class HeatIndex(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'heat_index'

class Humidity(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'humidity'

class MeditionsToSensors(models.Model):
    codsensormonitored = models.IntegerField(db_column='codSensorMonitored') # Field name made lowercase.
    codsensormonitor = models.IntegerField(db_column='codSensorMonitor') # Field name made lowercase.
    class Meta:
        db_table = u'meditions_to_sensors'

class Pressure(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'pressure'

class Radiation(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'radiation'

class Rain(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'rain'

class RainRate(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'rain_rate'

class Station(models.Model):
    class Meta:
        db_table = u'station'

    codStation = models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.CharField(max_length=150)
    idContact = models.CharField(max_length=90)

    def _get_last_temperature(self):
        last_sensor = self.sensor_set.filter(parameterType = 'temperature').order_by('-dateBegin')[0]
        last_temperature = last_sensor.temperature_set.order_by('-measureDate')[0]

        return (last_temperature.valor, last_sensor.unit)

    last_temperature = property(_get_last_temperature)

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

class Temperature(models.Model):
    class Meta:
        db_table = u'temperature'

    measureDate = models.DateTimeField()
    valor = models.FloatField()

    codSensor = models.ForeignKey(Sensor, db_column='codSensor')

class Uv(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'uv'

class WindDirection(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'wind_direction'

class WindGust(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'wind_gust'

class WindGustDir(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'wind_gust_dir'

class WindSpeed(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'wind_speed'

class Windchill(models.Model):
    measuredate = models.DateTimeField(db_column='measureDate') # Field name made lowercase.
    valor = models.FloatField()
    codsensor = models.IntegerField(db_column='codSensor') # Field name made lowercase.
    class Meta:
        db_table = u'windchill'

