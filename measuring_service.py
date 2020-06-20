# connect to database
# if table does not exist, create it
# start measurements
# save them to database with timestamp
import sched, time

from Application import Application
from BeamBreakEvent import BeamBreakEvent
from BreakBeamSensor import BreakBeamSensor
from BeamBreakModel import BeamBreakModel
from DataBase import DataBase
from TemperatureHumidityModel import TemperatureHumidityModel
from TemperatureHumiditySensor import TemperatureHumiditySensor
from Notification import Notification

app = Application()

BEAM_PIN = 4
TEMP_HUM_PIN = 4

beam_sensor = BreakBeamSensor(BEAM_PIN)
beam_sensor.on_beam_break_callback_fn(lambda beam_break_event: BeamBreakEvent(

    app.notify_user(Notification(
        'Mozgás érzékelése',
        'Mozgást érzékeltünk itt meg itt, ekkor: '
        + beam_break_event.time
        + ' leírás '
        + beam_break_event.description
    ))

)).on_beam_connect_callback_fn(lambda: (

)).start()

message = input("Press enter to quit\n\n")
beam_sensor.stop()



#MEASUREMENT_INTERVAL_SEC = 5

#database = DataBase('pydb')

#if not database.table_exists(TemperatureHumidityModel.table_name):
 #   database.execute('CREATE TABLE ' + TemperatureHumidityModel.table_name
                     #+ ' (temperature VARCHAR(20), humidity VARCHAR(20), device_id VARCHAR(20), time VARCHAR(20))')

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
    #temp_hum_model.save_data(temp, hum, TEMP_HUM_PIN)


#scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (scheduler,))
#scheduler.run()
