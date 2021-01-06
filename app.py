from flask import Flask , request , render_template , abort, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

fake_data = []

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/polluants/<polluantname>')
def show_polluants_data(polluantname):
    # show the user profile for that user
    return show_polluants_info(polluantname)

@app.route('/meteo/<meteofactname>')
def show_meteo_data(meteofactname):
    # show the user profile for that user
    return show_meteo_info(meteofactname)

@app.route('/hopital/<hopitaldataname>')
def show_hopital_data(hopitaldataname):
    # show the user profile for that user
    return show_hopital_info(hopitaldataname)

if __name__ == '__main__':
    app.run()