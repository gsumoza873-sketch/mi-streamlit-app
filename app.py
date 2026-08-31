import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Trivia Vinotinto 🇻🇪",
    page_icon="🇻🇪",
    layout="centered",
)

LEADERBOARD_FILE = "leaderboard.csv"
IMAGES_DIR = "images"  # coloca aquí tus fotos: angel_falls.jpg, avila.jpg, caracas.jpg, etc.

# =========================================================
# ESTILOS - COLORES DE VENEZUELA
# =========================================================
st.markdown("""
<style>
:root {
    --amarillo: #FFCC00;
    --azul: #00247D;
    --rojo: #CF142B;
    --vinotinto: #7B1E3A;
    --blanco: #FFFFFF;
}

.stApp {
    background: linear-gradient(160deg, #FFF6D9 0%, #FDEFE9 35%, #EAF0FB 70%, #FFF6D9 100%);
}

/* Franja tricolor decorativa fija en la parte superior */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 8px;
    background: linear-gradient(90deg, var(--amarillo) 0%, var(--amarillo) 33%, var(--azul) 33%, var(--azul) 66%, var(--rojo) 66%, var(--rojo) 100%);
    z-index: 999;
}

/* Barra de progreso con los colores del tema */
[data-testid="stProgress"] div[role="progressbar"] {
    background-color: var(--vinotinto) !important;
}
[data-testid="stProgress"] > div > div {
    background-color: #f0d9d9 !important;
}

/* Forzar texto oscuro en todo el contenido para que no se vuelva invisible
   si el navegador/celular del usuario está en modo oscuro */
.stApp p, .stApp li, .stApp span, .stApp label,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4,
.stRadio label p, .stRadio label span,
.stCaption, [data-testid="stCaptionContainer"] {
    color: #262626 !important;
}

.stButton>button, .stButton>button * {
    color: white !important;
}

.stApp p.firma-top {
    text-align: center;
    color: var(--vinotinto) !important;
    font-size: 0.85em;
    font-weight: bold;
    margin-top: -10px;
    margin-bottom: 18px;
    opacity: 0.85;
}

.stApp p.firma-bottom {
    text-align: center;
    color: var(--vinotinto) !important;
    font-size: 0.85em;
    font-weight: bold;
    margin-top: 30px;
    padding-top: 14px;
    border-top: 1px solid #e5cfd6;
}

.header-banner {
    background: linear-gradient(90deg, var(--amarillo) 0%, var(--azul) 50%, var(--rojo) 100%);
    padding: 28px 20px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
}

.header-banner h1 {
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin: 0;
    font-size: 2.1em;
}

.header-banner p {
    color: white !important;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    margin-top: 6px;
    font-size: 1.05em;
}

.result-box h1, .result-box h2, .result-box p {
    color: white !important;
}

/* Tarjeta de pregunta: usamos el contenedor nativo con borde de Streamlit
   (st.container(border=True)) y lo re-estilizamos aquí, porque un <div>
   abierto/cerrado en st.markdown NO puede envolver widgets reales como st.radio */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white !important;
    border: 2px solid var(--vinotinto) !important;
    border-radius: 14px !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    padding: 6px 6px 2px 6px;
    margin-bottom: 16px;
}

.stApp span.category-tag {
    display: inline-block;
    background: var(--vinotinto);
    color: #ffffff !important;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78em;
    font-weight: bold;
    margin-bottom: 10px;
}

.stApp span.difficulty-tag {
    display: inline-block;
    background: var(--azul);
    color: #ffffff !important;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78em;
    font-weight: bold;
    margin-bottom: 10px;
}

.leaderboard-row {
    padding: 10px 14px;
    border-radius: 10px;
    margin-bottom: 6px;
    font-size: 1.02em;
}

.rank-1 { background: linear-gradient(90deg, #FFD700, #FFCC00); font-weight: bold; }
.rank-2 { background: #E8E8E8; font-weight: bold; }
.rank-3 { background: #D7B899; font-weight: bold; }
.rank-other { background: #FBEFEF; }

.stButton>button {
    background-color: var(--vinotinto);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 8px 20px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: var(--rojo);
    color: white;
}

.result-box {
    text-align: center;
    padding: 24px;
    border-radius: 16px;
    background: linear-gradient(135deg, var(--amarillo), var(--rojo));
    color: white;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# BANCO DE PREGUNTAS (35 preguntas: 15 cultura general VE por dificultad,
# 5 béisbol, 5 fútbol, 5 Miss Venezuela, 5 cultura general mundial)
# =========================================================
PREGUNTAS = [
    # ---------- CULTURA GENERAL VENEZUELA - FÁCIL (5) ----------
    {"categoria": "Cultura General VE", "dificultad": "Fácil", "pregunta": "¿Cuál es la capital de Venezuela?",
     "opciones": ["Maracaibo", "Caracas", "Valencia", "Barquisimeto"], "correcta": "Caracas"},
    {"categoria": "Cultura General VE", "dificultad": "Fácil", "pregunta": "¿Cuál es el idioma oficial de Venezuela?",
     "opciones": ["Portugués", "Español", "Francés", "Inglés"], "correcta": "Español"},
    {"categoria": "Cultura General VE", "dificultad": "Fácil", "pregunta": "¿Cuál es la moneda oficial de Venezuela?",
     "opciones": ["Peso", "Sol", "Bolívar", "Colón"], "correcta": "Bolívar"},
    {"categoria": "Cultura General VE", "dificultad": "Fácil", "pregunta": "¿Qué mar bordea la costa norte de Venezuela?",
     "opciones": ["Mar Caribe", "Océano Pacífico", "Mar Mediterráneo", "Mar de los Sargazos"], "correcta": "Mar Caribe"},
    {"categoria": "Cultura General VE", "dificultad": "Fácil", "pregunta": "¿Cuál es el plato típico navideño venezolano hecho con masa de maíz envuelta en hojas de plátano?",
     "opciones": ["Tamal", "Hallaca", "Cachapa", "Arepa"], "correcta": "Hallaca"},

    # ---------- CULTURA GENERAL VENEZUELA - INTERMEDIO (5) ----------
    {"categoria": "Cultura General VE", "dificultad": "Intermedio", "pregunta": "¿Cómo se llama la caída de agua más alta del mundo, ubicada en Venezuela?",
     "opciones": ["Salto Ángel", "Cataratas del Niágara", "Salto del Chorro", "Cascada Kaieteur"], "correcta": "Salto Ángel"},
    {"categoria": "Cultura General VE", "dificultad": "Intermedio", "pregunta": "¿Cómo se llama el parque nacional venezolano famoso por sus tepuyes, como el Roraima?",
     "opciones": ["Canaima", "Morrocoy", "Henri Pittier", "Los Roques"], "correcta": "Canaima"},
    {"categoria": "Cultura General VE", "dificultad": "Intermedio", "pregunta": "¿Cuál es el nombre del libertador venezolano considerado héroe de la independencia sudamericana?",
     "opciones": ["José de San Martín", "Simón Bolívar", "Francisco de Miranda", "Antonio José de Sucre"], "correcta": "Simón Bolívar"},
    {"categoria": "Cultura General VE", "dificultad": "Intermedio", "pregunta": "¿Cuál es el ave nacional de Venezuela?",
     "opciones": ["El turpial", "El colibrí", "El guacamayo", "El paují"], "correcta": "El turpial"},
    {"categoria": "Cultura General VE", "dificultad": "Intermedio", "pregunta": "¿Cuál es el árbol nacional de Venezuela?",
     "opciones": ["El araguaney", "El samán", "El apamate", "El bucare"], "correcta": "El araguaney"},

    # ---------- CULTURA GENERAL VENEZUELA - DIFÍCIL (5) ----------
    {"categoria": "Cultura General VE", "dificultad": "Difícil", "pregunta": "¿En qué año se firmó el Acta de Independencia de Venezuela?",
     "opciones": ["1808", "1811", "1821", "1830"], "correcta": "1811"},
    {"categoria": "Cultura General VE", "dificultad": "Difícil", "pregunta": "¿Quién fue el primer presidente de Venezuela?",
     "opciones": ["Cristóbal Mendoza", "José Antonio Páez", "Antonio Guzmán Blanco", "Juan Vicente Gómez"], "correcta": "Cristóbal Mendoza"},
    {"categoria": "Cultura General VE", "dificultad": "Difícil", "pregunta": "¿Cuál es el estado venezolano con mayor extensión territorial?",
     "opciones": ["Zulia", "Amazonas", "Bolívar", "Apure"], "correcta": "Bolívar"},
    {"categoria": "Cultura General VE", "dificultad": "Difícil", "pregunta": "¿Qué escritor venezolano es autor de la novela \"Doña Bárbara\"?",
     "opciones": ["Rómulo Gallegos", "Arturo Uslar Pietri", "Teresa de la Parra", "Andrés Bello"], "correcta": "Rómulo Gallegos"},
    {"categoria": "Cultura General VE", "dificultad": "Difícil", "pregunta": "¿En qué año fue fundada la ciudad de Caracas?",
     "opciones": ["1498", "1521", "1567", "1602"], "correcta": "1567"},

    # ---------- BÉISBOL (5) ----------
    {"categoria": "Béisbol", "pregunta": "¿Cómo se le conoce popularmente al béisbol en Venezuela?",
     "opciones": ["El rey del deporte", "El deporte blanco", "La pelota chica", "El juego real"], "correcta": "El rey del deporte"},
    {"categoria": "Béisbol", "pregunta": "¿Cuántos equipos conforman actualmente la Liga Venezolana de Béisbol Profesional (LVBP)?",
     "opciones": ["6", "8", "10", "12"], "correcta": "8"},
    {"categoria": "Béisbol", "pregunta": "¿Qué venezolano ganó múltiples Guantes de Oro y Triple Corona jugando para los Tigres de Detroit?",
     "opciones": ["Miguel Cabrera", "Omar Vizquel", "Bob Abreu", "Víctor Martínez"], "correcta": "Miguel Cabrera"},
    {"categoria": "Béisbol", "pregunta": "¿Cómo se llama el torneo final donde compiten los campeones de las ligas de invierno del Caribe?",
     "opciones": ["Serie Mundial", "Serie del Caribe", "Copa Caribeña", "Clásico del Caribe"], "correcta": "Serie del Caribe"},
    {"categoria": "Béisbol", "pregunta": "¿En qué posición jugaba históricamente Luis Aparicio, venezolano miembro del Salón de la Fama?",
     "opciones": ["Receptor", "Jardinero central", "Campocorto (shortstop)", "Primera base"], "correcta": "Campocorto (shortstop)"},

    # ---------- FÚTBOL (5) ----------
    {"categoria": "Fútbol", "pregunta": "¿Cómo se le apoda a la selección de fútbol de Venezuela?",
     "opciones": ["La Tricolor", "La Vinotinto", "Los Llaneros", "La Roja"], "correcta": "La Vinotinto"},
    {"categoria": "Fútbol", "pregunta": "¿En qué año Venezuela fue anfitriona de la Copa América?",
     "opciones": ["2001", "2004", "2007", "2011"], "correcta": "2007"},
    {"categoria": "Fútbol", "pregunta": "¿Cómo se llama el estadio sede histórica de la selección Vinotinto en Caracas?",
     "opciones": ["Estadio Olímpico de la UCV", "Estadio Metropolitano de Mérida", "Estadio Pueblo Nuevo", "Estadio Brígido Iriarte"], "correcta": "Estadio Olímpico de la UCV"},
    {"categoria": "Fútbol", "pregunta": "¿Cuál de estos futbolistas venezolanos fue capitán y referente histórico de la Vinotinto?",
     "opciones": ["Salomón Rondón", "James Rodríguez", "Falcao García", "Luis Suárez"], "correcta": "Salomón Rondón"},
    {"categoria": "Fútbol", "pregunta": "¿A qué confederación de fútbol pertenece Venezuela?",
     "opciones": ["UEFA", "CONCACAF", "CONMEBOL", "CAF"], "correcta": "CONMEBOL"},

    # ---------- MISS VENEZUELA / MISS UNIVERSO (5) ----------
    {"categoria": "Miss Venezuela", "pregunta": "¿Cuántas veces ha ganado Venezuela el título de Miss Universo?",
     "opciones": ["Cinco", "Seis", "Siete", "Nueve"], "correcta": "Siete"},
    {"categoria": "Miss Venezuela", "pregunta": "¿Quién fue la primera venezolana en ganar el Miss Universo, en 1979?",
     "opciones": ["Maritza Sayalero", "Irene Sáez", "Bárbara Palacios", "Alicia Machado"], "correcta": "Maritza Sayalero"},
    {"categoria": "Miss Venezuela", "pregunta": "¿Qué venezolana ganó el Miss Universo en 1996?",
     "opciones": ["Dayana Mendoza", "Alicia Machado", "Stefanía Fernández", "María Gabriela Isler"], "correcta": "Alicia Machado"},
    {"categoria": "Miss Venezuela", "pregunta": "¿En qué año ganó Venezuela su corona más reciente de Miss Universo, con María Gabriela Isler?",
     "opciones": ["2009", "2011", "2013", "2015"], "correcta": "2013"},
    {"categoria": "Miss Venezuela", "pregunta": "¿Cómo se llama el certamen nacional que elige a la representante de Venezuela para el Miss Universo?",
     "opciones": ["Miss Venezuela", "Miss Mundo VE", "Reina Vinotinto", "Belleza Nacional"], "correcta": "Miss Venezuela"},

    # ---------- CULTURA GENERAL MUNDIAL (5) ----------
    {"categoria": "Cultura General Mundial", "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
     "opciones": ["Saturno", "Júpiter", "Neptuno", "Urano"], "correcta": "Júpiter"},
    {"categoria": "Cultura General Mundial", "pregunta": "¿En qué continente se encuentra Egipto?",
     "opciones": ["Asia", "África", "Europa", "Oceanía"], "correcta": "África"},
    {"categoria": "Cultura General Mundial", "pregunta": "¿Aproximadamente cuántos huesos tiene el cuerpo humano adulto?",
     "opciones": ["156", "206", "256", "306"], "correcta": "206"},
    {"categoria": "Cultura General Mundial", "pregunta": "¿Quién pintó la Mona Lisa?",
     "opciones": ["Pablo Picasso", "Leonardo da Vinci", "Miguel Ángel", "Rafael"], "correcta": "Leonardo da Vinci"},
    {"categoria": "Cultura General Mundial", "pregunta": "¿Cuál es el océano más grande del mundo?",
     "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"], "correcta": "Pacífico"},
]

TOTAL_PREGUNTAS = len(PREGUNTAS)

# =========================================================
# FUNCIONES DE LEADERBOARD (persistencia en CSV local)
# =========================================================
def cargar_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        return pd.read_csv(LEADERBOARD_FILE)
    return pd.DataFrame(columns=["nombre", "puntaje", "total", "fecha"])

def guardar_resultado(nombre, puntaje, total):
    df = cargar_leaderboard()
    nueva_fila = pd.DataFrame([{
        "nombre": nombre,
        "puntaje": puntaje,
        "total": total,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }])
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv(LEADERBOARD_FILE, index=False)
    return df

def obtener_puesto(df, nombre, puntaje, fecha):
    df_ordenado = df.sort_values(by=["puntaje", "fecha"], ascending=[False, True]).reset_index(drop=True)
    match = df_ordenado[(df_ordenado["nombre"] == nombre) & (df_ordenado["puntaje"] == puntaje) & (df_ordenado["fecha"] == fecha)]
    if not match.empty:
        return match.index[0] + 1
    return None

# =========================================================
# IMAGEN DE ENCABEZADO (opcional, con fallback si no existe)
# =========================================================
def mostrar_imagen_si_existe(nombre_archivo, caption=""):
    ruta = os.path.join(IMAGES_DIR, nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=caption)
        return True
    return False

# =========================================================
# INICIALIZAR SESSION STATE
# =========================================================
if "etapa" not in st.session_state:
    st.session_state.etapa = "registro"  # registro -> jugando -> finalizado
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respuesta_seleccionada" not in st.session_state:
    st.session_state.respuesta_seleccionada = None
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "orden_preguntas" not in st.session_state:
    orden = list(range(TOTAL_PREGUNTAS))
    random.shuffle(orden)
    st.session_state.orden_preguntas = orden

# =========================================================
# ENCABEZADO
# =========================================================
st.markdown("""
<div class="header-banner">
    <h1>🇻🇪 Trivia Vinotinto</h1>
    <p>Cultura general, béisbol y fútbol de Venezuela</p>
</div>
""", unsafe_allow_html=True)

if not mostrar_imagen_si_existe("venezuela_banner.jpg"):
    pass  # si agregas la imagen 'images/venezuela_banner.jpg' se mostrará aquí automáticamente

st.markdown('<p class="firma-top">Trivia creada por Gabriel.S</p>', unsafe_allow_html=True)

# =========================================================
# ETAPA 1: REGISTRO
# =========================================================
if st.session_state.etapa == "registro":
    st.markdown("### 📝 Regístrate para jugar")
    nombre_input = st.text_input("Escribe tu nombre:", placeholder="Ej: Fulanito de Tal")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Registrarme y empezar", use_container_width=True):
            if nombre_input.strip() == "":
                st.warning("Por favor escribe tu nombre antes de continuar.")
            else:
                st.session_state.nombre = nombre_input.strip()
                st.session_state.etapa = "jugando"
                st.session_state.pregunta_actual = 0
                st.session_state.puntaje = 0
                st.session_state.respondido = False
                st.rerun()

    with col2:
        if st.button("🏆 Ver tabla de posiciones", use_container_width=True):
            st.session_state.etapa = "leaderboard_previo"
            st.rerun()

# =========================================================
# ETAPA AUXILIAR: VER LEADERBOARD SIN JUGAR
# =========================================================
elif st.session_state.etapa == "leaderboard_previo":
    st.markdown("### 🏆 Tabla de posiciones")
    df = cargar_leaderboard()
    if df.empty:
        st.info("Todavía no hay jugadores registrados. ¡Sé el primero!")
    else:
        df_ordenado = df.sort_values(by=["puntaje", "fecha"], ascending=[False, True]).reset_index(drop=True)
        for i, fila in df_ordenado.iterrows():
            clase = "rank-1" if i == 0 else "rank-2" if i == 1 else "rank-3" if i == 2 else "rank-other"
            st.markdown(f"""
            <div class="leaderboard-row {clase}">
                #{i+1} — {fila['nombre']} — {fila['puntaje']}/{fila['total']} pts
            </div>
            """, unsafe_allow_html=True)

    if st.button("⬅️ Volver"):
        st.session_state.etapa = "registro"
        st.rerun()

# =========================================================
# ETAPA 2: JUGANDO
# =========================================================
elif st.session_state.etapa == "jugando":
    idx = st.session_state.orden_preguntas[st.session_state.pregunta_actual]
    pregunta_data = PREGUNTAS[idx]

    st.markdown(f"**Jugador:** {st.session_state.nombre} &nbsp;|&nbsp; **Puntaje actual:** {st.session_state.puntaje}")
    st.progress((st.session_state.pregunta_actual) / TOTAL_PREGUNTAS)
    st.caption(f"Pregunta {st.session_state.pregunta_actual + 1} de {TOTAL_PREGUNTAS}")

    with st.container(border=True):
        etiquetas = f'<span class="category-tag">{pregunta_data["categoria"]}</span>'
        if "dificultad" in pregunta_data:
            etiquetas += f' <span class="difficulty-tag">{pregunta_data["dificultad"]}</span>'
        st.markdown(etiquetas, unsafe_allow_html=True)
        st.markdown(f"#### {pregunta_data['pregunta']}")

        opciones = pregunta_data["opciones"]
        seleccion = st.radio(
            "Selecciona tu respuesta:",
            opciones,
            index=None,
            key=f"radio_{st.session_state.pregunta_actual}",
            disabled=st.session_state.respondido,
        )

    if not st.session_state.respondido:
        if st.button("✅ Confirmar respuesta", disabled=(seleccion is None)):
            st.session_state.respuesta_seleccionada = seleccion
            st.session_state.respondido = True
            if seleccion == pregunta_data["correcta"]:
                st.session_state.puntaje += 1
                st.success("¡Correcto! 🎉")
            else:
                st.error(f"Incorrecto. La respuesta correcta era: **{pregunta_data['correcta']}**")
            st.rerun()
    else:
        if st.session_state.respuesta_seleccionada == pregunta_data["correcta"]:
            st.success("¡Correcto! 🎉")
        else:
            st.error(f"Incorrecto. La respuesta correcta era: **{pregunta_data['correcta']}**")

        es_ultima = st.session_state.pregunta_actual == TOTAL_PREGUNTAS - 1
        texto_boton = "🏁 Ver resultado final" if es_ultima else "➡️ Siguiente pregunta"
        if st.button(texto_boton):
            if es_ultima:
                st.session_state.etapa = "finalizado"
            else:
                st.session_state.pregunta_actual += 1
                st.session_state.respondido = False
                st.session_state.respuesta_seleccionada = None
            st.rerun()

# =========================================================
# ETAPA 3: FINALIZADO
# =========================================================
elif st.session_state.etapa == "finalizado":
    # Guardar el resultado una sola vez
    if "resultado_guardado" not in st.session_state:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.fecha_resultado = fecha_actual
        df = guardar_resultado(st.session_state.nombre, st.session_state.puntaje, TOTAL_PREGUNTAS)
        st.session_state.resultado_guardado = True

    df = cargar_leaderboard()
    puesto = obtener_puesto(df, st.session_state.nombre, st.session_state.puntaje, st.session_state.fecha_resultado)

    st.markdown(f"""
    <div class="result-box">
        <h2>¡Juego terminado, {st.session_state.nombre}!</h2>
        <h1>{st.session_state.puntaje} / {TOTAL_PREGUNTAS}</h1>
        <p>Quedaste en el puesto #{puesto if puesto else '-'} de la tabla general</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🏆 Tabla de posiciones")
    df_ordenado = df.sort_values(by=["puntaje", "fecha"], ascending=[False, True]).reset_index(drop=True)
    for i, fila in df_ordenado.iterrows():
        es_yo = (fila["nombre"] == st.session_state.nombre and fila["fecha"] == st.session_state.fecha_resultado)
        clase = "rank-1" if i == 0 else "rank-2" if i == 1 else "rank-3" if i == 2 else "rank-other"
        marcador = " 👈 Tú" if es_yo else ""
        st.markdown(f"""
        <div class="leaderboard-row {clase}">
            #{i+1} — {fila['nombre']} — {fila['puntaje']}/{fila['total']} pts{marcador}
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Jugar de nuevo", use_container_width=True):
            for clave in ["etapa", "pregunta_actual", "puntaje", "respondido",
                          "respuesta_seleccionada", "orden_preguntas", "resultado_guardado"]:
                if clave in st.session_state:
                    del st.session_state[clave]
            st.rerun()
    with col2:
        if st.button("👤 Cambiar de jugador", use_container_width=True):
            for clave in list(st.session_state.keys()):
                del st.session_state[clave]
            st.rerun()

# =========================================================
# PIE DE PÁGINA (visible en todas las etapas)
# =========================================================
st.markdown('<p class="firma-bottom">Trivia creada por Gabriel.S</p>', unsafe_allow_html=True)
