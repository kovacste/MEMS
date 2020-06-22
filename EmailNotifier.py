import Mailer
import Notification
import UserModel


class EmailNotifier:

    def __init__(self, user: UserModel, notification: Notification, mailer: Mailer):
        self.user = user
        self.notification = notification
        self.mailer = mailer

    def notify_user(self):
        self.mailer.set_to(self.user.get_email())
        self.mailer.set_message(self.notification.get_message())
        self.mailer.set_subject(self.notification.get_title())
        self.mailer.send_email()

