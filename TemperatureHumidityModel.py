from DataBase import DataBase
import datetime


class TemperatureHumidityModel:

    table_name = 'temperature_humidity'

    def __init__(self, db: DataBase):
        self.db = db

    def save_data(self, temperature, humidity):
        now = datetime.datetime.utcnow()
        query = 'INSERT INTO temperature_humidity (humidity, temperature, time) VALUES (?, ?, ?)'
        val = (humidity, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        return self.db.insert(query, val)

    def get_latest(self):
        query = 'SELECT * FROM temperature_humidity order by time DESC LIMIT 1'
        return self.db.find_all(query)


