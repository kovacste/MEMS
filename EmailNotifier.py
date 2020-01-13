import Email
import Notification
import User


class EmailNotifier:

    def __init__(self, user: User, notification: Notification, email: Email):
        self.user = user
        self.notification = notification
        self.email = email

    def notify_user(self):
        self.email.set_to(self.user.get_email())
        self.email.set_message(self.notification.get_message()).set_title(self.notification.get_title())
        self.email.send_email()

