import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Piano Virtual & Guía de Acordes",
    page_icon="🎹",
    layout="centered"
)

# 2. Estilos CSS para diseñar el teclado del piano (Teclas blancas y negras)
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

    <script>
    // Sintetizador Nativo en Javascript para evitar bloqueos de audio
    function playNote(frequency) {
        try {
            // Inicializar el contexto de audio del navegador
            var AudioContext = window.AudioContext || window.webkitAudioContext;
            var ctx = new AudioContext();
            
            // Crear el oscilador (generador de onda) y la ganancia (volumen)
            var osc = ctx.createOscillator();
            var gainNode = ctx.createGain();
            
            // Configurar tipo de onda suave para que suene agradable (tipo piano/órgano)
            osc.type = 'triangle'; 
            osc.frequency.value = frequency;
            
            // Configurar envolvente de volumen (ataque rápido y desvanecimiento progresivo)
            gainNode.gain.setValueAtTime(0.5, ctx.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 1.2);
            
            // Conectar componentes
            osc.connect(gainNode);
            gainNode.connect(ctx.destination);
            
            // Reproducir y detener automáticamente
            osc.start();
            osc.stop(ctx.currentTime + 1.2);
        } catch(e) {
            console.error("Error al reproducir audio:", e);
        }
    }
    </script>
""", unsafe_allow_html=True)

# 3. Título del software
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🎹 Piano Virtual Interactivo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Selecciona un acorde para aprender a tocarlo o haz clic en las teclas para escuchar el sonido sintético real.</p>", unsafe_allow_html=True)

# 4. Diccionario de Acordes (Mapeo de notas)
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

# 5. Estructura de las teclas con sus frecuencias exactas en Hertz (Hz)
teclas = [
    {"nota": "C4", "tipo": "blanca", "hz": 261.63, "label": "DO"},
    {"nota": "Db4", "tipo": "negra", "hz": 277.18, "label": "Do#"},
    {"nota": "D4", "tipo": "blanca", "hz": 293.66, "label": "RE"},
    {"nota": "Eb4", "tipo": "negra", "hz": 311.13, "label": "Re#"},
    {"nota": "E4", "tipo": "blanca", "hz": 329.63, "label": "MI"},
    {"nota": "F4", "tipo": "blanca", "hz": 349.23, "label": "FA"},
    {"nota": "Gb4", "tipo": "negra", "hz": 369.99, "label": "Fa#"},
    {"nota": "G4", "tipo": "blanca", "hz": 392.00, "label": "SOL"},
    {"nota": "Ab4", "tipo": "negra", "hz": 415.30, "label": "Sol#"},
    {"nota": "A4", "tipo": "blanca", "hz": 440.00, "label": "LA"},
    {"nota": "Bb4", "tipo": "negra", "hz": 466.16, "label": "La#"},
    {"nota": "B4", "tipo": "blanca", "hz": 493.88, "label": "SI"},
    {"nota": "C5", "tipo": "blanca", "hz": 523.25, "label": "DO+"},
    {"nota": "Db5", "tipo": "negra", "hz": 554.37, "label": "Do#+"},
    {"nota": "D5", "tipo": "blanca", "hz": 587.33, "label": "RE+"},
    {"nota": "Eb5", "tipo": "negra", "hz": 622.25, "label": "Re#+"},
    {"nota": "E5", "tipo": "blanca", "hz": 659.25, "label": "MI+"}
]

# 6. Construcción del HTML del Piano llamando a la función JS local
html_piano = '<div class="piano-container">'

for t in teclas:
    es_activa = "activa" if t["nota"] in notas_a_iluminar else ""
    # Llamamos a playNote pasando la frecuencia en Hertz directamente
    html_piano += f"""
    <div class="tecla-{t['tipo']} {es_activa}" onclick="playNote({t['hz']});">
        <span class="nota-label">{t['label']}</span>
    </div>"""

html_piano += '</div>'

# Renderizar el piano HTML
st.markdown(html_piano, unsafe_allow_html=True)

# 7. Cuadro informativo de teoría musical rápida
st.write("---")
with st.expander("🎓 Teoría musical rápida"):
    if acorde_seleccionado == "Ninguno (Modo Libre)":
        st.write("💡 ¡Estás en modo libre! El sistema genera las ondas sonoras directamente en tu navegador usando la Web Audio API nativa.")
    else:
        st.write(f"🎼 **Análisis del {acorde_seleccionado}:**")
        st.write(f"- **Notas que lo componen:** {', '.join(notas_a_iluminar)}")
        st.write("- **Características:** Esta combinación de frecuencias genera el acorde iluminado en el tablero.")

st.caption("🎹 Web Audio API Engine • Sistema Autónomo Antivolúmenes Bloqueados.")
