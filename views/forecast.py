import streamlit as st
from scripts.plot import plot_forecast_module

def show():
    st.markdown("<h1 style='font-size: 38px;'>🔮 Adivinar cómo estará el clima</h1>", unsafe_allow_html=True)
    plot_forecast_module()
