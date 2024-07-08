import streamlit as st
import pandas as pd

data = {
    'Fruit': ['Manzana', 'Plátano', 'Cereza', 'Dátil', 'Baya de saúco'],
    'Cantidad': [10, 15, 20, 25, 30],
    'Precio': [0.5, 0.25, 0.75, 1.0, 2.0]
}
df = pd.DataFrame(data)

st.dataframe(df)

columna = st.selectbox('Seleccionar columna para filtrar', df.columns)

# Verificar si la columna seleccionada es numérica
if pd.api.types.is_numeric_dtype(df[columna]):
    valor_min, valor_max = st.slider('Seleccionar rango de valores', min(df[columna]), max(df[columna]), (min(df[columna]), max(df[columna])))

    df_filtrado = df[(df[columna] >= valor_min) & (df[columna] <= valor_max)]
    st.dataframe(df_filtrado)
else:
    st.warning(f'La columna "{columna}" seleccionada no es numérica. No se puede aplicar el filtro.')
