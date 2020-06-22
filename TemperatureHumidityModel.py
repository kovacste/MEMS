from DataBase import DataBase
import datetime


class TemperatureHumidityModel:

    table_name = 'temperature_humidity'

    def __init__(self, db):
        self.db = db

    def save_data(self, temperature, humidity, device_id):
        now = datetime.datetime.utcnow()
        query = 'INSERT INTO temperature_humidity (humidity, temperature, device_id, time) VALUES (?, ?, ?)'
        val = (humidity, temperature, device_id, now.strftime('%Y-%m-%d %H:%M:%S'))
        return self.db.insert(query, val)

    def get_latest(self, limit):
        query = 'SELECT * FROM temperature_humidity order by time DESC LIMIT ' + limit
        return self.db.find_all(query)


