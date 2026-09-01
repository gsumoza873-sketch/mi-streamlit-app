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
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap');

:root {
    --verde: #0E6B3A;
    --verde-oscuro: #0A4D2A;
    --verde-claro: #E8F5EC;
    --dorado: #C9962C;
    --dorado-claro: #FBF0DC;
    --blanco: #FFFFFF;
    --texto: #1A1A1A;
}

.stApp {
    background:
        radial-gradient(circle at 50% -5%, rgba(255,255,255,0.55) 0%, transparent 32%),
        repeating-linear-gradient(100deg, #CDEEDA 0px, #CDEEDA 70px, #B4E3C4 70px, #B4E3C4 140px);
    font-family: 'Segoe UI', Roboto, Arial, sans-serif;
}

.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 6px;
    background: linear-gradient(90deg, var(--verde-oscuro), var(--verde), var(--dorado));
    z-index: 999;
}

/* Regla base de texto oscuro con especificidad CERO (gracias a :where),
   así cualquier clase específica (badges, botones, banners) la gana sin pelear. */
:where(
    .stApp p, .stApp li, .stApp span, .stApp label,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4,
    .stRadio label p, .stRadio label span,
    .stCaption, [data-testid="stCaptionContainer"]
) {
    color: var(--texto) !important;
}

h1, h2, h3, h4 {
    font-family: 'Poppins', 'Segoe UI', sans-serif !important;
    letter-spacing: -0.02em;
}

.header-banner {
    background:
        repeating-linear-gradient(135deg, rgba(255,255,255,0.05) 0px, rgba(255,255,255,0.05) 14px, transparent 14px, transparent 28px),
        linear-gradient(100deg, var(--verde-oscuro), var(--verde));
    padding: 30px 22px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 6px;
    box-shadow: 0 6px 18px rgba(10,77,42,0.25);
}
.header-banner h1 { color: #ffffff !important; text-shadow: 2px 2px 6px rgba(0,0,0,0.35); margin: 0; font-size: 2.1em; }
.header-banner p { color: #EAF7EE !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.3); margin-top: 8px; font-size: 1.02em; }

p.firma {
    text-align: center;
    color: var(--verde-oscuro) !important;
    font-size: 0.82em;
    font-weight: 600;
    opacity: 0.8;
    margin-top: 4px;
    margin-bottom: 18px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--blanco) !important;
    border: 2px solid var(--verde) !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 14px rgba(14,107,58,0.10);
    padding: 10px;
    margin-bottom: 18px;
}

span.tag-verde {
    display: inline-block; background: var(--verde); color: #ffffff !important;
    padding: 5px 14px; border-radius: 20px; font-size: 0.78em; font-weight: 700;
    letter-spacing: 0.02em; margin-bottom: 10px;
}
span.tag-dorado {
    display: inline-block; background: var(--dorado); color: #ffffff !important;
    padding: 5px 14px; border-radius: 20px; font-size: 0.78em; font-weight: 700;
    letter-spacing: 0.02em; margin-bottom: 10px;
}

.stat-box {
    background: linear-gradient(160deg, #ffffff, var(--verde-claro));
    border: 2px solid var(--verde);
    border-radius: 14px;
    padding: 14px 6px 10px 6px;
    text-align: center;
    margin-bottom: 10px;
    box-shadow: 0 3px 10px rgba(14,107,58,0.12);
}
.stat-box .icono { font-size: 1.3em; display: block; margin-bottom: 2px; }
.stat-box .valor { font-family: 'Poppins', sans-serif; font-size: 1.9em; font-weight: 800; color: var(--verde-oscuro) !important; line-height: 1.1; }
.stat-box .etiqueta { font-size: 0.76em; color: var(--texto) !important; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; }

/* Tarjeta de jugador estilo "carta" con bandera, posición y OVR destacado */
.jugador-card {
    background: linear-gradient(120deg, var(--verde-oscuro) 0%, var(--verde) 60%, var(--dorado) 130%);
    border-radius: 20px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 8px 22px rgba(10,77,42,0.28);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
}
.jugador-card .info h3 { color: #ffffff !important; margin: 0 0 2px 0; font-size: 1.3em; }
.jugador-card .info p { color: #EAF7EE !important; margin: 0; font-size: 0.92em; font-weight: 600; }
.jugador-card .bandera { font-size: 2.6em; line-height: 1; }
.jugador-card .ovr-gema {
    background: #ffffff;
    color: var(--verde-oscuro) !important;
    border-radius: 50%;
    width: 68px; height: 68px;
    display: flex; align-items: center; justify-content: center;
    flex-direction: column;
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    border: 3px solid var(--dorado);
}
.jugador-card .ovr-gema .num { font-size: 1.5em; font-weight: 800; color: var(--verde-oscuro) !important; line-height: 1; }
.jugador-card .ovr-gema .lbl { font-size: 0.55em; font-weight: 700; color: var(--verde) !important; letter-spacing: 0.05em; }

span.tag-club {
    display: inline-block; color: #ffffff !important;
    padding: 5px 14px; border-radius: 20px; font-size: 0.78em; font-weight: 700;
    letter-spacing: 0.02em; margin-bottom: 10px;
}

.oferta-card {
    background: linear-gradient(160deg, #ffffff, var(--dorado-claro));
    border: 2px solid var(--dorado);
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 10px;
}

.resultado-box {
    text-align: center; padding: 26px; border-radius: 18px;
    background: linear-gradient(135deg, var(--verde-oscuro), var(--verde));
    color: white; margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(10,77,42,0.3);
}
.resultado-box h1, .resultado-box h2, .resultado-box p { color: #ffffff !important; }

.stButton>button {
    background-color: var(--verde-oscuro);
    color: white; border-radius: 12px; border: none;
    padding: 10px 22px; font-weight: 700; letter-spacing: 0.01em;
    transition: background-color 0.15s ease;
}
.stButton>button:hover { background-color: var(--verde); color: white; }
.stButton>button, .stButton>button * { color: white !important; }
.stButton>button:disabled, .stButton>button:disabled * { color: #ffffffaa !important; }

.leaderboard-row { padding: 11px 16px; border-radius: 12px; margin-bottom: 7px; font-weight: 500; }
.rank-1 { background: linear-gradient(90deg, #FFE9A8, var(--dorado)); font-weight: 700; }
.rank-2 { background: #E9ECEA; font-weight: 700; }
.rank-3 { background: #E3CBAA; font-weight: 700; }
.rank-other { background: var(--verde-claro); }

hr { border-color: var(--verde-claro) !important; }
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

# Color propio de cada club, para que la app se sienta distinta según dónde firmes
COLOR_CLUB = {
    "Real Madrid": "#8A6D00", "Manchester City": "#6CABDD", "Bayern Múnich": "#DC052D",
    "Flamengo": "#C8102E", "Boca Juniors": "#1E3A8A",
    "Sevilla FC": "#D2001C", "AS Mónaco": "#E4002B", "River Plate": "#E30613",
    "Deportivo Táchira": "#8B1E3F", "Millonarios FC": "#004C97",
    "Estudiantes de Mérida": "#6B2E8C", "Zamora FC": "#7A1FA2", "Deportivo Lara": "#003DA5",
    "CD Godoy Cruz": "#004B87", "Real Cartagena": "#B5121B",
}

BANDERAS = {
    "Venezuela": "🇻🇪", "Argentina": "🇦🇷", "Brasil": "🇧🇷", "Colombia": "🇨🇴",
    "España": "🇪🇸", "México": "🇲🇽", "Otro": "🌍",
}

ICONO_ATRIBUTO = {
    "Finalización": "🎯", "Regate": "🌀", "Táctica Ofensiva": "🧠",
    "Llegada": "🚀", "Pase": "🎯", "Visión de Juego": "🧠",
    "Anticipación": "🛡️", "Salida de Balón": "🎯", "Táctica Defensiva": "🧠",
    "Reflejos": "🧤", "Distribución": "🎯", "Colocación": "🧠",
}

# =========================================================
# CONFIGURACIÓN POR POSICIÓN
# (cada posición tiene sus propios 3 atributos, su propio banco de
#  preguntas tácticas y su propio vocabulario de jugadas para el reto
#  de memoria — así un portero nunca entrena ni es evaluado como delantero)
# =========================================================
POSICIONES = {
    "Delantero": {
        "atr1_nombre": "Finalización",
        "atr2_nombre": "Regate",
        "atr3_nombre": "Táctica Ofensiva",
        "desc_precision": "Carga el remate y dispara al arco cuando estés en la zona ideal.",
        "desc_memoria": "Memoriza la secuencia de gambetas y repítela para superar al rival.",
        "jugadas_memoria": ["🌀 Elástica", "⚡ Cambio de ritmo", "↩️ Recorte interior", "🎯 Amague"],
        "stats_base": {"atr1": 52, "atr2": 42, "atr3": 38},
        "preguntas": [
            {"pregunta": "El arquero rival achica el ángulo y sale a tu encuentro uno contra uno. ¿Qué decides?",
             "opciones": ["Rematar fuerte al cuerpo", "Amagar y definir con el exterior lejos del arquero", "Centrar sin necesidad", "Perder tiempo regateando de más"],
             "correcta": "Amagar y definir con el exterior lejos del arquero"},
            {"pregunta": "Estás en fuera de juego posicional constantemente. ¿Qué ajustas?",
             "opciones": ["Sincronizar tu carrera con el pase del compañero", "Adelantarte siempre lo más posible", "Quedarte quieto todo el partido", "Jugar de espaldas todo el tiempo"],
             "correcta": "Sincronizar tu carrera con el pase del compañero"},
            {"pregunta": "Tienes un centro raso al primer palo. ¿Cómo defines mejor?",
             "opciones": ["Remate de primera al primer palo", "Dejar pasar el balón", "Rematar de espaldas al arco", "Esperar que rebote"],
             "correcta": "Remate de primera al primer palo"},
            {"pregunta": "El defensor central rival es más lento que tú. ¿Cómo lo explotas?",
             "opciones": ["Con carreras al espacio en profundidad", "Jugando siempre de espaldas a él", "Evitando esa zona", "Bajando a mediocampo todo el partido"],
             "correcta": "Con carreras al espacio en profundidad"},
            {"pregunta": "Estás en el área chica con un pase bajo cruzado. ¿Qué haces?",
             "opciones": ["Remate de primera sin pensarlo", "Controlar y girar perdiendo el tiempo justo", "Dejar pasar el balón", "Centrar de nuevo"],
             "correcta": "Remate de primera sin pensarlo"},
            {"pregunta": "Vas uno contra uno contra el último defensor con espacio para correr. ¿Qué conviene?",
             "opciones": ["Encarar directo a máxima velocidad", "Parar a esperar apoyo", "Retroceder el balón", "Buscar una falta táctica innecesaria"],
             "correcta": "Encarar directo a máxima velocidad"},
            {"pregunta": "El equipo rival marca en zona en los córners. ¿Cómo te posicionas como delantero?",
             "opciones": ["Buscando espacios entre los marcadores con movimientos", "Quedándote fijo en un punto", "Saliendo del área antes del centro", "Yendo a la otra área"],
             "correcta": "Buscando espacios entre los marcadores con movimientos"},
            {"pregunta": "Fallaste un mano a mano importante. ¿Qué actitud táctica conviene para seguir siendo útil?",
             "opciones": ["Seguir generando desmarques y buscando la siguiente jugada", "Dejar de participar el resto del partido", "Discutir con el árbitro", "Bajar a defender toda la línea"],
             "correcta": "Seguir generando desmarques y buscando la siguiente jugada"},
        ],
    },
    "Centrocampista": {
        "atr1_nombre": "Llegada",
        "atr2_nombre": "Pase",
        "atr3_nombre": "Visión de Juego",
        "desc_precision": "Carga el remate de media distancia y dispara en el momento justo.",
        "desc_memoria": "Memoriza la secuencia de pases para conducir la jugada.",
        "jugadas_memoria": ["⬆️ Vertical", "↔️ Horizontal", "🔄 Diagonal", "⚡ Pared (uno-dos)"],
        "stats_base": {"atr1": 35, "atr2": 52, "atr3": 48},
        "preguntas": [
            {"pregunta": "Estás en contragolpe 3 contra 2. ¿Qué haces?",
             "opciones": ["Driblas a los dos defensores tú solo", "Abres el balón al compañero libre en la banda", "Retienes el balón esperando refuerzos", "Tiras un centro al área vacía"],
             "correcta": "Abres el balón al compañero libre en la banda"},
            {"pregunta": "El rival presiona muy alto desde el saque de meta. ¿Cómo ayudas a salir a tu equipo?",
             "opciones": ["Pelotazo largo sin pensar", "Pidiendo el balón corto con apoyos y triangulaciones", "Quedándote quieto sin moverte", "Saque directo a la banda contraria"],
             "correcta": "Pidiendo el balón corto con apoyos y triangulaciones"},
            {"pregunta": "Tu equipo domina la posesión pero no genera ocasiones claras. ¿Qué falta?",
             "opciones": ["Más pases hacia atrás", "Profundidad: pases entre líneas y desmarques de ruptura", "Jugar más lento todavía", "Sacar al portero"],
             "correcta": "Profundidad: pases entre líneas y desmarques de ruptura"},
            {"pregunta": "Vas ganando 1-0 en el minuto 85. ¿Qué prioridad táctica tiene el equipo?",
             "opciones": ["Buscar el segundo gol a toda costa", "Controlar el ritmo, rotar el balón y evitar pérdidas", "Sacar a todos los defensores por atacantes", "Jugar sin portero para tener un jugador extra"],
             "correcta": "Controlar el ritmo, rotar el balón y evitar pérdidas"},
            {"pregunta": "Tienes el balón en el centro del campo con dos rivales presionando cerca. ¿Qué haces primero?",
             "opciones": ["Buscar el pase de salida más simple y seguro", "Intentar un túnel arriesgado", "Perder tiempo regateando ahí mismo", "Devolver siempre al arquero"],
             "correcta": "Buscar el pase de salida más simple y seguro"},
            {"pregunta": "Ves a un compañero desmarcado entre líneas rivales. ¿Qué prioridad táctica tiene ese pase?",
             "opciones": ["Es la mejor opción, rompe líneas rivales", "Nunca conviene arriesgar ese pase", "Mejor pasar atrás siempre", "Ignorarlo y driblar"],
             "correcta": "Es la mejor opción, rompe líneas rivales"},
            {"pregunta": "Tu equipo necesita controlar el partido ganando por la mínima en los últimos 15 minutos. ¿Qué haces con el balón?",
             "opciones": ["Circularlo con paciencia sin arriesgar pérdidas", "Buscar siempre el pase vertical arriesgado", "Perder la posesión a propósito", "Jugar solo pases largos"],
             "correcta": "Circularlo con paciencia sin arriesgar pérdidas"},
            {"pregunta": "El rival te marca hombre a hombre muy de cerca. ¿Cómo te desmarcas?",
             "opciones": ["Con movimientos cortos y cambios de ritmo para generar espacio", "Quedándote quieto esperando el balón", "Corriendo siempre en línea recta", "Alejándote del juego por completo"],
             "correcta": "Con movimientos cortos y cambios de ritmo para generar espacio"},
        ],
    },
    "Defensa": {
        "atr1_nombre": "Anticipación",
        "atr2_nombre": "Salida de Balón",
        "atr3_nombre": "Táctica Defensiva",
        "desc_precision": "Carga el timing y entra a la disputa justo cuando el rival esté a tu alcance.",
        "desc_memoria": "Memoriza la secuencia de pases para salir jugando desde el fondo.",
        "jugadas_memoria": ["↔️ Corto al lateral", "⬆️ Vertical al mediocampista", "🔙 Retroceso al portero", "↗️ Diagonal larga"],
        "stats_base": {"atr1": 52, "atr2": 42, "atr3": 50},
        "preguntas": [
            {"pregunta": "El delantero rival te encara de frente con velocidad. ¿Qué haces?",
             "opciones": ["Retroceder controlando la distancia sin lanzarte", "Entrar directo a la disputa de inmediato", "Dejarlo pasar sin marcar", "Empujarlo desde atrás"],
             "correcta": "Retroceder controlando la distancia sin lanzarte"},
            {"pregunta": "Defiendes un córner rival. ¿Qué prioridad tienes?",
             "opciones": ["Cubrir el primer palo y marcar a los rematadores clave", "Ir todos a buscar el balón sin marca", "Salir del área antes del centro", "Ignorar a los rematadores altos"],
             "correcta": "Cubrir el primer palo y marcar a los rematadores clave"},
            {"pregunta": "Tu equipo juega con un jugador menos (10 contra 11). ¿Qué formación conviene?",
             "opciones": ["Formación compacta con líneas cortas", "Formación ofensiva con 3 delanteros", "Todos atacando sin orden", "Cambiar de arquero de campo"],
             "correcta": "Formación compacta con líneas cortas"},
            {"pregunta": "Tienes el balón bajo presión cerca de tu propia área. ¿Qué decisión es más segura?",
             "opciones": ["Pase simple y seguro a un compañero libre", "Intentar un túnel arriesgado ahí mismo", "Despejar sin mirar hacia ningún lado", "Regatear a dos rivales dentro de tu área"],
             "correcta": "Pase simple y seguro a un compañero libre"},
            {"pregunta": "El extremo rival es mucho más rápido que tú. ¿Cómo lo neutralizas mejor?",
             "opciones": ["Manteniendo distancia corta sin dejarlo girar con espacio", "Pegándote a él sin importar dónde está el balón", "Ignorándolo por completo", "Dejándolo siempre con espacio libre"],
             "correcta": "Manteniendo distancia corta sin dejarlo girar con espacio"},
            {"pregunta": "Tu equipo gana por la mínima a falta de 5 minutos. ¿Qué prioridad defensiva tienes?",
             "opciones": ["Achicar espacios y evitar faltas innecesarias cerca del área", "Buscar la expulsión propia con una entrada dura", "Salir a atacar dejando espacios atrás", "Discutir con el árbitro constantemente"],
             "correcta": "Achicar espacios y evitar faltas innecesarias cerca del área"},
            {"pregunta": "El rival tiene un delantero fuerte que juega de espaldas al arco. ¿Cómo lo defiendes?",
             "opciones": ["Anticipándote antes de que reciba y controle", "Empujándolo por la espalda todo el partido", "Dejándolo girar libremente", "Marcándolo solo dentro del área"],
             "correcta": "Anticipándote antes de que reciba y controle"},
            {"pregunta": "Tienes que iniciar la jugada desde el fondo bajo presión rival. ¿Qué priorizas?",
             "opciones": ["Buscar líneas de pase seguras con apoyos cercanos", "Un pelotazo largo sin pensar", "Perder tiempo driblando en tu propia área", "Pasarle siempre al arquero y nada más"],
             "correcta": "Buscar líneas de pase seguras con apoyos cercanos"},
        ],
    },
    "Portero": {
        "atr1_nombre": "Reflejos",
        "atr2_nombre": "Distribución",
        "atr3_nombre": "Colocación",
        "desc_precision": "Carga tu reacción y estira las manos en el momento justo para atajar.",
        "desc_memoria": "Memoriza la secuencia de saques para iniciar el ataque de tu equipo.",
        "jugadas_memoria": ["🤾 Saque corto", "🚀 Saque largo", "↔️ Lateral al defensa", "⚡ Contragolpe rápido"],
        "stats_base": {"atr1": 50, "atr2": 35, "atr3": 45},
        "preguntas": [
            {"pregunta": "El rival remata desde fuera del área con espacio. ¿Cómo te posicionas?",
             "opciones": ["Achicando el ángulo hacia el punto de disparo", "Pegado a un palo fijo siempre", "En el centro exacto del arco sin ajustar", "Fuera del área todo el tiempo"],
             "correcta": "Achicando el ángulo hacia el punto de disparo"},
            {"pregunta": "Viene un mano a mano contra un delantero rival. ¿Qué haces primero?",
             "opciones": ["Achicar el ángulo avanzando de forma controlada", "Quedarte parado en la línea de gol", "Salir corriendo sin control hacia él", "Tirarte antes de que decida"],
             "correcta": "Achicar el ángulo avanzando de forma controlada"},
            {"pregunta": "Tienes el balón en las manos tras una atajada, con el rival presionando alto. ¿Qué opción de salida es mejor?",
             "opciones": ["Buscar al compañero libre con un saque corto o medio preciso", "Patear siempre lo más lejos posible sin mirar", "Salir driblando rivales dentro del área", "Esperar sin decidir nada"],
             "correcta": "Buscar al compañero libre con un saque corto o medio preciso"},
            {"pregunta": "Es un córner rival con varios rematadores altos. ¿Qué prioridad tienes como portero?",
             "opciones": ["Salir a despejar los balones dentro de tu radio de acción", "Quedarte fijo en la línea sin salir nunca", "Ignorar el área chica por completo", "Salir completamente del área"],
             "correcta": "Salir a despejar los balones dentro de tu radio de acción"},
            {"pregunta": "El rival ejecuta un tiro libre directo cerca del área. ¿Cómo organizas la barrera?",
             "opciones": ["Cubrir un palo con la barrera y tú cubrir el otro ángulo", "No poner barrera nunca", "Poner toda la barrera y dejar el arco vacío", "Salir del arco antes del disparo"],
             "correcta": "Cubrir un palo con la barrera y tú cubrir el otro ángulo"},
            {"pregunta": "Tu equipo gana por la mínima en el último minuto con un córner en contra. ¿Qué priorizas?",
             "opciones": ["Concentración total y salir a cualquier balón disputable", "Relajarte porque el partido ya está resuelto", "Salir del área sin necesidad", "Discutir con tus compañeros la formación"],
             "correcta": "Concentración total y salir a cualquier balón disputable"},
            {"pregunta": "Recibes un pase atrás de un compañero con un rival presionando de cerca. ¿Qué haces?",
             "opciones": ["Controlar rápido y buscar una salida segura con pie o mano", "Quedarte quieto sin decidir", "Patear el balón directo al rival", "Salir del área a driblar innecesariamente"],
             "correcta": "Controlar rápido y buscar una salida segura con pie o mano"},
            {"pregunta": "El delantero rival remata cruzado desde un ángulo cerrado. ¿Qué cubres primero?",
             "opciones": ["El primer palo, la zona más probable de remate", "El segundo palo siempre", "El centro del arco sin ajustar", "Sales del arco a tapar el ángulo completo"],
             "correcta": "El primer palo, la zona más probable de remate"},
        ],
    },
}

# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def calcular_ovr(stats):
    return round((stats["atr1"] + stats["atr2"] + stats["atr3"]) / 3)


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


def simular_temporada(stats, club, posicion):
    ovr = calcular_ovr(stats)
    fuerza = club["fuerza"]
    if ovr >= fuerza:
        partidos = random.randint(24, 30)
    elif ovr >= fuerza - 15:
        partidos = random.randint(14, 22)
    else:
        partidos = random.randint(4, 10)

    resultado = {"partidos": partidos, "goles": 0, "asistencias": 0,
                 "atajadas": 0, "vallas_invictas": 0,
                 "convocado_seleccion": False, "gana_titulo": False}

    if posicion == "Portero":
        for _ in range(partidos):
            remates_recibidos = random.randint(2, 7)
            prob_atajar = 0.45 + (stats["atr1"] / 100) * 0.45
            atajadas_partido = sum(1 for _ in range(remates_recibidos) if random.random() < prob_atajar)
            resultado["atajadas"] += atajadas_partido
            prob_valla = 0.10 + (stats["atr3"] / 100) * 0.35
            if random.random() < prob_valla:
                resultado["vallas_invictas"] += 1
    else:
        coef = {
            "Delantero":      {"gol": 0.45, "asist": 0.20},
            "Centrocampista": {"gol": 0.18, "asist": 0.42},
            "Defensa":        {"gol": 0.06, "asist": 0.14},
        }[posicion]
        prob_gol = (stats["atr1"] / 100) * coef["gol"]
        prob_asist = (stats["atr2"] / 100) * coef["asist"]
        resultado["goles"] = sum(1 for _ in range(partidos) if random.random() < prob_gol)
        resultado["asistencias"] = sum(1 for _ in range(partidos) if random.random() < prob_asist)

    if ovr >= 85:
        resultado["convocado_seleccion"] = True
    elif ovr >= 75 and random.random() < 0.4:
        resultado["convocado_seleccion"] = True

    if club["tier"] == "grande" and ovr >= fuerza - 8 and random.random() < 0.30:
        resultado["gana_titulo"] = True
    elif club["tier"] == "mediano" and ovr >= fuerza - 5 and random.random() < 0.15:
        resultado["gana_titulo"] = True

    return resultado


def cargar_carreras():
    if os.path.exists(CARRERAS_FILE):
        df = pd.read_csv(CARRERAS_FILE)
        if "nacionalidad" not in df.columns:
            df["nacionalidad"] = "Otro"
        return df
    return pd.DataFrame(columns=["nombre", "posicion", "nacionalidad", "ovr_pico", "goles", "asistencias", "atajadas", "trofeos", "fecha"])


def guardar_carrera(nombre, posicion, nacionalidad, ovr_pico, goles, asistencias, atajadas, trofeos):
    df = cargar_carreras()
    nueva = pd.DataFrame([{
        "nombre": nombre, "posicion": posicion, "nacionalidad": nacionalidad, "ovr_pico": ovr_pico,
        "goles": goles, "asistencias": asistencias, "atajadas": atajadas, "trofeos": trofeos,
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


def reset_reto_memoria(posicion):
    jugadas = POSICIONES[posicion]["jugadas_memoria"]
    st.session_state.memoria_objetivo = [random.choice(jugadas) for _ in range(5)]
    st.session_state.memoria_usuario = []
    st.session_state.memoria_fase = "mostrando"
    st.session_state.memoria_score = 0


def reset_reto_trivia(posicion):
    banco = POSICIONES[posicion]["preguntas"]
    st.session_state.trivia_preguntas = random.sample(banco, min(5, len(banco)))
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
    st.session_state.totales = {"goles": 0, "asistencias": 0, "atajadas": 0, "vallas_invictas": 0,
                                 "partidos": 0, "trofeos": 0, "convocatorias": 0}
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
        posicion = st.selectbox("Posición:", list(POSICIONES.keys()))
        nacionalidad = st.selectbox("Nacionalidad:", ["Venezuela", "Argentina", "Brasil", "Colombia", "España", "México", "Otro"])
    with col2:
        pie = st.selectbox("Pie preferido:", ["Derecho", "Izquierdo", "Ambidiestro"])

    cfg = POSICIONES[posicion]
    st.caption(f"Como {posicion}, tus atributos serán: **{cfg['atr1_nombre']}**, **{cfg['atr2_nombre']}** y **{cfg['atr3_nombre']}**.")

    if st.button("🚀 Empezar carrera", use_container_width=True):
        if nombre.strip() == "":
            st.warning("Escribe un nombre para tu jugador.")
        else:
            st.session_state.jugador = {"nombre": nombre.strip(), "posicion": posicion, "nacionalidad": nacionalidad, "pie": pie}
            st.session_state.stats = dict(POSICIONES[posicion]["stats_base"])
            for k in st.session_state.stats:
                st.session_state.stats[k] = max(15, min(60, st.session_state.stats[k] + random.randint(-5, 5)))
            st.session_state.ovr_pico = calcular_ovr(st.session_state.stats)
            st.session_state.etapa = "inicio_temporada"
            st.rerun()

# =========================================================
# ETAPA: INICIO DE TEMPORADA
# =========================================================
elif st.session_state.etapa == "inicio_temporada":
    j = st.session_state.jugador
    s = st.session_state.stats
    cfg = POSICIONES[j["posicion"]]
    ovr = calcular_ovr(s)

    club_nombre = st.session_state.club_actual["club"] if st.session_state.club_actual else "Sin club (cantera)"
    bandera = BANDERAS.get(j["nacionalidad"], "🌍")

    st.markdown(f"""
    <div class="jugador-card">
        <div class="bandera">{bandera}</div>
        <div class="info" style="flex:1; min-width:150px;">
            <h3>{j['nombre']}</h3>
            <p>{j['posicion']} · {j['nacionalidad']} · Temporada {st.session_state.temporada} · {st.session_state.edad} años</p>
            <p>🏟️ {club_nombre}</p>
        </div>
        <div class="ovr-gema"><div class="num">{ovr}</div><div class="lbl">OVR</div></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    for col, nombre_attr, valor in zip([col1, col2, col3],
                                        [cfg["atr1_nombre"], cfg["atr2_nombre"], cfg["atr3_nombre"]],
                                        [s["atr1"], s["atr2"], s["atr3"]]):
        icono = ICONO_ATRIBUTO.get(nombre_attr, "⚽")
        col.markdown(f'<div class="stat-box"><span class="icono">{icono}</span><div class="valor">{valor}</div><div class="etiqueta">{nombre_attr}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"Esta temporada te tocan **3 retos** hechos a la medida de un {j['posicion'].lower()}. Tu desempeño define cuánto mejoran tus estadísticas y qué clubes se fijan en ti.")

    if st.button("🎯 Comenzar retos de la temporada", use_container_width=True):
        reset_reto_precision()
        st.session_state.etapa = "reto_precision"
        st.rerun()

    if st.session_state.edad >= EDAD_MIN_RETIRO_VOLUNTARIO:
        if st.button("🏁 Retirarme ahora", use_container_width=True):
            st.session_state.etapa = "retirado"
            st.rerun()

# =========================================================
# ETAPA: RETO DE PRECISIÓN (atr1)
# =========================================================
elif st.session_state.etapa == "reto_precision":
    j = st.session_state.jugador
    cfg = POSICIONES[j["posicion"]]
    st.markdown(f"### 🎯 Reto de {cfg['atr1_nombre']}")
    st.caption(cfg["desc_precision"])

    with st.container(border=True):
        st.markdown('<span class="tag-verde">Reto 1 de 3</span>', unsafe_allow_html=True)
        potencia = st.session_state.precision_potencia
        st.progress(min(potencia, 100) / 100)
        st.markdown(f"**Carga actual:** {min(potencia, 100)}%")

        if not st.session_state.precision_disparado:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⚡ Cargar", use_container_width=True):
                    st.session_state.precision_potencia += random.randint(6, 14)
                    st.rerun()
            with col2:
                if st.button("🥅 ¡Ejecutar!", use_container_width=True, disabled=(potencia == 0)):
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
                st.success(f"¡Excelente! Zona ideal: {t_min}-{t_max}% · Tu carga: {min(potencia,100)}% · Puntaje: {score}")
            elif score >= 60:
                st.info(f"Buen intento. Zona ideal: {t_min}-{t_max}% · Tu carga: {min(potencia,100)}% · Puntaje: {score}")
            else:
                st.error(f"No salió bien. Zona ideal: {t_min}-{t_max}% · Tu carga: {min(potencia,100)}% · Puntaje: {score}")

            if st.button("➡️ Siguiente reto", use_container_width=True):
                reset_reto_memoria(j["posicion"])
                st.session_state.etapa = "reto_memoria"
                st.rerun()

# =========================================================
# ETAPA: RETO DE MEMORIA (atr2)
# =========================================================
elif st.session_state.etapa == "reto_memoria":
    j = st.session_state.jugador
    cfg = POSICIONES[j["posicion"]]
    st.markdown(f"### 🧠 Reto de {cfg['atr2_nombre']}")
    st.caption(cfg["desc_memoria"])

    with st.container(border=True):
        st.markdown('<span class="tag-verde">Reto 2 de 3</span>', unsafe_allow_html=True)

        if st.session_state.memoria_fase == "mostrando":
            secuencia_txt = "  →  ".join(st.session_state.memoria_objetivo)
            st.info(f"**Secuencia a memorizar:**\n\n{secuencia_txt}")
            if st.button("👁️ Ya la memoricé, ocultar y repetir", use_container_width=True):
                st.session_state.memoria_fase = "repitiendo"
                st.rerun()

        elif st.session_state.memoria_fase == "repitiendo":
            largo = len(st.session_state.memoria_objetivo)
            progreso = len(st.session_state.memoria_usuario)
            st.markdown(f"**Tu secuencia hasta ahora ({progreso}/{largo}):** " + " → ".join(st.session_state.memoria_usuario))
            jugadas = cfg["jugadas_memoria"]
            cols = st.columns(len(jugadas))
            for c, jugada in zip(cols, jugadas):
                if c.button(jugada, use_container_width=True, disabled=(progreso >= largo)):
                    st.session_state.memoria_usuario.append(jugada)
                    if len(st.session_state.memoria_usuario) == largo:
                        correctas = sum(1 for a, b in zip(st.session_state.memoria_usuario, st.session_state.memoria_objetivo) if a == b)
                        st.session_state.memoria_score = round(correctas / largo * 100)
                        st.session_state.memoria_fase = "resultado"
                    st.rerun()

        elif st.session_state.memoria_fase == "resultado":
            score = st.session_state.memoria_score
            st.markdown("**Secuencia correcta:** " + " → ".join(st.session_state.memoria_objetivo))
            st.markdown("**Tu secuencia:** " + " → ".join(st.session_state.memoria_usuario))
            if score >= 90:
                st.success(f"¡Jugada perfecta! Puntaje: {score}")
            elif score >= 50:
                st.info(f"Jugada aceptable. Puntaje: {score}")
            else:
                st.error(f"Se te complicó la jugada. Puntaje: {score}")

            if st.button("➡️ Siguiente reto", use_container_width=True):
                reset_reto_trivia(j["posicion"])
                st.session_state.etapa = "reto_trivia"
                st.rerun()

# =========================================================
# ETAPA: RETO TÁCTICO (atr3)
# =========================================================
elif st.session_state.etapa == "reto_trivia":
    j = st.session_state.jugador
    cfg = POSICIONES[j["posicion"]]
    st.markdown(f"### 📋 Reto de {cfg['atr3_nombre']}")
    st.caption("Lee la jugada y elige la mejor decisión.")

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
    j = st.session_state.jugador
    cfg = POSICIONES[j["posicion"]]
    s = st.session_state.stats
    p_score = st.session_state.precision_score
    m_score = st.session_state.memoria_score
    t_score = st.session_state.trivia_score
    nota_prueba = round((p_score + m_score + t_score) / 3)

    ganancia_atr1 = round(p_score / 100 * 6)
    ganancia_atr2 = round(m_score / 100 * 6)
    ganancia_atr3 = round(t_score / 100 * 6)

    if "aplicado_ganancias" not in st.session_state or st.session_state.aplicado_ganancias != st.session_state.temporada:
        s["atr1"] = min(99, s["atr1"] + ganancia_atr1)
        s["atr2"] = min(99, s["atr2"] + ganancia_atr2)
        s["atr3"] = min(99, s["atr3"] + ganancia_atr3)
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
    for col, nombre_attr, valor in zip([col1, col2, col3],
                                        [cfg["atr1_nombre"], cfg["atr2_nombre"], cfg["atr3_nombre"]],
                                        [p_score, m_score, t_score]):
        icono = ICONO_ATRIBUTO.get(nombre_attr, "⚽")
        col.markdown(f'<div class="stat-box"><span class="icono">{icono}</span><div class="valor">{valor}</div><div class="etiqueta">{nombre_attr}</div></div>', unsafe_allow_html=True)

    st.markdown(f"**Nota general de la prueba:** {nota_prueba}/100")
    st.markdown(f"{cfg['atr1_nombre']} +{ganancia_atr1} · {cfg['atr2_nombre']} +{ganancia_atr2} · {cfg['atr3_nombre']} +{ganancia_atr3}")

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
                color_club = COLOR_CLUB.get(oferta["club"], "#C9962C")
                st.markdown(f'<span class="tag-dorado">{etiqueta_tier}</span> <span class="tag-club" style="background:{color_club};">⚽ {oferta["club"]}</span>', unsafe_allow_html=True)
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
        "club": "Cantera (sin club)", "goles": 0, "asistencias": 0, "atajadas": 0, "partidos": 0,
    })
    st.session_state.temporada += 1
    st.session_state.edad += 1
    st.session_state.etapa = "inicio_temporada"
    st.rerun()

# =========================================================
# ETAPA: SIMULAR TEMPORADA CON CLUB
# =========================================================
elif st.session_state.etapa == "simular_temporada":
    j = st.session_state.jugador
    if "temporada_simulada" not in st.session_state or st.session_state.temporada_simulada != st.session_state.temporada:
        resultado = simular_temporada(st.session_state.stats, st.session_state.club_actual, j["posicion"])
        st.session_state.resultado_temporada = resultado
        st.session_state.totales["goles"] += resultado["goles"]
        st.session_state.totales["asistencias"] += resultado["asistencias"]
        st.session_state.totales["atajadas"] += resultado["atajadas"]
        st.session_state.totales["vallas_invictas"] += resultado["vallas_invictas"]
        st.session_state.totales["partidos"] += resultado["partidos"]
        if resultado["gana_titulo"]:
            st.session_state.totales["trofeos"] += 1
        if resultado["convocado_seleccion"]:
            st.session_state.totales["convocatorias"] += 1
        st.session_state.historial_temporadas.append({
            "temporada": st.session_state.temporada, "edad": st.session_state.edad,
            "club": st.session_state.club_actual["club"], "goles": resultado["goles"],
            "asistencias": resultado["asistencias"], "atajadas": resultado["atajadas"],
            "partidos": resultado["partidos"],
        })
        st.session_state.temporada_simulada = st.session_state.temporada

    r = st.session_state.resultado_temporada
    color_club = COLOR_CLUB.get(st.session_state.club_actual["club"], "#0E6B3A")
    bandera = BANDERAS.get(j["nacionalidad"], "🌍")
    st.markdown(f"""
    <div class="jugador-card" style="background: linear-gradient(120deg, {color_club} 0%, var(--verde-oscuro) 100%);">
        <div class="bandera">{bandera}</div>
        <div class="info" style="flex:1; min-width:150px;">
            <h3>📅 Temporada {st.session_state.temporada}</h3>
            <p>{j['nombre']} · {st.session_state.club_actual['club']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if j["posicion"] == "Portero":
        col1, col2, col3 = st.columns(3)
        col1.markdown(f'<div class="stat-box"><div class="valor">{r["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="stat-box"><div class="valor">{r["atajadas"]}</div><div class="etiqueta">Atajadas</div></div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="stat-box"><div class="valor">{r["vallas_invictas"]}</div><div class="etiqueta">Vallas invictas</div></div>', unsafe_allow_html=True)
    else:
        col1, col2, col3 = st.columns(3)
        col1.markdown(f'<div class="stat-box"><div class="valor">{r["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="stat-box"><div class="valor">{r["goles"]}</div><div class="etiqueta">Goles</div></div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="stat-box"><div class="valor">{r["asistencias"]}</div><div class="etiqueta">Asistencias</div></div>', unsafe_allow_html=True)

    if r["convocado_seleccion"]:
        st.success(f"🇻🇪 ¡Fuiste convocado a la selección de {j['nacionalidad']} esta temporada!")
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
        guardar_carrera(j["nombre"], j["posicion"], j["nacionalidad"], st.session_state.ovr_pico, t["goles"], t["asistencias"], t["atajadas"], t["trofeos"])
        st.session_state.carrera_guardada = True

    bandera = BANDERAS.get(j["nacionalidad"], "🌍")
    st.markdown(f"""
    <div class="resultado-box">
        <div style="font-size:2.8em; line-height:1;">{bandera}</div>
        <h2>🏁 {j['nombre']} se retira</h2>
        <p>{j['posicion']} · {j['nacionalidad']} · {st.session_state.temporada - 1} temporadas jugadas</p>
        <h1>OVR pico: {st.session_state.ovr_pico}</h1>
    </div>
    """, unsafe_allow_html=True)

    if j["posicion"] == "Portero":
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f'<div class="stat-box"><div class="valor">{t["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="stat-box"><div class="valor">{t["atajadas"]}</div><div class="etiqueta">Atajadas</div></div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="stat-box"><div class="valor">{t["vallas_invictas"]}</div><div class="etiqueta">Vallas invictas</div></div>', unsafe_allow_html=True)
        col4.markdown(f'<div class="stat-box"><div class="valor">{t["trofeos"]}</div><div class="etiqueta">Títulos</div></div>', unsafe_allow_html=True)
    else:
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f'<div class="stat-box"><div class="valor">{t["partidos"]}</div><div class="etiqueta">Partidos</div></div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="stat-box"><div class="valor">{t["goles"]}</div><div class="etiqueta">Goles</div></div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="stat-box"><div class="valor">{t["asistencias"]}</div><div class="etiqueta">Asistencias</div></div>', unsafe_allow_html=True)
        col4.markdown(f'<div class="stat-box"><div class="valor">{t["trofeos"]}</div><div class="etiqueta">Títulos</div></div>', unsafe_allow_html=True)

    if t["convocatorias"] > 0:
        st.info(f"Fuiste convocado a la selección nacional {t['convocatorias']} temporada(s).")

    st.markdown("### 🏆 Salón de la Fama")
    df = cargar_carreras()
    df_ordenado = df.sort_values(by=["ovr_pico"], ascending=False).reset_index(drop=True)
    for i, fila in df_ordenado.head(10).iterrows():
        clase = "rank-1" if i == 0 else "rank-2" if i == 1 else "rank-3" if i == 2 else "rank-other"
        if fila["posicion"] == "Portero":
            detalle = f"{int(fila['atajadas'])} atajadas"
        else:
            detalle = f"{int(fila['goles'])} goles"
        bandera_fila = BANDERAS.get(fila.get("nacionalidad", "Otro"), "🌍")
        st.markdown(f"""
        <div class="leaderboard-row {clase}">
            #{i+1} — {bandera_fila} {fila['nombre']} ({fila['posicion']}) — OVR pico {fila['ovr_pico']} · {detalle} · {int(fila['trofeos'])} títulos
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Crear un nuevo jugador", use_container_width=True):
        for clave in list(st.session_state.keys()):
            del st.session_state[clave]
        st.rerun()

st.markdown('<p class="firma">Los nombres de clubes se usan solo con fines de ambientación, sin afiliación oficial.</p>', unsafe_allow_html=True)
