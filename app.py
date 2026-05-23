import streamlit as st
import time
import random

# 1. Configuración de la página única
st.set_page_config(
    page_title="Test de Ipia",
    page_icon="🌈",
    layout="centered"
)

# 2. Diseño estético de alta calidad (Dark Mode con detalles Neón)
st.markdown("""
    <style>
    .stApp {
        background-color: #090d16;
        color: #e2e8f0;
    }
    .main-panel {
        background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #6366f1;
        box-shadow: 0 0 25px rgba(99, 102, 241, 0.3);
        text-align: center;
        margin-bottom: 30px;
    }
    .titulo {
        color: #f43f5e !important;
        font-family: 'Impact', sans-serif;
        font-weight: bold;
        letter-spacing: 1px;
    }
    .pregunta-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #a855f7;
        margin-top: 25px;
        margin-bottom: 25px;
    }
    .resultado-box {
        background-color: #064e3b;
        border: 2px solid #10b981;
        padding: 20px;
        border-radius: 10px;
        color: #34d399;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    h3 {
        color: #f1f5f9 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado de la broma
st.markdown("""
    <div class="main-panel">
        <h1 class="titulo">🌈 TEST PARA DESCUBRIR POR QUÉ IPIA ES TAN GAY 🌈</h1>
        <p style='color: #94a3b8; font-size: 15px; margin-top: 10px;'>Análisis interactivo definitivo para el caso de Sebastián Ipia</p>
    </div>
""", unsafe_allow_html=True)

st.info("ℹ️ **Aviso del Sistema:** Este cuestionario recopila datos en tiempo real para determinar el origen exacto de las conductas alegres de Ipia. Responde con la verdad.")

# Inicializar estados de la memoria de Streamlit
if "procesado" not in st.session_state:
    st.session_state.procesado = False
if "resultado_actual" not in st.session_state:
    st.session_state.resultado_actual = ""

# Lista de resultados aleatorios bien cerrada para evitar SyntaxError
resultados_locos = [
    "🚨 DIAGNÓSTICO TRÁGICO: Los niveles de sospecha superan el 99.8%. No hay retorno. Se recomienda regalarle una cartera rosa de inmediato.",
    "🧬 ANÁLISIS ADN: Se detectó que Sebastián prefiere ver partidos de fútbol solo para analizar los pantalones de los jugadores. Caso confirmado.",
    "🎭 INFORME FINAL: El sujeto finge que le gustan las mujeres pero se sabe la discografía completa de Katy Perry y baila frente al espejo cuando nadie lo ve.",
    "⚠️ ALERTA DE SISTEMA: El algoritmo colapsó debido al exceso de energía delicada detectada en el historial de Sebastián. Veredicto: Recontra confirmado.",
    "📈 ESTADÍSTICA CIENTÍFICA: El 100% de los satélites espaciales confirman que a Sebastián se le moja la canoa incluso cuando no está lloviendo."
]

# --- BLOQUE DE PREGUNTAS ---

# Pregunta 1: Selección Múltiple
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 1️⃣ ¿Cuál crees que fue el detonante principal en su vida?")
p1 = st.radio(
    "Selecciona la teoría más acertada:",
    [
        "--- Selecciona una opción ---",
        "Se cayó de chiquito en un balde de agua bendita con brillantina.",
        "Escuchó una canción de Lady Gaga al revés a los 8 años.",
        "Un defecto genético que lo obliga a caminar con un flow sospechoso.",
        "Todas las anteriores juntas (Teoría más respaldada)."
    ],
    key="pregunta_1"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 2: CASILLA ABIERTA PARA ESCRIBIR LA RESPUESTA
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 2️⃣ Teoría Libre del Evaluador")
st.markdown("<p style='color: #94a3b8; font-size: 14px;'>Escribe aquí detalladamente tu respuesta y por qué consideras que él es así:</p>", unsafe_allow_html=True)

respuesta_libre = st.text_area(
    "Tu respuesta:", 
    placeholder="Ej: Yo opino que desde que empezó a usar pantalones tubito se le nota que...",
    key="respuesta_usuario"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 3: Selección Múltiple de Síntomas
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 3️⃣ Síntoma más evidente en el día a día")
p3 = st.radio(
    "¿En qué momento es imposible disimularlo?",
    [
        "--- Selecciona una opción ---",
        "Cuando saluda y se le dobla la muñeca automáticamente.",
        "Cuando mira fijamente a sus amigos con ojos de enamorado.",
        "Cuando le da miedo ensuciarse los tenis y camina en puntitas.",
        "Cuando respira."
    ],
    key="pregunta_3"
)
st.markdown('</div>', unsafe_allow_html=True)


# --- BOTÓN DE ENVÍO Y EFECTO MÁGICO ---

st.write("")
if st.button("🚀 ENVIAR RESPUESTAS AL SERVIDOR CENTRAL", use_container_width=True):
    if not respuesta_libre or p1 == "--- Selecciona una opción ---" or p3 == "--- Selecciona una opción ---":
        st.warning("⚠️ Debes llenar todo el cuestionario y escribir tu respuesta para que el sistema lo analice.")
    else:
        with st.spinner("🧠 Analizando texto libre enviado..."):
            time.sleep(1.2)
        with st.spinner("🛰️ Midiendo niveles de desviación en el servidor de Ipia..."):
            time.sleep(1.2)
        with st.spinner("💾 Encriptando y borrando respuestas del historial..."):
            time.sleep(0.8)
        
        st.session_state.resultado_actual = random.choice(resultados_locos)
        st.session_state.procesado = True
        st.rerun()

# Mostrar el resultado
if st.session_state.procesado:
    st.markdown(f"""
        <div class="resultado-box">
            <h3>📊 VERDICTO DEL ALGORITMO:</h3>
            <p style='font-size: 18px;'>{st.session_state.resultado_actual}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Realizar nueva prueba de laboratorio"):
        st.session_state.procesado = False
        st.session_state.resultado_actual = ""
        st.rerun()

st.write("---")
st.caption("🔬 Software de Entretenimiento de Código Abierto • Prohibido para Sebastián Ipia 🤫")
