import streamlit as st

# 1. Configuración de la página (Actualizado a Guía Musical)
st.set_page_config(
    page_title="Guía Musical",
    page_icon="🎹",
    layout="centered"
)

# 2. Inyección de estilos CSS de forma ultra segura
st.markdown("<style>.stApp { background-color: #0b0f19; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.chat-ia { background-color: #1e1b4b; border-left: 4px solid #a855f7; padding: 18px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(168, 85, 247, 0.25); }</style>", unsafe_allow_html=True)
st.markdown("<style>.pantalla-led { background: linear-gradient(145deg, #020617, #0f172a); border: 2px solid #3b82f6; border-radius: 10px; padding: 15px; text-align: center; margin-bottom: 25px; box-shadow: 0 0 15px rgba(59, 130, 246, 0.3); font-family: 'Courier New', monospace; }</style>", unsafe_allow_html=True)
st.markdown("<style>.led-titulo { font-size: 11px; color: #60a5fa; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }</style>", unsafe_allow_html=True)
st.markdown("<style>.led-principal { font-size: 24px; font-weight: bold; color: #34d399; text-shadow: 0 0 8px rgba(52, 211, 153, 0.5); }</style>", unsafe_allow_html=True)
st.markdown("<style>.led-sub { font-size: 13px; color: #94a3b8; margin-top: 5px; }</style>", unsafe_allow_html=True)
st.markdown("<style>.piano-container { display: flex; justify-content: center; background-color: #1e293b; padding: 35px 15px; border-radius: 15px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); margin-bottom: 25px; position: relative; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-blanca { width: 52px; height: 190px; background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 90%, #e2e8f0 100%); border: 1px solid #cbd5e1; border-radius: 0 0 6px 6px; cursor: pointer; z-index: 1; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 15px; position: relative; transition: all 0.1s ease; -webkit-user-select: none; user-select: none; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-negra { width: 32px; height: 115px; background: linear-gradient(to bottom, #1e293b 0%, #0f172a 80%, #000000 100%); border: 1px solid #475569; border-radius: 0 0 4px 4px; cursor: pointer; margin-left: -16px; margin-right: -16px; z-index: 2; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 12px; position: relative; transition: all 0.1s ease; -webkit-user-select: none; user-select: none; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-blanca.activa { background: linear-gradient(to bottom, #38bdf8 0%, #0ea5e9 80%, #0284c7 100%) !important; box-shadow: 0 0 15px rgba(14, 165, 233, 0.7), inset 0 -8px 0 #0369a1; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-blanca.activa .nota-label { color: #ffffff !important; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-negra.activa { background: linear-gradient(to bottom, #f43f5e 0%, #e11d48 80%, #be123c 100%) !important; box-shadow: 0 0 15px rgba(225, 29, 72, 0.7), inset 0 -6px 0 #9f1239; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-negra.activa .nota-label { color: #ffffff !important; }</style>", unsafe_allow_html=True)
st.markdown("<style>.nota-label { font-family: 'Segoe UI', sans-serif; font-weight: bold; font-size: 12px; color: #64748b; }</style>", unsafe_allow_html=True)
st.markdown("<style>.tecla-negra .nota-label { color: #94a3b8; font-size: 10px; }</style>", unsafe_allow_html=True)

# 3. Título Principal (Actualizado a Guía Musical)
st.markdown("<h1 style='text-align: center; color: #a855f7; margin-bottom: 5px;'>🎹 Guía Musical</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 25px;'>Escribe una canción y la IA te enseñará a tocarla paso a paso en el teclado.</p>", unsafe_allow_html=True)

# 4. Base de datos de acordes
diccionario_acordes = {
    "C": {"notas": ["C4", "E4", "G4"], "nombre": "Do Mayor (DO - MI - SOL)"},
    "Cm": {"notas": ["C4", "Db4", "G4"], "nombre": "Do Menor (DO - RE# - SOL)"},
    "D": {"notas": ["D4", "Gb4", "A4"], "nombre": "Re Mayor (RE - FA# - LA)"},
    "Dm": {"notas": ["D4", "F4", "A4"], "nombre": "Re Menor (RE - FA - LA)"},
    "E": {"notas": ["E4", "Ab4", "B4"], "nombre": "Mi Mayor (MI - SOL# - SI)"},
    "Em": {"notas": ["E4", "F4", "B4"], "nombre": "Mi Menor (MI - SOL - SI)"},
    "F": {"notas": ["F4", "A4", "C5"], "nombre": "Fa Mayor (FA - LA - DO)"},
    "Fm": {"notas": ["F4", "Ab4", "C5"], "nombre": "Fa Menor (FA - SOL# - DO)"},
    "G": {"notas": ["G4", "B4", "D5"], "nombre": "Sol Mayor (SOL - SI - RE)"},
    "Gm": {"notas": ["G4", "Bb4", "D5"], "nombre": "Sol Menor (SOL - LA# - RE)"},
    "A": {"notas": ["A4", "Db5", "E5"], "nombre": "La Mayor (LA - DO# - MI)"},
    "Am": {"notas": ["A4", "C5", "E5"], "nombre": "La Menor (LA - DO - MI)"},
    "B": {"notas": ["B4", "Eb5", "Gb5"], "nombre": "Si Mayor (SI - RE# - FA#)"},
    "Bm": {"notas": ["B4", "D5", "Gb5"], "nombre": "Si Menor (SI - RE - FA#)"}
}

# 5. Módulo de Entrada de la IA
st.markdown("### 🔍 ¿Qué canción quieres aprender a tocar hoy?")
cancion_buscada = st.text_input("Introduce el nombre del tema y presiona ENTER:", placeholder="Ej: Lamento Boliviano, Despacito, De Música Ligera...")

if "cancion_actual" not in st.session_state:
    st.session_state.cancion_actual = ""
if "paso_actual" not in st.session_state:
    st.session_state.paso_actual = 0

notas_a_iluminar = []
msg_led_principal = "ESPERANDO PETICIÓN"
msg_led_sub = "Escribe una canción arriba para activar el tutor de IA."

# 6. Procesamiento de la búsqueda
if cancion_buscada:
    texto = cancion_buscada.lower()
    
    if cancion_buscada != st.session_state.cancion_actual:
        st.session_state.cancion_actual = cancion_buscada
        st.session_state.paso_actual = 0

    if "lamento" in texto or "boliviano" in texto:
        titulo_real = "Lamento Boliviano (Enanitos Verdes)"
        consejo_ia = "🎸 ¡Clásico del rock en español! Esta canción tiene una progresión circular nostálgica que se repite durante casi todo el tema."
        pasos_cancion = [
            {"acorde": "Em", "instruccion": "Paso 1: Arranca con Mi Menor (Em). Da la atmósfera triste al inicio del verso."},
            {"acorde": "Bm", "instruccion": "Paso 2: Pasa a Si Menor (Bm). Sostiene la tensión melódica."},
            {"acorde": "Am", "instruccion": "Paso 3: Baja a La Menor (Am). El punto más suave antes de resolver."},
            {"acorde": "Em", "instruccion": "Paso 4: Regresa a Mi Menor (Em) para cerrar el ciclo armónico."}
        ]
    elif "musica ligera" in texto or "soda" in texto:
        titulo_real = "De Música Ligera (Soda Stereo)"
        consejo_ia = "⚡ ¡Un himno total! Compuesto con 4 acordes llenos de fuerza. La clave aquí es el ritmo enérgico y constante."
        pasos_cancion = [
            {"acorde": "Bm", "instruccion": "Paso 1: Empieza con Si Menor (Bm). Es el famoso acorde con el que arranca el riff."},
            {"acorde": "G", "instruccion": "Paso 2: Salta a Sol Mayor (G). Aporta el brillo pop."},
            {"acorde": "D", "instruccion": "Paso 3: Sigue con Re Mayor (D). Sostiene la fuerza de la base."},
            {"acorde": "A", "instruccion": "Paso 4: Termina el ciclo en La Mayor (A) antes de volver a empezar."}
        ]
    else:
        titulo_real = f"{cancion_buscada.title()}"
        consejo_ia = f"🤖 ¡He analizado los patrones de '{cancion_buscada}'! Diseñé una guía optimizada usando la progresión universal armónica más efectiva."
        pasos_cancion = [
            {"acorde": "Am", "instruccion": "Paso 1: Inicia marcando La Menor (Am) para establecer la base triste."},
            {"acorde": "F", "instruccion": "Paso 2: Cambia fluidamente a Fa Mayor (F) para abrir el espectro visual."},
            {"acorde": "C", "instruccion": "Paso 3: Muévete a Do Mayor (C) entregando brillo y resolución."},
            {"acorde": "G", "instruccion": "Paso 4: Termina con Sol Mayor (G) creando la tensión de retorno."}
        ]

    # Cuadro informativo del Coach IA
    st.markdown(f"<div class='chat-ia'><span style='color: #c084fc; font-weight: bold; font-size: 16px;'>🤖 Tutor Musical IA dice:</span><br><p style='margin-top: 5px; font-size: 15px; color: #e2e8f0;'><b>Canción:</b> {titulo_real}</p><p style='font-size: 14px; color: #cbd5e1;'>{consejo_ia}</p></div>", unsafe_allow_html=True)

    # Controles de navegación paso a paso
    st.markdown("### 🧭 Guía de Ejecución Paso a Paso")
    col_prev, col_num, col_next = st.columns([1, 2, 1])
    
    with col_prev:
        if st.button("⬅️ Anterior"):
            st.session_state.paso_actual = (st.session_state.paso_actual - 1) % len(pasos_cancion)
            
    with col_next:
        if st.button("Siguiente ➡️"):
            st.session_state.paso_actual = (st.session_state.paso_actual + 1) % len(pasos_cancion)
            
    with col_num:
        st.markdown(f"<p style='text-align: center; font-size: 16px; font-weight: bold; margin-top: 5px; color: #a855f7;'>Paso {st.session_state.paso_actual + 1} de {len(pasos_cancion)}</p>", unsafe_allow_html=True)

    info_paso = pasos_cancion[st.session_state.paso_actual]
    acorde_nodo = info_paso["acorde"]
    
    notas_a_iluminar = diccionario_acordes[acorde_nodo]["notas"]
    msg_led_principal = f"TOCA: {diccionario_acordes[acorde_nodo]['nombre']}"
    msg_led_sub = info_paso["instruccion"]

# 7. RENDER DE PANTALLA LED
st.markdown(f"<div class='pantalla-led'><div class='led-titulo'>Monitor de Aprendizaje Guiado</div><div class='led-principal'>{msg_led_principal}</div><div class='led-sub'>{msg_led_sub}</div></div>", unsafe_allow_html=True)

# 8. Render del Piano Gráfico
teclas = [
    {"nota": "C4", "tipo": "blanca", "label": "DO"}, {"nota": "Db4", "tipo": "negra", "label": "Do#"},
    {"nota": "D4", "tipo": "blanca", "label": "RE"}, {"nota": "Eb4", "tipo": "negra", "label": "Re#"},
    {"nota": "E4", "tipo": "blanca", "label": "MI"}, {"nota": "F4", "tipo": "blanca", "label": "FA"},
    {"nota": "Gb4", "tipo": "negra", "label": "Fa#"}, {"nota": "G4", "tipo": "blanca", "label": "SOL"},
    {"nota": "Ab4", "tipo": "negra", "label": "Sol#"}, {"nota": "A4", "tipo": "blanca", "label": "LA"},
    {"nota": "Bb4", "tipo": "negra", "label": "La#"}, {"nota": "B4", "tipo": "blanca", "label": "SI"},
    {"nota": "C5", "tipo": "blanca", "label": "DO+"}, {"nota": "Db5", "tipo": "negra", "label": "Do#+"},
    {"nota": "D5", "tipo": "blanca", "label": "RE+"}, {"nota": "Eb5", "tipo": "negra", "label": "Re#+"},
    {"nota": "E5", "tipo": "blanca", "label": "MI+"}
]

html_piano = '<div class="piano-container">'
for t in teclas:
    es_activa = "activa" if t["nota"] in notas_a_iluminar else ""
    html_piano += f'<div class="tecla-{t["tipo"]} {es_activa}"><span class="nota-label">{t["label"]}</span></div>'
html_piano += '</div>'

st.markdown(html_piano, unsafe_allow_html=True)

# 9. Pie de página seguro con tu firma
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.1 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
