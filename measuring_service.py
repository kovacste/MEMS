# connect to database
# if table does not exist, create it
# start measurements
# save them to database with timestamp
import sched, time
from DataBase import DataBase
from TemperatureHumidityModel import TemperatureHumidityModel
from TemperatureHumiditySensor import TemperatureHumiditySensor
import RPi.GPIO as GPIO

BEAM_PIN = 4

def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        print('OTT VAN VALAMI')
    else:
        print('NINCS OTT SEMMI')

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()


#MEASUREMENT_INTERVAL_SEC = 5

#database = DataBase('pydb')

#if not database.table_exists(TemperatureHumidityModel.table_name):
 #   database.execute('CREATE TABLE ' + TemperatureHumidityModel.table_name
                     #+ ' (temperature VARCHAR(20), humidity VARCHAR(20), time VARCHAR(20))')

#scheduler = sched.scheduler(time.time, time.sleep)

#temp_hum_sensor = TemperatureHumiditySensor()
#temp_hum_model = TemperatureHumidityModel(database)


#temp_hum_model.save_data('10', '20')
#temp_hum_model.save_data('15', '22')

#hum_records = database.find_all('select * from ' + TemperatureHumidityModel.table_name)
#print(hum_records)

#def do_measurements(sc):
 #   scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (sc,))
  #  temp = temp_hum_sensor.get_temp()
   # hum = temp_hum_sensor.get_humidity()
    #temp_hum_model.save_data(temp, hum)


#scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (scheduler,))
#scheduler.run()
