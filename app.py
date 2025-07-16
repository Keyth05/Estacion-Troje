import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os
import re
from scripts.load_data import cargar_datos_csv
from scripts.alerts import verificar_alerta
from scripts.mapa import crear_mapa
from scripts.gemini import configurar_gemini, consultar_gemini
from scripts.plot import plot_forecast_module, comparar_variables
from scripts.estacion import mostrar_estacion_troje
from PIL import Image
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()



# =======================================
# CONFIGURACIONES GENERALES
# =======================================
st.set_page_config(layout="wide")
API_KEY = os.getenv("GEMINI_API_KEY")
modelo = configurar_gemini(API_KEY)

# CSS personalizado
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 18px !important;
    }
    .stDataFrame div {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# =======================================
# FUNCIONES DE LIMPIEZA DE RESPUESTA
# =======================================
def formatear_respuesta(texto):
    resumen_limpio = {
        "1.": "Para que el sistema cueste menos, podemos usar sensores más baratos que igual hacen bien su trabajo. También podemos usar sensores que no necesitan cables y así ahorrar. Si tenemos sensores viejitos que aún sirven, los usamos de nuevo. Y si necesitamos muchos sensores, es mejor comprar muchos de una sola vez porque salen más baratos. Otra opción es usar computadoras pequeñitas como Arduino, que ayudan y no cuestan mucho.",
        "2.": "El software es como el cerebro del sistema. En lugar de pagar por programas caros, podemos usar programas gratis que hacen lo mismo. Algunos ya existen en internet y los podemos usar sin pagar nada.",
        "3.": "Cuando instalamos todo, es bueno hacerlo bien desde el comienzo. Por ejemplo, no poner cosas de más. También es mejor si el sistema se puede cambiar o mejorar después sin tener que gastar mucho.",
        "4.": "Si el lugar no necesita cosas muy complicadas, se puede usar una forma más simple de monitorear. A veces, con revisar cada cierto tiempo a mano también está bien. También podemos unir este sistema con otros que ya existen para ahorrar."
    }
    cuerpo = ""
    for clave, valor in resumen_limpio.items():
        cuerpo += f"<p><strong>{clave}</strong> {valor}</p>"
    return f"""
        <div style='background-color: #ffffff; color: #000000; padding: 20px; border-radius: 12px;
                    border: 1px solid #ccc; font-size: 18px; line-height: 1.8; text-align: justify;'>
            {cuerpo}
        </div>
    """

# =======================================
# CARGAR DATOS Y PÁGINAS
# =======================================
pagina = st.sidebar.selectbox("Elige una opción", [
    "🌊 Ver cómo corre el río",
    "🔮 Adivinar el clima",
    "📊 Comparar cosas del clima",
    "🏠 Nueva Estación el Troje",
    "📦 Ver materiales del proyecto",
    "🌐 Conexión del Sistema",
    "📡 Otra forma de Comunicación",
    "⚠️ Impacto y Deslizamientos",
    "🤖 Ideas de nuestro robot de IA"
])

# ---------------------------------------
if pagina == "🌊 Ver cómo corre el río":
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

# ---------------------------------------
elif pagina == "🔮 Adivinar el clima":
    st.markdown("<h1 style='font-size: 38px;'>🔮 Adivinar cómo estará el clima</h1>", unsafe_allow_html=True)
    plot_forecast_module()

# ---------------------------------------
elif pagina == "📊 Comparar cosas del clima":
    st.markdown("<h1 style='font-size: 38px;'>📊 Ver qué cosas del clima cambian</h1>", unsafe_allow_html=True)
    comparar_variables()

# ---------------------------------------
elif pagina == "🏠 Nueva Estación el Troje":
    mostrar_estacion_troje()

# ---------------------------------------
elif pagina == "📦 Ver materiales del proyecto":
    st.markdown("<h1 style='font-size: 38px;'>📦 Visualización de Materiales del Proyecto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Aquí puedes ver cada componente con su imagen, cantidad y costo estimado.</p>", unsafe_allow_html=True)

    materiales = [
        ("Sensor de Precipitación (Pluviómetro de balancín)", "Sensor de Precipitación (Pluviómetro de balancín).jpg", "1", "40.00 $"),
        ("Sensor de Temperatura y Humedad (DHT22)", "Sensor de Temperatura y Humedad (DHT22).webp", "1", "10.00 $"),
        ("Sensor de Radiación Solar (TSL2561 o similar)", "Sensor de Radiación Solar (TSL2561 o similar).jpg", "1", "12.00 $"),
        ("Microcontrolador (ESP32 con WiFi)", "Microcontrolador (ESP32 con WiFi).jpg", "1", "18.00 $"),
        ("Módulo de Almacenamiento MicroSD", "Módulo de Almacenamiento MicroSD.webp", "1", "4.00 $"),
        ("Panel Solar 5V + Controlador de Carga", "Panel Solar 5V + Controlador de Carga.png", "1", "20.00 $"),
        ("Batería Recargable (Li-ion 18650)", "Batería Recargable (Li-ion 18650).webp", "2", "10.00 $"),
        ("Caja Estanca - Aislante", "Caja Estanca - Aislante.jpg", "1", "15.00 $"),
        ("Soporte Metálico - PVC para fijación", "Soporte Metálico - PVC para fijación.jpg", "1", "10.00 $"),
        ("Cables, conectores y protoboard", "Cables, conectores y protoboard.jpg", "Varios", "8.00 $"),
        ("Módulo RTC (reloj en tiempo real)", "Módulo RTC (reloj en tiempo real).png", "1", "6.00 $"),
        ("Costo de instalación y mano de obra", "Costo de instalación y mano de obra.png", "1", "20.00 $"),
    ]

    for nombre, imagen, cantidad, costo in materiales:
        st.markdown("<div style='display: flex; align-items: center; justify-content: flex-start;'>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            ruta = os.path.join("fotos", imagen)
            if os.path.exists(ruta):
                st.image(ruta, width=250)
            else:
                st.error("Imagen no encontrada.")

        with col2:
            st.markdown(f"""
                <div style='padding-left: 20px;'>
                    <h3 style='margin-bottom: 0;'>🧩 Material:</h3>
                    <p style='font-size: 22px; font-weight: bold; margin-top: 5px;'>{nombre}</p>
                    <p><strong>Cantidad:</strong> {cantidad}</p>
                    <p><strong>Costo estimado:</strong> {costo}</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div><hr>", unsafe_allow_html=True)
# ---------------------------------------
elif pagina == "🌐 Conexión del Sistema":
    st.markdown("<h1 style='font-size: 36px; text-align:center;'>🌐 Conexión del Sistema</h1>", unsafe_allow_html=True)

    # Mostrar imagen primero
    imagen_path = os.path.join("fotos", "Conexión de Datos Remota.png")
    if os.path.exists(imagen_path):
        st.image(imagen_path, caption="Esquema técnico: Conexión desde Rumihuco hasta El Troje mediante red 3G", width=900)
    else:
        st.warning("⚠️ No se encontró la imagen ilustrativa.")

    # Explicación técnica tipo estudiante de ingeniería
    st.markdown("""
    <div style='font-size: 19px; text-align: justify; padding-top: 20px;'>
        El sistema de monitoreo ambiental propuesto tiene como objetivo transmitir en tiempo real los datos recolectados en <strong>Rumihuco</strong> (temperatura, humedad, radiación solar y caudal) 
        hacia el sector de <strong>El Troje</strong>, donde serán visualizados y analizados.
        <br><br>
        Dado que el sector de Rumihuco no cuenta con acceso a internet por fibra óptica ni redes Wi-Fi estables, se plantea una solución de comunicación basada en tecnología <strong>3G</strong>. 
        Para ello, se implementa un <strong>módem SIM800L</strong>, el cual se conecta directamente a un <strong>microcontrolador ESP32</strong>. Este microcontrolador se encarga de tomar las mediciones 
        de los sensores y enviarlas a través del módulo 3G usando una tarjeta SIM activa, mediante el protocolo HTTP o MQTT hacia un servidor web remoto.
        <br><br>
        Esta arquitectura permite:
        <ul style="padding-left: 20px;">
            <li>💡 Transmisión de datos autónoma desde zonas rurales sin cobertura fija.</li>
            <li>📶 Uso eficiente de datos móviles gracias a la optimización en el envío.</li>
            <li>🔋 Bajo consumo energético ideal para estaciones alimentadas por energía solar.</li>
        </ul>
        Además, este tipo de solución es escalable, permitiendo que otras estaciones remotas puedan integrarse usando la misma lógica de conexión móvil.
        <br><br>
        <strong>Conclusión:</strong> Este esquema de conexión mediante red celular 3G permite superar las limitaciones geográficas y tecnológicas del sector, garantizando 
        una comunicación efectiva entre la estación en Rumihuco y el punto de visualización en El Troje.
    </div>

    <div style='margin-top: 30px; padding: 15px; border: 2px solid #4CAF50; border-radius: 10px; background-color: #e8f5e9;'>
        <h4 style='color: #2E7D32; font-size: 22px;'>📘 Glosario de términos técnicos</h4>
        <ul style='font-size: 17px; color: #1B1B1B; padding-left: 20px;'>
            <li>📡 <strong>3G:</strong> Red de telefonía móvil de tercera generación que permite enviar datos (como mensajes o sensores) a través del celular.</li>
            <li>🔌 <strong>Módem SIM800L:</strong> Dispositivo que permite conectarse a la red celular usando una tarjeta SIM, como lo hace un teléfono.</li>
            <li>🧠 <strong>ESP32:</strong> Microcontrolador que actúa como el "cerebro" del sistema, recolectando datos de sensores y enviándolos.</li>
            <li>🌐 <strong>Protocolo HTTP:</strong> Lenguaje que usan los navegadores para enviar y recibir información en la web.</li>
            <li>📊 <strong>Protocolo MQTT:</strong> Protocolo liviano usado en IoT, ideal para enviar datos de sensores de forma eficiente.</li>
            <li>🖥️ <strong>Servidor web remoto:</strong> Computadora o plataforma online que recibe los datos y permite verlos desde otro lugar, como El Troje.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
# ---------------------------------------
elif pagina == "📡 Otra forma de Comunicación":
    st.markdown("<h1 style='font-size: 36px; text-align:center;'>📡 Otra forma de Comunicación</h1>", unsafe_allow_html=True)

    # Mostrar imagen LoRaWAN
    imagen_path = os.path.join("fotos", "Otra forma de comunicacion .png")
    if os.path.exists(imagen_path):
        st.image(imagen_path, caption="Esquema técnico: Comunicación mediante LoRaWAN como alternativa al 3G", width=900)
    else:
        st.warning("⚠️ No se encontró la imagen ilustrativa.")

    # Explicación técnica para ingeniero
    st.markdown("""
    <div style='font-size: 19px; text-align: justify; padding-top: 20px;'>
        Como alternativa a la red celular 3G, se plantea el uso del protocolo <strong>LoRaWAN</strong> para la transmisión de datos desde Rumihuco hacia una plataforma de visualización.
        <br><br>
        LoRaWAN (Long Range Wide Area Network) es una tecnología de comunicación inalámbrica de bajo consumo y largo alcance, ideal para entornos rurales donde la cobertura móvil es limitada o inexistente.
        <br><br>
        En esta arquitectura, la estación de monitoreo equipada con sensores ambientales envía los datos recolectados a través de una antena LoRa hacia una <strong>Gateway</strong> (puerta de enlace), 
        que actúa como intermediaria entre los sensores y el servidor. Luego, esta gateway transmite los datos mediante conexión Ethernet o WiFi hacia la plataforma web ubicada en El Troje u otro sitio.
        <br><br>
        <strong>Ventajas principales:</strong>
        <ul style="padding-left: 20px;">
            <li>📶 Cobertura de varios kilómetros con muy bajo consumo energético.</li>
            <li>🔋 Ideal para estaciones alimentadas por paneles solares.</li>
            <li>🌍 No requiere infraestructura de red celular, reduciendo costos a largo plazo.</li>
        </ul>
        Esta solución es especialmente útil cuando se desea cubrir grandes extensiones rurales con una sola antena LoRa y múltiples sensores distribuidos.
        <br><br>
        <strong>Conclusión:</strong> LoRaWAN ofrece una solución robusta, sostenible y eficiente para sistemas de monitoreo ambiental en zonas remotas, representando una opción tecnológica viable frente al 3G.
    </div>

    <div style='margin-top: 30px; padding: 15px; border: 2px solid #0277BD; border-radius: 10px; background-color: #E3F2FD;'>
        <h4 style='color: #01579B; font-size: 22px;'>📘 Glosario de términos técnicos</h4>
        <ul style='font-size: 17px; color: #1B1B1B; padding-left: 20px;'>
            <li>📡 <strong>LoRaWAN:</strong> Protocolo de comunicación inalámbrica de largo alcance y bajo consumo, usado en IoT.</li>
            <li>🛰️ <strong>Gateway:</strong> Dispositivo que recibe datos de los sensores LoRa y los envía a internet vía Ethernet o WiFi.</li>
            <li>🔁 <strong>Antena LoRa:</strong> Componente que permite emitir y recibir señales de radiofrecuencia a larga distancia.</li>
            <li>📶 <strong>Red de largo alcance:</strong> Tecnología que cubre grandes áreas sin necesidad de torres celulares.</li>
            <li>🌞 <strong>Estación solar:</strong> Sistema autónomo alimentado por energía solar, ideal para sensores remotos.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
# ---------------------------------------
elif pagina == "⚠️ Impacto y Deslizamientos":
    st.markdown("<h1 style='text-align:center; font-size:36px;'>⚠️ Impacto y Deslizamientos - El Troje</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:20px; text-align:justify;'>
    En julio de 2025, fuertes lluvias provocaron un <strong>deslizamiento en la quebrada La Mica</strong>, dañado la infraestructura de conducción de agua que abastece la planta <strong>El Troje</strong>.
    </p>
    """, unsafe_allow_html=True)

    # Infografía estilo tarjetas
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

    st.markdown("---")

    # Imagen ilustrativa
    imagen = os.path.join("fotos", "Datos 2025.png")
    if os.path.exists(imagen):
        img = Image.open(imagen)
        st.image(img, caption="📷 Daño en infraestructura tras el deslizamiento", width=800)
    else:
        st.warning("⚠️ Coloca aquí una imagen real o ilustrativa del deslizamiento")

    # Explicación detallada (redactada profesionalmente)
    st.markdown("""
    <div style='font-size:18px; text-align:justify; margin-top:25px;'>
    El colapso fue provocado por la saturación del suelo tras lluvias intensas, lo que ocasionó la ruptura de parte del sistema de conducción <strong>Mica–Quito Sur</strong>, dejando inoperativa la planta El Troje. 
    Ante esta emergencia, se interrumpió el suministro de agua potable en seis parroquias del sur de Quito. 
    Las autoridades activaron un plan de contingencia con tanqueros para abastecer hospitales, escuelas y comunidades prioritarias. 
    El COE-M desplegó maquinaria y 70 operarios que lograron remover aproximadamente 180 000 m³ de escombros en un intento por restablecer el servicio.
    </div>
    """, unsafe_allow_html=True)

    # Título tabla
    st.markdown("<h4 style='margin-top:30px; color:#FFCC00;'>📊 Resumen del Impacto</h4>", unsafe_allow_html=True)

    # Tabla visualmente separada
    st.markdown("""
    <style>
    thead tr th {
        background-color: #2c3e50;
        color: white !important;
    }
    tbody tr td {
        background-color: #f9f9f9;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

    df_incidentes = pd.DataFrame({
        "Indicador": ["Parroquias sin agua", "Personas afectadas", "Longitud tubería dañada"],
        "Valor": ["6", "≈350 000–400 000", "≈350 m"]
    })

    st.markdown('<div class="custom-table">', unsafe_allow_html=True)
    st.table(df_incidentes)
    st.markdown('</div>', unsafe_allow_html=True)

    # Recomendaciones
    st.markdown("""
    <p style='font-size:18px; text-align:justify;'>
    👉 Este evento revela la urgencia de contar con una <strong>estación de monitoreo ambiental</strong> en El Troje, que permita:
    <ul>
        <li>Anticipar cortes por fenómenos hidrológicos extremos.</li>
        <li>Mejorar la planificación preventiva de emergencia.</li>
        <li>Activar alertas tempranas para protección comunitaria.</li>
    </ul>
    </p>
    """, unsafe_allow_html=True)

# ---------------------------------------
elif pagina == "🤖 Ideas de nuestro robot de IA":
    modelo = configurar_gemini(API_KEY)

    st.markdown("""
        <h1 style='text-align: center; font-size: 40px;'>🤖 Asistente de Inteligencia Artificial</h1>
        <p style='text-align: center; font-size: 20px;'>Consulta sobre presupuesto, sensores o redes de comunicación</p>
    """, unsafe_allow_html=True)

    st.markdown("### 💰 <strong>Presupuesto del Proyecto</strong>", unsafe_allow_html=True)
    st.markdown("Costo estimado actual: <strong>$2500 USD</strong>", unsafe_allow_html=True)

    if st.button("💡 Optimizar presupuesto con IA"):
        with st.spinner("Consultando a Gemini..."):
            pregunta = "Sugerencias para reducir el costo del sistema de monitoreo con alternativas eficientes."
            respuesta = consultar_gemini(modelo, pregunta)
            st.success("✅ Recomendación de Gemini:")
            st.markdown(formatear_respuesta(respuesta), unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📶 <strong>Tecnología de Comunicación</strong>", unsafe_allow_html=True)
    st.markdown("Sensores conectados por red <strong>GSM o LoRaWAN</strong>", unsafe_allow_html=True)

    if st.button("💡 Evaluar tecnología con IA"):
        with st.spinner("Consultando a Gemini..."):
            pregunta = "Comparación entre GSM y LoRaWAN para transmitir datos en zonas rurales."
            respuesta = consultar_gemini(modelo, pregunta)
            st.success("✅ Evaluación de Gemini:")
            st.markdown(formatear_respuesta(respuesta), unsafe_allow_html=True)
