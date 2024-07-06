import streamlit as st
import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'comite-etl-all.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()

# Inicializar el estado de sesión si no está ya inicializado
if "df_selection" not in st.session_state:
    st.session_state.df_selection = {"selected_rows": [], "selected_columns": []}

# Muestra el DataFrame con la selección habilitada
selected_points = st.dataframe(
    df,
    key="df",
    height=300
)

# Obtener las filas y columnas seleccionadas
selected_rows = st.session_state.df_selection["selected_rows"]
selected_columns = st.session_state.df_selection["selected_columns"]

# Filtra el DataFrame original para obtener los datos seleccionados
if selected_rows and selected_columns:
    selected_data = df.iloc[selected_rows, selected_columns]
    
    # Mostrar los datos seleccionados
    st.write("Datos seleccionados:")
    st.dataframe(selected_data)
    
    # Guardar los datos seleccionados en un archivo CSV
    selected_data.to_csv('selected_data.csv', index=False)
    st.write("Datos seleccionados guardados en 'selected_data.csv'.")

# Mostrar el estado de selección en formato JSON
st.json(st.session_state.df_selection)


