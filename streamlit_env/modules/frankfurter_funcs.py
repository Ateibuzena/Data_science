import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import requests

@st.cache_data
def currency_evolution(currency, year):
    
    url = "https://api.frankfurter.app"

    date = f"{year}-01-01"
    
    if year != datetime.now().year:
        
        date_ = f"{year}-12-31"
        
        endpoint = f"{url}/{date}..{date_}?to={currency}"
        
    else:
        
        endpoint = f"{url}/{date}..?to={currency}"

    data = requests.get(endpoint).json()
    
    fechas = list(data["rates"].keys())

    fechas = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas]
    
    moneda = [data["rates"][fecha][currency] for fecha in data["rates"].keys()]

    df = pd.DataFrame(data    = np.array([fechas, moneda]).T,
                      columns = ["date", "currency"])
    
    return df

# def get_all_currencies():

    # data = requests.get(url = "https://api.frankfurter.app/currencies").json()

    # data = [f"{k} - {v}" for k, v in data.items() if k != "EUR"]

    # with open(file = "currencias.pkl", mode = "bw") as file:
    #     pickle.dump(obj = data, file = file)

    # with open(file = "currencies.pkl", mode = "br") as file:
    #     data = pickle.load(file = file)

    # return currencies