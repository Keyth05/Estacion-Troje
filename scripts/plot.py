import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 🔮 Módulo de predicción (Forecasting)
def plot_forecast_module():
    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6, p, label, .stButton>button {
            font-size: 18px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='font-size: 40px;'>🔮 Módulo de Predicción (Forecasting)</h1>", unsafe_allow_html=True)

    file = st.selectbox("Selecciona la serie de tiempo:", [
        "C03-Rumihurco_Temperatura_ambiente-Mensual.csv",
        "C02-Rumihurco_Precipitación-Mensual.csv",
        "C03-Rumihurco_Humedad_relativa-Mensual.csv",
        "C03-Rumihurco_Radiación_solar-Mensual.csv"
    ])

    df = pd.read_csv(f"data/{file}")
    df['fecha'] = pd.to_datetime(df['fecha'])
    df = df.sort_values('fecha')

    # ⚠️ Verifica y elimina valores faltantes
    if df['valor'].isnull().any():
        st.warning("⚠️ Se encontraron valores vacíos en la columna 'valor'. Serán eliminados para continuar.")
        df = df.dropna(subset=['valor'])

    # Predecir
    dias_pred = st.slider("Días a predecir:", 30, 365, 90)

    df['n'] = np.arange(len(df))
    X = df['n'].values.reshape(-1, 1)
    y = df['valor'].values.reshape(-1, 1)

    modelo = LinearRegression()
    modelo.fit(X, y)

    X_pred = np.arange(len(df), len(df) + dias_pred).reshape(-1, 1)
    y_pred = modelo.predict(X_pred)

    fechas_pred = pd.date_range(df['fecha'].iloc[-1], periods=dias_pred + 1, freq='M')[1:]

    # Visualización
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['fecha'], y, label="Histórico", marker='o')
    ax.plot(fechas_pred, y_pred, label="Predicción", linestyle='--')
    ax.set_title("Pronóstico de " + file.split("_")[1])
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 📊 Comparación de Variables Normalizadas
def comparar_variables():
    st.markdown("<h1 style='font-size: 40px;'>📊 Comparación Múltiple de Variables</h1>", unsafe_allow_html=True)

    archivos = st.multiselect("Selecciona archivos para comparar:", [
        "C03-Rumihurco_Temperatura_ambiente-Mensual.csv",
        "C02-Rumihurco_Precipitación-Mensual.csv",
        "C03-Rumihurco_Humedad_relativa-Mensual.csv",
        "C03-Rumihurco_Radiación_solar-Mensual.csv"
    ])

    if len(archivos) >= 2:
        df_comparacion = pd.DataFrame()

        for archivo in archivos:
            df_temp = pd.read_csv(f"data/{archivo}")
            df_temp['fecha'] = pd.to_datetime(df_temp['fecha'])
            df_temp = df_temp.sort_values('fecha')
            df_temp.set_index('fecha', inplace=True)

            # Eliminar NaN
            df_temp = df_temp.dropna(subset=['valor'])

            variable = archivo.split("_")[1]
            df_comparacion[variable] = (df_temp['valor'] - df_temp['valor'].min()) / (df_temp['valor'].max() - df_temp['valor'].min())

        st.line_chart(df_comparacion)
    else:
        st.warning("Selecciona al menos 2 archivos para comparar.")
