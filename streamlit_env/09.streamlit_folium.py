import streamlit as st
import pandas as pd
# pip instal lxml

import folium
from modules.weather_func import *

# pip install streamlit_folium
from streamlit_folium import st_folium

def main():

    st.set_page_config(page_title = "Spain Weather - Streamlit",
                       page_icon  = ":cloud:",
                       layout     = "centered") # wide
    # Title
    st.title("OpenWeatherAPI & Streamlit :face_in_clouds:")
    st.markdown("Spain's current weather by capital.")

    # Weather Data
    df = get_weather_data()

    # DataFrame
    with st.expander(label = "Open Weather DataFrame", expanded = False):
        st.dataframe(df)
        st.write(f"DataFrame dimensions: {df.shape[0]}x{df.shape[1]}")
        st.balloons()

    # Mapa
    center = st.selectbox(label   = "Select capital:",
                          options = df["capital"].values,
                          index   = 26)

    map = folium.Map(location   =  df[df["capital"] == "Zamora"][["lat", "lon"]].values,
                     zoom_start = 5)

    # Data
    data_columns = ["capital", "temp", "lat", "lon"]
    points = folium.map.FeatureGroup()

    for capital, temp, lat, lng, in df[data_columns].values:

        display_info = f"Capital: {capital}\nTemp: {temp}"

        points.add_child(folium.Marker(location = [lat, lng],
                                       popup    = display_info))

    map.add_child(points)

    st_folium(fig = map, width = 1000)

    df_center = df[df["capital"] == center]

    st.write(f"Current weather in {center} :umbrella_with_rain_drops: :")
    st.write(df_center.iloc[0, :-2].to_dict())

if __name__ == "__main__":
    main()
