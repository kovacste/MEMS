import sys
import Adafruit_DHT


class Humidity:

    def __init__(self):
        self.humidity = None

    def get_humidity(self):
        self.humidity = Adafruit_DHT.read_retry(11, 4)
        return self.humidity

