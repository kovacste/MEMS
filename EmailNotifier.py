import Email
import Notification
import UserModel


class EmailNotifier:

    def __init__(self, user, notification, email):
        self.user = user
        self.notification = notification
        self.email = email

    def notify_user(self):
        self.email.set_to(self.user.get_email())
        self.email.set_message(self.notification.get_message())
        self.email.set_subject(self.notification.get_title())
        self.email.send_email()

