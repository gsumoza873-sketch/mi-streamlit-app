import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Scanner de Personalidad Pro", page_icon="🧠")

# Estilo visual: Moderno y Oscuro
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Animación de pelotas cayendo (⚾) */
    @keyframes falling {
        0% { transform: translateY(-100vh) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(360deg); }
    }

    .ball {
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

st.title("🧠 TEST DE PERSONALIDAD AVANZADO")
st.write("---")
st.info("Este test utiliza algoritmos de comportamiento para determinar rasgos ocultos de **Yeferson**.")

# --- CUESTIONARIO DE 7 PREGUNTAS ---

with st.container():
    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p1 = st.selectbox("1. ¿Qué tipo de música prefiere Yeferson para relajarse?", 
                    ["Pop de divas (Dua Lipa, Taylor Swift)", "Electrónica intensa", "Baladas sentimentales"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p2 = st.radio("2. En un grupo de amigos, Yeferson suele ser el que...", 
                ["Se fija en cómo están vestidos todos", "Se preocupa por el chisme", "Organiza las salidas a bailar"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p3 = st.select_slider("3. Nivel de cuidado personal (Skincare, perfume, cabello):", 
                        options=["Básico", "Intermedio", "Obsesión Total"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p4 = st.radio("4. Si Yeferson ve a un hombre con buen físico, su reacción interna es:", 
                ["'Quiero ser como él'", "'Qué bien se ve'", "'Me quedé sin palabras'"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p5 = st.selectbox("5. ¿Cuál es la red social donde Yeferson pasa más tiempo?", 
                    ["TikTok (coreografías)", "Instagram (modelos)", "X (Twitter)"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p6 = st.radio("6. ¿Cómo describirías la forma en que Yeferson camina?", 
                ["Con mucha elegancia", "Con un movimiento de cadera sospechoso", "Como si estuviera en una pasarela"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    p7 = st.selectbox("7. ¿Qué busca Yeferson en una pareja ideal?", 
                    ["Protección y fuerza masculina", "Sentido del humor", "Alguien que cuide su piel"])
    st.markdown('</div>', unsafe_allow_html=True)

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

    # LLUVIA DE PELOTAS (⚾)
    balls_html = "".join([f'<div class="ball" style="left: {i*8}%; animation-delay: {i*0.2}s;">⚾</div>' for i in range(12)])
    st.markdown(balls_html, unsafe_allow_html=True)

    # El veredicto final
    st.markdown("""
        <div style='background-color: #6a0dad; padding: 40px; border-radius: 20px; text-align: center; border: 4px solid gold;'>
            <h1 style='color: white; font-size: 35px;'>📁 EXPEDIENTE: YEFERSON</h1>
            <h2 style='color: #f1c40f;'>ESTADO FINAL:</h2>
            <h1 style='color: white; font-size: 60px;'>🏳️‍🌈 100% GAY 🏳️‍🌈</h1>
            <hr style='border: 1px solid white;'>
            <p style='color: #ddd; font-size: 20px;'>El algoritmo no miente. <br> ¡Salió del closet!</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.snow()

# Barra lateral
st.sidebar.title("👨‍🔬 Analista")
st.sidebar.header("Gabriel")
st.sidebar.write("---")
st.sidebar.warning("Los resultados son definitivos.")
