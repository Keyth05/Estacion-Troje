import streamlit as st
import os

def show():
    st.markdown("<h1 style='font-size: 36px; text-align:center;'>🌐 Conexión del Sistema</h1>", unsafe_allow_html=True)

    imagen_path = os.path.join("fotos", "Conexión de Datos Remota.png")
    if os.path.exists(imagen_path):
        st.image(imagen_path, caption="Esquema técnico: Conexión desde Rumihuco hasta El Troje mediante red 3G", width=900)
    else:
        st.warning("⚠️ No se encontró la imagen ilustrativa.")

    # Texto directamente incrustado (copiado del original)
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
