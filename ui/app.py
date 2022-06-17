from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
import datetime
from sklearn.tree import DecisionTreeRegressor

dtr = pickle.load(open('cabfare.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        data1 = request.form["day"]
        day = int(pd.to_datetime(data1, format="%Y-%m-%dT%H:%M").day)
        Month = int(pd.to_datetime(data1, format ="%Y-%m-%dT%H:%M").month)
        year= int(pd.to_datetime(data1, format ="%Y-%m-%dT%H:%M").year)
        Hour = int(pd.to_datetime(data1, format ="%Y-%m-%dT%H:%M").hour)
        Minute = int(pd.to_datetime(data1, format ="%Y-%m-%dT%H:%M").minute)
        data2=request.form["DayofWeek"]
        data3=request.form['passenger_count']
        data4=request.form['distance']
        data=[[day,Month,year,Hour,Minute,data2,data3,data4]]
        prediction=dtr.predict(data)[0]
    return render_template('index.html',prediction="Your cab price is {} ".format(prediction))

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/ContactUs.html') 
def info():
    return render_template('ContactUs.html')


if __name__ == "__main__":
    app.run(debug=True)