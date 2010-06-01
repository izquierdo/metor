from datetime import datetime
import sys
import csv
import MySQLdb

estacion_id = 1

# IDs de cada sensor en la BD para cada sensor de esta estacion
sensor_ids = {
    "barometer": 3,
    "pressure": 11,
    "temperature": 4,
    "humidity": 10,
    "wind_speed": 1,
    "wind_direction":6,
    "wind_gust": 16,
    "wind_gust_dir": 15,
    "rain_rate": 13,
    "rain": 9,
    "dewpoint": 5,
    "windchill": 2,
    "heat_index": 12,
    "et": 14,
    "radiation": 8,
    "uv": 7
    }

# en que columnas del csv de entrada se encuentra cada variable
csv_columns = {
    "barometer": 3,
    "pressure": 4,
    "temperature": 7,
    "humidity": 9,
    "wind_speed": 10,
    "wind_direction": 11,
    "wind_gust": 12,
    "wind_gust_dir": 13,
    "rain_rate": 14,
    "rain": 15,
    "dewpoint": 16,
    "windchill": 17,
    "heat_index": 18,
    "et": 19,
    "radiation": 20,
    "uv": 21,
    }

    

def parse_date(s):
    return datetime.strptime(s[:-6], "%Y-%m-%dT%H:%M:%S")

def process(filename):
    r = csv.reader(open(filename))
    r.next()                            # descartar el header
    dbrows = dict((k, []) for k in sensor_ids)
    for row in r:
        assert len(row) == 22
        date = parse_date(row[0])
        for name,index in csv_columns.iteritems():
            try:
                dbrows[name].append((date, float(row[index])))
            except ValueError:
                # print "hubo un error parseando '%s' (%s) como float en el dia %s" % (row[index],
                #                                                                      name,
                #                                                                      date)
                pass

    conn = MySQLdb.connect(host="localhost",
                           user="emisiones",
                           passwd="emisiones",
                           db="emisiones")
    cur = conn.cursor()
    for table, values in dbrows.iteritems():
        cur.executemany("INSERT INTO %s (measureDate, value, sensorId) VALUES (%%s, %%s, %%s)" % table,
                        [(date, value, sensor_ids[table]) for date, value in values])

    conn.commit()

if __name__ == "__main__":
    process(sys.argv[1])
