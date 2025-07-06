import pandas as pd
import streamlit as st
from io import BytesIO

def mostrar_estacion_troje():
    materiales = {
        "Material / Componente": [
            "Sensor de Precipitación (Pluviómetro de balancín)",
            "Sensor de Temperatura y Humedad (DHT22)",
            "Sensor de Radiación Solar (TSL2561 o similar)",
            "Microcontrolador (ESP32 con WiFi)",
            "Módulo de Almacenamiento MicroSD",
            "Panel Solar 5V + Controlador de Carga",
            "Batería Recargable (Li-ion 18650)",
            "Caja Estanca / Aislante",
            "Soporte Metálico / PVC para fijación",
            "Cables, conectores y protoboard",
            "Módulo RTC (reloj en tiempo real)",
            "Costo de instalación y mano de obra"
        ],
        "Cantidad": [1, 1, 1, 1, 1, 1, 2, 1, 1, "Varios", 1, 1],
        "Costo Estimado (USD)": [40, 10, 12, 18, 4, 20, 10, 15, 10, 8, 6, 20]
    }

    df = pd.DataFrame(materiales)

    # Calcular costo total
    costo_total = sum([c for c in materiales["Costo Estimado (USD)"] if isinstance(c, (int, float))])

    # Formato para mostrar
    df_visual = df.copy()
    df_visual["Costo Estimado (USD)"] = df_visual["Costo Estimado (USD)"].apply(
        lambda x: f"{x:.2f} $" if isinstance(x, (int, float)) else x
    )

    # Título
    st.markdown("<h1 style='font-size: 32px;'>🧰 Materiales para Estación de Monitoreo en El Troje</h1>", unsafe_allow_html=True)
    st.write("A continuación se listan los componentes necesarios para construir una estación de monitoreo de bajo costo:")

    # Mostrar tabla sin íconos adicionales
    st.table(df_visual)

    # Mostrar costo total
    st.markdown(f"### 💰 Costo Total Estimado: **${costo_total:.2f} USD**")

    # Descarga como Excel
    try:
        buffer = BytesIO()
        df.to_excel(buffer, index=False, sheet_name="Materiales", engine="openpyxl")
        st.download_button(
            label="📥 Descargar Excel",
            data=buffer.getvalue(),
            file_name="materiales_estacion_el_troje.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except ModuleNotFoundError:
        st.warning("⚠️ No se puede generar el Excel porque falta el módulo `openpyxl`. Instálalo con:\n```bash\npip install openpyxl\n```")

    st.markdown("---")
    st.markdown("### 🛠️ Procedimiento de Instalación:")
    st.markdown("""
    1. **Montaje de Sensores**: Fijar el pluviómetro y sensores en el soporte metálico/PVC.  
    2. **Cableado y Ensamblaje**: Conectar sensores al ESP32, usar la protoboard o soldaduras seguras.  
    3. **Alimentación Solar**: Instalar el panel solar con batería y controlador de carga.  
    4. **Caja Estanca**: Aislar los componentes electrónicos en la caja plástica.  
    5. **Configuración del ESP32**: Programar la recolección de datos, conexión a WiFi o almacenamiento local.  
    6. **Instalación Física**: Colocar la estación en sitio seguro con buena exposición al cielo.  
    7. **Verificación de Datos**: Probar funcionamiento durante varios días y ajustar calibraciones si es necesario.  
    """)
