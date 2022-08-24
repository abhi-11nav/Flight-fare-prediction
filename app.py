#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:12:02 2022

@author: abhinav
"""

from flask import Flask, render_template, request
import numpy as np 
import pandas as pd
import pickle 


app = Flask(__name__, template_folder="template")

model = pickle.load(open("modek.pkl", "rb"))

scaler = pickle.load(open("scaler.pkl","rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("/index.html")


@app.route("/", methods=["POST"])
def predict():
    if request.method == "POST":
        
        airline = request.form["airline"]
        if airline == "Jet Airways":
            Air_India = 0   
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 1 
            Multiple_carriers = 0 
            SpiceJet = 0
            Vistara = 0
        elif airline == "IndiGo":
            Air_India = 0
            GoAir = 0
            IndiGo = 1
            Jet_Airways = 0 
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
        elif airline == "Air India":
            Air_India = 1
            GoAir = 0
            IndiGo = 0
            Jet_Airways =0 
            Multiple_carriers = 0 
            SpiceJet = 0
            Vistara = 0
        elif airline == "Multiple Carriers":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0 
            Multiple_carriers = 1 
            SpiceJet = 0
            Vistara = 0
        elif airline == "SpiceJet":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
        elif airline == "Vistara":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Multiple_carriers =0 
            SpiceJet = 0
            Vistara = 1
        elif airline == "GoAir":
            Air_India = 0
            GoAir = 1
            IndiGo = 0
            Jet_Airways = 0 
            Multiple_carriers = 0  
            SpiceJet = 0
            Vistara = 0
        elif airline == "Air Asia":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
 
        date_of_Journey = request.form["departure_time"]
        travel_day = int(pd.to_datetime(date_of_Journey, format="%Y-%m-%dT%H:%M").day)
        travel_month = int(pd.to_datetime(date_of_Journey, format="%Y-%m-%dT%H:%M").month)
        
        source = request.form["source"]
        if source == "Delhi":
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0 
            Source_Mumbai = 0
        elif source == "Kolkata":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1 
            Source_Mumbai = 0
        elif source == "Chennai":
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
        elif source == "Mumbai":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata =0 
            Source_Mumbai = 1
        else:
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0 
            Source_Mumbai = 0
        
        
        destination = request.form["destination"]
        if destination == "Cochin":
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination == "Kolkata":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0 
            Destination_Kolkata = 1
            Destination_New_Delhi = 0
        elif destination == "Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0 
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination == "New Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0 
            Destination_Kolkata = 0
            Destination_New_Delhi = 1
        elif destination == "Hyderabad":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1 
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination == "Banglore":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0 
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
            
        departure_time = request.form["departure_time"]
        Departure_hour = int(pd.to_datetime(departure_time, format="%Y-%m-%dT%H:%M").hour)
        Departure_minute = int(pd.to_datetime(departure_time, format="%Y-%m-%dT%H:%M").minute)
        
        arrival_time = request.form["arrival_time"]
        Arrival_hour = int(pd.to_datetime(arrival_time, format="%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(arrival_time, format="%Y-%m-%dT%H:%M").minute)
        
        
        duration_hours = abs(Arrival_hour - Departure_hour)
        duration_minutes = abs(Arrival_minute - Departure_minute) 
        
        total_stops = int(request.form["total_stops"])
        
        features = np.array([total_stops, travel_day, travel_month, Arrival_hour,Arrival_minute, Departure_hour, Departure_minute,duration_hours, duration_minutes, Air_India, GoAir, IndiGo,Jet_Airways, Multiple_carriers, SpiceJet, Vistara,Source_Chennai, Source_Delhi, Source_Kolkata, Source_Mumbai,Destination_Cochin, Destination_Delhi, Destination_Hyderabad,Destination_Kolkata, Destination_New_Delhi])
                             
        pred = model.predict(features.reshape(1,-1))[0]
                
        return render_template("/index.html", prediction_text = "YOUR PREDICTED FLIGHT PRICE IS " + str(pred))
    

if __name__ == "__main__":
    app.run(debug=True)
        
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             