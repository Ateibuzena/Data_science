import pandas as pd
import requests
from time import sleep
import streamlit as st

api_key = "cd31574dc65a379909d4f921033a7e96"

@st.cache_data
def read_page():

    df = pd.read_html(io = "https://www.ign.es/web/ane-datos-geograficos/-/datos-geograficos/datosPoblacion?tipoBusqueda=capitales")

    df = df[1]

    # Transform Lat & Lon
    df["Lat ETRS89"] = df["Lat ETRS89"]/100_000_000
    df["Lon ETRS89"] = df["Lon ETRS89"]/100_000_000

    # Rename columns
    df.rename(mapper = {col : col.split(" ")[0] for col in df.columns if "ETRS89" in col}, axis = 1, inplace = True)

    return df


@st.cache_data
def get_weather_data():

    df = read_page()
    weather_data = list()

    for lat, lon in df[["Lat", "Lon"]].values:
        
        weather_endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
        data = requests.get(url = weather_endpoint).json()
        
        try:
            description = data["weather"][0]["description"]
            temp        = data["main"]["temp"]
            feels_like  = data["main"]["feels_like"]
            temp_min    = data["main"]["temp_min"]
            temp_max    = data["main"]["temp_max"]
            pressure    = data["main"]["pressure"]
            humidity    = data["main"]["humidity"]
            wind_speed  = data["wind"]["speed"]
            dt          = data["dt"]
            lat         = data["coord"]["lat"]
            lon         = data["coord"]["lon"]
            name        = data["name"]
            
            weather_data.append([name, description, temp, feels_like, temp_min,
                                temp_max, pressure, humidity, wind_speed, dt, lat, lon])
        except:
            pass
                
        sleep(0.1)

    df_weather = pd.DataFrame(data = weather_data,
                          columns = ["capital", "description", "temp", "feels_like", "temp_min",
                                     "temp_max", "pressure", "humidity", "wind_speed", "dt", "lat", "lon"])
    
    return df_weather
