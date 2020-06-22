from DataBase import DataBase
import datetime


class BeamBreakModel:

    table_name = 'beam_break'

    def __init__(self, db):
        self.db = db

    def save_data(self, connection_status, device_id):
        now = datetime.datetime.utcnow()
        query = 'INSERT INTO beam_break (connection_status, device_id, time) VALUES (?, ?, ?)'
        val = (connection_status, device_id, now.strftime('%Y-%m-%d %H:%M:%S'))
        return self.db.insert(query, val)
