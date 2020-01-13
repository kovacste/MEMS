from flask import Flask, request, make_response, jsonify

from Email import Email
from EmailNotifier import EmailNotifier
from SMTPOptions import SMTPOptions
from User import User
from Notification import Notificaion
from DataBase import DataBase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/login', methods=["POST"])
def login():
    database = DataBase('pydb')
    login_data = request.get_json(force=True)
    user = User(login_data['username'], login_data['password'], database)
    database.close()
    response = make_response("RESPONSE")
    response.set_cookie('API-KEY', value="HESS")
    return response


@app.route('/homeData', methods=["GET"])
def make_home_data_response():
    temp = 5
    return jsonify({'temp': temp})


@app.route('/email')
def email_test():
    smtp_options = SMTPOptions('smtp.gmail.com', 'kovacst.elod@gmail.com', 'vxcntyhtymrodelw', 587)
    email = Email(smtp_options)
    email.set_to("kovacst.elod@gmail.com").set_message("Teszt uzenet").send_email()

    user = User("admin", "admin", DataBase("pydb"))
    notificaion = Notificaion("Teszt notification", "Ez egy teszt email notification!")

    notifier = EmailNotifier(user, notificaion, email)
    notifier.notify_user()
