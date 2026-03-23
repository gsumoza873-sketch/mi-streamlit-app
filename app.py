import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Test de Fútbol", page_icon="⚽")

# Estilo visual corregido para que SE VEA TODO
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0e14;
        color: #f1f1f1;
    }
    .football-card {
        background-color: #1c2128;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #22c55e;
        margin-bottom: 20px;
    }
    /* Forzar color de texto en etiquetas */
    label, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 TEST: ¿QUÉ TAN FÚTBOL ERES?")
st.write("Responde estas 5 preguntas:")

# --- CUESTIONARIO ---
with st.container():
    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q1 = st.selectbox("1. ¿Cuál es tu equipo favorito?", ["Selecciona...", "Real Madrid", "Barcelona", "Boca", "River", "Selección Nacional", "Otro"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q2 = st.radio("2. ¿Ves partidos completos?", ["Nunca", "A veces", "Siempre"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q3 = st.radio("3. ¿Cómo celebras un gol?", ["Callado", "Aplauso", "Grito de loco"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q4 = st.selectbox("4. ¿Jugador histórico?", ["Selecciona...", "Messi", "Cristiano", "Maradona", "Pelé", "Zidane"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q5 = st.select_slider("5. Importancia del fútbol:", options=["Baja", "Media", "Alta", "Mi vida"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTÓN FINAL ---
if st.button("📊 GENERAR RESULTADO"):
    if q1 == "Selecciona..." or q4 == "Selecciona...":
        st.error("Responde todas las preguntas.")
    else:
        with st.spinner("Analizando..."):
            time.sleep(2)
        st.balloons()
        st.success("¡ERES 100% FÚTBOL!")
        st.markdown("<h2 style='text-align:center;'>⚽ ¡ERES UN CRACK! ⚽</h2>", unsafe_allow_html=True)

# Sidebar simple sin comillas triples para evitar errores
st.sidebar.title("Analista:")
st.sidebar.write("Gabriel")
