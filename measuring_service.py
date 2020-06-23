# coding=utf-8
import sched, time

from Application import Application
from BeamBreakSensor import BeamBreakSensor
from BeamBreakModel import BeamBreakModel
from TemperatureHumidityModel import TemperatureHumidityModel
from TemperatureHumiditySensor import TemperatureHumiditySensor
from Notification import Notification

MEASUREMENT_INTERVAL_SEC = 5
BEAM_PIN = 4
TEMP_HUM_PIN = 4
app = Application()


"""temp_hum_sensor = TemperatureHumiditySensor(TEMP_HUM_PIN)
temp_hum_model = TemperatureHumidityModel(app.database)
scheduler = sched.scheduler(time.time, time.sleep)


def do_measurements(sc):
    scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (sc,))
    temp = temp_hum_sensor.get_temp()
    hum = temp_hum_sensor.get_humidity()
    print(temp)
    temp_hum_model.save_data(temp, hum, TEMP_HUM_PIN)


scheduler.enter(MEASUREMENT_INTERVAL_SEC, 1, do_measurements, (scheduler,))
scheduler.run()
"""

def beam_break_callback(beam_break_event):
    app.notify_user(Notification(
        "Mozgás érzékelése",
        "Mozgást érzékeltünk itt meg itt, ekkor: "
        + beam_break_event.event_time
        + " leírás "
        + beam_break_event.event_description
    ))
    beam_sensor_model.save_data(beam_break_event.connection_status, BEAM_PIN)


def beam_connect_callback(beam_break_event):
    beam_sensor_model.save_data(beam_break_event.connection_status, BEAM_PIN)


beam_sensor_model = BeamBreakModel(app.database)
beam_sensor = BeamBreakSensor(BEAM_PIN)
beam_sensor\
    .on_beam_break(beam_break_callback)\
    .on_beam_connect(beam_connect_callback)\
    .start()


message = input("Press enter to quit\n\n")
beam_sensor.stop()
