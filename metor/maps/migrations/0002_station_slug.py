# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Station.slug'
        db.add_column(u'station', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(default='slug', max_length=100, populate_from='name', db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Station.slug'
        db.delete_column(u'station', 'slug')


    models = {
        'maps.barometer': {
            'Meta': {'object_name': 'Barometer', 'db_table': "u'barometer'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "u'contact'"},
            'contactId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'maps.dewpoint': {
            'Meta': {'object_name': 'Dewpoint', 'db_table': "u'dewpoint'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.et': {
            'Meta': {'object_name': 'Et', 'db_table': "u'et'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.heatindex': {
            'Meta': {'object_name': 'HeatIndex', 'db_table': "u'heat_index'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.humidity': {
            'Meta': {'object_name': 'Humidity', 'db_table': "u'humidity'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.meditionstosensors': {
            'Meta': {'unique_together': "(('sensorMonitorId', 'sensorMonitoredId'),)", 'object_name': 'MeditionsToSensors', 'db_table': "u'meditions_to_sensors'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensorMonitorId': ('django.db.models.fields.IntegerField', [], {}),
            'sensorMonitoredId': ('django.db.models.fields.IntegerField', [], {})
        },
        'maps.pressure': {
            'Meta': {'object_name': 'Pressure', 'db_table': "u'pressure'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.radiation': {
            'Meta': {'object_name': 'Radiation', 'db_table': "u'radiation'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.rain': {
            'Meta': {'object_name': 'Rain', 'db_table': "u'rain'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.rainrate': {
            'Meta': {'object_name': 'RainRate', 'db_table': "u'rain_rate'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.sensor': {
            'Meta': {'unique_together': "(('sensorId', 'begin', 'end'),)", 'object_name': 'Sensor', 'db_table': "u'sensor'"},
            'begin': ('django.db.models.fields.DateTimeField', [], {'db_column': "'dateBegin'"}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'dateEnd'", 'blank': 'True'}),
            'granularity': ('django.db.models.fields.IntegerField', [], {}),
            'medition_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'meditionType'"}),
            'parameter_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sensorId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Station']", 'db_column': "'stationId'"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'maps.station': {
            'Meta': {'object_name': 'Station', 'db_table': "u'station'"},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Contact']", 'db_column': "'contactId'"}),
            'elevation': ('django.db.models.fields.FloatField', [], {'db_column': "'altitude'"}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'stationName'"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'default': "'slug'", 'max_length': '100', 'populate_from': "'name'", 'db_index': 'True'}),
            'stationId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'maps.synctime': {
            'Meta': {'object_name': 'SyncTime', 'db_table': "'sync_times'"},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Station']"})
        },
        'maps.temperature': {
            'Meta': {'object_name': 'Temperature', 'db_table': "u'temperature'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.uv': {
            'Meta': {'object_name': 'Uv', 'db_table': "u'uv'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.windchill': {
            'Meta': {'object_name': 'Windchill', 'db_table': "u'windchill'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.winddirection': {
            'Meta': {'object_name': 'WindDirection', 'db_table': "u'wind_direction'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.windgust': {
            'Meta': {'object_name': 'WindGust', 'db_table': "u'wind_gust'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.windgustdir': {
            'Meta': {'object_name': 'WindGustDir', 'db_table': "u'wind_gust_dir'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'maps.windspeed': {
            'Meta': {'object_name': 'WindSpeed', 'db_table': "u'wind_speed'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'measureDate'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maps.Sensor']", 'db_column': "'sensorId'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['maps']
