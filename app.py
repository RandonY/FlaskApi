from flask import Flask , request , render_template , abort, redirect, url_for
from markupsafe import escape
import pandas as pd


app = Flask(__name__)

fake_data = {
        "06-01-2021":{              #date format DD-MM-YYYY
            "polluants": {
                "ozone":5,                     #indice entre 1 et 10 (indice ATMO)
                "dioxyde de souffre":3,        #indice entre 1 et 10 (indice ATMO)
                "particule fine":4             #indice entre 1 et 10 (indice ATMO)
            },
            "meteo":{
                "temperature": 16.4,           #en °C
                "pluie": 0,                    #en mm/h
                "vent": 5,                     #en km/h
                "pression":1018.4              #en hPa
            },
            "hopital":{
                "nb entree urgence":500
            }
        },

        "07-01-2021":{              #date format DD-MM-YYYY
            "polluants": {
                "ozone":6,                     #indice entre 1 et 10
                "dioxyde de souffre":1,        #indice entre 1 et 10
                "particule fine":6             #indice entre 1 et 10
            },
            "meteo":{
                "temperature": 17.4,           #en °C
                "pluie": 1,                    #en mm/h
                "vent": 7,                     #en km/h
                "pression":1020.7             #en hPa
            },
            "hopital":{
                "nb entree urgence":450
            }
        }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polluants')
def show_polluants_data():
    date_info = fake_data.keys()
    polluants_data = []
    for date in date_info:
        polluants_data.append([date, fake_data.get(date).get("polluants").get("ozone"),
                                     fake_data.get(date).get("polluants").get("dioxyde de souffre"),
                                     fake_data.get(date).get("polluants").get("particule fine")])
    return render_template('polluants.html', polluants_data = polluants_data)


@app.route('/meteo')
def show_meteo_data():
    date_info = fake_data.keys()
    meteo_data = []
    for date in date_info:
        meteo_data.append([date, fake_data.get(date).get("meteo").get("temperature"),
                               fake_data.get(date).get("meteo").get("pluie"),
                               fake_data.get(date).get("meteo").get("vent"),
                               fake_data.get(date).get("meteo").get("pression")
                           ])
    return render_template('meteos.html', meteo_data=meteo_data)


@app.route('/hopital')
def show_hopital_data():
    # show the user profile for that user
    date_info = fake_data.keys()
    hopital_data= []
    for date in date_info:
        hopital_data.append([date, fake_data.get(date).get("hopital").get("nb entree urgence")])
    return render_template("hopitals.html", hopital_data = hopital_data)

@app.route('/date/<date>')
def show_info_date(date):
    info_brut = fake_data.get(date)
    return info_brut

if __name__ == '__main__':
    app.run(debug=True)