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

# Lista de resultados aleatorios bien caleños sin artistas viejos
resultados_locos = [
    "🚨 VERDICTO TRÁGICO: El visaje supera el 100%. No hay nada que hacer, mano. Ya le están tramitando una cartera rosa para que salga a dar vueltas por el parque.",
    "🧬 ANÁLISIS CIENTÍFICO: Se confirmó que Sebastián solo va a las rumbas a mirar cómo les quedan los pantalones a los otros manes. Caso recontra cerrado.",
    "🎭 INFORME SECRETO: El tipo se las da de muy parado, pero en el baño se pone a ensayar las canciones de Karol G frente al espejo haciendo los pasitos prohibidos. ¡Pillado!",
    "⚠️ ALERTA DE SUCURSAL: El sistema colapsó por exceso de energía delicada. Este man bota más plumas que una gallina en un trancón. Veredicto: Es bien pato.",
    "📈 ESTADÍSTICA LOCAL: Los satélites de la zona confirman que a Sebastián se le quiebra la muñeca solita apenas escucha un sartenazo de salsa baúl."
]

# --- BLOQUE DE PREGUNTAS (6 PREGUNTAS CORREGIDAS) ---

# Pregunta 1
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 1️⃣ ¿Cuál fue el detonante principal para que Ipia se volviera así?")
p1 = st.radio(
    "Selecciona la teoría más respaldada por el barrio:",
    [
        "--- Selecciona una opción ---",
        "Se tomó un champús vencido que le alteró las hormonas.",
        "Un duende de Pance lo asustó y lo dejó picado de la rosca.",
        "Se la pasa escuchando temas de La Rosalía a escondidas y se le pegó el flow.",
        "Se tragó la brillantina de una cartelera del colegio y se transformó."
    ],
    key="pregunta_1"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 2: CASILLA ABIERTA (La que se auto-borra)
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 2️⃣ Teoría Libre de la Pipol")
st.markdown("<p style='color: #94a3b8; font-size: 14px;'>Escribe aquí tu propia hipótesis de por qué a este man se le moja la canoa tanto:</p>", unsafe_allow_html=True)

respuesta_libre = st.text_area(
    "Tu respuesta sin filtro:", 
    placeholder="Ej: Yo digo que desde que se la pasa metido en el gimnasio se la pasa mirándole el bote a los profes...",
    key="respuesta_usuario"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 3
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 3️⃣ El síntoma más evidente en el día a día")
p3 = st.radio(
    "¿En qué momento se le nota más lo pato?",
    [
        "--- Selecciona una opción ---",
        "Cuando saluda y la muñeca se le dobla a 180 grados en cámara lenta.",
        "Cuando ve a un man acuerpado y muerde el labio disimuladamente.",
        "Cuando le da miedo ensuciar los tenis blancos y camina empinado pareciendo una garza.",
        "A toda hora, desde que se levanta hasta que se acuesta."
    ],
    key="pregunta_3"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 4
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 4️⃣ ¿Cómo disimula Ipia cuando está con mujeres?")
p4 = st.radio(
    "Estrategia de camuflaje de Sebastián:",
    [
        "--- Selecciona una opción ---",
        "Empieza a hablar grueso y a decir '¿Qué dice, mi pez?' cada tres palabras.",
        "Se pone a cantar las de Karol G a todo pulmón diciendo que es 'por la cultura'.",
        "Le da un ataque de tos y se va corriendo al baño a ver tiktoks de hombres fit.",
        "No disimula nada, ellas se dan cuenta a los dos segundos por la forma en que pestañea."
    ],
    key="pregunta_4"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 5
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 5️⃣ En una rumba, ¿cuál es el comportamiento típico de Sebastián?")
p5 = st.radio(
    "Su actitud en la pista de baile:",
    [
        "--- Selecciona una opción ---",
        "Pide una Smirnoff de manzana y la sostiene levantando el dedo meñique.",
        "Se altera todo y empieza a hacer las poses de Bizcochito de Rosalía cuando nadie lo ve.",
        "Dice que no baila salsa porque le cansa la cintura, pero le ponen reggaetón y baja hasta el subsuelo.",
        "Se pasa toda la noche tomándose selfies con filtro de perrito para subirlas a mejores amigos."
    ],
    key="pregunta_5"
)
st.markdown('</div>', unsafe_allow_html=True)


# Pregunta 6
st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
st.markdown("### 6️⃣ Si Ipia tuviera un novio secreto, ¿cómo sería?")
p6 = st.radio(
    "El prototipo ideal de Sebastián según la ciencia:",
    [
        "--- Selecciona una opción ---",
        "Un barbero bien peludo que le haga la ceja y le hable al oído.",
        "Un mototaxista con gorra de lado que lo lleve a dar vueltas.",
        "Un pelado del gimnasio que le ayude a cargar las mancuernas pesadas.",
        "Cualquier man que le preste atención por más de cinco minutos."
    ],
    key="pregunta_6"
)
st.markdown('</div>', unsafe_allow_html=True)


# --- BOTÓN DE ENVÍO Y EFECTO MÁGICO ---

st.write("")
if st.button("🚀 PROCESAR EXAMEN EN EL SATÉLITE VALLUNO", use_container_width=True):
    if (not respuesta_libre or 
        p1 == "--- Selecciona una opción ---" or 
        p3 == "--- Selecciona una opción ---" or 
        p4 == "--- Selecciona una opción ---" or 
        p5 == "--- Selecciona una opción ---" or 
        p6 == "--- Selecciona una opción ---"):
        st.warning("⚠️ ¡No seas flojo! Tienes que responder todas las preguntas y meter la teoría libre para poder calcular el visaje.")
    else:
        with st.spinner("🕵️‍♂️ Analizando la respuesta libre con los chismosos del barrio..."):
            time.sleep(1.2)
        with st.spinner("🛵 Escaneando el historial de Ipia cuando pasa por la recta de Cali..."):
            time.sleep(1.2)
        with st.spinner("🗑️ Borrando evidencias para que Sebastián no se ponga a llorar..."):
            time.sleep(0.8)
        
        st.session_state.resultado_actual = random.choice(resultados_locos)
        st.session_state.procesado = True
        st.rerun()

# Mostrar el resultado
if st.session_state.procesado:
    st.markdown(f"""
        <div class="resultado-box">
            <h3>📊 VERDICTO DEL ALGORITMO CALEÑO:</h3>
            <p style='font-size: 18px;'>{st.session_state.resultado_actual}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Volver a escanear a Ipia"):
        st.session_state.procesado = False
        st.session_state.resultado_actual = ""
        st.rerun()

st.write("---")
st.caption("🔬 Software Anti-Visaje Organizado • Prohibido para Sebastián Ipia • Jamundí, Valle 🤫")
