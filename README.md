# 🌊 Sistema de Monitoreo Ambiental en El Troje

Este proyecto es una plataforma web interactiva desarrollada en **Python** y **Streamlit**, orientada al monitoreo preventivo de condiciones ambientales en el sector **El Troje** (Quito, Ecuador), una zona con alta vulnerabilidad a eventos como deslizamientos o precipitaciones extremas.

La aplicación permite visualizar datos climáticos históricos, analizar variables mediante modelos de predicción y proponer una estación de monitoreo físico de bajo costo con soporte de inteligencia artificial.

---

## 🚀 Funcionalidades principales

- 📍 **Visualización geográfica de estaciones** (Rumihurco y propuesta en El Troje)
- 📊 **Monitoreo de datos climáticos**: precipitación, temperatura, humedad, radiación solar
- 🔮 **Módulo de predicción climática** usando regresión lineal
- 📈 **Comparación de variables normalizadas** en forma gráfica
- 🧰 **Diseño de estación de monitoreo física** con materiales y costos estimados
- 🧠 **IA Gemini** integrada para sugerencias de optimización presupuestaria
- 🌐 **Simulación de conexión remota 3G GSM** desde zonas rurales

---

## ⚙️ Instalación y ejecución

1. **Clona el repositorio:**

```bash
git clone https://github.com/Keyth05/troje-monitoring-platform.git
cd troje-monitoring-platform
```

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. Agrega tu archivo .env con la clave de API de Gemini:
```bash
GEMINI_API_KEY=tu_clave_aqui
```

## 🧠 Tecnología utilizada

- Python 3.12
- Streamlit para el frontend web interactivo
- Pandas / Matplotlib / Scikit-learn para análisis y predicción
- Folium para mapas
- Google Generative AI (Gemini) para asistencia inteligente
- OpenPyXL para exportar materiales a Excel


