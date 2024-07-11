import streamlit as st
import seaborn as sns
import plotly.express as px


penguins = sns.load_dataset("penguins")

@st.experimental_fragment
def crossfilter():
    scatter_chart = px.scatter(
        penguins,
        x = "bill_length_mm",
        y = "bill_depth_mm",


    )