import streamlit as st
import time
import random

# 1. Configuración de la página única
st.set_page_config(
    page_title="Test de Ipia",
    page_icon="🌈",
    layout="centered"
)

# 2. Diseño estético (Dark Mode con detalles Neón)
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

st.info("ℹ️ **Aviso del Sistema:** Este cuestionario recopila el visaje en tiempo real para determinar por qué a Ipia se le moja la canoa tan feo. Responde la firme.")

# Inicializar estados de la memoria de Streamlit
if "procesado" not in st.session_state:
    st.session_state.procesado = False
if "resultado_actual" not in st.session_state:
    st.session_state.resultado_actual = ""

# Lista de resultados aleatorios bien caleños y exagerados
resultados_locos = [
    "🚨 VERDICTO TRÁGICO: El visaje supera el 100%. No hay nada que hacer, mano. Ya le están tramitando una cartera rosa para que salga a dar vueltas por el parque.",
    "🧬 ANÁLISIS CIENTÍFICO: Se confirmó que Sebastián solo va a las rumbas a mirar cómo les quedan los pantalones a los otros manes. Caso recontra cerrado.",
    "🎭 INFORME SECRETO: El tipo se las da de muy parado, pero en el baño se pone a ensayar las canciones de Karol G frente al espejo haciendo los pasitos prohibidos. ¡Pillado!",
    "⚠️ ALERTA DE SUCURSAL: El sistema colapsó por exceso de energía delicada. Este man bota más plumas que una gallina en un trancón. Veredicto: Es bien pato.",
    "📈 ESTADÍSTICA LOCAL: Los satélites de la zona confirman que a Sebastián se le quiebra la muñeca solita apenas escucha un sartenazo de salsa baúl."
]

# --- BLOQUE DE PREGUNTAS (6 PREGUNTAS) ---

# Pregunta 1
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 1️⃣ ¿Cuál fue el detonante principal para que Ipia se volviera así?")
p1 = st.radio(
    "Selecciona la teoría más respaldada por el barrio:",
