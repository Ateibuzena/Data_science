import streamlit as st

import numpy as np
import pandas as pd
import requests


def main():
    # Title
    st.title("Hello Streamlit App.")

    # Text
    st.text("Hello World!")
    st.text("New Line.")
    name = "Daniel"
    st.text("Prueba.")
    st.text("{}".format(name))

    # # Header
    st.header("Header1")

    # # Subheader
    st.subheader("Subheader1")

    # # Markdown
    st.markdown("# This is markdown.")

    # # Display Colored Text/Boostraps Alert
    st.success("Success.")
    st.warning("This is a WARNING.")
    st.info("Info.")
    st.error("This is an ERROR.")
    st.exception("This is an exception.")

    # .write()
    st.write("Normal Text.")
    st.write("## This is a markdown text")
    st.write(1 + 2)
    #st.dataframe(dir(st))

    # # Help
    st.help(range)

    # Display Data
    df = pd.read_csv(filepath_or_buffer = "sources/AccidentesBicicletas_2021.csv", sep = ";")
    
    # Dinamic Data
    st.dataframe(df)
    # st.write(df)

    # Static Table
    # st.table(df)

    # Adding Color
    # st.dataframe(df.select_dtypes(include=np.number).style.highlight_max(axis = 0, ))

    # Seleccionar columnas numéricas y aplicar estilo
    # numeric_columns = df.select_dtypes(include=np.number)
    # styled_df = numeric_columns.style.highlight_max(axis=0, color="orange")

    # Mostrar el DataFrame con estilo en Streamlit
    st.dataframe(styled_df)

    # Display JSON
    endpoint = "https://api.frankfurter.app/latest"
    response = requests.get(url = endpoint)
    st.json(response.json())

    # Display Code
    code = """
    def func():
        return x**2
    """
    st.code(body = code, language = "python")

if __name__ == "__main__":
    main()
    