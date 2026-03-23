import streamlit as st
import time

# 1. Configuración Básica
st.set_page_config(page_title="Beauty Quiz Roseline", page_icon="💄")

st.title("💄 ROSELINE: BEAUTY QUIZ")
st.write("---")

# --- PREGUNTAS SIMPLES ---
st.subheader("Responde con sinceridad:")

m1 = st.selectbox("1. ¿Producto para que el maquillaje dure?", ["Selecciona...", "Primer", "Corrector", "Base"])
m2 = st.radio("2. ¿Para qué sirve el 'Baking'?", ["Cocinar", "Sellar maquillaje", "Limpiar"])
m3 = st.radio("3. ¿Te maquillas seguido?", ["Nunca", "A veces", "Siempre"])
m4 = st.radio("4. ¿Tragas o escupes?", ["Trago", "Escupo", "Depende"])
m5 = st.selectbox("5. ¿Mejor herramienta para la base?", ["Brocha", "Esponja", "Dedos"])

st.write("---")

# --- BOTÓN DE RESULTADO ---
if st.button("VER MI DIAGNÓSTICO"):
    if m1 == "Selecciona...":
        st.warning("Responde la primera pregunta primero.")
    else:
        with st.spinner("Analizando..."):
            time.sleep(2)
        
        st.balloons()
        st.success("¡ANÁLISIS COMPLETADO!")
        
        # Cuadro de resultado
        st.markdown(f"""
            <div style="background-color: #ffc0cb; padding: 20px; border-radius: 10px; text-align: center;">
                <h2 style="color: #d63384;">✨ RESULTADO PARA ROSELINE ✨</h2>
                <p style="color: black; font-size: 20px;">¡Eres una experta total!</p>
                <h1 style="color: #d63384;">¡SALIÓ POSITIVO! 🌈</h1>
            </div>
        """, unsafe_allow_html=True)

st.sidebar.write("Creado por: **Gabriel**")
