from BeamBreakModel import BeamBreakModel
from DataBase import DataBase
from Mailer import Mailer
from EmailNotifier import EmailNotifier
from SMTPOptions import SMTPOptions
from TemperatureHumidityModel import TemperatureHumidityModel
from UserModel import UserModel


class Application:

    def __init__(self):
        self.database = DataBase('pydb')
        self.user = UserModel('admin', 'admin', self.database)
        self.mailer = Mailer(SMTPOptions(
            'smtp.gmail.com',
            'kovacst.elod@gmail.com',
            'vxcntyhtymrodelw',
            587
        ))
        self.init()

    def get_db(self):
        return self.database

    def get_user(self):
        return self.user

    def get_mailer(self):
        return self.mailer

    def notify_user(self, notification):
        EmailNotifier(self.user, notification, self.mailer).notify_user()

    def init(self):
        if not self.database.table_exists(TemperatureHumidityModel.table_name):
            self.database.execute('CREATE TABLE ' + TemperatureHumidityModel.table_name
                                  + ' (temperature VARCHAR(20), humidity VARCHAR(20), device_id VARCHAR(20), '
                                    'time VARCHAR(20))')

        if not self.database.table_exists(BeamBreakModel.table_name):
            self.database.execute('CREATE TABLE ' + BeamBreakModel.table_name
                                  + ' (connection_status BOOLEAN, device_id VARCHAR(20), time VARCHAR(20))')
