import streamlit as st
import os

def show():
    st.markdown("<h1 style='font-size: 36px; text-align:center;'>📡 Otra forma de Comunicación</h1>", unsafe_allow_html=True)

    # Mostrar imagen LoRaWAN
    imagen_path = os.path.join("fotos", "Otra forma de comunicacion .png")
    if os.path.exists(imagen_path):
        st.image(imagen_path, caption="Esquema técnico: Comunicación mediante LoRaWAN como alternativa al 3G", width=900)
    else:
        st.warning("⚠️ No se encontró la imagen LoRaWAN en la carpeta /fotos.")

    # Introducción y explicación
    st.markdown("""
    <div style='font-size: 19px; text-align: justify; padding-top: 20px;'>
        En caso de que no se pueda utilizar la red 3G en Rumihuco, se propone como alternativa una red de largo alcance y bajo consumo llamada <strong>LoRaWAN</strong>.
        <br><br>
        Esta tecnología permite enviar datos de sensores hasta 15 km de distancia en línea recta, usando muy poca energía, lo que la hace ideal para zonas rurales.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ul style="padding-left: 30px; font-size: 19px;">
        <li>📶 No necesita internet en el lugar de origen, solo en el receptor.</li>
        <li>🔋 Muy bajo consumo de energía, ideal para energía solar.</li>
        <li>📡 Cobertura amplia, incluso en lugares sin señal celular.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 19px; text-align: justify;'>
        En este esquema, el nodo sensor en Rumihuco enviaría datos a través de LoRa a una gateway ubicada en Lloa o Cutuglagua, que sí tengan acceso a internet. Ese Gateway luego sube los datos a la nube.
        <br><br>
        <strong>Comparación con la red 3G:</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ul style="padding-left: 30px; font-size: 19px;">
        <li>📶 <strong>3G:</strong> Más velocidad y autonomía, pero requiere cobertura celular e internet en el lugar de origen.</li>
        <li>📡 <strong>LoRaWAN:</strong> Más alcance y menos consumo, ideal para lugares remotos.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 19px; text-align: justify;'>
        <br>
        <strong>Conclusión:</strong> LoRaWAN ofrece una solución robusta, sostenible y eficiente para sistemas de monitoreo ambiental en zonas remotas, representando una opción tecnológica viable frente al 3G.
    </div>
    """, unsafe_allow_html=True)

    # Glosario
    st.markdown("""
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
