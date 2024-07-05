import streamlit as st
import seaborn as sns
import pandas as pd



# Especifica la ruta del archivo CSV
file_path = 'comite-etl-all.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()

selected_points = st.dataframe(
    df,
    key="df",
    on_select="rerun",
    selection_mode= ["multi-row","multi-column"],
    height=300

)

st.json(selected_points)

