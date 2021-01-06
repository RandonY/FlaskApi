from flask import Flask , request , render_template , abort, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

fake_data = []

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/polluants')
def show_polluants_data():
    # show the user profile for that user
    return render_template('polluant.html')

@app.route('/meteo')
def show_meteo_data():
    # show the user profile for that user
    return render_template('meteo.html')

@app.route('/hopital')
def show_hopital_data():
    # show the user profile for that user
    return render_template('hopital.html')

if __name__ == '__main__':
    app.run()