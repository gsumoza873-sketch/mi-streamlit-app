import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Scanner de Personalidad Pro", page_icon="🧠")

# Estilo visual: Moderno, Oscuro y Minimalista
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Animación de berenjenas cayendo (🍆) */
    @keyframes falling {
        0% { transform: translateY(-100vh) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(360deg); }
    }

    .eggplant {
        position: fixed;
        top: -10%;
        font-size: 2.5rem;
        z-index: 9999;
        animation: falling 3s linear infinite;
    }

    .question-box {
        background-color: #262730;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 TEST DE PERSONALIDAD AVANZADO: CASO YEFERSON")
st.write("---")
st.info("Este test utiliza algoritmos avanzados para determinar rasgos ocultos de personalidad y orientación.")

# --- CUESTIONARIO ---

with st.container():
    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p1 = st.selectbox("1. ¿Qué parte de hombre te gusta más?", 
                    ["Cara", "Pecho", "Glúteos", "Manos", "Piernas"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p2 = st.radio("2. ¿Te maquillas muy seguido?", 
                ["Nunca", "A veces", "Frecuentemente", "Todos los días", "Ocasionalmente"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p3 = st.radio("3. ¿Tragas o escupes?", 
                ["Trago", "Escupo", "Depende", "Solo cuando es necesario", "Prefiero no responder"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Puedes agregar más preguntas aquí si lo deseas, siguiendo el mismo formato.

# --- RESULTADO FINAL ---

if st.button("📊 GENERAR DIAGNÓSTICO FINAL"):
    
    with st.status("Procesando respuestas en el servidor central...", expanded=True) as status:
        time.sleep(1.5)
        st.write("Analizando patrones de consumo de medios...")
        time.sleep(1.5)
        st.write("Detectando alta afinidad con la comunidad...")
        time.sleep(1.5)
        st.write("Confirmando predisposición genética...")
        time.sleep(1)
        status.update(label="¡ANÁLISIS COMPLETADO!", state="complete", expanded=False)

    # LLUVIA DE BERENJENAS (🍆)
    eggplants_html = "".join([f'<div class="eggplant" style="left: {i*8}%; animation-delay: {i*0.2}s;">🍆</div>' for i in range(12)])
    st.markdown(eggplants_html, unsafe_allow_html=True)

    # El veredicto final, siempre positivo
    st.markdown("""
        <div style='background-color: #6a0dad; padding: 40px; border-radius: 20px; text-align: center; border: 4px solid gold;'>
            <h1 style='color: white; font-size: 35px;'>📁 EXPEDIENTE: YEFERSON</h1>
            <h2 style='color: #f1c40f;'>ESTADO FINAL:</h2>
            <h1 style='color: white; font-size: 60px;'>🏳️‍🌈 100% GAY 🏳️‍🌈</h1>
            <hr style='border: 1px solid white;'>
            <p style='color: #ddd; font-size: 20px;'>El algoritmo es infalible. <br> ¡Salió del closet con honores!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # También lanzamos nieve para un efecto extra
    st.snow()

# Barra lateral
st.sidebar.title("👨‍🔬 Analista Principal")
st.sidebar.header("Gabriel")
st.sidebar.write("---")
st.sidebar.warning("Los resultados de este análisis son definitivos e irrevocables.")
