# connect to database
# if table does not exist, create it
# start measurements
# save them to database with timestamp
import sched, time
from DataBase import DataBase
from TemperatureHumidityModel import TemperatureHumidityModel
from TemperatureHumiditySensor import TemperatureHumiditySensor

MEASUREMENT_INTERVAL_SEC = 5

database = DataBase('pydb')

if not database.table_exists(TemperatureHumidityModel.table_name):
    database.execute('CREATE TABLE ' + TemperatureHumidityModel.table_name + ' (temperature VARCHAR(20), humidity VARCHAR(20), time VARCHAR(20))')

scheduler = sched.scheduler(time.time, time.sleep)

temp_hum_sensor = TemperatureHumiditySensor()
temp_hum_model = TemperatureHumidityModel(database)


#temp_hum_model.save_data('10', '20')
#temp_hum_model.save_data('15', '22')

hum_records = database.find_all('select * from ' + TemperatureHumidityModel.table_name)
print(hum_records)

def do_measurements(sc):
    scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (sc,))
    print('Measurement..')
    temp = temp_hum_sensor.get_temp()
    hum = temp_hum_sensor.get_humidity()
    temp_hum_model.save_data(temp, hum)


scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (scheduler,))
scheduler.run()
