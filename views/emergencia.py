import streamlit as st
import os

def show():
    st.markdown("## 🚨 Emergencia por Corte de Agua en Quito")
    current_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta vistas
    image_path = os.path.abspath(os.path.join(current_dir, "..", "fotos", "Desastre_Mica.jpg"))

    if os.path.exists(image_path):
        st.image(image_path, caption="Lugar del colapso en El Troje", width=700)
    else:
        st.warning("⚠️ No se encontró la imagen 'Desastre_Mica.jpg' en la carpeta /fotos.")

    st.markdown("### 📍 ¿Qué pasó en El Troje y el sistema Mica?")
    st.markdown("Un gran deslizamiento provocado por lluvias intensas rompió el sistema de tuberías Mica–Quito Sur, dejando inoperativa la planta de El Troje.")

    st.markdown("### 🚱 ¿Por qué el sur de Quito se quedó sin agua?")
    st.markdown("- El sistema Mica transporta agua desde los páramos.\n- El deslizamiento tapó y rompió las tuberías.\n- Se cortó el servicio por 14 días en 6 parroquias del sur.")

    st.markdown("### 📆 ¿Qué hicieron las autoridades?")
    st.markdown("- Activaron un plan de emergencia con tanqueros.\n- Removieron 180,000 m³ de escombros.\n- Priorizaron hospitales, escuelas y zonas críticas.")

    st.markdown("### 📊 Impacto en las personas")
    st.markdown("- Más de 400,000 personas sin agua.\n- Escuelas y negocios cerrados.\n- Barrios como Guamaní, Chillogallo y La Ecuatoriana afectados.")

    st.markdown("### 🧠 ¿Qué podemos aprender de esto?")
    st.markdown("- Monitorear los ríos y laderas todo el tiempo.\n- Usar sensores económicos y confiables.\n- Tener rutas alternativas de abastecimiento.")

    st.markdown("### 📈 ¿Se puede evitar en el futuro?")
    st.markdown("✅ Sí. Podemos usar sensores, comunicación en tiempo real e inteligencia artificial para anticiparnos a los desastres.")

    st.success("Esta historia real muestra por qué necesitamos monitorear y actuar con tecnología accesible.")
