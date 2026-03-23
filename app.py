import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Test de Fútbol", page_icon="⚽", layout="centered")

# Estilo visual: Fondo OSCURO, Texto CLARO (Contraste Asegurado)
st.markdown("""
    <style>
    /* Fondo oscuro para toda la aplicación */
    .stApp {
        background-color: #1f2937; /* Azul muy oscuro/Grisáceo */
        color: #fef08a; /* Amarillo pastel claro para texto principal */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Títulos claros */
    h1, h2, h3, h4, h5, h6, .stMarkdown p {
        color: #fef08a !important; /* Asegurar amarillo pastel claro */
    }

    /* Tarjetas de preguntas OSCURAS con borde VERDE */
    .football-card {
        background-color: #374151; /* Gris oscuro para el fondo de la tarjeta */
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #22c55e; /* Borde VERDE brillante */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
        color: white; /* Texto blanco DENTRO de la tarjeta */
    }
    
    /* Título de la pregunta dentro de la tarjeta */
    .football-card h3 {
        color: white !important;
        margin-bottom: 15px;
    }

    /* Botón personalizado VERDE */
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
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 5px 15px rgba(34, 197, 94, 0.4);
    }

    /* Texto de validación y advertencias en AMARILLO */
    .stAlert p {
        color: #facc15 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Título y bienvenida
st.markdown("<h1 style='text-align: center; color: #fef08a;'>🏆 TEST INFALIBLE: ¿QUÉ TAN FÚTBOL ERES?</h1>", unsafe_allow_html=True)
st.write("---")
st.markdown("<h3 style='text-align: center; color: #fef08a;'>Contesta estas 5 preguntas para evaluar tu nivel de fanatismo por el fútbol.</h3>", unsafe_allow_html=True)
st.write("")

# --- CUESTIONARIO DE FÚTBOL ---

with st.container():
    # Pregunta 1
    st.markdown('<div class="football-card"><h3>1. ¿Cuál es tu equipo favorito (o selección)?</h3>', unsafe_allow_html=True)
    q1 = st.selectbox("", 
                    ["Selecciona uno...", "Real Madrid", "FC Barcelona", "Manchester United", "Boca Juniors", "River Plate", "AC Milan", "Bayern Múnich", "Mi Selección Nacional", "Otro"],
                    key="q1_selectbox")
    st.markdown('</div>', unsafe_allow_html=True)

    # Pregunta 2
    st.markdown('<div class="football-card"><h3>2. ¿Con qué frecuencia ves partidos de fútbol completos?</h3>', unsafe_allow_html=True)
    q2 = st.radio("", 
                ["Nunca", "Ocasionalmente (solo finales/mundial)", "Todos los fines de semana", "Diariamente (veo cualquier liga)", "Obsesivamente (no me pierdo ni los amistosos)"],
                key="q2_radio")
    st.markdown('</div>', unsafe_allow_html=True)

    # Pregunta 3
    st.markdown('<div class="football-card"><h3>3. ¿Cómo celebras un gol de tu equipo?</h3>', unsafe_allow_html=True)
    q3 = st.radio("", 
                ["Me quedo callado/a", "Grito 'gol' y aplaudo", "Salto y abrazo a quien esté cerca", "Grito como un/a loco/a y pierdo la voz", "Me pongo a llorar de emoción"],
                key="q3_radio")
    st.markdown('</div>', unsafe_allow_html=True)

    # Pregunta 4
    st.markdown('<div class="football-card"><h3>4. ¿Cuál es tu jugador histórico favorito?</h3>', unsafe_allow_html=True)
    q4 = st.selectbox("", 
                    ["Selecciona uno...", "Pelé", "Diego Maradona", "Lionel Messi", "Cristiano Ronaldo", "Zinedine Zidane", "Ronaldo Nazário", "Johan Cruyff", "Andrés Iniesta", "Otro"],
                    key="q4_selectbox")
    st.markdown('</div>', unsafe_allow_html=True)

    # Pregunta 5
    st.markdown('<div class="football-card"><h3>5. ¿Qué tan importante es el fútbol en tu vida (del 1 al 5)?</h3>', unsafe_allow_html=True)
    q5 = st.select_slider("", 
                        options=["1 (No me importa)", "2 (Un pasatiempo)", "3 (Lo disfruto mucho)", "4 (Esencial)", "5 (El fútbol ES mi vida)"],
                        key="q5_slider")
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTÓN DE RESULTADOS ---

if st.button("📊 GENERAR DIAGNÓSTICO FINAL"):
    # Validación simple
    if q1 == "Selecciona uno..." or q4 == "Selecciona uno...":
        st.warning("⚠️ Por favor, responde todas las preguntas (selecciona un equipo y un jugador) antes de generar el diagnóstico.")
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
        st.markdown(f"""
            <div style='background-color: #374151; padding: 40px; border-radius: 20px; text-align: center; border: 4px solid #22c55e; color: white; box-shadow: 0 10px 20px rgba(0,0,0,0.5);'>
                <h1 style='font-size: 35px; color: white !important;'>📁 EXPEDIENTE: FANÁTICO DE FÚTBOL</h1>
                <h2 style='color: #22c55e !important;'>ESTADO FINAL:</h2>
                <h1 style='font-size: 60px; color: white !important;'>⚽ 100% FÚTBOL ⚽</h1>
                <hr style='border: 1px solid #22c55e;'>
                <p style='font-size: 20px; color: white !important;'>El algoritmo ha confirmado que el fútbol corre por tus venas.</p>
                <p style='color: white !important;'>¡Eres un verdadero <b>Guerrero de la Cancha</b>!</p>
            </div>
        """, unsafe_allow_html=True)

# Barra lateral
st.sidebar.markdown(f"""
    <div style='text-align: center; color: #fef08a;'>
        <h2 style='color: #fef08a;'>ANALISTA PRINCIPAL</h2>
        <hr style='border: 1px solid #fef08a;'>
