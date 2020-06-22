import smtplib, ssl
from email.mime.text import MIMEText


class Email:

    def __init__(self, smtp_options):
        self.to_address = ''
        self.port = 465
        self.message = ''
        self.subject = ''
        self.from_address = 'noreply@mysmarhome.hu'
        self.reply_to = ''
        self.cc = None
        self.bcc = None
        self.smtp_options = smtp_options

    def send_email(self):
        try:
            msg = MIMEText(self.message)
            msg['Subject'] = self.subject

            context = ssl.create_default_context()  # TODO::wat
            server = smtplib.SMTP(self.smtp_options.host, self.smtp_options.port)
            server.starttls()
            server.login(self.smtp_options.username, self.smtp_options.password)
            server.sendmail(self.from_address, self.to_address, msg.as_string())

        except Exception as e:
            print(e)

    def set_message(self, message):
        self.message = message
        return self

    def set_port(self, port):
        self.port = port
        return self

    def set_from(self, from_address):
        self.from_address = from_address
        return self

    def set_to(self, to_address):
        self.to_address = to_address
        return self

    def set_cc(self, cc):
        self.cc = cc
        return self

    def set_bcc(self, bcc):
        self.bcc = bcc
        return self

    def set_reply_to(self, reply_to):
        self.reply_to = reply_to
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self
