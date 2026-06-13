import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Piano Virtual & Guía de Acordes",
    page_icon="🎹",
    layout="centered"
)

# 2. Estilos CSS para diseñar el teclado del piano
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .piano-container {
        display: flex;
        justify-content: center;
        background-color: #1e293b;
        padding: 30px 10px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        margin-bottom: 25px;
        position: relative;
        overflow-x: auto; /* Para que en móvil se pueda hacer scroll si es necesario */
    }
    /* Estilo de Teclas Blancas */
    .tecla-blanca {
        width: 50px;
        height: 180px;
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 0 0 5px 5px;
        cursor: pointer;
        z-index: 1;
        transition: background-color 0.1s;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 10px;
        position: relative;
    }
    .tecla-blanca:active {
        background-color: #e2e8f0;
    }
    /* Estilo de Teclas Negras */
    .tecla-negra {
        width: 30px;
        height: 110px;
        background-color: #000000;
        border: 1px solid #334155;
        border-radius: 0 0 4px 4px;
        cursor: pointer;
        margin-left: -15px;
        margin-right: -15px;
        z-index: 2;
        transition: background-color 0.1s;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 10px;
        position: relative;
    }
    .tecla-negra:active {
        background-color: #1e293b;
    }
    /* Iluminación de teclas activa por acorde seleccionado */
    .tecla-blanca.activa {
        background-color: #38bdf8 !important;
        box-shadow: inset 0 -10px 0 #0284c7;
    }
    .tecla-negra.activa {
        background-color: #f43f5e !important;
        box-shadow: inset 0 -8px 0 #be123c;
    }
    .nota-label {
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: 12px;
        user-select: none;
        color: #64748b;
    }
    .tecla-negra .nota-label {
        color: #94a3b8;
        font-size: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Título del software
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🎹 Piano Virtual Interactivo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Selecciona un acorde para aprender a tocarlo o haz clic en las teclas.</p>", unsafe_allow_html=True)

# 4. Diccionario de Acordes
acordes = {
    "Ninguno (Modo Libre)": [],
    "Do Mayor (C)": ["C4", "E4", "G4"],
    "Do Menor (Cm)": ["C4", "Db4", "G4"],
    "Re Mayor (D)": ["D4", "Gb4", "A4"],
    "Re Menor (Dm)": ["D4", "F4", "A4"],
    "Mi Mayor (E)": ["E4", "Ab4", "B4"],
    "Mi Menor (Em)": ["E4", "F4", "B4"],
    "Fa Mayor (F)": ["F4", "A4", "C5"],
    "Fa Menor (Fm)": ["F4", "Ab4", "C5"],
    "Sol Mayor (G)": ["G4", "B4", "D5"],
    "Sol Menor (Gm)": ["G4", "Bb4", "D5"],
    "La Mayor (A)": ["A4", "Db5", "E5"],
    "La Menor (Am)": ["A4", "C5", "E5"],
    "Si Mayor (B)": ["B4", "Eb5", "Gb5"],
    "Si Menor (Bm)": ["B4", "D5", "Gb5"]
}

# Selector de acordes
acorde_seleccionado = st.selectbox(
    "🔎 ¿Qué acorde quieres visualizar?", 
    options=list(acordes.keys())
)
notas_a_iluminar = acordes[acorde_seleccionado]

# 5. Estructura de las teclas (corregida)
base_url = "https://raw.githubusercontent.com/keithwhor/audiosynth/master/samples/piano/"
teclas = [
    {"nota": "C4", "tipo": "blanca", "file": "4c.mp3", "label": "DO"},
    {"nota": "Db4", "tipo": "negra", "file": "4cs.mp3", "label": "Do#"},
    {"nota": "D4", "tipo": "blanca", "file": "4d.mp3", "label": "RE"},
    {"nota": "Eb4", "tipo": "negra", "file": "4ds.mp3", "label": "Re#"},
    {"nota": "E4", "tipo": "blanca", "file": "4e.mp3", "label": "MI"},
    {"nota": "F4", "tipo": "blanca", "file": "4f.mp3", "label": "FA"},
    {"nota": "Gb4", "tipo": "negra", "file": "4fs.mp3", "label": "Fa#"},
    {"nota": "G4", "tipo": "blanca", "file": "4g.mp3", "label": "SOL"},
    {"nota": "Ab4", "tipo": "negra", "file": "4gs.mp3", "label": "Sol#"},
    {"nota": "A4", "tipo": "blanca", "file": "4a.mp3", "label": "LA"},
    {"nota": "Bb4", "tipo": "negra", "file": "4as.mp3", "label": "La#"},
    {"nota": "B4", "tipo": "blanca", "file": "4b.mp3", "label": "SI"},
    {"nota": "C5", "tipo": "blanca", "file": "5c.mp3", "label": "DO+"},
    {"nota": "Db5", "tipo": "negra", "file": "5cs.mp3", "label": "Do#+"},
    {"nota": "D5", "tipo": "blanca", "file": "5d.mp3", "label": "RE+"},
    {"nota": "Eb5", "tipo": "negra", "file": "5ds.mp3", "label": "Re#+"},
    {"nota": "E5", "tipo": "blanca", "file": "5e.mp3", "label": "MI+"}
]

# 6. Construcción del HTML del Piano con Javascript (Sintaxis Corregida)
html_piano = '<div class="piano-container">'

for t in teclas:
    # Arreglo el espacio que causaba el error de sintaxis en image_3.png
    es_activa = "activa" if t["nota"] in notas_a_iluminar else ""
    url_audio = f"{base_url}{t['file']}"
    
    # Inyección JS limpia: onclick="...play();". Se usa un Audio por tecla para permitir polifonía
    html_piano += f"""
    <div class="tecla-{t['tipo']} {es_activa}" onclick="var snd = new Audio('{url_audio}'); snd.play();">
        <span class="nota-label">{t['label']}</span>
    </div>"""

html_piano += '</div>'

# Renderizar el piano HTML
st.markdown(html_piano, unsafe_allow_html=True)

# 7. Cuadro informativo
st.write("---")
with st.expander("🎓 Teoría musical rápida"):
    if acorde_seleccionado == "Ninguno (Modo Libre)":
        st.write("💡 ¡Estás en modo libre! Toca cualquier tecla para escuchar su sonido. Las blancas son notas naturales y las negras alteraciones.")
    else:
        st.write(f"🎼 **Análisis del {acorde_seleccionado}:**")
        st.write(f"- **Notas que lo componen:** {', '.join(notas_a_iluminar)}")
        st.write("- **Características:** Esta combinación de notas crea el acorde que visualizas en azul o rojo.")

st.caption("🎹 Audio-Synthesizer Engine • Sube el volumen.")
