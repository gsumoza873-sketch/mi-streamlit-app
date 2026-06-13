import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="AI Music Guide & Piano Studio",
    page_icon="🎹",
    layout="centered"
)

# 2. Estilos CSS Avanzados (Diseño de la Pantalla LED, el Teclado y el Chat)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    /* Contenedor de la IA / Chat */
    .chat-ia {
        background-color: #1e1b4b;
        border-left: 4px solid #a855f7;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(168, 85, 247, 0.2);
    }
    
    /* Pantalla Digital del Sintetizador */
    .pantalla-led {
        background: linear-gradient(145deg, #020617, #0f172a);
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
        font-family: 'Courier New', monospace;
    }
    .led-titulo {
        font-size: 11px;
        color: #60a5fa;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    .led-principal {
        font-size: 22px;
        font-weight: bold;
        color: #34d399;
        text-shadow: 0 0 8px rgba(52, 211, 153, 0.5);
    }
    .led-sub {
        font-size: 13px;
        color: #94a3b8;
        margin-top: 5px;
    }

    /* Contenedor del Piano */
    .piano-container {
        display: flex;
        justify-content: center;
        background-color: #1e293b;
        padding: 35px 15px;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        position: relative;
    }

    /* Teclas Blancas Animadas */
    .tecla-blanca {
        width: 52px;
        height: 190px;
        background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 90%, #e2e8f0 100%);
        border: 1px solid #cbd5e1;
        border-radius: 0 0 6px 6px;
        cursor: pointer;
        z-index: 1;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 15px;
        position: relative;
        transition: all 0.1s ease;
        -webkit-user-select: none;
        user-select: none;
    }
    .tecla-blanca:active {
        transform: scaleY(0.98);
        background: #cbd5e1;
    }

    /* Teclas Negras Animadas */
    .tecla-negra {
        width: 32px;
        height: 115px;
        background: linear-gradient(to bottom, #1e293b 0%, #0f172a 80%, #000000 100%);
        border: 1px solid #475569;
        border-radius: 0 0 4px 4px;
        cursor: pointer;
        margin-left: -16px;
        margin-right: -16px;
        z-index: 2;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 12px;
        position: relative;
        transition: all 0.1s ease;
        -webkit-user-select: none;
        user-select: none;
    }
    .tecla-negra:active {
        background: #334155;
    }

    /* Iluminación Neon de Acordes Activos */
    .tecla-blanca.activa {
        background: linear-gradient(to bottom, #38bdf8 0%, #0ea5e9 80%, #0284c7 100%) !important;
        box-shadow: 0 0 15px rgba(14, 165, 233, 0.7), inset 0 -8px 0 #0369a1;
    }
    .tecla-blanca.activa .nota-label {
        color: #ffffff !important;
    }

    .tecla-negra.activa {
        background: linear-gradient(to bottom, #f43f5e 0%, #e11d48 80%, #be123c 100%) !important;
        box-shadow: 0 0 15px rgba(225, 29, 72, 0.7), inset 0 -6px 0 #9f1239;
    }
    .tecla-negra.activa .nota-label {
        color: #ffffff !important;
    }

    .nota-label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
        font-size: 12px;
        color: #64748b;
    }
    .tecla-negra .nota-label {
        color: #94a3b8;
        font-size: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Título Principal
st.markdown("<h1 style='text-align: center; color: #a855f7; margin-bottom: 5px;'>🤖 AI Music Coach & Piano</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 25px;'>Dile a la IA qué quieres tocar y ella te guiará visualmente.</p>", unsafe_allow_html=True)

# 4. Diccionario Global de Acordes para el Piano
diccionario_acordes = {
    "C": {"notas": ["C4", "E4", "G4"], "msg": "DO - MI - SOL"},
    "Cm": {"notas": ["C4", "Db4", "G4"], "msg": "DO - RE# - SOL"},
    "D": {"notas": ["D4", "Gb4", "A4"], "msg": "RE - FA# - LA"},
    "Dm": {"notas": ["D4", "F4", "A4"], "msg": "RE - FA - LA"},
    "E": {"notas": ["E4", "Ab4", "B4"], "msg": "MI - SOL# - SI"},
    "Em": {"notas": ["E4", "F4", "B4"], "msg": "MI - SOL - SI"},
    "F": {"notas": ["F4", "A4", "C5"], "msg": "FA - LA - DO"},
    "Fm": {"notas": ["F4", "Ab4", "C5"], "msg": "FA - SOL# - DO"},
    "G": {"notas": ["G4", "B4", "D5"], "msg": "SOL - SI - RE"},
    "Gm": {"notas": ["G4", "Bb4", "D5"], "msg": "SOL - LA# - RE"},
    "A": {"notas": ["A4", "Db5", "E5"], "msg": "LA - DO# - MI"},
    "Am": {"notas": ["A4", "C5", "E5"], "msg": "LA - DO - MI"},
    "B": {"notas": ["B4", "Eb5", "Gb5"], "msg": "SI - RE# - FA#"},
    "Bm": {"notas": ["B4", "D5", "Gb5"], "msg": "SI - RE - FA#"}
}

# 5. Módulo del Buscador de la IA (Guía Musical Completa)
st.markdown("### 🔍 Consulta al Asistente de IA")
cancion_buscada = st.text_input("💬 Escribe el nombre de la canción o artista que quieres aprender (Ej: 'Blinding Lights', 'Bohemian Rhapsody', 'Perfect'):", placeholder="Escribe aquí...")

# Variables por defecto
acorde_a_mostrar = "C"
analisis_ia = "Introduce una canción arriba para que el Coach de IA analice su estructura armónica, ritmo y te monte los acordes en el piano."

if cancion_buscada:
    texto = cancion_buscada.lower()
    # Base de conocimiento simulada de la IA para dar respuestas ultra personalizadas
    if "light" in texto or "weekend" in texto:
        acorde_a_mostrar = "Fm"
        analisis_ia = "🎵 **Análisis de 'Blinding Lights' (The Weeknd):** Esta obra de Synth-Pop moderno se mueve en una vibra ochentera espectacular. Su progresión principal usa los acordes: **Fm - Cm - Eb - Db**. **Consejo de Ejecución:** Mantén un ritmo de pulso constante en la mano izquierda marcando los bajos, mientras que con la derecha marcas los acordes abiertos en el segundo tiempo."
    elif "perfect" in texto or "sheeran" in texto:
        acorde_a_mostrar = "G"
        analisis_ia = "🎵 **Análisis de 'Perfect' (Ed Sheeran):** Una balada romántica en compás de 6/8. Sus acordes base son: **G - Em - C - D**. **Consejo de Ejecución:** Al ser un ritmo ternario, debes tocar la mano derecha haciendo arpegios de tres notas o marcando tres pulsos suaves por cada acorde para lograr ese balance de vals pop."
    elif "rhapsody" in texto or "queen" in texto:
        acorde_a_mostrar = "Bb4" # Mapeado a un acorde cercano para la interfaz
        acorde_a_mostrar = "Cm"
        analisis_ia = "🎵 **Análisis de 'Bohemian Rhapsody' (Queen):** Una obra maestra compleja. La sección de la balada inicial está en **Bb Mayor**, pasando por **Gm** y **Cm**. **Consejo de Ejecución:** Freddie Mercury usaba mucho los acordes rotos. Practica haciendo la transición de Do Menor (Cm) a Fa Mayor (F) para dominar el puente dramático."
    elif "stay" in texto or "bieber" in texto:
        acorde_a_mostrar = "F"
        analisis_ia = "🎵 **Análisis de 'Stay' (The Kid LAROI & Justin Bieber):** Energía pura. Se basa en una progresión circular muy pegajosa: **F - G - Am - Em**. **Consejo de Ejecución:** Es una canción súper rápida. Concéntrate en cambiar de acorde exactamente en el golpe de la caja (batería) para no perder el ritmo dinámico."
    else:
        # Respuesta genérica inteligente si buscan cualquier otra cosa
        acorde_a_mostrar = "Am"
        analisis_ia = f"🎵 **Análisis de '{cancion_buscada}':** He analizado tu petición. Para este tipo de piezas, la estructura estándar suele basarse en la combinación menor/mayor relativa. Te recomiendo arrancar montando la base en **La Menor (Am)** y **Sol Mayor (G)**. **Consejo de Ejecución:** Toca primero los acordes de forma estática en bloques de 4 tiempos para memorizar las posiciones antes de sumarle cualquier ritmo."

    # Cuadro de respuesta de la IA
    st.markdown(f"""
        <div class="chat-ia">
            <span style="color: #c084fc; font-weight: bold;">🤖 AI Music Coach dice:</span><br>
            <p style="margin-top: 5px; font-size: 14.5px; line-height: 1.5; color: #e2e8f0;">{analisis_ia}</p>
        </div>
    """, unsafe_allow_html=True)

# 6. Selector de Práctica Basado en la Guía
st.markdown("### 🛠️ Entrenador de Teclado")
lista_opciones_acordes = list(diccionario_acordes.keys())
# Si la IA recomendó un acorde, lo pre-seleccionamos automáticamente
index_default = lista_opciones_acordes.index(acorde_a_mostrar) if acorde_a_mostrar in lista_opciones_acordes else 0

acorde_seleccionado = st.selectbox(
    "🎹 Elige qué acorde de la guía quieres visualizar en el piano:",
    options=lista_opciones_acordes,
    index=index_default
)

notas_a_iluminar = diccionario_acordes[acorde_seleccionado]["notas"]
msg_led = diccionario_acordes[acorde_seleccionado]["msg"]

# 7. PANTALLA LED VIRTUAL
st.markdown(f"""
    <div class="pantalla-led">
        <div class="led-titulo">Monitor de Notas Guía</div>
        <div class="led-principal">{msg_led}</div>
        <div class="led-sub">Visualizando la posición exacta en el tablero inferior</div>
    </div>
""", unsafe_allow_html=True)

# 8. Estructura Fija de Teclas
teclas = [
    {"nota": "C4", "tipo": "blanca", "label": "DO"},
    {"nota": "Db4", "tipo": "negra", "label": "Do#"},
    {"nota": "D4", "tipo": "blanca", "label": "RE"},
    {"nota": "Eb4", "tipo": "negra", "label": "Re#"},
    {"nota": "E4", "tipo": "blanca", "label": "MI"},
    {"nota": "F4", "tipo": "blanca", "label": "FA"},
    {"nota": "Gb4", "tipo": "negra", "label": "Fa#"},
    {"nota": "G4", "tipo": "blanca", "label": "SOL"},
    {"nota": "Ab4", "tipo": "negra", "label": "Sol#"},
    {"nota": "A4", "tipo": "blanca", "label": "LA"},
    {"nota": "Bb4", "tipo": "negra", "label": "La#"},
    {"nota": "B4", "tipo": "blanca", "label": "SI"},
    {"nota": "C5", "tipo": "blanca", "label": "DO+"},
    {"nota": "Db5", "tipo": "negra", "label": "Do#+"},
    {"nota": "D5", "tipo": "blanca", "label": "RE+"},
    {"nota": "Eb5", "tipo": "negra", "label": "Re#+"},
    {"nota": "E5", "tipo": "blanca", "label": "MI+"}
]

# 9. Renderizado Gráfico del Piano
html_piano = '<div class="piano-container">'
for t in teclas:
    es_activa = "activa" if t["nota"] in notas_a_iluminar else ""
    html_piano += f"""
    <div class="tecla-{t['tipo']} {es_activa}">
        <span class="nota-label">{t['label']}</span>
    </div>"""
html_piano += '</div>'

st.markdown(html_piano, unsafe_allow_html=True)

# Pie de página con tu firma
st.caption("⚡ AI Learning Music Engine v4.0 • Sistema de Guía Teórica • Hecho por Gabriel.s")
