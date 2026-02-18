# Import Required Libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import requests
import os

# Load the model
model = joblib.load('power_prediction.sav')

# Initialize the app
app = Flask(
    __name__
)

# Configure API End-Points and Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/windapi', methods=['POST'])
def windapi():
    city = request.form.get('city')
    apikey = os.getenv('OPENWEATHER_API_KEY')
    url = r'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apikey
    resp = requests.get(url)
    resp = resp.json()
    temp = str(round(resp['main']['temp'] - 273, 1)) + ' °C'
    humid = str(resp['main']['humidity']) + ' %'
    pressure = str(resp['main']['pressure']) + ' hPa'
    speed = str(resp['wind']['speed']) + ' m/s'

    return render_template('predict.html', temp=temp, humid=humid, pressure=pressure, speed=speed)

@app.route('/y_predict', methods=['POST'])
def y_predict():
    '''
    For rendereing results on HTML GUI
    '''
    val_X = [[float(x) for x in request.form.values()]]

    prediction = model.predict(val_X)
    print(prediction)
    output = prediction[0]

    return render_template('predict.html', prediction_text=f'The energy predicted is {output:.2f} KWh')
