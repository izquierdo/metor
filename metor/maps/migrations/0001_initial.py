# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table(u'contact', (
            ('contactId', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('maps', ['Contact'])

        # Adding model 'Station'
        db.create_table(u'station', (
            ('stationId', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='stationName')),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('elevation', self.gf('django.db.models.fields.FloatField')(db_column='altitude')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Contact'], db_column='contactId')),
        ))
        db.send_create_signal('maps', ['Station'])

        # Adding model 'Sensor'
        db.create_table(u'sensor', (
            ('sensorId', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin', self.gf('django.db.models.fields.DateTimeField')(db_column='dateBegin')),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column='dateEnd', blank=True)),
            ('granularity', self.gf('django.db.models.fields.IntegerField')()),
            ('medition_type', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='meditionType')),
            ('parameter_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Station'], db_column='stationId')),
        ))
        db.send_create_signal('maps', ['Sensor'])

        # Adding unique constraint on 'Sensor', fields ['sensorId', 'begin', 'end']
        db.create_unique(u'sensor', ['sensorId', 'dateBegin', 'dateEnd'])

        # Adding model 'SyncTime'
        db.create_table('sync_times', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Station'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('maps', ['SyncTime'])

        # Adding model 'MeditionsToSensors'
        db.create_table(u'meditions_to_sensors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sensorMonitorId', self.gf('django.db.models.fields.IntegerField')()),
            ('sensorMonitoredId', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('maps', ['MeditionsToSensors'])

        # Adding unique constraint on 'MeditionsToSensors', fields ['sensorMonitorId', 'sensorMonitoredId']
        db.create_unique(u'meditions_to_sensors', ['sensorMonitorId', 'sensorMonitoredId'])

        # Adding model 'Barometer'
        db.create_table(u'barometer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Barometer'])

        # Adding model 'Dewpoint'
        db.create_table(u'dewpoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Dewpoint'])

        # Adding model 'Et'
        db.create_table(u'et', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Et'])

        # Adding model 'HeatIndex'
        db.create_table(u'heat_index', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['HeatIndex'])

        # Adding model 'Humidity'
        db.create_table(u'humidity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Humidity'])

        # Adding model 'Pressure'
        db.create_table(u'pressure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Pressure'])

        # Adding model 'Radiation'
        db.create_table(u'radiation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Radiation'])

        # Adding model 'Rain'
        db.create_table(u'rain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Rain'])

        # Adding model 'RainRate'
        db.create_table(u'rain_rate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['RainRate'])

        # Adding model 'Temperature'
        db.create_table(u'temperature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Temperature'])

        # Adding model 'Uv'
        db.create_table(u'uv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Uv'])

        # Adding model 'Windchill'
        db.create_table(u'windchill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['Windchill'])

        # Adding model 'WindDirection'
        db.create_table(u'wind_direction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['WindDirection'])

        # Adding model 'WindGust'
        db.create_table(u'wind_gust', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['WindGust'])

        # Adding model 'WindGustDir'
        db.create_table(u'wind_gust_dir', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['WindGustDir'])

        # Adding model 'WindSpeed'
        db.create_table(u'wind_speed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='measureDate')),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Sensor'], db_column='sensorId')),
        ))
        db.send_create_signal('maps', ['WindSpeed'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table(u'contact')

        # Deleting model 'Station'
        db.delete_table(u'station')

        # Deleting model 'Sensor'
        db.delete_table(u'sensor')

        # Removing unique constraint on 'Sensor', fields ['sensorId', 'begin', 'end']
        db.delete_unique(u'sensor', ['sensorId', 'dateBegin', 'dateEnd'])

        # Deleting model 'SyncTime'
        db.delete_table('sync_times')

        # Deleting model 'MeditionsToSensors'
        db.delete_table(u'meditions_to_sensors')

        # Removing unique constraint on 'MeditionsToSensors', fields ['sensorMonitorId', 'sensorMonitoredId']
        db.delete_unique(u'meditions_to_sensors', ['sensorMonitorId', 'sensorMonitoredId'])

        # Deleting model 'Barometer'
        db.delete_table(u'barometer')

        # Deleting model 'Dewpoint'
        db.delete_table(u'dewpoint')

        # Deleting model 'Et'
        db.delete_table(u'et')

        # Deleting model 'HeatIndex'
        db.delete_table(u'heat_index')

        # Deleting model 'Humidity'
        db.delete_table(u'humidity')

        # Deleting model 'Pressure'
        db.delete_table(u'pressure')

        # Deleting model 'Radiation'
        db.delete_table(u'radiation')

        # Deleting model 'Rain'
        db.delete_table(u'rain')

        # Deleting model 'RainRate'
        db.delete_table(u'rain_rate')

        # Deleting model 'Temperature'
        db.delete_table(u'temperature')

        # Deleting model 'Uv'
        db.delete_table(u'uv')

        # Deleting model 'Windchill'
        db.delete_table(u'windchill')

        # Deleting model 'WindDirection'
        db.delete_table(u'wind_direction')

        # Deleting model 'WindGust'
        db.delete_table(u'wind_gust')

        # Deleting model 'WindGustDir'
        db.delete_table(u'wind_gust_dir')

        # Deleting model 'WindSpeed'
        db.delete_table(u'wind_speed')


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
