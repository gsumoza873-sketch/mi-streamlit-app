import streamlit as st

# 1. Configuración de pantalla
st.set_page_config(page_title="LVBP Master Stats", page_icon="🇻🇪", layout="wide")

# CSS para el estilo Estadio
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #001a00 0%, #004d00 100%);
        color: white;
    }
    .titulo-estadio {
        background-color: #000;
        color: #f1c40f;
        padding: 15px;
        border: 4px solid #f1c40f;
        border-radius: 10px;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
    }
    .stRadio > div {
        background-color: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #f1c40f;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL: HISTORIA Y CRÉDITOS ---
with st.sidebar:
    st.markdown("<h1 style='color: #f1c40f;'>🏟️ INFO LVBP</h1>", unsafe_allow_html=True)
    st.write(f"Creado por: **Gabriel**")
    st.divider()
    
    st.subheader("📚 Historia de los Equipos")
    equipo = st.selectbox("Selecciona un equipo para ver su historia:", [
        "Leones del Caracas", "Navegantes del Magallanes", "Tigres de Aragua", 
        "Cardenales de Lara", "Tiburones de La Guaira", "Águilas del Zulia",
        "Caribes de Anzoátegui", "Bravos de Margarita"
    ])
    
    # Datos de los equipos
    info_equipos = {
        "Leones del Caracas": {"títulos": 21, "jugador": "Víctor Davalillo", "historia": "Fundados en 1942. Es el equipo con más títulos en la historia de la liga."},
        "Navegantes del Magallanes": {"títulos": 13, "jugador": "Luis 'Camaleón' García", "historia": "El equipo más antiguo de Venezuela (1917). Protagonista del eterno rival."},
        "Tigres de Aragua": {"títulos": 10, "jugador": "David Concepción", "historia": "Famosos por su dinastía en los 2000 ganando varios títulos seguidos."},
        "Cardenales de Lara": {"títulos": 6, "jugador": "Robert Pérez", "historia": "Símbolo de constancia en el occidente del país."},
        "Tiburones de La Guaira": {"títulos": 8, "jugador": "Luis Aparicio", "historia": "Rompieron una sequía histórica en la 23-24 de la mano de Ozzie Guillén."},
        "Águilas del Zulia": {"títulos": 6, "jugador": "Luis Aparicio", "historia": "Gran tradición zuliana, campeones de dos Series del Caribe."},
        "Caribes de Anzoátegui": {"títulos": 4, "jugador": "Eliézer Alfonzo", "historia": "La 'Tribu' ha sido el equipo más dominante del oriente en la última década."},
        "Bravos de Margarita": {"títulos": 0, "jugador": "Henry Blanco", "historia": "Anteriormente Pastora de los Llanos, ahora representan a la Isla de Margarita."}
    }
    
    # Mostrar la info en la barra lateral
    st.info(f"**Títulos:** {info_equipos[equipo]['títulos']}\n\n**Máximo Jugador:** {info_equipos[equipo]['jugador']}\n\n**Reseña:** {info_equipos[equipo]['historia']}")

# --- CUERPO PRINCIPAL: TRIVIA ---
st.markdown('<div class="titulo-estadio"><h1>⚾ DESAFÍO DE BÉISBOL PROFESIONAL ⚾</h1></div>', unsafe_allow_html=True)
st.write("")

# Diccionario de preguntas para poder comparar después
trivia = [
    {"id": "p1", "q": "¿Quién es el actual campeón (23-24)?", "ops": ["Magallanes", "Tiburones", "Leones"], "ans": "Tiburones"},
    {"id": "p2", "q": "¿Qué equipo tiene más títulos?", "ops": ["Magallanes", "Leones", "Tigres"], "ans": "Leones"},
    {"id": "p3", "q": "¿Dónde juegan las Águilas?", "ops": ["Maracay", "Maracaibo", "Valencia"], "ans": "Maracaibo"},
    {"id": "p4", "q": "¿Apodo del Magallanes?", "ops": ["Los Melenudos", "La Nave Turca", "Los Salados"], "ans": "La Nave Turca"},
    {"id": "p5", "q": "¿Quién es 'El Señor Pelota'?", "ops": ["Luis Aparicio", "Víctor Davalillo", "Robert Pérez"], "ans": "Víctor Davalillo"}
]

# Guardar respuestas
user_ans = {}
for item in trivia:
    user_ans[item["id"]] = st.radio(item["q"], item["ops"], key=item["id"])
    st.write("")

if st.button("🏟️ FINALIZAR JUEGO"):
    puntos = 0
    st.subheader("📋 REPORTE DEL UMPIRE:")
    
    for item in trivia:
        if user_ans[item["id"]] == item["ans"]:
            st.success(f"✅ **CORRECTO:** {item['q']} -> **{item['ans']}**")
            puntos += 1
        else:
            # AQUÍ TE DICE EN CUÁL TE EQUIVOCASTE
            st.error(f"❌ **ERROR:** {item['q']}\n\nElegiste: *{user_ans[item['id']]}*. La correcta era: **{item['ans']}**")
    
    st.divider()
    if puntos == 5:
        st.balloons()
        st.write(f"## 🏆 ¡GRAND SLAM! Puntaje: {puntos}/5")
    else:
        st.write(f"## ⚾ Puntaje Final: {puntos}/5. ¡Sigue practicando, Gabriel!")
