import streamlit as st

# ===============================
# Importar todas las vistas
# ===============================
from views import (
    river_monitor,
    forecast,
    comparar,
    estacion,
    materiales,
    conexion,
    comunicacion,
    impacto,
    emergencia,
    gemini_ai  # ⚠️ Asegúrate de que el archivo se llame `gemini_ia.py`, no `gemini_ai.py`
)

# ===============================
# Configuración general
# ===============================
st.set_page_config(page_title="Monitoreo del Río", layout="wide")

# Estilo personalizado global
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-size: 18px !important;
    }
    .stDataFrame div {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# Menú lateral de navegación
# ===============================
pagina = st.sidebar.selectbox("📌 Elige una opción", [
    "🌊 Ver cómo corre el río",
    "🔮 Adivinar el clima",
    "📊 Comparar cosas del clima",
    "🏠 Nueva Estación el Troje",
    "📦 Ver materiales del proyecto",
    "🌐 Conexión del Sistema",
    "📡 Otra forma de Comunicación",
    "⚠️ Impacto y Deslizamientos",
    "🧊 Zona de Emergencia: Quito sin Agua",
    "🤖 Ideas de nuestro robot de IA"
])

# ===============================
# Ruteo de vistas
# ===============================
if pagina == "🌊 Ver cómo corre el río":
    river_monitor.show()

elif pagina == "🔮 Adivinar el clima":
    forecast.show()

elif pagina == "📊 Comparar cosas del clima":
    comparar.show()

elif pagina == "🏠 Nueva Estación el Troje":
    estacion.show()

elif pagina == "📦 Ver materiales del proyecto":
    materiales.show()

elif pagina == "🌐 Conexión del Sistema":
    conexion.show()

elif pagina == "📡 Otra forma de Comunicación":
    comunicacion.show()

elif pagina == "⚠️ Impacto y Deslizamientos":
    impacto.show()

elif pagina == "🧊 Zona de Emergencia: Quito sin Agua":
    emergencia.show()

elif pagina == "🤖 Ideas de nuestro robot de IA":
    gemini_ai.show()  # Asegúrate de que este archivo exista en /views con esa función show()
