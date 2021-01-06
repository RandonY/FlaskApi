from flask import Flask , request , render_template , abort, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

fake_data = {
        "06-01-2021":{              #date format DD-MM-YYYY
            "polluants": {
                "ozone":5,                     #indice entre 1 et 10 (indice ATMO)
                "dioxyde de souffre":3,        #indice entre 1 et 10 (indice ATMO)
                "dioxyde d'azote":7,           #indice entre 1 et 10 (indice ATMO)
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
                "dioxyde d'azote":2,           #indice entre 1 et 10
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

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/polluants')
def show_polluants_data():
    # show the user profile for that user
    date_info = fake_data.keys()
    for date in date_info:
        print("\n", date)
        meteo_info_key = fake_data.get(date).get("polluants").keys()
        for key in meteo_info_key:
            print(key, fake_data.get(date).get("polluants").get(key))
    return render_template('polluant.html')

@app.route('/meteo')
def show_meteo_data():
    # show the user profile for that user
    date_info = fake_data.keys()
    for date in date_info:
        print("\n",date)
        meteo_info_key = fake_data.get(date).get("meteo").keys()
        for key in meteo_info_key :
            print (key, fake_data.get(date).get("meteo").get(key))
    return render_template('meteo.html')

@app.route('/hopital')
def show_hopital_data():
    # show the user profile for that user
    date_info = fake_data.keys()
    for date in date_info:
        print(date , fake_data.get(date).get("hopital").get("nb entree urgence"))
    return render_template('hopital.html')

@app.route('/date/<date>')
def show_info_date(date):
    info_brut = fake_data.get(date)
    return info_brut

if __name__ == '__main__':
    app.run()