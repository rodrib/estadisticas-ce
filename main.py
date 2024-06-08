import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch

# with open("docs/introduction.md", "r") as f:
#     st.markdown(f.read())

# ui.date_picker()

st.header("Trabajos presentados al CEI (2019 a 2024)")
ui.badges(badge_list=[("shadcn", "default"), ("in", "secondary"), ("streamlit", "destructive")], class_name="flex gap-2", key="main_badges1")
st.caption("A Streamlit component library for building beautiful apps easily. Bring the power of Shadcn UI to your Streamlit apps!")
st.caption("Get started with pip install streamlit-shadcn-ui")


with ui.element("div", className="flex gap-2", key="buttons_group1"):
    ui.element("button", text="Get Started", className="btn btn-primary", key="btn1")
    ui.element("link_button", text="Github", url="https://github.com/ObservedObserver/streamlit-shadcn-ui", variant="outline", key="btn2")

st.subheader("Dashboard")

ui.tabs(options=['Overview', 'Analytics', 'Reports', 'Notifications'], default_value='Overview', key="main_tabs")

ui.date_picker(key="date_picker1")

cols = st.columns(3)
with cols[0]:
    # with ui.card():
    #     ui.element()
    ui.card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card1").render()
with cols[1]:
    ui.card(title="Subscriptions", content="+2350", description="+180.1% from last month", key="card2").render()
with cols[2]:
    ui.card(title="Sales", content="+12,234", description="+19% from last month", key="card3").render()

def generate_sales_data():
    np.random.seed(0)  # For reproducible results
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = np.random.randint(1000, 5000, size=len(months))
    return pd.DataFrame({'Month': months, 'Sales': sales})

with card_container(key="chart1"):
    st.vega_lite_chart(generate_sales_data(), {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(173, 250, 29)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Month', 'type': 'ordinal'},
            'y': {'field': 'Sales', 'type': 'quantitative', 'axis': {'grid': False}},
        },
    }, use_container_width=True)

# Sample data
data = [
    {"invoice": "INV001", "paymentStatus": "Paid", "totalAmount": 500, "paymentMethod": "Credit Card"},
    {"invoice": "INV002", "paymentStatus": "Unpaid", "totalAmount": 200, "paymentMethod": "Cash"},
    {"invoice": "INV003", "paymentStatus": "Paid", "totalAmount": 150, "paymentMethod": "Debit Card"},
    {"invoice": "INV004", "paymentStatus": "Unpaid", "totalAmount": 350, "paymentMethod": "Credit Card"},
    {"invoice": "INV005", "paymentStatus": "Paid", "totalAmount": 400, "paymentMethod": "PayPal"},
    # Add more records as needed
]

# Creating a DataFrame
invoice_df = pd.DataFrame(data)

with card_container(key="table1"):
    ui.table(data=invoice_df, maxHeight=300)


ui_result = ui.button("Button", key="btn")
st.write("UI Button Clicked:", ui_result)


##
import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'comite-etl1 - comite-etl1.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame en Streamlit
st.title('Mostrar DataFrame en Streamlit')
st.dataframe(df.head())


######
# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts = df['Proyecto/tesis/Resumen'].value_counts().reset_index()
resumen_counts.columns = ['Proyecto/tesis/Resumen', 'Cantidad']

# Mostrar gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de Proyecto/tesis/Resumen")
with card_container(key="chart2"):
    st.vega_lite_chart(resumen_counts, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(29, 250, 173)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Proyecto/tesis/Resumen', 'type': 'ordinal', 'axis': {'title': 'Proyecto/tesis/Resumen'}},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)


    # Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts = df['Proyecto/tesis/Resumen'].value_counts().reset_index()
resumen_counts.columns = ['Proyecto/tesis/Resumen', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'Proyecto/tesis/Resumen':")
st.write(resumen_counts)

###########
# Definir los datos
data = {
    'Proyecto/tesis/Resumen': ['Tesis', 'Proyecto', 'Tesis Maestria', 'Resumen', 'Ensayo clinico', 'Tesis Doctoral', 'Tesis Especialidad'],
    'Cantidad': [69, 52, 14, 7, 2, 1, 1]
}

# Crear el DataFrame
df1 = pd.DataFrame(data)

# Ordenar los datos por 'Cantidad' de mayor a menor
df1 = df1.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order = df1['Proyecto/tesis/Resumen'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de Proyecto/tesis/Resumen")
with card_container(key="chart2"):
    st.vega_lite_chart(df1, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(173, 250, 29)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Proyecto/tesis/Resumen', 'type': 'ordinal', 'axis': {'title': 'Proyecto/tesis/Resumen'}, 'sort': category_order},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)

# Calcular la cantidad para cada valor único en 'Cuanti/Cuali'
cantidad_por_categoria = df['Cuanti/Cuali'].value_counts().reset_index()
cantidad_por_categoria.columns = ['Cuanti/Cuali', 'Cantidad']

# Ordenar los datos por 'Cantidad' de mayor a menor
cantidad_por_categoria = cantidad_por_categoria.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order = cantidad_por_categoria['Cuanti/Cuali'].tolist()

# Mostrar el gráfico basado en Cuanti/Cuali
st.subheader("Distribución de Cuanti/Cuali")
with card_container(key="chart2"):
    st.vega_lite_chart(cantidad_por_categoria, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(29, 250, 173)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Cuanti/Cuali', 'type': 'ordinal', 'axis': {'title': 'Cuanti/Cuali'}, 'sort': category_order},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)


###########

# Calcular la cantidad para cada combinación única de 'Año' y 'Cuanti/Cuali'
cantidad_por_ano_categoria = df.groupby(['Año', 'Cuanti/Cuali']).size().reset_index(name='Cantidad')

# Ordenar los datos por 'Ano' y 'Cantidad'
cantidad_por_ano_categoria = cantidad_por_ano_categoria.sort_values(by=['Año', 'Cantidad'], ascending=[True, False])

# Obtener los años únicos
anos_unicos = cantidad_por_ano_categoria['Año'].unique().tolist()

# Mostrar el gráfico de barras agrupadas
st.subheader("Distribución de Cuanti/Cuali por Año")
with card_container(key="chart3"):
    st.vega_lite_chart(cantidad_por_ano_categoria, {
        "mark": "bar",
        "encoding": {
            "x": {"field": "Año", "type": "ordinal", "title": "Año"},
            "y": {"field": "Cantidad", "type": "quantitative", "title": "Cantidad"},
            "color": {"field": "Cuanti/Cuali", "type": "nominal", "title": "Cuanti/Cuali"}
        },
    }, use_container_width=True)