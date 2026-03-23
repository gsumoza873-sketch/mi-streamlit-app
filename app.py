import streamlit as st
import time

# ─── Configuración ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Encuesta Fútbol | Perfil del Aficionado",
    page_icon="⚽",
    layout="centered"
)

# ─── Estilos Profesionales ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Reset y base */
.stApp {
    background-color: #080c10;
    font-family: 'DM Sans', sans-serif;
}

/* Fondo con patrón sutil */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(circle at 20% 80%, rgba(34,197,94,0.06) 0%, transparent 50%),
                      radial-gradient(circle at 80% 20%, rgba(34,197,94,0.04) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

/* Header principal */
.survey-header {
    text-align: center;
    padding: 48px 0 32px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 40px;
}
.survey-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #22c55e;
    margin-bottom: 12px;
}
.survey-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(40px, 8vw, 68px);
    letter-spacing: 2px;
    color: #ffffff;
    line-height: 1;
    margin: 0 0 16px;
}
.survey-subtitle {
    font-size: 15px;
    color: rgba(255,255,255,0.45);
    font-weight: 300;
    max-width: 400px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Tarjeta de pregunta */
.q-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.01) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.q-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #22c55e, #16a34a);
    border-radius: 3px 0 0 3px;
}
.q-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    color: #22c55e;
    margin-bottom: 6px;
}
.q-label {
    font-size: 16px;
    font-weight: 500;
    color: #f0f0f0;
    margin-bottom: 20px;
}

/* Separador decorativo */
.divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 36px 0;
}
.divider-line {
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.07);
}
.divider-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #22c55e;
    opacity: 0.6;
}

/* Anular estilos Streamlit en widgets */
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stRadio"] label,
div[data-testid="stSlider"] label {
    color: #d1d5db !important;
    font-size: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
}
div[data-testid="stSelectbox"] > div {
    background-color: #111418 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: #f0f0f0 !important;
}
div[data-testid="stRadio"] > div {
    gap: 8px !important;
}

/* Botón */
.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: #fff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 40px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: opacity 0.2s, transform 0.1s !important;
}
.stButton > button:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}

/* Resultado */
.result-card {
    background: linear-gradient(135deg, #0d1f0e, #0a1a1a);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    margin-top: 24px;
}
.result-badge {
    display: inline-block;
    background: rgba(34,197,94,0.12);
    color: #22c55e;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 20px;
    border: 1px solid rgba(34,197,94,0.2);
    margin-bottom: 20px;
}
.result-score {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 80px;
    color: #22c55e;
    line-height: 1;
    margin: 0;
}
.result-label {
    font-size: 20px;
    font-weight: 600;
    color: #ffffff;
    margin-top: 8px;
}
.result-desc {
    font-size: 14px;
    color: rgba(255,255,255,0.45);
    margin-top: 12px;
    font-weight: 300;
    line-height: 1.7;
    max-width: 360px;
    margin-left: auto;
    margin-right: auto;
}

/* Barra de progreso de resultado */
.score-bar-bg {
    background: rgba(255,255,255,0.06);
    border-radius: 100px;
    height: 6px;
    margin: 24px 0 8px;
    overflow: hidden;
}
.score-bar-fill {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(90deg, #22c55e, #86efac);
    transition: width 1s ease;
}
.score-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: rgba(255,255,255,0.3);
    margin-bottom: 4px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}
section[data-testid="stSidebar"] * {
    color: #d1d5db !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Progress indicator */
.progress-row {
    display: flex;
    gap: 6px;
    justify-content: center;
    margin-bottom: 32px;
}
.progress-dot {
    width: 28px;
    height: 4px;
    border-radius: 4px;
    background: rgba(255,255,255,0.1);
}
.progress-dot.active {
    background: #22c55e;
}

/* Mensajes de error */
div[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)


# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="survey-header">
    <div class="survey-eyebrow">Encuesta · Perfil del aficionado</div>
    <div class="survey-title">¿QUÉ TAN<br>FUTBOLERO ERES?</div>
    <div class="survey-subtitle">5 preguntas para descubrir tu nivel de pasión por el fútbol. Responde con honestidad.</div>
</div>
""", unsafe_allow_html=True)


# ─── Preguntas ────────────────────────────────────────────────────────────────

# P1
st.markdown("""
<div class="q-card">
    <div class="q-number">PREGUNTA 01 / 05</div>
    <div class="q-label">¿Cuál es tu equipo favorito?</div>
</div>
""", unsafe_allow_html=True)
q1 = st.selectbox(
    "equipo",
    ["Selecciona una opción…", "Real Madrid", "Barcelona", "Boca Juniors", "River Plate", "Selección Nacional", "Otro"],
    label_visibility="collapsed"
)

st.markdown('<div class="divider"><div class="divider-line"></div><div class="divider-dot"></div><div class="divider-line"></div></div>', unsafe_allow_html=True)

# P2
st.markdown("""
<div class="q-card">
    <div class="q-number">PREGUNTA 02 / 05</div>
    <div class="q-label">¿Con qué frecuencia ves partidos completos?</div>
</div>
""", unsafe_allow_html=True)
q2 = st.radio(
    "partidos",
    ["Nunca o casi nunca", "Solo los importantes", "La mayoría de partidos", "Todos sin excepción"],
    label_visibility="collapsed"
)

st.markdown('<div class="divider"><div class="divider-line"></div><div class="divider-dot"></div><div class="divider-line"></div></div>', unsafe_allow_html=True)

# P3
st.markdown("""
<div class="q-card">
    <div class="q-number">PREGUNTA 03 / 05</div>
    <div class="q-label">¿Cómo sueles reaccionar ante un gol?</div>
</div>
""", unsafe_allow_html=True)
q3 = st.radio(
    "celebracion",
    ["Me quedo callado/a", "Aplauso discreto", "Me levanto y aplaudo", "Grito y celebro sin control"],
    label_visibility="collapsed"
)

st.markdown('<div class="divider"><div class="divider-line"></div><div class="divider-dot"></div><div class="divider-line"></div></div>', unsafe_allow_html=True)

# P4
st.markdown("""
<div class="q-card">
    <div class="q-number">PREGUNTA 04 / 05</div>
    <div class="q-label">¿Quién es el mejor jugador de la historia para ti?</div>
</div>
""", unsafe_allow_html=True)
q4 = st.selectbox(
    "jugador",
    ["Selecciona una opción…", "Lionel Messi", "Cristiano Ronaldo", "Diego Maradona", "Pelé", "Zinédine Zidane", "Otro"],
    label_visibility="collapsed"
)

st.markdown('<div class="divider"><div class="divider-line"></div><div class="divider-dot"></div><div class="divider-line"></div></div>', unsafe_allow_html=True)

# P5
st.markdown("""
<div class="q-card">
    <div class="q-number">PREGUNTA 05 / 05</div>
    <div class="q-label">¿Qué tan importante es el fútbol en tu vida?</div>
</div>
""", unsafe_allow_html=True)
q5 = st.select_slider(
    "importancia",
    options=["No me interesa", "Es un pasatiempo", "Me apasiona", "Es parte de mí", "Es mi vida entera"],
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)


# ─── Botón y resultado ────────────────────────────────────────────────────────

# Scoring
score_map = {
    "q2": {"Nunca o casi nunca": 0, "Solo los importantes": 1, "La mayoría de partidos": 2, "Todos sin excepción": 3},
    "q3": {"Me quedo callado/a": 0, "Aplauso discreto": 1, "Me levanto y aplaudo": 2, "Grito y celebro sin control": 3},
    "q5": {"No me interesa": 0, "Es un pasatiempo": 1, "Me apasiona": 2, "Es parte de mí": 3, "Es mi vida entera": 4},
}

def get_profile(pct):
    if pct >= 90:
        return "⚽ Crack Total", "Vives y respiras fútbol. El balón es parte de tu identidad.", 100
    elif pct >= 70:
        return "🏆 Aficionado Fiel", "El fútbol es una pasión real. Rara vez te pierdes un partido.", 80
    elif pct >= 45:
        return "📺 Seguidor Casual", "Disfrutas el fútbol cuando hay ambiente, aunque no es tu prioridad.", 55
    else:
        return "🌱 Recién Iniciado", "El fútbol no es lo tuyo por ahora, pero quizás aún puede enamorarte.", 25

if st.button("GENERAR MI PERFIL →"):
    if q1 == "Selecciona una opción…" or q4 == "Selecciona una opción…":
        st.error("Por favor responde todas las preguntas antes de continuar.")
    else:
        with st.spinner("Analizando tu perfil…"):
            time.sleep(2)

        score = (
            score_map["q2"][q2] +
            score_map["q3"][q3] +
            score_map["q5"][q5]
        )
        max_score = 10
        pct = round((score / max_score) * 100)

        title, desc, bar_pct = get_profile(pct)

        st.balloons()

        st.markdown(f"""
        <div class="result-card">
            <div class="result-badge">Resultado · Encuesta Fútbol 2025</div>
            <div class="result-score">{pct}%</div>
            <div class="result-label">{title}</div>
            <div class="result-desc">{desc}</div>
            <div class="score-bar-label">
                <span>Nivel de afición</span>
                <span>{pct} / 100</span>
            </div>
            <div class="score-bar-bg">
                <div class="score-bar-fill" style="width:{bar_pct}%"></div>
            </div>
            <div style="margin-top:24px; font-size:12px; color:rgba(255,255,255,0.2); letter-spacing:1px; text-transform:uppercase;">
                Equipo · {q1} &nbsp;·&nbsp; Ídolo · {q4}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📋 Encuesta")
    st.markdown("**Autor:** Gabriel")
    st.markdown("**Edición:** 2025")
    st.markdown("---")
    st.markdown("Esta encuesta mide el nivel de afición futbolística a través de 5 indicadores clave.")
    st.markdown("---")
    st.caption("© 2025 · Todos los derechos reservados")
