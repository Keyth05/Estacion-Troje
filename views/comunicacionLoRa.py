import streamlit as st
import os

def show():
    st.markdown("<h1 style='font-size: 36px; text-align:center;'>📡 Comunicación mediante LoRaWAN</h1>", unsafe_allow_html=True)

    imagen_path = os.path.join("fotos", "Otra forma de comunicacion .png")
    if os.path.exists(imagen_path):
        st.image(imagen_path, caption="Esquema técnico: Comunicación mediante LoRaWAN como alternativa al 3G", width=900)
    else:
        st.warning("⚠️ No se encontró la imagen ilustrativa.")

    st.markdown("""
    <div style='font-size: 19px; text-align: justify; padding-top: 20px;'>
        La tecnología <strong>LoRaWAN</strong> (Long Range Wide Area Network) es una red de baja potencia y largo alcance diseñada para conectar dispositivos IoT distribuidos en grandes áreas rurales o urbanas, sin necesidad de usar redes móviles tradicionales.
        <br><br>
        La comunicación funciona mediante:
        <ul style="padding-left: 20px;">
            <li>🔗 <strong>Sensores LoRa:</strong> Capturan datos ambientales y los transmiten usando ondas de radiofrecuencia.</li>
            <li>📶 <strong>Gateways LoRaWAN:</strong> Reciben la señal de los sensores y la reenvían a internet (usando Wi-Fi, Ethernet o 4G).</li>
            <li>☁️ <strong>Servidor en la nube:</strong> Interpreta y visualiza los datos en una plataforma web.</li>
        </ul>
        LoRaWAN es especialmente útil en zonas como <strong>Rumihuco</strong> donde no existe conectividad fija ni 3G. Gracias a su bajo consumo energético y gran alcance, permite monitorear variables como temperatura, precipitaciones y nivel del río desde estaciones remotas.
    </div>

    <div style='margin-top: 30px; padding: 15px; border: 2px solid #FF9800; border-radius: 10px; background-color: #FFF3E0;'>
        <h4 style='color: #E65100; font-size: 22px;'>🛠️ Procedimiento de Instalación de una estación LoRaWAN</h4>
        <ol style='font-size: 17px; color: #1B1B1B; padding-left: 20px;'>
            <li><strong>Montaje de sensores:</strong> Instalar sensores de temperatura, humedad, presión, nivel de río y pluviómetro en un mástil metálico resistente.</li>
            <li><strong>Conexión al módulo LoRa:</strong> Cada sensor se conecta mediante cableado al módulo TTGO/Heltec.</li>
            <li><strong>Energía:</strong> Instalar panel solar con batería Li-Ion recargable para autonomía completa.</li>
            <li><strong>Antena externa:</strong> Aumenta el alcance del módulo LoRa para asegurar cobertura hacia el gateway.</li>
            <li><strong>Configuración LoRaWAN:</strong> Registrar el dispositivo en The Things Network (TTN) y asociarlo a una aplicación.</li>
            <li><strong>Enlace a plataforma web:</strong> Enviar los datos del TTN a tu servidor o visualizador (Streamlit, Grafana, etc.).</li>
        </ol>
    </div>

    <div style='margin-top: 30px; padding: 15px; border: 2px solid #1565C0; border-radius: 10px; background-color: #E3F2FD;'>
        <h4 style='color: #0D47A1; font-size: 22px;'>💼 Componentes propuestos para estación LoRaWAN</h4>
        <table style='font-size: 17px; width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #90CAF9; color: #0D47A1;'>
                    <th style='text-align:left; padding: 6px;'>Componente</th>
                    <th style='text-align:center;'>Cantidad</th>
                    <th style='text-align:center;'>Costo unitario (USD)</th>
                    <th style='text-align:center;'>Total aprox.</th>
                </tr>
            </thead>
            <tbody style='color: #1B1B1B;'>
                <tr><td>Sensor LoRa (temp/humedad/presión)</td><td align='center'>1</td><td align='center'>$68</td><td align='center'>$72</td></tr>
                <tr><td>Pluviómetro LoRa</td><td align='center'>1</td><td align='center'>$50</td><td align='center'>$50</td></tr>
                <tr><td>Sensor nivel río ultrasónico + módulo LoRa</td><td align='center'>1</td><td align='center'>$57</td><td align='center'>$65</td></tr>
                <tr><td>Módulo LoRa TTGO/Heltec</td><td align='center'>1</td><td align='center'>$20</td><td align='center'>$20</td></tr>
                <tr><td>Antena externa LoRa</td><td align='center'>1</td><td align='center'>$15</td><td align='center'>$15</td></tr>
                <tr><td>Carcasa IP65</td><td align='center'>1</td><td align='center'>$16</td><td align='center'>$16</td></tr>
                <tr><td>Panel solar + baterías Li-Ion</td><td align='center'>1</td><td align='center'>$80</td><td align='center'>$80</td></tr>
                <tr><td>Mástil metálico galvanizado</td><td align='center'>1</td><td align='center'>$75</td><td align='center'>$75</td></tr>
                <tr><td>Montaje, cables, conectores</td><td align='center'>—</td><td align='center'>$30</td><td align='center'>$30</td></tr>
            </tbody>
        </table>
        <p style='font-size: 18px; padding-top: 10px; color: #1B1B1B;'><strong>Total por estación: ≈ $423 USD</strong></p>
    </div>

    <div style='margin-top: 30px; padding: 15px; border: 2px solid #4CAF50; border-radius: 10px; background-color: #e8f5e9;'>
        <h4 style='color: #2E7D32; font-size: 22px;'>📘 Glosario de términos técnicos</h4>
        <ul style='font-size: 17px; color: #1B1B1B; padding-left: 20px;'>
            <li>📡 <strong>LoRa:</strong> Tecnología de largo alcance y bajo consumo para transmitir datos inalámbricamente.</li>
            <li>🛰️ <strong>LoRaWAN:</strong> Protocolo de red para administrar múltiples dispositivos LoRa y conectarlos a internet.</li>
            <li>☁️ <strong>TTN (The Things Network):</strong> Red pública y gratuita para dispositivos LoRaWAN.</li>
            <li>🔋 <strong>Panel solar + baterías:</strong> Fuente de energía para autonomía 24/7 sin depender de electricidad.</li>
            <li>📶 <strong>Gateway:</strong> Dispositivo puente entre los sensores LoRa y la nube.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
