import RPi.GPIO as GPIO

from BeamBreakEvent import BeamBreakEvent
import datetime


class BeamBreakSensor:

    def __init__(self, pin_no):
        self.beam_connected = False
        self.pin_no = pin_no
        self.on_beam_connect_callback_fn = None
        self.on_beam_break_callback_fn = None

    def on_beam_break(self, callback_fn):
        self.on_beam_break_callback_fn = callback_fn
        return self

    def on_beam_connect(self, callback_fn):
        self.on_beam_connect_callback_fn = callback_fn
        return self

    def start(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_no, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin_no, GPIO.BOTH, callback=self.default_cb_fn)
        return self

    def stop(self):
        GPIO.cleanup()
        return self

    def default_cb_fn(self, param):
        print(param)
        if GPIO.input(self.pin_no):
            if self.on_beam_connect_callback_fn is not None:
                self.on_beam_connect_callback_fn(BeamBreakEvent(
                    datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                    'Beam connected at device ' + str(self.pin_no),
                    False
                ))
        else:
            if self.on_beam_break_callback_fn is not None:
                self.on_beam_break_callback_fn(BeamBreakEvent(
                    datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                    'Beam was broken at device ' + str(self.pin_no),
                    False
                ))
        return self
