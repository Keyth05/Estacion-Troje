import streamlit as st
from scripts.plot import comparar_variables

def show():
    st.markdown("<h1 style='font-size: 38px;'>📊 Ver qué cosas del clima cambian</h1>", unsafe_allow_html=True)
    comparar_variables()
