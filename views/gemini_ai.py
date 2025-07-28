import os
import streamlit as st
import re
from scripts.gemini import configurar_gemini, consultar_gemini
from dotenv import load_dotenv

# ===========================
# Cargar .env para obtener la API key
# ===========================
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# ===========================


# Función para dar formato limpio a la respuesta generada
# ===========================
def formatear_respuesta(texto):
    import re

    # 1. Eliminar numeraciones tipo "1.", "2)", "3.*", incluso si están antes de subtítulos
    texto = re.sub(r'(?m)^\s*\d+[\.\)\-]?\s*(\*\s*)?', '', texto)

    # 2. Eliminar numeraciones embebidas como: "\n4. GSM", "5) * Batería:"
    texto = re.sub(r'(?m)(?:^|\n)\s*\d+[\.\)\-]?\s*(\*\s*)?', '\n', texto)

    # 3. Quitar asteriscos solos o delante de subtítulos
    texto = re.sub(r'(?m)^\s*\*\s*', '', texto)

    # 4. Reemplazar negritas Markdown por <strong>
    texto = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)
    texto = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', texto)

    # 5. Limpiar líneas vacías y unir párrafos
    lineas = [linea.strip() for linea in texto.strip().splitlines() if linea.strip()]
    parrafo = ""
    for linea in lineas:
        if linea.startswith("|") and linea.endswith("|"):
            parrafo += f"<p style='font-family: monospace;'>{linea}</p>"
        else:
            parrafo += linea + " "

    # 6. Devolver bloque HTML limpio
    return f"""
    <div style='background-color: #ffffff; color: #000000; padding: 20px; border-radius: 12px; border: 1px solid #ccc;
                font-size: 18px; line-height: 1.8; text-align: justify;'>
        <p>{parrafo.strip()}</p>
    </div>
    """


# ===========================
# Página principal
# ===========================
def show():
    #st.set_page_config(layout="wide")

    # Configurar modelo Gemini con clave del .env
    modelo = configurar_gemini(api_key)

    st.markdown("<h1 style='text-align: center; font-size: 40px;'>🤖 Asistente de Inteligencia Artificial</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Consulta sobre presupuesto, sensores o redes de comunicación</p>", unsafe_allow_html=True)

    # -----------------------
    # Optimización de presupuesto
    # -----------------------
    st.markdown("### 💰 <strong>Presupuesto del Proyecto</strong>", unsafe_allow_html=True)
    st.markdown("Costo estimado actual: <strong>$2500 USD</strong>", unsafe_allow_html=True)

    if st.button("💡 Optimizar presupuesto con IA"):
        with st.spinner("Consultando a Gemini..."):
            prompt = (
                "Redacta tu respuesta sin usar listas, números ni títulos."
                "Explica de forma sencilla cómo se puede reducir el costo de un sistema de monitoreo de agua. "
                "Haz recomendaciones prácticas, fáciles de entender para alguien que no es técnico. "
                "Usa frases cortas, evita palabras complicadas y da ejemplos concretos. "
                "La idea es ahorrar sin afectar la calidad del sistema."
                
            )
            respuesta = consultar_gemini(modelo, prompt)
            st.success("✅ Recomendación de Gemini:")
            st.markdown(formatear_respuesta(respuesta), unsafe_allow_html=True)

    st.markdown("---")

    # -----------------------
    # Comparación de tecnologías
    # -----------------------
    st.markdown("### 📶 <strong>Tecnología de Comunicación</strong>", unsafe_allow_html=True)
    st.markdown("Sensores conectados por red <strong>GSM o LoRaWAN</strong>", unsafe_allow_html=True)

    if st.button("💡 Evaluar tecnología con IA"):
        with st.spinner("Consultando a Gemini..."):
            prompt = (
                "Redacta tu respuesta sin usar listas, números ni títulos."
                "Compara GSM y LoRaWAN para enviar datos desde sensores en el campo, pero sin lenguaje técnico. "
                "Explica cuál es más barato, cuál funciona mejor en zonas alejadas y cuál gasta menos batería. "
                "Hazlo como si se lo explicaras a alguien que no sabe de tecnología, usando ejemplos simples."
                
            )
            respuesta = consultar_gemini(modelo, prompt)
            st.success("✅ Evaluación de Gemini:")
            st.markdown(formatear_respuesta(respuesta), unsafe_allow_html=True)
