# MEMS
MEMS beadandó 


# Fejlesztői dokumentáció

## A projekt célja
Okos otthon szolgáltatáshoz kényelmi, védelmi funkciókat ellátó hardware és software elkészítése. 

## Hardware
- Raspberry Pi 3 Model B+
- DHT11 Hőmérséklet és páratartalom érzékelő
- A2167 Infra LED-es fénysorompó

## Software
- Raspbian GNU/Linux 10 (buster) operációs rendszer
- Flask web framework
- Python 3.7

## A program működése
A programnak két fő belépési pontja van. Az első `app.py` aminek az elindításával Flask-es webszerver elindul, ez szolgálja ki a webes felületet a megjelenítendő adatokkal, valamint a `measuring_service.py` ami pedig folyamatos méréseket végez a bekapcsolt szenzorok segítségével.

## Mérések készítése
A mérések elindításához a measuring_service.py programot kell elindítanunk. Jelenleg két szenzor használatára van lehetőségünk, egy hőmérséklet- és páratartalom érzékelőre és egy infra ledes fénysorompóra.

### Hőmérséklet és páratartalom mérése
A hőmérséklet és páratartalom méréséhez példányosítanunk kell a `TemperatureHumiditySensor` osztályt, ami a konstruktorában annak a pin-nek a sorszámát várja, amihez a szenzorunk csatlakoztatva van. Az pillanatnyi értékek leolvasását az adott példány `get_temp()` valamint a `get_humidity()` függvényeivel tehetjük meg. Az osztály csak az aktuális érték leolvasására alkalmas, folyamatos méréshez az ütemezést az osztályon kívül kell megvalósítanunk. 
```python
from TemperatureHumiditySensor import TemperatureHumiditySensor

#példa a hőmérséklet és a páratartalom lekérdezésére
TEMP_HUM_PIN = 4
temp_hum_sensor = TemperatureHumiditySensor(TEMP_HUM_PIN)
current_temperature = temp_hum_sensor.get_temp()
current_humidity = temp_hum_sensor.get_humidity()
```

### Mozgás érzékelése
A mozgás érzékeléséhez a `BeamBreakSensor` egy példányára van szükségünk. Az osztály a konstruktorában annak a pin-nek a sorszámát várja, amihez csatlakoztatva van. A kapu állapotának vizsgálata folyamatosan történik, ha megszakad vagy újracsatlakozik egy esemény generálódik. Ezeknek az eseményeknek a kezelésére adhatunk meg metódusokat az `on_beam_break(callback_fn)` valamint az `on_beam_connect(callback_fn)` osztálymetódusok segítségével. A callback függvények egy `BeamBreakEvent` példányt kaptak meg paraméterként, melyek tartalmazzák az adott esemény keletkezésének idejét, leírását és a kapcsolat státuszát, mint `event_time` `event_description` és `connection_status` osztály változók.  A szenzor működését a `start()` metódussal indíthatjuk el, valamint a `stop()` metódussal állíthatjuk le.
```python
from BeamBreakSensor import BeamBreakSensor

#példa az infra kapu használatára

BEAM_PIN = 4
beam_sensor = BeamBreakSensor(BEAM_PIN)
beam_sensor.on_beam_connect(lambda event: BeamBreakEvent(  
    print('Handling beam connection event')  
))  
beam_sensor.on_beam_break(lambda event: BeamBreakEvent(  
    print('Handling beam break event')  
))
```

## Mérések naplózása
A mérések naplózását a szenzorokhoz tartozó modell osztályokkal lehet végezni. Az adatok mentése adatbázisba történik a `BreakBeamModel` és `TemperatureHumidityModel` osztályok `save_data()` metódusa segítségével a megfelelő paraméterek megadása mellett. 

```python

from DataBase import DataBase
from BeamBreakModel import BeamBreakModel
from TemperatureHumidityModel import TemperatureHumidityModel


BEAM_PIN = 4
TEMP_HUM_PIN = 4

"""A példa feltételezi a szükséges adatbázis struktúra meglétét"""
database = DataBase('pydb')
beam_sensor_model = BeamBreakModel(database)
temp_hum_model = TemperatureHumidityModel(database)

"""
paraméterben a kapuk aktuális állapota 'connection_status' False ha meg van szakítva, 
True ha nincs, valamint az eszköz azonosítója, hogy honnan jött az adott esemény
"""
beam_sensor_model.save_data(False, BEAM_PIN)

"""
paraméterben a hőmérséklet, a páratartalom, valamint az eszköz azonosítója, ahonnan a mérés
 érkezett
 """
temp_hum_model.save_data('27.0', '54.2', TEMP_HUM_PIN)
```

## Kommunikáció 
A felhasználó számára e-mail formájában van lehetőség információ átadásra. Adott felhasználólak e-mailes értesítés küldésére az `EmailNotifier` osztállyal van lehetőség, melynek konstruktora egy felhasználó `UserModel` egy értesítés `Notification` és egy levelező `Mailer` objektumot vár, majd a `notify_user()` osztály metódussal küldi el az adott értesítést. 

```python
from Mailer import Mailer
from SMTPOptions import SMTPOptions
from UserModel import UserModel
from Notification import Notification
from DataBase import DataBase
from EmailNotifier import EmailNotifier

data_base = DataBase('pydb')
smtp_options = SMTPOptions(  
    'smtp.gmail.com',
    'kovacst.elod@gmail.com',
    'password',
    587  
)
mailer = Mailer(smtp_options)

"""
A felhasználó kezelése nem képezi jelenleg a rendszer részét, 
a program működésében így csak minimális szerepet játszik
"""
user = UserModel('admin', 'admin', database)

notificaion = Notification("Értesítés címe", "Értesítés szövege")

email_notifier = EmailNotifier(user, notification, mailer).notify_user()
```

## Webes felület
Az alkalmazáshoz tartozó webes felületen a szenzorok által mért értékeket és észlelt eseményeket jelenítjük meg. A webes felület eléréséhez (csak development módban) el kell indítanunk az `app.py` programot és a Flask web framework elindít nekünk egy webszervert.
```python
from flask import Flask, request, make_response, jsonify


app = Flask(__name__)
if __name__ == '__main__':  
    # A hosztot '0.0.0.0'-ra állítva a webszerver nem csak lokálisan lesz elérhető 
    app.run(debug=True, host='0.0.0.0')
```
A gyökérútvonalon a szerver egy bejelentkező képernyővel válaszol. Belépést követően a frontend  meghatározott időközönként a `/homeData` címről GET kérésekre kapott legaktuálisabb adatokat megjeleníti, mint az aktuális hőmérsékletet, páratartalmat és az utolsó észlelt mozgás időpontját.

A `/homeData` kérést kezelő metódus:

```python
#adott útvonalú és típusú http kérés kezelő metódusa
@app.route('/homeData', methods=["GET"])  
def make_home_data_response():  
# az utolsó mért adatok lekérdezése adatbázisból és http válasz tartalmának visszaadádása 
    model = TemperatureHumidityModel(DataBase('pydb'))  
    latest_row = model.get_latest('1')  
    bb_model = BeamBreakModel(DataBase('pydb'))  
    return jsonify([latest_row, bb_model.get_latest('1')])
```


