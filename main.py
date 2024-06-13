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


##
import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'comite-etl-all.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()

# Mostrar las primeras filas del DataFrame en Streamlit
#st.title('Mostrar DataFrame')
#st.dataframe(df)



ui.table(data=df.head(), maxHeight=300)

st.write(ui.table)

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
#st.write(resumen_counts)

ui.table(data=resumen_counts, maxHeight=300)

st.write(ui.table)


###########
# Definir los datos
# Definir los datos
data = {
    'Proyecto/tesis/Resumen': ['Tesis', 'Proyecto', 'Trabajo de Investigacion', 'Tesis Maestria', 'Resumen', 'Ensayo Clinico', 'Tesis Doctoral', 'Tesis Especialidad'],
    'Cantidad': [174, 68, 64, 22, 7, 3, 2, 1]
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
st.subheader("Distribución de Tipo de Estudio por Año")
with card_container(key="chart3"):
    st.vega_lite_chart(cantidad_por_ano_categoria, {
        "mark": "bar",
        "encoding": {
            "x": {"field": "Año", "type": "ordinal", "title": "Año"},
            "y": {"field": "Cantidad", "type": "quantitative", "title": "Cantidad"},
            "color": {"field": "Cuanti/Cuali", "type": "nominal", "title": "Cuanti/Cuali"}
        },
    }, use_container_width=True)




########
import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from local_components import card_container

# Tu DataFrame con las columnas 'Politica' y 'Año'
# Asumiendo que tu DataFrame se llama df y tiene las columnas 'Politica' y 'Año'

# Calcular la cantidad para cada combinación única de 'Año' y 'Politica'
cantidad_por_ano_politica = df.groupby(['Año', 'Politica']).size().reset_index(name='Cantidad')

# Ordenar los datos por 'Año' y 'Cantidad'
cantidad_por_ano_politica = cantidad_por_ano_politica.sort_values(by=['Año', 'Cantidad'], ascending=[True, False])

# Obtener los años únicos
anos_unicos = cantidad_por_ano_politica['Año'].unique().tolist()

# Mostrar el gráfico de barras agrupadas
st.subheader("Temas Prioritarios")
with card_container(key="chart5"):
    st.vega_lite_chart(cantidad_por_ano_politica, {
        "mark": "bar",
        "encoding": {
            "x": {"field": "Año", "type": "ordinal", "title": "Año"},
            "y": {"field": "Cantidad", "type": "quantitative", "title": "Cantidad"},
            "color": {"field": "Politica", "type": "nominal", "title": "Politica"}
        },
    }, use_container_width=True)


    ###########




import streamlit_shadcn_ui as ui

st.header("Nube de palabras segun los Proyectos")

#with open("docs/components/tabs.md", "r") as f:
 #   st.markdown(f.read())



# import streamlit as st
# import streamlit_shadcn_ui as ui

# value = ui.tabs(options=['PyGWalker', 'Graphic Walker'], default_value='PyGWalker', key="kanaries")

# with ui.card(key="image"):
#     if value == "PyGWalker":
#         ui.element("img", src="https://pub-8e7aa5bf51e049199c78b4bc744533f8.r2.dev/pygwalker-banner.png", className="w-full")
#         ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
#     elif value == "Graphic Walker":
#         ui.element("img", src="https://pub-8e7aa5bf51e049199c78b4bc744533f8.r2.dev/graphic-walker-banner.png", className="w-full")
#         ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/graphic-walker", className="mt-2", key="btn2")

# # Mostrar el contenido de las pestañas
# st.write(ui.tabs)


########
import streamlit as st
import streamlit_shadcn_ui as ui

value = ui.tabs(options=['2019','2020','2021','2022','2023','2024'], default_value='2019', key="kanaries")

with ui.card(key="image"):
    if value == "2019":
        st.image("nube2019.png", caption="PyGWalker", use_column_width=True)
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == "2024":
        st.image("nube2024.png", caption="PyGWalker", use_column_width=True)
        #ui.element("img", src="https://pub-8e7aa5bf51e049199c78b4bc744533f8.r2.dev/graphic-walker-banner.png", className="w-full")
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/graphic-walker", className="mt-2", key="btn2")
    elif value == '2020':
        st.image("nube2020.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2021':
        st.image("nube2021.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2022':
        st.image("nube2022.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2023':
        st.image("nube2023.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
# Mostrar el contenido de las pestañas
st.write(ui.tabs)


import streamlit as st
import pandas as pd
import numpy as np

# Crear el DataFrame de la tabla proporcionada
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "Tema": [
        "Curso de Vida Salud materno infantil", "Enfermedades Transmisibles", "Enfermedades Transmisibles",
        "Enfermedades Transmisibles", "Enfermedades Transmisibles", "Enfermedades Transmisibles",
        "Organización del Sistema Sanitario", "Curso de Vida Salud materno infantil",
        "Organización del Sistema Sanitario", "Organización del Sistema Sanitario",
        "ECNT Salud mental", "Enfermedades Transmisibles", "ECNT Salud mental"
    ],
    "Subtema": [
        "Análisis del seguimiento de los casos de infecciones, desnutrición, y adicciones de las gestantes",
        "Evaluación de resultados de implementación de líneas de prevención y tratamiento de las enfermedades infecciosas más prevalentes (dengue, chikunguña, chagas)",
        "Enfermedades Transmisibles que se cronifican (Tuberculosis, Chagas, VIH)",
        "Prevención y control, alcances en el agua, animales y seres humanos.",
        "Análisis del diagnóstico y seguimiento de los casos de Sífilis y VIH",
        "Implementación y pilotaje de posibles innovaciones en la prevención y seguimiento de casos de patologías transmitidas por vectores, nuevas tecnologías; resistencias",
        "Evaluación de las gestiones hospitalarias y de centros de salud, así como de ciertos servicios de particular interés como guardias hospitalarias, y aquellos que presenten indicadores críticos o de excelencia.",
        "Análisis de las principales causas según criterio de reducibilidad",
        "CAPACITACIÓN para la GESTIÓN PÚBLICA Y SANITARIA: Necesidades a cubrir",
        "Relación entre la gestión, la calidad de atención y los indicadores de servicio",
        "Análisis del CONSUMO PROBLEMÁTICO DE SUSTANCIAS Y ADICCIONES (adolescentes y jóvenes, adultos)",
        "Casos de Sífilis congénita y expuestos perinatales VIH",
        "Análisis del seguimiento de los casos de infecciones, desnutrición, y adicciones de las gestantes; relación con las estadísticas perinatales y de mortalidad materna"
    ],
}

df = pd.DataFrame(data)

# Función para calcular la similitud del coseno
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# Función para convertir el texto en vectores utilizando la frecuencia de palabras
def text_to_vector(text, vocab):
    vector = np.zeros(len(vocab))
    for word in text.split():
        if word in vocab:
            vector[vocab[word]] += 1
    return vector

# Función para encontrar la categoría más similar
def find_most_similar_category(input_text, df):
    documents = df["Subtema"].tolist()
    documents.append(input_text)
    
    # Crear vocabulario
    vocab = {}
    for doc in documents:
        for word in doc.split():
            if word not in vocab:
                vocab[word] = len(vocab)
    
    input_vector = text_to_vector(input_text, vocab)
    max_similarity = -1
    most_similar_index = -1
    
    for i, doc in enumerate(documents[:-1]):
        doc_vector = text_to_vector(doc, vocab)
        similarity = cosine_similarity(input_vector, doc_vector)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_index = i
    
    return df.iloc[most_similar_index]["Tema"]

# Interfaz de usuario de Streamlit
st.title("Asignación de Categoría Basada en Resumen")

input_text = st.text_area("Ingrese el resumen del trabajo:")

if st.button("Asignar Categoría"):
    if input_text:
        categoria = find_most_similar_category(input_text, df)
        st.write(f"La categoría asignada es: **{categoria}**")
    else:
        st.write("Por favor, ingrese un resumen.")

# Mostrar la tabla de referencia
st.write("Tabla de Referencia:")
st.dataframe(df)
