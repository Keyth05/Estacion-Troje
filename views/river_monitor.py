import streamlit as st
import pandas as pd
from scripts.load_data import cargar_datos_csv
from scripts.mapa import crear_mapa
import os
import streamlit.components.v1 as components


def show():
    st.markdown("<h1 style='font-size: 42px;'>🌊 Ver cómo corre el río</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Mira si hay poca o mucha agua, y si todo está bien o hay peligro.</p>", unsafe_allow_html=True)

    with st.expander("📘 ¿De qué trata esto?"):
        st.markdown("""
        - 📍 Está en un lugar llamado El Troje.  
        - 🚨 A veces no sabemos si habrá peligro.  
        - 💡 Con sensores y pantallas, podemos ver qué pasa.  
        - 💰 Cuesta $2500 y se hace en 3 semanas.  
        - 👥 Ayuda a muchas familias
        """)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<h3 style='font-size: 28px;'>📍 Aquí están los sensores</h3>", unsafe_allow_html=True)
        components.html(crear_mapa(), height=500)


    with col2:
        st.markdown("<h3 style='font-size: 28px;'>📊 Tabla con lluvias y alertas</h3>", unsafe_allow_html=True)
        df = cargar_datos_csv("data/P03-Rumihurco_Machángara_Precipitación-Mensual.csv")
        df_last12 = df.sort_values('fecha', ascending=False).head(12).sort_values('fecha')
        df_last12['estado'] = df_last12['valor'].apply(lambda x: '🔴 Alerta' if x < 10 else '🟢 OK')
        st.dataframe(df_last12[['fecha', 'valor', 'estado']])
