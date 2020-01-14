import sys
import Adafruit_DHT


class TemperatureHumiditySensor:

    def __init__(self):
        self.humidity = None
        self.temp = None

    def get_humidity(self):
        self.humidity, self.temp = Adafruit_DHT.read_retry(11, 4)
        return self.humidity

    def get_temp(self):
        self.humidity, self.temp = Adafruit_DHT.read_retry(11, 4)
        return self.temp

