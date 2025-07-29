import streamlit as st
import os

def show():
    st.markdown("<h1 style='font-size: 38px;'>📦 Visualización de Materiales LoRaWAN</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Aquí puedes ver cada componente con su imagen, cantidad y costo estimado por estación.</p>", unsafe_allow_html=True)

    materiales_lora = [
        ("Sensor LoRa (temp/humedad/presión)", "Heltec LoRa-LoRaWAN.png", "1", "$68", "$72"),
        ("Pluviómetro LoRa", "Pluviómetro LoRa.png", "1", "$50", "$50"),
        ("Sensor nivel río ultrasónico + módulo LoRa", "LORA LORAWAN-SENSOR de nivel de agua ultrasónico inalámbrico.png", "1", "$57", "$65"),
        ("Módulo LoRa TTGO/Heltec", "Módulo LoRa TTGO-Heltec.png", "1", "$20", "$20"),
        ("Antena externa LoRa", "Antena externa LoRa.png", "1", "$15", "$15"),
        ("Carcasa IP65", "Carcasa IP65.png", "1", "$16", "$16"),
        ("Panel solar 6V–12V + batería Li-Ion 18650", "Panel solar - lora.png", "1", "$80", "$80"),
        ("Mástil metálico galvanizado", "Mástil.png", "1", "$75", "$75"),
        ("Costo de instalación y mano de obra", "Costo de instalación y mano de obra.png", "—", "$30", "$30"),
    ]

    for nombre, imagen, cantidad, costo_unitario, total in materiales_lora:
        col1, col2 = st.columns([1, 3])

        with col1:
            ruta = os.path.join("fotos", imagen)
            if os.path.exists(ruta):
                st.image(ruta, width=250)
            else:
                st.error(f"Imagen no encontrada: {imagen}")

        with col2:
            st.markdown(f"""
                <div style='padding-left: 20px;'>
                    <h3 style='margin-bottom: 0;'>🧩 Material:</h3>
                    <p style='font-size: 22px; font-weight: bold; margin-top: 5px;'>{nombre}</p>
                    <p><strong>Cantidad:</strong> {cantidad}</p>
                    <p><strong>Costo unitario:</strong> {costo_unitario}</p>
                    <p><strong>Total aprox.:</strong> {total}</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

    # Total general
    st.markdown("""
    <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50;'>
        <h2 style='color: #2E7D32;'>💰 Costo total estimado por estación: ≈ <strong>$423 USD</strong></h2>
    </div>
    """, unsafe_allow_html=True)
