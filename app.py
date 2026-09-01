import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Rumbo a la Cima ⚽",
    page_icon="⚽",
    layout="centered",
)

CARRERAS_FILE = "carreras.csv"
EDAD_INICIAL = 16
EDAD_RETIRO_FORZOSO = 36
EDAD_MIN_RETIRO_VOLUNTARIO = 30

# =========================================================
# ESTILOS
# =========================================================
st.markdown("""
<style>
:root {
    --verde: #1B7A3D;
    --verde-oscuro: #0F4F27;
    --dorado: #D4A017;
    --blanco: #FFFFFF;
    --gris-osc: #262626;
}

.stApp {
    background: linear-gradient(160deg, #EAF7EE 0%, #FFFFFF 40%, #FFF9E8 100%);
}

.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 8px;
    background: linear-gradient(90deg, var(--verde), var(--dorado));
    z-index: 999;
}

/* Forzar texto oscuro en todo el contenido para que no se vuelva invisible
   si el navegador/celular está en modo oscuro */
.stApp p, .stApp li, .stApp span, .stApp label,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4,
.stRadio label p, .stRadio label span,
.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--gris-osc) !important;
}

.header-banner {
    background: linear-gradient(90deg, var(--verde-oscuro), var(--verde));
    padding: 26px 20px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 10px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
}
.header-banner h1 { color: white !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0; font-size: 2em; }
.header-banner p { color: white !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); margin-top: 6px; }

.stApp p.firma {
    text-align: center;
    color: var(--verde-oscuro) !important;
    font-size: 0.85em;
    font-weight: bold;
    opacity: 0.85;
    margin-bottom: 18px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white !important;
    border: 2px solid var(--verde) !important;
    border-radius: 14px !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    padding: 8px;
    margin-bottom: 16px;
}

.stApp span.tag-verde {
    display: inline-block; background: var(--verde); color: #ffffff !important;
    padding: 4px 12px; border-radius: 20px; font-size: 0.78em; font-weight: bold; margin-bottom: 8px;
}
.stApp span.tag-dorado {
    display: inline-block; background: var(--dorado); color: #ffffff !important;
    padding: 4px 12px; border-radius: 20px; font-size: 0.78em; font-weight: bold; margin-bottom: 8px;
}

.stat-box {
    background: white; border: 2px solid var(--verde); border-radius: 12px;
    padding: 10px; text-align: center; margin-bottom: 8px;
}
.stat-box .valor { font-size: 1.6em; font-weight: bold; color: var(--verde-oscuro) !important; }
.stat-box .etiqueta { font-size: 0.8em; color: var(--gris-osc) !important; }

.oferta-card {
    background: white; border: 2px solid var(--dorado); border-radius: 12px;
    padding: 14px; margin-bottom: 10px;
}

.resultado-box {
    text-align: center; padding: 22px; border-radius: 16px;
    background: linear-gradient(135deg, var(--verde-oscuro), var(--verde));
    color: white; margin-bottom: 18px;
}
.resultado-box h1, .resultado-box h2, .resultado-box p { color: white !important; }

.stButton>button { background-color: var(--verde-oscuro); color: white; border-radius: 10px; border: none; padding: 8px 20px; font-weight: bold; }
.stButton>button:hover { background-color: var(--verde); color: white; }
.stButton>button, .stButton>button * { color: white !important; }

.leaderboard-row { padding: 10px 14px; border-radius: 10px; margin-bottom: 6px; }
.rank-1 { background: linear-gradient(90deg, #FFD700, #D4A017); font-weight: bold; }
.rank-2 { background: #E8E8E8; font-weight: bold; }
.rank-3 { background: #D7B899; font-weight: bold; }
.rank-other { background: #EAF7EE; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATOS: CLUBES POR NIVEL
# =========================================================
CLUBES = {
    "grande": ["Real Madrid", "Manchester City", "Bayern Múnich", "Flamengo", "Boca Juniors"],
    "mediano": ["Sevilla FC", "AS Mónaco", "River Plate", "Deportivo Táchira", "Millonarios FC"],
    "pequeño": ["Estudiantes de Mérida", "Zamora FC", "Deportivo Lara", "CD Godoy Cruz", "Real Cartagena"],
}
FUERZA_CLUB = {"grande": 88, "mediano": 74, "pequeño": 58}

# =========================================================
# DATOS: RETO DE MEMORIA (secuencias de jugadas)
# =========================================================
JUGADAS = ["⬆️ Vertical", "↔️ Horizontal", "🔄 Diagonal", "⚡ Pared (uno-dos)"]
LARGO_SECUENCIA = 5

# =========================================================
# DATOS: RETO TÁCTICO (banco de preguntas)
# =========================================================
PREGUNTAS_TACTICAS = [
    {"pregunta": "Estás en contragolpe 3 contra 2. ¿Qué haces?",
     "opciones": ["Driblas a los dos defensores tú solo", "Abres el balón al compañero libre en la banda", "Retienes el balón esperando refuerzos", "Tiras un centro al área vacía"],
     "correcta": "Abres el balón al compañero libre en la banda"},
    {"pregunta": "Tu equipo pierde 0-1 a falta de 10 minutos. ¿Qué ajuste táctico es más razonable?",
     "opciones": ["Meter un defensor central más", "Subir líneas y arriesgar con un delantero extra", "Cerrar el equipo atrás a defender el resultado", "Cambiar de portero"],
     "correcta": "Subir líneas y arriesgar con un delantero extra"},
    {"pregunta": "El rival presiona muy alto desde el saque de meta. ¿Cómo saca tu equipo el balón?",
     "opciones": ["Pelotazo largo sin pensar", "Pase corto en salida con apoyos y triangulaciones", "El portero se queda quieto con el balón", "Saque directo a la banda contraria"],
     "correcta": "Pase corto en salida con apoyos y triangulaciones"},
    {"pregunta": "Vas ganando 1-0 en el minuto 85. ¿Qué prioridad táctica tiene el equipo?",
     "opciones": ["Buscar el segundo gol a toda costa", "Controlar el ritmo, rotar el balón y evitar pérdidas", "Sacar a todos los defensores por atacantes", "Jugar sin portero para tener un jugador extra"],
     "correcta": "Controlar el ritmo, rotar el balón y evitar pérdidas"},
    {"pregunta": "Un defensor rival es muy lento pero fuerte físicamente. ¿Cómo lo explotas?",
     "opciones": ["Con centros al área para que él despeje de cabeza", "Con carreras al espacio para ganarle en velocidad", "Evitando esa banda por completo", "Con pases atrás constantes"],
     "correcta": "Con carreras al espacio para ganarle en velocidad"},
    {"pregunta": "Falta cerca del área rival, con barrera armada. ¿Qué opción táctica es más efectiva?",
     "opciones": ["Tiro directo siempre, sin importar el ángulo", "Jugada ensayada con pase corto para cambiar el ángulo de disparo", "Centro largo directo al área", "Esperar a que pase el tiempo"],
     "correcta": "Jugada ensayada con pase corto para cambiar el ángulo de disparo"},
    {"pregunta": "Tu equipo tiene un jugador expulsado (10 contra 11). ¿Qué formación conviene?",
     "opciones": ["Formación ofensiva con 3 delanteros", "Formación más compacta con líneas cortas", "Todos los jugadores atacando sin orden", "Cambiar de arquero de campo"],
     "correcta": "Formación más compacta con líneas cortas"},
    {"pregunta": "El rival marca en zona (no al hombre) en los córners. ¿Qué movimiento ayuda más?",
     "opciones": ["Quedarse quieto esperando el centro", "Generar movimientos y desmarques para desordenar la zona", "Poner a todos los jugadores en la misma zona", "No mandar a nadie al área"],
     "correcta": "Generar movimientos y desmarques para desordenar la zona"},
    {"pregunta": "Tu equipo domina la posesión pero no genera ocasiones claras. ¿Qué falta?",
     "opciones": ["Más pases hacia atrás", "Profundidad: pases entre líneas y desmarques de ruptura", "Jugar más lento todavía", "Sacar al portero"],
     "correcta": "Profundidad: pases entre líneas y desmarques de ruptura"},
    {"pregunta": "Estás defendiendo un córner rival. ¿Qué prioridad táctica es más importante?",
     "opciones": ["Cubrir el primer palo y marcar a los rematadores clave", "Que todos vayan a buscar el balón sin marca", "Salir todos del área antes del centro", "Ignorar a los rematadores altos"],
     "correcta": "Cubrir el primer palo y marcar a los rematadores clave"},
    {"pregunta": "Tu rival juega con línea defensiva muy alta. ¿Qué recurso ofensivo la castiga mejor?",
     "opciones": ["Pases largos por encima de la defensa a la espalda", "Centros bajos constantes", "Jugar todo por el medio sin profundidad", "Balón parado únicamente"],
     "correcta": "Pases largos por encima de la defensa a la espalda"},
    {"pregunta": "Vas perdiendo 2-0 al descanso. ¿Qué mensaje táctico da más resultado?",
     "opciones": ["Resignarse al resultado", "Ajustar la presión y simplificar el juego para recuperar confianza", "Cambiar todo el sistema sin explicar nada", "Jugar más lento a propósito"],
     "correcta": "Ajustar la presión y simplificar el juego para recuperar confianza"},
    {"pregunta": "Tienes un extremo muy rápido y un lateral rival lento. ¿Qué haces?",
     "opciones": ["Cambias al extremo de banda", "Buscas encararlo uno contra uno constantemente", "Lo sacas del partido", "Lo pones de defensa central"],
     "correcta": "Buscas encararlo uno contra uno constantemente"},
    {"pregunta": "El árbitro está permitiendo un juego muy físico. ¿Qué ajuste conviene?",
     "opciones": ["Jugar con más pases cortos y evitar duelos innecesarios", "Buscar más peleas físicas", "Salir del campo en protesta", "Ignorar la situación por completo"],
     "correcta": "Jugar con más pases cortos y evitar duelos innecesarios"},
    {"pregunta": "Faltan 2 minutos y vas empatando. Tienes el balón en tu área. ¿Qué haces?",
     "opciones": ["Arriesgar con un pase corto bajo presión", "Despejar y buscar mantener la posesión en zonas seguras", "Regatear a todo el equipo rival", "Perder tiempo discutiendo con el árbitro"],
     "correcta": "Despejar y buscar mantener la posesión en zonas seguras"},
]

# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def stats_iniciales(posicion):
    base = {
        "Delantero":      {"finalizacion": 52, "pase": 40, "tactica": 38},
        "Centrocampista": {"finalizacion": 38, "pase": 52, "tactica": 48},
        "Defensa":        {"finalizacion": 30, "pase": 42, "tactica": 52},
        "Portero":        {"finalizacion": 20, "pase": 35, "tactica": 45},
    }[posicion]
    return {k: max(15, min(60, v + random.randint(-5, 5))) for k, v in base.items()}


def calcular_ovr(stats):
    return round((stats["finalizacion"] + stats["pase"] + stats["tactica"]) / 3)


def generar_ofertas(nota_prueba, ovr):
    combinada = (nota_prueba + ovr) / 2
    if combinada >= 78:
        tiers = ["grande", "grande", "mediano"]
    elif combinada >= 58:
        tiers = ["mediano", "mediano", "pequeño"]
    elif combinada >= 38:
        tiers = ["pequeño", "pequeño", "mediano"]
    else:
        tiers = ["pequeño"]
    ofertas = []
    usados = set()
    for tier in tiers:
        opciones_disp = [c for c in CLUBES[tier] if c not in usados]
        if not opciones_disp:
            continue
        club = random.choice(opciones_disp)
        usados.add(club)
        ofertas.append({"club": club, "tier": tier, "fuerza": FUERZA_CLUB[tier]})
    return ofertas


def simular_temporada(stats, club, edad):
    ovr = calcular_ovr(stats)
    fuerza = club["fuerza"]
    if ovr >= fuerza:
        partidos = random.randint(24, 30)
    elif ovr >= fuerza - 15:
        partidos = random.randint(14, 22)
    else:
        partidos = random.randint(4, 10)

    prob_gol = (stats["finalizacion"] / 100) * 0.45
    prob_asist = (stats["pase"] / 100) * 0.40

    goles = sum(1 for _ in range(partidos) if random.random() < prob_gol)
    asistencias = sum(1 for _ in range(partidos) if random.random() < prob_asist)

    convocado_seleccion = False
    if ovr >= 85:
        convocado_seleccion = True
    elif ovr >= 75 and random.random() < 0.4:
        convocado_seleccion = True

    gana_titulo = False
    if club["tier"] == "grande" and ovr >= fuerza - 8 and random.random() < 0.30:
        gana_titulo = True
    elif club["tier"] == "mediano" and ovr >= fuerza - 5 and random.random() < 0.15:
        gana_titulo = True

    return {
        "partidos": partidos, "goles": goles, "asistencias": asistencias,
        "convocado_seleccion": convocado_seleccion, "gana_titulo": gana_titulo,
    }


def cargar_carreras():
    if os.path.exists(CARRERAS_FILE):
        return pd.read_csv(CARRERAS_FILE)
    return pd.DataFrame(columns=["nombre", "posicion", "ovr_pico", "goles", "asistencias", "trofeos", "fecha"])


def guardar_carrera(nombre, posicion, ovr_pico, goles, asistencias, trofeos):
    df = cargar_carreras()
    nueva = pd.DataFrame([{
        "nombre": nombre, "posicion": posicion, "ovr_pico": ovr_pico,
        "goles": goles, "asistencias": asistencias, "trofeos": trofeos,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }])
    df = pd.concat([df, nueva], ignore_index=True)
    df.to_csv(CARRERAS_FILE, index=False)
    return df


def reset_reto_precision():
    ancho = random.randint(10, 16)
    inicio = random.randint(45, 85 - ancho)
    st.session_state.precision_target = (inicio, inicio + ancho)
    st.session_state.precision_potencia = 0
    st.session_state.precision_disparado = False
    st.session_state.precision_score = 0


def reset_reto_memoria():
    st.session_state.memoria_objetivo = [random.choice(JUGADAS) for _ in range(LARGO_SECUENCIA)]
    st.session_state.memoria_usuario = []
    st.session_state.memoria_fase = "mostrando"
    st.session_state.memoria_score = 0


def reset_reto_trivia():
    st.session_state.trivia_preguntas = random.sample(PREGUNTAS_TACTICAS, 5)
    st.session_state.trivia_idx = 0
    st.session_state.trivia_correctas = 0
    st.session_state.trivia_respondido = False
    st.session_state.trivia_score = 0

# =========================================================
# INICIALIZAR SESSION STATE
# =========================================================
if "etapa" not in st.session_state:
    st.session_state.etapa = "crear_jugador"
if "edad" not in st.session_state:
    st.session_state.edad = EDAD_INICIAL
if "temporada" not in st.session_state:
    st.session_state.temporada = 1
if "club_actual" not in st.session_state:
    st.session_state.club_actual = None
if "totales" not in st.session_state:
    st.session_state.totales = {"goles": 0, "asistencias": 0, "partidos": 0, "trofeos": 0, "convocatorias": 0}
if "ovr_pico" not in st.session_state:
    st.session_state.ovr_pico = 0
if "historial_temporadas" not in st.session_state:
    st.session_state.historial_temporadas = []

# =========================================================
# ENCABEZADO
# =========================================================
st.markdown("""
<div class="header-banner">
    <h1>⚽ Rumbo a la Cima</h1>
    <p>Tu carrera depende de tu desempeño, no de la suerte</p>
</div>
""", unsafe_allow_html=True)
st.markdown('<p class="firma">Creado por Gabriel.S</p>', unsafe_allow_html=True)

# =========================================================
# ETAPA: CREAR JUGADOR
# =========================================================
if st.session_state.etapa == "crear_jugador":
    st.markdown("### 📝 Crea tu futbolista")
    nombre = st.text_input("Nombre del jugador:", placeholder="Ej: Carlos Pérez")
    col1, col2 = st.columns(2)
    with col1:
        posicion = st.selectbox("Posición:", ["Delantero", "Centrocampista", "Defensa", "Portero"])
        nacionalidad = st.selectbox("Nacionalidad:", ["Venezuela", "Argentina", "Brasil", "Colombia", "España", "México", "Otro"])
    with col2:
        pie = st.selectbox("Pie preferido:", ["Derecho", "Izquierdo", "Ambidiestro"])

    if st.button("🚀 Empezar carrera", use_container_width=True):
        if nombre.strip() == "":
            st.warning("Escribe un nombre para tu jugador.")
        else:
            st.session_state.jugador = {"nombre": nombre.strip(), "posicion": posicion, "nacionalidad": nacionalidad, "pie": pie}
            st.session_state.stats = stats_iniciales(posicion)
            st.session_state.ovr_pico = calcular_ovr(st.session_state.stats)
            st.session_state.etapa = "inicio_temporada"
            st.rerun()

# =========================================================
# ETAPA: INICIO DE TEMPORADA
# =========================================================
elif st.session_state.etapa == "inicio_temporada":
    j = st.session_state.jugador
    s = st.session_state.stats
    ovr = calcular_ovr(s)

    st.markdown(f"### 👤 {j['nombre']} — {j['posicion']} ({j['nacionalidad']})")
    club_nombre = st.session_state.club_actual["club"] if st.session_state.club_actual else "Sin club (cantera)"
    st.markdown(f"**Temporada {st.session_state.temporada}** · Edad: {st.session_state.edad} años · Club actual: {club_nombre}")

    col1, col2, col3, col4 = st.columns(4)
    for col, (etiqueta, valor) in zip([col1, col2, col3, col4],
                                       [("Finalización", s["finalizacion"]), ("Pase", s["pase"]),
                                        ("Táctica", s["tactica"]), ("OVR", ovr)]):
        col.markdown(f'<div class="stat-box"><div class="valor">{valor}</div><div class="etiqueta">{etiqueta}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("Esta temporada te tocan **3 retos**: Precisión, Memoria y Táctica. Tu desempeño en ellos define cuánto mejoran tus estadísticas y qué clubes se fijan en ti.")

    if st.button("🎯 Comenzar retos de la temporada", use_container_width=True):
        reset_reto_precision()
        st.session_state.etapa = "reto_precision"
        st.rerun()

    if st.session_state.edad >= EDAD_MIN_RETIRO_VOLUNTARIO:
        if st.button("🏁 Retirarme ahora", use_container_width=True):
            st.session_state.etapa = "retirado"
            st.rerun()

# =========================================================
# ETAPA: RETO DE PRECISIÓN
# =========================================================
elif st.session_state.etapa == "reto_precision":
    st.markdown("### 🎯 Reto de Precisión")
    st.caption("Carga la potencia y dispara cuando creas que estás en la zona ideal. Mejora tu **Finalización**.")

    with st.container(border=True):
        st.markdown('<span class="tag-verde">Reto 1 de 3</span>', unsafe_allow_html=True)
        potencia = st.session_state.precision_potencia
        st.progress(min(potencia, 100) / 100)
        st.markdown(f"**Potencia actual:** {min(potencia, 100)}%")

        if not st.session_state.precision_disparado:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⚡ Cargar potencia", use_container_width=True):
                    st.session_state.precision_potencia += random.randint(6, 14)
                    st.rerun()
            with col2:
                if st.button("🥅 ¡Disparar!", use_container_width=True, disabled=(potencia == 0)):
                    t_min, t_max = st.session_state.precision_target
                    if t_min <= potencia <= t_max:
                        score = 100
                    else:
                        diff = min(abs(potencia - t_min), abs(potencia - t_max))
                        score = max(0, 100 - diff * 4)
                    st.session_state.precision_score = score
                    st.session_state.precision_disparado = True
                    st.rerun()
        else:
            t_min, t_max = st.session_state.precision_target
            score = st.session_state.precision_score
            if score >= 90:
                st.success(f"¡GOLAZO! Zona ideal: {t_min}-{t_max}% · Tu potencia: {min(potencia,100)}% · Puntaje: {score}")
            elif score >= 60:
                st.info(f"Tiro decente. Zona ideal: {t_min}-{t_max}% · Tu potencia: {min(potencia,100)}% · Puntaje: {score}")
            else:
                st.error(f"Fallaste el tiro. Zona ideal: {t_min}-{t_max}% · Tu potencia: {min(potencia,100)}% · Puntaje: {score}")

            if st.button("➡️ Siguiente reto", use_container_width=True):
                reset_reto_memoria()
                st.session_state.etapa = "reto_memoria"
                st.rerun()

# =========================================================
# ETAPA: RETO DE MEMORIA
# =========================================================
elif st.session_state.etapa == "reto_memoria":
    st.markdown("### 🧠 Reto de Memoria")
    st.caption("Memoriza la secuencia de jugadas y repítela en el mismo orden. Mejora tu **Pase**.")

    with st.container(border=True):
        st.markdown('<span class="tag-verde">Reto 2 de 3</span>', unsafe_allow_html=True)

        if st.session_state.memoria_fase == "mostrando":
            secuencia_txt = "  →  ".join(st.session_state.memoria_objetivo)
            st.info(f"**Secuencia a memorizar:**\n\n{secuencia_txt}")
            if st.button("👁️ Ya la memoricé, ocultar y repetir", use_container_width=True):
                st.session_state.memoria_fase = "repitiendo"
                st.rerun()

        elif st.session_state.memoria_fase == "repitiendo":
            progreso = len(st.session_state.memoria_usuario)
            st.markdown(f"**Tu secuencia hasta ahora ({progreso}/{LARGO_SECUENCIA}):** " + " → ".join(st.session_state.memoria_usuario))
            cols = st.columns(len(JUGADAS))
            for c, jugada in zip(cols, JUGADAS):
                if c.button(jugada, use_container_width=True, disabled=(progreso >= LARGO_SECUENCIA)):
                    st.session_state.memoria_usuario.append(jugada)
                    if len(st.session_state.memoria_usuario) == LARGO_SECUENCIA:
                        correctas = sum(1 for a, b in zip(st.session_state.memoria_usuario, st.session_state.memoria_objetivo) if a == b)
                        st.session_state.memoria_score = round(correctas / LARGO_SECUENCIA * 100)
                        st.session_state.memoria_fase = "resultado"
                    st.rerun()

        elif st.session_state.memoria_fase == "resultado":
            score = st.session_state.memoria_score
            st.markdown("**Secuencia correcta:** " + " → ".join(st.session_state.memoria_objetivo))
            st.markdown("**Tu secuencia:** " + " → ".join(st.session_state.memoria_usuario))
            if score >= 90:
                st.success(f"¡Pase perfecto! Puntaje: {score}")
            elif score >= 50:
                st.info(f"Jugada aceptable. Puntaje: {score}")
            else:
                st.error(f"Se te complicó la jugada. Puntaje: {score}")

            if st.button("➡️ Siguiente reto", use_container_width=True):
                reset_reto_trivia()
                st.session_state.etapa = "reto_trivia"
                st.rerun()

# =========================================================
# ETAPA: RETO TÁCTICO
# =========================================================
elif st.session_state.etapa == "reto_trivia":
    st.markdown("### 📋 Reto Táctico")
    st.caption("Lee la jugada y elige la mejor decisión. Mejora tu **Táctica**.")

    idx = st.session_state.trivia_idx
    preguntas = st.session_state.trivia_preguntas

    with st.container(border=True):
        st.markdown('<span class="tag-verde">Reto 3 de 3</span>', unsafe_allow_html=True)
        st.caption(f"Situación {idx + 1} de {len(preguntas)}")
        p = preguntas[idx]
        st.markdown(f"#### {p['pregunta']}")

        seleccion = st.radio("Elige tu decisión:", p["opciones"], index=None,
                              key=f"trivia_radio_{idx}", disabled=st.session_state.trivia_respondido)

        if not st.session_state.trivia_respondido:
            if st.button("✅ Confirmar decisión", disabled=(seleccion is None)):
                st.session_state.trivia_respondido = True
                if seleccion == p["correcta"]:
                    st.session_state.trivia_correctas += 1
                    st.success("¡Buena lectura del juego!")
                else:
                    st.error(f"No era lo ideal. La mejor decisión era: **{p['correcta']}**")
                st.rerun()
        else:
            es_ultima = idx == len(preguntas) - 1
            if st.button("➡️ Siguiente" if not es_ultima else "🏁 Ver resultado del reto"):
                if es_ultima:
                    st.session_state.trivia_score = round(st.session_state.trivia_correctas / len(preguntas) * 100)
                    st.session_state.etapa = "resumen_entrenamiento"
                else:
                    st.session_state.trivia_idx += 1
                    st.session_state.trivia_respondido = False
                st.rerun()

# =========================================================
# ETAPA: RESUMEN DE ENTRENAMIENTO + OFERTAS
# =========================================================
elif st.session_state.etapa == "resumen_entrenamiento":
    s = st.session_state.stats
    p_score = st.session_state.precision_score
    m_score = st.session_state.memoria_score
    t_score = st.session_state.trivia_score
    nota_prueba = round((p_score + m_score + t_score) / 3)

    ganancia_fin = round(p_score / 100 * 6)
    ganancia_pase = round(m_score / 100 * 6)
    ganancia_tac = round(t_score / 100 * 6)

    if "aplicado_ganancias" not in st.session_state or st.session_state.aplicado_ganancias != st.session_state.temporada:
        s["finalizacion"] = min(99, s["finalizacion"] + ganancia_fin)
        s["pase"] = min(99, s["pase"] + ganancia_pase)
        s["tactica"] = min(99, s["tactica"] + ganancia_tac)
        if st.session_state.edad >= 30:
            for k in s:
                s[k] = max(30, s[k] - random.randint(0, 2))
        ovr_actual = calcular_ovr(s)
        if ovr_actual > st.session_state.ovr_pico:
            st.session_state.ovr_pico = ovr_actual
        st.session_state.aplicado_ganancias = st.session_state.temporada
        st.session_state.ofertas_actuales = generar_ofertas(nota_prueba, ovr_actual)

    st.markdown("### 📊 Resultado de los retos")
    col1, col2, col3 = st.columns(3)
    col1.markdown(f'<div class="stat-box"><div class="valor">{p_score}</div><div class="etiqueta">Precisión</div></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="stat-box"><div class="valor">{m_score}</div><div class="etiqueta">Memoria</div></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="stat-box"><div class="valor">{t_score}</div><div class="etiqueta">Táctica</div></div>', unsafe_allow_html=True)

    st.markdown(f"**Nota general de la prueba:** {nota_prueba}/100")
    st.markdown(f"Finalización +{ganancia_fin} · Pase +{ganancia_pase} · Táctica +{ganancia_tac}")

    st.markdown("### 📨 Ofertas de clubes")
    if not st.session_state.ofertas_actuales:
        st.warning("Ningún club se fijó en ti esta temporada. Te quedas en la cantera entrenando otro año más.")
        if st.button("➡️ Continuar", use_container_width=True):
            st.session_state.etapa = "cerrar_temporada_sin_club"
            st.rerun()
    else:
        st.markdown("Elige el club con el que quieres firmar:")
        for i, oferta in enumerate(st.session_state.ofertas_actuales):
            with st.container(border=True):
                etiqueta_tier = {"grande": "Club grande", "mediano": "Club mediano", "pequeño": "Club pequeño"}[oferta["tier"]]
                st.markdown(f'<span class="tag-dorado">{etiqueta_tier}</span>', unsafe_allow_html=True)
                st.markdown(f"#### {oferta['club']}")
                if st.button(f"✍️ Firmar con {oferta['club']}", key=f"firmar_{i}", use_container_width=True):
                    st.session_state.club_actual = oferta
                    st.session_state.etapa = "simular_temporada"
                    st.rerun()

# =========================================================
# ETAPA: SIN CLUB ESTA TEMPORADA
# =========================================================
elif st.session_state.etapa == "cerrar_temporada_sin_club":
    st.session_state.historial_temporadas.append({
        "temporada": st.session_state.temporada, "edad": st.session_state.edad,
        "club": "Cantera (sin club)", "goles": 0, "asistencias": 0, "partidos": 0,
    })
    st.session_state.temporada += 1
    st.session_state.edad += 1
    st.session_state.etapa = "inicio_temporada"
    st.rerun()

# =========================================================
# ETAPA: SIMULAR TEMPORADA CON CLUB
# =========================================================
elif st.session_state.etapa == "simular_temporada":
    if "temporada_simulada" not in st.session_state or st.session_state.temporada_simulada != st.session_state.temporada:
        resultado = simular_temporada(st.session_state.stats, st.session_state.club_actual, st.session_state.edad)
        st.session_state.resultado_temporada = resultado
        st.session_state.totales["goles"] += resultado["goles"]
        st.session_state.totales["asistencias"] += resultado["asistencias"]
        st.session_state.totales["partidos"] += resultado["partidos"]
        if resultado["gana_titulo"]:
            st.session_state.totales["trofeos"] += 1
        if resultado["convocado_seleccion"]:
            st.session_state.totales["convocatorias"] += 1
        st.session_state.historial_temporadas.append({
            "temporada": st.session_state.temporada, "edad": st.session_state.edad,
            "club": st.session_state.club_actual["club"], "goles": resultado["goles"],
            "asistencias": resultado["asistencias"], "partidos": resultado["partidos"],
        })
        st.session_state.temporada_simulada = st.session_state.temporada

    r = st.session_state.resultado_temporada
    st.markdown(f"### 📅 Resumen — Temporada {st.session_state.temporada} en {st.session_state.club_actual['club']}")
    col1, col2, col3 = st.columns(3)
    col1.markdown(f'<div class="stat-box"><div class="valor">{r["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="stat-box"><div class="valor">{r["goles"]}</div><div class="etiqueta">Goles</div></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="stat-box"><div class="valor">{r["asistencias"]}</div><div class="etiqueta">Asistencias</div></div>', unsafe_allow_html=True)

    if r["convocado_seleccion"]:
        st.success(f"🇻🇪 ¡Fuiste convocado a la selección de {st.session_state.jugador['nacionalidad']} esta temporada!")
    if r["gana_titulo"]:
        st.success(f"🏆 ¡Ganaste un título con el {st.session_state.club_actual['club']}!")

    if st.button("➡️ Siguiente temporada", use_container_width=True):
        st.session_state.temporada += 1
        st.session_state.edad += 1
        st.session_state.etapa = "inicio_temporada"
        st.rerun()

    if st.session_state.edad >= EDAD_MIN_RETIRO_VOLUNTARIO:
        if st.button("🏁 Retirarme ahora", use_container_width=True):
            st.session_state.etapa = "retirado"
            st.rerun()

    if st.session_state.edad >= EDAD_RETIRO_FORZOSO:
        st.warning("Tu jugador ya alcanzó la edad de retiro. La próxima temporada será obligatorio retirarte.")

# =========================================================
# ETAPA: RETIRADO — RESUMEN DE CARRERA
# =========================================================
elif st.session_state.etapa == "retirado":
    j = st.session_state.jugador
    t = st.session_state.totales

    if "carrera_guardada" not in st.session_state:
        guardar_carrera(j["nombre"], j["posicion"], st.session_state.ovr_pico, t["goles"], t["asistencias"], t["trofeos"])
        st.session_state.carrera_guardada = True

    st.markdown(f"""
    <div class="resultado-box">
        <h2>🏁 {j['nombre']} se retira</h2>
        <p>{j['posicion']} · {j['nacionalidad']} · {st.session_state.temporada - 1} temporadas jugadas</p>
        <h1>OVR pico: {st.session_state.ovr_pico}</h1>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f'<div class="stat-box"><div class="valor">{t["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="stat-box"><div class="valor">{t["goles"]}</div><div class="etiqueta">Goles</div></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="stat-box"><div class="valor">{t["asistencias"]}</div><div class="etiqueta">Asistencias</div></div>', unsafe_allow_html=True)
    col4.markdown(f'<div class="stat-box"><div class="valor">{t["trofeos"]}</div><div class="etiqueta">Títulos</div></div>', unsafe_allow_html=True)

    if t["convocatorias"] > 0:
        st.info(f"Fuiste convocado a la selección nacional {t['convocatorias']} temporada(s).")

    st.markdown("### 🏆 Salón de la Fama")
    df = cargar_carreras()
    df_ordenado = df.sort_values(by=["ovr_pico", "goles"], ascending=[False, False]).reset_index(drop=True)
    for i, fila in df_ordenado.head(10).iterrows():
        clase = "rank-1" if i == 0 else "rank-2" if i == 1 else "rank-3" if i == 2 else "rank-other"
        st.markdown(f"""
        <div class="leaderboard-row {clase}">
            #{i+1} — {fila['nombre']} ({fila['posicion']}) — OVR pico {fila['ovr_pico']} · {fila['goles']} goles · {fila['trofeos']} títulos
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Crear un nuevo jugador", use_container_width=True):
        for clave in list(st.session_state.keys()):
            del st.session_state[clave]
        st.rerun()

st.markdown('<p class="firma">Los nombres de clubes se usan solo con fines de ambientación, sin afiliación oficial.</p>', unsafe_allow_html=True)
