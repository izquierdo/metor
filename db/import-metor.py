from datetime import datetime
import sys
import csv
import MySQLdb

estacion_id = 1

# IDs de cada sensor en la BD para cada sensor de esta estacion
sensor_ids = {'barometer': 50L,
 'dewpoint': 52L,
 'heat_index': 53L,
 'humidity': 57L,
 'rain': 56L,
 'rain_rate': 55L,
 'temperature': 51L,
 'wind_direction': 54L,
 'wind_speed': 48L,
 'windchill': 49L}



# en que columnas del csv de entrada se encuentra cada variable
csv_columns = {
    "temperature": 2,
    "humidity": 3,
    "dewpoint": 4,
    "wind_speed": 5,
    "wind_direction": 6,
    "windchill": 7,
    "heat_index": 8,
    "barometer": 9,
    "rain": 10,
    "rain_rate": 11,
    }

degrees = dict(N=0, NNE=22.5, NE=45, ENE=67.5,
               E=90, ESE=112.5, SE=135, SSE=157.5,
               S=180, SSW=202.5, SW=225, WSW=247.5,
               W=270, WNW=292.5, NW=315, NNW
               =337.5)


def parse_date(row):
    return datetime.strptime(row[0] + " " + row[1] + "m",
                             "%d/%m/%y %I:%M %p")

def process(filename):
    r = csv.reader(open(filename))
    r.next()                            # descartar el header
    dbrows = dict((k, []) for k in sensor_ids)
    for row in r:
        if row[-1] == '5':
            date = parse_date(row)
            if row[csv_columns['wind_direction']] == '---':
                # no considerar el viento
                # print date, 'no tiene viento'
                pass
            else:
                dbrows["wind_direction"].append((date, degrees[row[csv_columns["wind_direction"]]]))
                dbrows["wind_speed"].append((date, row[csv_columns["wind_speed"]]))
                #print date, row[csv_columns['wind_speed']], degrees[row[csv_columns['wind_direction']]]
                pass

            for colname,colindex in csv_columns.items():
                if colname.startswith("wind"):
                    continue
                if row[colindex] == '---':
                    continue

                dbrows[colname].append((date, row[colindex]))

    # assert len(dbrows["wind_direction"]) == len(dbrows["wind_speed"])
    # print dbrows["wind_speed"]
    conn = MySQLdb.connect(host="localhost",
                           user="emisiones",
                           passwd="emisiones",
                           db="emisiones")
    cur = conn.cursor()
    for table, values in dbrows.iteritems():
        print table
        cur.executemany("INSERT INTO %s (measureDate, value, sensorId) VALUES (%%s, %%s, %%s)" % table,
                        [(date, value, sensor_ids[table]) for date, value in values])

    conn.commit()

if __name__ == "__main__":
    process("METOR/metor.csv")
