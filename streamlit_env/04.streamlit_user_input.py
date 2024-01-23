import streamlit as st
import pandas as pd


# Text Input
name = st.text_input(label = "Name", 
                     max_chars = 20,
                     placeholder = "Tu nombre")


password = st.text_input(label = "Contraseña", 
                         placeholder = "Tu contraseña",
                         type = "password")

st.title(name)
st.title(password)

# Text Area
texto = st.text_area(label = "Enter Text", 
                    height = 150, 
                    max_chars = 2000,
                    placeholder = "Review")
st.write(texto)

# Input Numbers
number = st.number_input(label = "Enter Number",
                        min_value = -256,
                        max_value = 255,
                        value = 0,
                        step = 10)

# Date Input
fecha = st.date_input(label = "Tutoria")

# Time Input
tiempo = st.time_input(label = "Hora")

# Color Picker
color = st.color_picker("Select Color")
st.write(f"Your color: {color}")