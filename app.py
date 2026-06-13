import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Piano Studio Visualizer",
    page_icon="🎹",
    layout="centered"
)

# 2. Estilos CSS Avanzados (Animaciones, Efectos de Pulsación y Pantalla LED)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    /* Pantalla Digital del Sintetizador */
    .pantalla-led {
        background: linear-gradient(145deg, #020617, #1e1b4b);
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
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
        text-shadow: 0 0 8px rgba(52, 211, 153, 0.6);
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
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
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
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .tecla-blanca:active {
        transform: scaleY(0.98);
        background: #cbd5e1;
        box-shadow: inset 0 5px 10px rgba(0,0,0,0.2);
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
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }
    .tecla-negra:active {
        background: #334155;
        box-shadow: inset 0 3px 5px rgba(0,0,0,0.5);
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

    /* Etiquetas de texto dentro de las teclas */
    .nota-label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
        font-size: 12px;
        color: #64748b;
        pointer-events: none;
    }
    .tecla-negra .nota-label {
        color: #94a3b8;
        font-size: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Título de la App
st.markdown("<h1 style='text-align: center; color: #3b82f6; margin-bottom: 5px;'>🎹 Visualizador de Acordes Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 25px;'>Estación de teoría interactiva para análisis armónico visual.</p>", unsafe_allow_html=True)

# 4. Base de datos expandida con emociones musicales
acordes_info = {
    "Ninguno (Modo Libre)": {"notas": [], "msg": "MODO LIBRE ACTIVO", "vibra": "Haz clic en las teclas para ver la respuesta visual del teclado."},
    "Do Mayor (C)": {"notas": ["C4", "E4", "G4"], "msg": "DO - MI - SOL", "vibra": "✨ Vibra: Alegre, brillante, completamente estable y triunfal."},
    "Do Menor (Cm)": {"notas": ["C4", "Db4", "G4"], "msg": "DO - RE# - SOL", "vibra": "🎬 Vibra: Dramática, misteriosa, típica de bandas sonoras de suspenso."},
    "Re Mayor (D)": {"notas": ["D4", "Gb4", "A4"], "msg": "RE - FA# - LA", "vibra": "🌅 Vibra: Épica, optimista, llena de energía de amanecer o victoria."},
    "Re Menor (Dm)": {"notas": ["D4", "F4", "A4"], "msg": "RE - FA - LA", "vibra": "🌧️ Vibra: Melancólica, seria, cargada de una profunda nostalgia."},
    "Mi Mayor (E)": {"notas": ["E4", "Ab4", "B4"], "msg": "MI - SOL# - SI", "vibra": "⚡ Vibra: Poderosa, mística, muy usada en himnos de Rock clásico."},
    "Mi Menor (Em)": {"notas": ["E4", "F4", "B4"], "msg": "MI - SOL - SI", "vibra": "🍃 Vibra: Orgánica, tranquila, excelente para baladas acústicas."},
    "Fa Mayor (F)": {"notas": ["F4", "A4", "C5"], "msg": "FA - LA - DO", "vibra": "⛪ Vibra: Espaciosa, gloriosa, genera sensación de paz y desahogo."},
    "Fa Menor (Fm)": {"notas": ["F4", "Ab4", "C5"], "msg": "FA - SOL# - DO", "vibra": "💔 Vibra: Trágica, desgarradora, ideal para expresar desamor profundo."},
    "Sol Mayor (G)": {"notas": ["G4", "B4", "D5"], "msg": "SOL - SI - RE", "vibra": "🎈 Vibra: Festiva, fiestera, el acorde más común del pop alegre."},
    "Sol Menor (Gm)": {"notas": ["G4", "Bb4", "D5"], "msg": "SOL - LA# - RE", "vibra": "⚓ Vibra: Oscura, pesada, evoca batallas marítimas o tensión urbana."},
    "La Mayor (A)": {"notas": ["A4", "Db5", "E5"], "msg": "LA - DO# - MI", "vibra": "🔥 Vibra: Brillante, fiera, transmite mucha confianza y actitud."},
    "La Menor (Am)": {"notas": ["A4", "C5", "E5"], "msg": "LA - DO - MI", "vibra": "🥀 Vibra: Poética, sentimental, la reina de las baladas latinas."},
    "Si Mayor (B)": {"notas": ["B4", "Eb5", "Gb5"], "msg": "SI - RE# - FA#", "vibra": "💎 Vibra: Exótica, compleja, un color brillante y muy llamativo."},
    "Si Menor (Bm)": {"notas": ["B4", "D5", "Gb5"], "msg": "SI - RE - FA#", "vibra": "⛰️ Vibra: Solitaria, fría, como explorar una montaña en la noche."}
}

# Selector de acordes estilizado
acorde_seleccionado = st.selectbox(
    "🎼 Selecciona un acorde para proyectar en el piano de pantalla:", 
    options=list(acordes_info.keys())
)

data = acordes_info[acorde_seleccionado]
notas_a_iluminar = data["notas"]

# 5. PANTALLA LED VIRTUAL (Le da el toque tecnológico e interactivo)
st.markdown(f"""
    <div class="pantalla-led">
        <div class="led-titulo">Frecuencímetro & Monitor Armónico</div>
        <div class="led-principal">{data["msg"]}</div>
        <div class="led-sub">{data["vibra"]}</div>
    </div>
""", unsafe_allow_html=True)

# 6. Definición de Teclas
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

# 7. Renderizado del Piano Gráfico
html_piano = '<div class="piano-container">'
for t in teclas:
    es_activa = "activa" if t["nota"] in notas_a_iluminar else ""
    html_piano += f"""
    <div class="tecla-{t['tipo']} {es_activa}">
        <span class="nota-label">{t['label']}</span>
    </div>"""
html_piano += '</div>'

st.markdown(html_piano, unsafe_allow_html=True)

# 8. Panel de Guía de Aprendizaje interactivo abajo
st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.info("💡 **Tips de Exposición:** Al cambiar el menú superior, muéstrale a la otra persona cómo cambian las combinaciones de colores de las teclas (Azul para las notas naturales y Rosado Neón para las sostenidas).")

with col2:
    st.success("📐 **Estructura Dinámica:** Cada acorde mapeado calcula automáticamente sus intervalos en el tablero LED superior sin necesidad de rec
