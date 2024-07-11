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
        color = "species",
        height=350,
    )


    selected_points = st.plotly_chart(
        scatter_chart,
        key="penguins",
        on_select="rerun",
    )

    st.dataframe(
        penguins.iloc[
            selected_points["selection"]["point_indices"]],
            height=350,
    )


crossfilter()