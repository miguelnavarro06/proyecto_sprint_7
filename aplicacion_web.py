import pandas as pd
import streamlit as st
import plotly.graph_objects as go
car_data = pd.read_csv('vehicles_us.csv')
st.header('Aplicacion basada en Streamlit')


hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma de la distribucion del odometro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

scattering_button = st.button('Construir diagrama de dispersion')
if scattering_button:
    st.write('Creación de un diagrama de dispersion que muestra la relacion entre el odometro y el precio')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relacion odometro vs precio')
    st.plotly_chart(fig, use_container_width=True)
    