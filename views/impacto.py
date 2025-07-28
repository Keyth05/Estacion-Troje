import streamlit as st
import pandas as pd
from PIL import Image
import os

def show():
    st.markdown("<h1 style='text-align:center; font-size:36px;'>⚠️ Impacto y Deslizamientos - El Troje</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:20px; text-align:justify;'>
    En julio de 2025, fuertes lluvias provocaron un <strong>deslizamiento en la quebrada La Mica</strong>, dañado la infraestructura de conducción de agua que abastece la planta <strong>El Troje</strong>.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background-color:#ffcccc; padding:15px; border-radius:10px; text-align:center; color:#000000;'>
            <h4>📌 Parroquias Afectadas</h4>
            <p style='font-size:15px;'>Argelia<br>Quitumbe<br>Turubamba<br>Guamaní<br>La Ecuatoriana<br>Chillogallo</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='background-color:#ccf2ff; padding:15px; border-radius:10px; text-align:center; color:#000000;'>
            <h4>💧 Población Impactada</h4>
            <p style='font-size:15px;'>≈350 000–400 000<br>habitantes sin agua potable</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='background-color:#d6eaff; padding:15px; border-radius:10px; text-align:center; color:#000000;'>
            <h4>🌊 Infraestructura Dañada</h4>
            <p style='font-size:15px;'>≈350 m de tubería rota<br>Planta El Troje inoperativa</p>
        </div>
        """, unsafe_allow_html=True)

    imagen = os.path.join("fotos", "Datos 2025.png")
    if os.path.exists(imagen):
        img = Image.open(imagen)
        st.image(img, caption="📷 Daño en infraestructura tras el deslizamiento", width=800)

    st.markdown("---")

    # ❌ BLOQUE ELIMINADO (no se usa el archivo HTML)

    st.markdown("""
    <div style='font-size:18px; text-align:justify; margin-top:25px;'>
    El colapso fue provocado por la saturación del suelo tras lluvias intensas, lo que ocasionó la ruptura de parte del sistema de conducción <strong>Mica–Quito Sur</strong>, dejando inoperativa la planta El Troje. 
    Ante esta emergencia, se interrumpió el suministro de agua potable en seis parroquias del sur de Quito. 
    Las autoridades activaron un plan de contingencia con tanqueros para abastecer hospitales, escuelas y comunidades prioritarias. 
    El COE-M desplegó maquinaria y 70 operarios que lograron remover aproximadamente 180 000 m³ de escombros en un intento por restablecer el servicio.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='margin-top:30px; color:#FFCC00;'>📊 Resumen del Impacto</h4>", unsafe_allow_html=True)

    df_incidentes = pd.DataFrame({
        "Indicador": ["Parroquias sin agua", "Personas afectadas", "Longitud tubería dañada"],
        "Valor": ["6", "≈350 000–400 000", "≈350 m"]
    })

    st.table(df_incidentes)
