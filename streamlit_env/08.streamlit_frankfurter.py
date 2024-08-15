import streamlit as st
import plotly.express as px
import modules.frankfurter_funcs as ffunc
from modules.currencies import currencies
from datetime import datetime

def main():

    st.title("Frankfurter API App.")
    st.markdown("""Simple script that calls the `Frankfurter API` and shows the EUR's evolution compared
                   to another currency over a selected year.""")

    currency = st.selectbox(label = "Select Currency", options = currencies)

    year = st.slider(label     = "Select Year",
                     min_value = 2015,
                     max_value = datetime.now().year,
                     value     = datetime.now().year - 1)
    
    currency = currency.split(" - ")[0]

    df = ffunc.currency_evolution(currency = currency, year = year)
    df.rename(mapper = {"currency" : currency}, axis = 1, inplace = True)

    with st.expander(label = "Frankfurter DataFrame", expanded = False):
        st.dataframe(df)

    df["month"] = df["date"].apply(lambda x : x.strftime("%B"))

    # Line Chart
    line_fig = px.line(data_frame = df,
                       x          = "date",
                       y          = currency,
                       title      = f"{currency} - EUR Relationship")
  
    # Lineas (Mean, Median, Max, Min)
    line_fig.add_hline(y = df[currency].mean(),
                       line_dash = "dash",
                       line_color = "blue",
                       line_width = 1,
                       annotation_position = "top left",
                       annotation_text = f"mean {df[currency].mean().round(2)}")

    line_fig.add_hline(y = df[currency].median(),
                       line_dash = "dash",
                       line_color = "yellow",
                       line_width = 1,
                       annotation_position = "bottom right",
                       annotation_text = f"median {df[currency].median().round(2)}")


    line_fig.add_hline(y = df[currency].max(),
                       line_dash = "dash",
                       line_color = "green",
                       line_width = 1,
                       annotation_position = "bottom right",
                       annotation_text = f"max {round(df[currency].max(), 2)}")


    line_fig.add_hline(y = df[currency].min(),
                       line_dash = "dash",
                       line_color = "red",
                       line_width = 1,
                       annotation_position = "bottom right",
                       annotation_text = f"min {round(df[currency].min(), 2)}")       

    hist_fig = px.histogram(data_frame = df, x = currency,  nbins = 50, opacity = 0.8)

    box_fig = px.box(data_frame = df, x = currency)

    # Plots
    st.plotly_chart(line_fig)
    st.plotly_chart(hist_fig)
    st.plotly_chart(box_fig)

    # Color
    line_fig2 = px.line(data_frame = df,
                       x           = "date",
                       y           = currency,
                       color       = "month",
                       title       = f"{currency} - EUR Relationship")

    hist_fig2 = px.histogram(data_frame = df, x = currency, color = "month",  nbins = 50, opacity = 0.8)

    box_fig2 = px.box(data_frame = df, x = currency, color = "month")

    # Plots 2
    st.plotly_chart(line_fig2)
    st.plotly_chart(hist_fig2)
    st.plotly_chart(box_fig2)

if __name__ == "__main__":
    main()
