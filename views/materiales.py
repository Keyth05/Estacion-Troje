import streamlit as st
import os

def show():
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

        st.markdown("<hr>", unsafe_allow_html=True)
