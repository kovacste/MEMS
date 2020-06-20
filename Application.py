from DataBase import DataBase
from Email import Email
from EmailNotifier import EmailNotifier
from SMTPOptions import SMTPOptions
from UserModel import UserModel


class Application:

    def __init__(self):
        self.database = DataBase('pydb')
        self.user = UserModel('admin', 'admin', self.database)
        self.mailer = Email(SMTPOptions(
            'smtp.gmail.com',
            'kovacst.elod@gmail.com',
            'vxcntyhtymrodelw',
            578
        ))

    def get_db(self):
        return self.database

    def get_user(self):
        return self.user

    def get_mailer(self):
        return self.mailer

    def notify_user(self, notification):
        EmailNotifier(self.user, notification, self.mailer).notify_user()
