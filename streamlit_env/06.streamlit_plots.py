import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    st.title("Plots")

    with st.expander(label = "DataFrame - Tips", expanded = False):
        df = sns.load_dataset(name = "tips")
        st.dataframe(df)

    # plt.scatter(x = df["total_bill"], y = df["tip"])
    # st.pyplot()

    fig, ax = plt.subplots()
    ax.scatter(x = df["total_bill"], y = df["tip"])
    plt.title("Total Bill vs Tip")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    st.pyplot(fig)


    fig = plt.figure()
    sns.countplot(x = df["sex"])
    st.pyplot(fig)

    fig = plt.figure()
    sns.scatterplot(x = df["total_bill"], y = df["tip"],
                    hue = df["smoker"], alpha = 0.5)
    st.pyplot(fig) 


    fig = plt.figure()
    sns.boxplot(x = df["day"], y = df["tip"], hue = df["smoker"])
    st.pyplot(fig) 


    fig, ax = plt.subplots(nrows = 2, ncols = 2)
    sns.histplot(x = df["total_bill"], kde = True, ax = ax[0, 0]);
    sns.countplot(x = df["size"], ax = ax[0, 1]);
    sns.scatterplot(x = df["tip"], y = df["size"], hue = df["smoker"], ax = ax[1, 0]);
    sns.boxplot(x = df["time"], y = df["total_bill"], ax = ax[1, 1]);
    st.pyplot(fig)


if __name__ == "__main__":
    main()