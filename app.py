import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Test de Fútbol", page_icon="⚽", layout="centered")

# Estilo visual: Tonos Verdes (Estilo Césped) y Blanco
st.markdown("""
    <style>
    .stApp {
        background-color: #f0fdf4; /* Verde muy pálido */
        color: #166534; /* Verde oscuro para texto */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    .football-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #22c55e; /* Verde brillante */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #333;
    }

    .stButton>button {
        background: linear-gradient(90deg, #22c55e 0%, #166534 100%) !important;
        color: white !important;
        border-radius: 25px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        height: 3em !important;
        width: 100%;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Título y bienvenida
st.title("🏆 TEST INFALIBLE: ¿QUÉ TAN FÚTBOL ERES?")
st.write("---")
st.write("### Contesta estas 5 preguntas para evaluar tu nivel de fanatismo por el fútbol.")

# --- CUESTIONARIO DE FÚTBOL ---

with st.container():
    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q1 = st.selectbox("1. ¿Cuál es tu equipo favorito (o selección)?", 
                    ["Selecciona uno...", "Real Madrid", "FC Barcelona", "Manchester United", "Boca Juniors", "River Plate", "AC Milan", "Bayern Múnich", "Mi Selección Nacional", "Otro"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q2 = st.radio("2. ¿Con qué frecuencia ves partidos de fútbol completos?", 
                ["Nunca", "Ocasionalmente (solo finales/mundial)", "Todos los fines de semana", "Diariamente (veo cualquier liga)", "Obsesivamente (no me pierdo ni los amistosos)"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q3 = st.radio("3. ¿Cómo celebras un gol de tu equipo?", 
                ["Me quedo callado/a", "Grito 'gol' y aplaudo", "Salto y abrazo a quien esté cerca", "Grito como un/a loco/a y pierdo la voz", "Me pongo a llorar de emoción"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q4 = st.selectbox("4. ¿Cuál es tu jugador histórico favorito?", 
                    ["Selecciona uno...", "Pelé", "Diego Maradona", "Lionel Messi", "Cristiano Ronaldo", "Zinedine Zidane", "Ronaldo Nazário", "Johan Cruyff", "Andrés Iniesta", "Otro"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="football-card">', unsafe_allow_html=True)
    q5 = st.select_slider("5. ¿Qué tan importante es el fútbol en tu vida (del 1 al 5)?", 
                        options=["1 (No me importa)", "2 (Un pasatiempo más)", "3 (Lo disfruto mucho)", "4 (Esencial)", "5 (El fútbol ES mi vida)"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTÓN DE RESULTADOS ---

if st.button("📊 GENERAR DIAGNÓSTICO FINAL"):
    # Validación simple
    if q1 == "Selecciona uno..." or q4 == "Selecciona uno...":
        st.warning("⚠️ Por favor, responde todas las preguntas antes de generar el diagnóstico.")
    else:
        with st.status("Procesando tus respuestas futboleras...", expanded=True) as status:
            time.sleep(1)
            st.write("Analizando patrones de consumo de partidos...")
            time.sleep(1)
            st.write("Evaluando intensidad de grito de gol...")
            time.sleep(1)
            st.write("Confirmando lealtad a colores y leyendas...")
            time.sleep(1)
            status.update(label="¡ANÁLISIS COMPLETADO!", state="complete", expanded=False)

        # Lluvia de balones (fútbol personalizado)
        st.balloons()
        
        # El veredicto final
        st.markdown("""
            <div style='background-color: white; padding: 40px; border-radius: 20px; text-align: center; border: 4px solid #166534; color: #166534;'>
                <h1 style='font-size: 35px;'>📁 EXPEDIENTE: FANÁTICO DE FÚTBOL</h1>
                <h2 style='color: #22c55e;'>ESTADO FINAL:</h2>
                <h1 style='font-size: 60px;'>⚽ 100% FÚTBOL ⚽</h1>
                <hr style='border: 1px solid #166534;'>
                <p style='font-size: 20px;'>El algoritmo ha confirmado que el fútbol corre por tus venas.</p>
                <p>¡Eres un verdadero <b>Guerrero de la Cancha</b>!</p>
            </div>
        """, unsafe_allow_html=True)

# Barra lateral
st.sidebar.markdown(f"""
    <div style='text-align: center;'>
        <h2 style='color: #166534;'>ANALISTA PRINCIPAL</h2>
        <hr>
        <h3 style='color: #22c55e;'>GABRIEL</h3>
    </div>
    """, unsafe_allow_html=True)
st.sidebar.warning("Los resultados son definitivos e irrevocables.")
