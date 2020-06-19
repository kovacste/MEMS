from flask import Flask, request, make_response, jsonify

from Email import Email
from EmailNotifier import EmailNotifier
from TemperatureHumidityModel import TemperatureHumidityModel
#from TemperatureHumiditySensor import TemperatureHumiditySensor
from SMTPOptions import SMTPOptions
from UserModel import UserModel
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
    user = UserModel(login_data['username'], login_data['password'], database)
    database.close()
    response = make_response("RESPONSE")
    response.set_cookie('API-KEY', value="HESS")
    return response


@app.route('/homeData', methods=["GET"])
def make_home_data_response():
    #temp_hum_sensor = TemperatureHumiditySensor()
    #hum = temp_hum_sensor.get_humidity()
    #temp = temp_hum_sensor.get_temp()
    model = TemperatureHumidityModel(DataBase('pydb'))
    latest_row = model.get_latest('1')
    return jsonify(latest_row)


@app.route('/tempStat', methods=["GET"])
def make_temp_data_response_for_stat():
    model = TemperatureHumidityModel(DataBase('pydb'))
    rows = model.get_latest('20')
    return jsonify(rows)


@app.route('/email')
def email_test():
    smtp_options = SMTPOptions(
        'smtp.gmail.com',
        'kovacst.elod@gmail.com',
        'vxcntyhtymrodelw',
        587
    )
    email = Email(smtp_options)
    email.set_to("kovacst.elod@gmail.com")\
        .set_message("Teszt uzenet")\
        .send_email()

    user = UserModel("admin", "admin", DataBase("pydb"))
    notificaion = Notificaion("Teszt notification", "Ez egy teszt email notification!")

    notifier = EmailNotifier(user, notificaion, email)
    notifier.notify_user()
