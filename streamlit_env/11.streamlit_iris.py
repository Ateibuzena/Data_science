import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def main():

    st.title("Iris Prediction with Streamlit & Sklearn.")

    iris = load_iris()

    X, y = iris["data"], iris["target"]
    target = iris["target_names"]
    feature_names = iris["feature_names"]

    df = pd.DataFrame(data = X, columns = feature_names)    

    with st.expander(label = "DataFrame Iris", expanded = False):
        st.dataframe(df)
        st.snow()

    sepal_length = st.slider(label = feature_names[0],
                             min_value = df[feature_names[0]].min(),
                             max_value = df[feature_names[0]].max(),
                             value = float(df[feature_names[0]].mean()))

    sepal_width = st.slider(label = feature_names[1],
                             min_value = df[feature_names[1]].min(),
                             max_value = df[feature_names[1]].max(),
                             value = float(df[feature_names[1]].mean()))

    petal_length = st.slider(label = feature_names[2],
                             min_value = df[feature_names[2]].min(),
                             max_value = df[feature_names[2]].max(),
                             value = float(df[feature_names[2]].mean()))

    petal_width = st.slider(label = feature_names[3],
                             min_value = df[feature_names[3]].min(),
                             max_value = df[feature_names[3]].max(),
                             value = float(df[feature_names[3]].mean()))

    data = [sepal_length, sepal_width, petal_length, petal_width]

    df_usuario = pd.DataFrame(data = [data], columns = feature_names)
    st.dataframe(df_usuario)

    model = RandomForestClassifier()
    model.fit(X, y)

    yhat = model.predict(df_usuario.values)

    st.success(f"La flor es **{[target[y] for y in yhat][0]}**")

    st.write("Probabilidad de pertenecer a cada clase:")
    st.dataframe(pd.DataFrame(model.predict_proba(df_usuario.values), columns = target))

if __name__ == "__main__":
    main()
    