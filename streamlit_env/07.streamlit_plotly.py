import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
import plotly.express as px
from modules.page_config_dict import PAGE_CONFIG

st.set_page_config(**PAGE_CONFIG)



def main():

    st.title("Streamlit App. & Plotly.")
    with st.expander(label = "DataFrame - Accidentes Bicicletas 2021", expanded = False):
        df = pd.read_csv(filepath_or_buffer = "sources/AccidentesBicicletas_2021.csv", sep = ";")
        st.dataframe(df)

    with st.expander(label = "DataFrame - Accidentes Bicicletas 2021 GroupBy Distrito", expanded = False):    
        df1 = df.groupby(by = "distrito", as_index = False)["num_expediente"].count()
        st.dataframe(data = df1, use_container_width = True)

    fig_pie = px.pie(data_frame = df1,
                     names      = "distrito",
                     values     = "num_expediente",
                     title      = "Num. Accidentes por Distrito")
    st.plotly_chart(figure_or_data = fig_pie, use_container_width = True)
    
    fig_bar = px.bar(data_frame = df1,
                     x          = "distrito",
                     y          = "num_expediente",
                     title      = "Num. Accidentes por Distrito")
    st.plotly_chart(figure_or_data = fig_bar, use_container_width = True)

    # Streamlit Plots
    
    with st.expander(label = "DataFrame - Diamonds", expanded = False):
        df2 = sns.load_dataset("taxis")
        df2 = df2.dropna().iloc[:50, :]
        df2 = df2.sort_values("pickup")
        st.dataframe(df2)

    # Bar Chart
    st.bar_chart(df2[["total", "fare"]])

    # Line Chart
    columns_list = df2._get_numeric_data().columns
    columns_choices = st.multiselect(label = "Choose Columns", options = columns_list, default = columns_list[-1])
    df2_filter = df2[columns_choices]
    st.line_chart(df2_filter)

    # Area Chart
    st.area_chart(df2_filter)

if __name__ == "__main__":
    main()