import streamlit as st
import random
import time

st.set_page_config(page_title="LVBP Master Stats", page_icon="⚾", layout="wide")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #001a00 0%, #004d00 100%); color: white; }
.titulo-estadio {
    background-color: #000; color: #f1c40f; padding: 15px;
    border: 4px solid #f1c40f; border-radius: 10px;
    text-align: center; font-family: 'Arial Black', sans-serif;
}
.stRadio > div {
    background-color: rgba(255,255,255,0.1); padding: 15px;
    border-radius: 10px; border-left: 5px solid #f1c40f;
}
</style>""", unsafe_allow_html=True)

# ── BANCO DE PREGUNTAS (15 en lugar de 5) ────────────────────────────────────
BANCO = {
    "fácil": [
        {"q": "¿Qué equipo tiene más títulos en la LVBP?",
         "ops": ["Magallanes", "Leones", "Tigres"], "ans": "Leones"},
        {"q": "¿Dónde juegan las Águilas del Zulia?",
         "ops": ["Maracay", "Valencia", "Maracaibo"], "ans": "Maracaibo"},
        {"q": "¿Quién es 'El Señor Pelota'?",
         "ops": ["Luis Aparicio", "Víctor Davalillo", "Robert Pérez"], "ans": "Víctor Davalillo"},
        {"q": "¿Cuál es el apodo del Magallanes?",
         "ops": ["Los Melenudos", "La Nave Turca", "Los Salados"], "ans": "La Nave Turca"},
        {"q": "¿Cuál fue el campeón de la temporada 23-24?",
         "ops": ["Magallanes", "Leones", "Tiburones"], "ans": "Tiburones"},
    ],
    "medio": [
        {"q": "¿Cuántos títulos tiene el Magallanes?",
         "ops": ["10", "13", "17"], "ans": "13"},
        {"q": "¿Dónde juegan los Caribes de Anzoátegui?",
         "ops": ["Maturín", "Puerto Ordaz", "Barcelona"], "ans": "Barcelona"},
        {"q": "¿Qué equipo fue anteriormente conocido como Pastora de los Llanos?",
         "ops": ["Caribes", "Bravos de Margarita", "Tigres"], "ans": "Bravos de Margarita"},
        {"q": "¿Quién dirigió a los Tiburones en su sequía histórica?",
         "ops": ["Felipe Alou", "Ozzie Guillén", "Luis Salazar"], "ans": "Ozzie Guillén"},
        {"q": "¿Cuántos títulos tienen los Tigres de Aragua?",
         "ops": ["6", "8", "10"], "ans": "10"},
    ],
    "difícil": [
        {"q": "¿En qué año fue fundado el Magallanes?",
         "ops": ["1917", "1920", "1930"], "ans": "1917"},
        {"q": "¿Quién es el máximo jugador histórico de los Tigres?",
         "ops": ["Andrés Galarraga", "David Concepción", "Omar Vizquel"], "ans": "David Concepción"},
        {"q": "¿Cuántos títulos tienen los Tiburones de La Guaira?",
         "ops": ["6", "8", "10"], "ans": "8"},
        {"q": "¿Qué equipo ganó más Series del Caribe representando a Venezuela?",
         "ops": ["Leones", "Magallanes", "Águilas"], "ans": "Leones"},
        {"q": "¿En qué año fue fundado el Caracas?",
         "ops": ["1942", "1950", "1938"], "ans": "1942"},
    ],
}

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "mejor_puntaje" not in st.session_state:
    st.session_state.mejor_puntaje = 0
if "juego_terminado" not in st.session_state:
    st.session_state.juego_terminado = False

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h1 style='color:#f1c40f;'>🏟️ INFO LVBP</h1>", unsafe_allow_html=True)
    st.write("Creado por: **Gabriel**")
    st.metric("🏆 Mejor puntaje", f"{st.session_state.mejor_puntaje}/5")
    st.divider()

    dificultad = st.radio("Dificultad:", ["fácil", "medio", "difícil"], index=1)

    st.subheader("📚 Historia de los Equipos")
    equipo = st.selectbox("Selecciona un equipo:", [
        "Leones del Caracas", "Navegantes del Magallanes", "Tigres de Aragua",
        "Cardenales de Lara", "Tiburones de La Guaira", "Águilas del Zulia",
        "Caribes de Anzoátegui", "Bravos de Margarita"
    ])
    info_equipos = {
        "Leones del Caracas":       {"títulos": 21, "jugador": "Víctor Davalillo", "historia": "Fundados en 1942. El equipo con más títulos de la liga."},
        "Navegantes del Magallanes":{"títulos": 13, "jugador": "Luis 'Camaleón' García", "historia": "El equipo más antiguo de Venezuela (1917)."},
        "Tigres de Aragua":         {"títulos": 10, "jugador": "David Concepción", "historia": "Famosos por su dinastía en los 2000."},
        "Cardenales de Lara":       {"títulos": 6,  "jugador": "Robert Pérez", "historia": "Símbolo del occidente del país."},
        "Tiburones de La Guaira":   {"títulos": 8,  "jugador": "Luis Aparicio", "historia": "Rompieron una sequía histórica en 23-24."},
        "Águilas del Zulia":        {"títulos": 6,  "jugador": "Luis Aparicio", "historia": "Gran tradición zuliana."},
        "Caribes de Anzoátegui":    {"títulos": 4,  "jugador": "Eliézer Alfonzo", "historia": "El equipo dominante del oriente en la última década."},
        "Bravos de Margarita":      {"títulos": 0,  "jugador": "Henry Blanco", "historia": "Anteriormente Pastora de los Llanos."},
    }
    e = info_equipos[equipo]
    st.info(f"**Títulos:** {e['títulos']}\n\n**Máximo Jugador:** {e['jugador']}\n\n**Reseña:** {e['historia']}")

# ── INICIO / RESET ────────────────────────────────────────────────────────────
def iniciar_juego():
    pool = BANCO[dificultad].copy()
    random.shuffle(pool)
    st.session_state.preguntas   = pool[:5]
    st.session_state.idx         = 0
    st.session_state.puntos      = 0
    st.session_state.respuestas  = {}
    st.session_state.juego_terminado = False

# ── CUERPO PRINCIPAL ──────────────────────────────────────────────────────────
st.markdown('<div class="titulo-estadio"><h1>⚾ DESAFÍO LVBP ⚾</h1></div>', unsafe_allow_html=True)
st.write("")

if not st.session_state.preguntas:
    st.info("Elige la dificultad en el panel izquierdo y presiona **Iniciar Juego**.")
    if st.button("▶ Iniciar Juego"):
        iniciar_juego()
        st.rerun()

elif not st.session_state.juego_terminado:
    # ── Barra de progreso y puntaje parcial ──
    progreso = st.session_state.idx / 5
    st.progress(progreso, text=f"Pregunta {st.session_state.idx + 1} de 5  |  Puntaje: {st.session_state.puntos}")

    item = st.session_state.preguntas[st.session_state.idx]
    ops  = item["ops"].copy()
    random.shuffle(ops)  # barajar opciones para que no siempre esté igual

    respuesta = st.radio(f"**{item['q']}**", ops, key=f"q_{st.session_state.idx}")

    if st.button("Responder ➜"):
        st.session_state.respuestas[st.session_state.idx] = {
            "pregunta": item["q"],
            "elegida":  respuesta,
            "correcta": item["ans"],
            "ok":       respuesta == item["ans"],
        }
        if respuesta == item["ans"]:
            st.session_state.puntos += 1

        st.session_state.idx += 1
        if st.session_state.idx >= 5:
            st.session_state.juego_terminado = True
            if st.session_state.puntos > st.session_state.mejor_puntaje:
                st.session_state.mejor_puntaje = st.session_state.puntos
        st.rerun()

else:
    # ── PANTALLA DE RESULTADOS ────────────────────────────────────────────────
    puntos = st.session_state.puntos

    if puntos == 5:
        st.balloons()
        st.markdown("## 🏆 ¡GRAND SLAM! Puntaje perfecto.")
    elif puntos >= 3:
        st.markdown(f"## ⚾ ¡Buen juego! Puntaje: {puntos}/5")
    else:
        st.markdown(f"## 📋 Sigue practicando. Puntaje: {puntos}/5")

    st.subheader("Reporte del árbitro:")
    for r in st.session_state.respuestas.values():
        if r["ok"]:
            st.success(f"✅ **Correcto** — {r['pregunta']}")
        else:
            st.error(f"❌ {r['pregunta']}\nElegiste: *{r['elegida']}* → Correcta: **{r['correcta']}**")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Jugar de nuevo (misma dificultad)"):
            iniciar_juego()
            st.rerun()
    with col2:
        if st.button("🆕 Cambiar dificultad"):
            st.session_state.preguntas = []
            st.rerun()
