import sys
import Adafruit_DHT


class TemperatureHumiditySensor:

    def __init__(self, pin_no):
        self.humidity = None
        self.temp = None
        self.pin_no = None

    def get_humidity(self):
        self.humidity, self.temp = Adafruit_DHT.read_retry(11, self.pin_no)
        return self.humidity

    def get_temp(self):
        self.humidity, self.temp = Adafruit_DHT.read_retry(11, self.pin_no)
        return self.temp

