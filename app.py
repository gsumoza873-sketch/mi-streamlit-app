import streamlit as st

# 1. Configuración de pantalla completa deportiva
st.set_page_config(page_title="LVBP Grand Slam Trivia", page_icon="🇻🇪", layout="wide")

# 2. CSS Avanzado para diseño "Estadio de Noche"
st.markdown("""
    <style>
    /* Fondo verde grama profundo */
    .stApp {
        background-color: #003300;
        background-image: linear-gradient(180deg, #001a00 0%, #004d00 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Título estilo pantalla de estadio */
    .titulo-estadio {
        background-color: #000;
        color: #f1c40f; /* Amarillo brillante */
        padding: 20px;
        border: 5px solid #bdc3c7;
        border-radius: 10px;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        box-shadow: 0px 0px 20px #f1c40f;
        margin-bottom: 30px;
    }

    /* Tarjetas de preguntas tipo Dugout */
    .stRadio > div {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #f1c40f;
        margin-top: 15px;
        transition: 0.3s;
    }

    /* Estilo para los botones */
    .stButton > button {
        background: linear-gradient(to bottom, #c0392b 5%, #96281b 100%);
        background-color: #c0392b;
        border-radius: 28px;
        border: 2px solid #ffffff;
        color: #ffffff !important;
        font-size: 22px !important;
        font-weight: bold;
        padding: 15px 40px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 4px solid #f1c40f;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado Impactante
st.markdown('<div class="titulo-estadio"><h1>🏟️ LVBP - EL DESAFÍO DEL FANÁTICO ⚾</h1></div>', unsafe_allow_html=True)

# 4. Preguntas de la Liga Venezolana
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 ¡Responde rápido, que te cantan el tercer strike!")
    
    p1 = st.radio("1. ¿Cuál es el actual campeón (2023-24) que rompió la sequía de casi 38 años?", 
                 ["Cardenales de Lara", "Leones del Caracas", "Tiburones de La Guaira", "Tigres de Aragua"])

    p2 = st.radio("2. ¿Quién es el máximo jonronero histórico de la LVBP?", 
                 ["Alex Cabrera", "Robert Pérez", "Eliezer Alfonzo", "Oscar Azócar"])

    p3 = st.radio("3. ¿Cuál de estos estadios es el nuevo hogar de los Leones y el más moderno de Latinoamérica?", 
                 ["Universitario", "Estadio Monumental Simón Bolívar", "José Bernardo Pérez", "Guatamare"])

    p4 = st.radio("4. ¿Qué equipo protagoniza junto al Magallanes el 'Eterno Rival'?", 
                 ["Caribes de Anzoátegui", "Águilas del Zulia", "Leones del Caracas", "Bravos de Margarita"])

    p5 = st.radio("5. ¿A qué leyenda se le conoce como 'El Señor Pelota'?", 
                 ["Luis Aparicio", "Andrés Galarraga", "Robert Pérez", "Víctor Davalillo"])

with col2:
    st.image("https://images.unsplash.com/photo-1547619232-983637691a3c?w=400&q=80", caption="¡Sentimiento Nacional!")
    st.info("💡 **Dato Curioso:** Venezuela es el país con más Series del Caribe ganadas después de República Dominicana.")

st.markdown("---")

# 5. Botón de RESULTADOS
if st.button("⚾ ¡CANTAR EL RESULTADO!"):
    nota = 0
    # Validación
    if p1 == "Tiburones de La Guaira": nota += 1
    if p2 == "Eliezer Alfonzo": nota += 1
    if p3 == "Estadio Monumental Simón Bolívar": nota += 1
    if p4 == "Leones del Caracas": nota += 1
    if p5 == "Víctor Davalillo": nota += 1

    st.markdown("### 📊 Pizarra Final:")
    
    if nota == 5:
        st.success(f"🏆 ¡JONRÓN CON LAS BASES LLENAS! Sacaste {nota}/5. ¡Eres un verdadero manager!")
        st.balloons()
    elif nota >= 3:
        st.warning(f"🏃 ¡A salvo en primera! Sacaste {nota}/5. Sabes de béisbol, pero te falta entrenamiento.")
    else:
        st.error(f"🧤 ¡PONCHADO! Sacaste {nota}/5. Tienes que ver más juegos en el estadio.")

# Barra lateral
with st.sidebar:
    st.title("👨‍💻 Info")
    st.write("Esta página es oficial de:")
    st.header("GABRIEL")
    st.write("---")
    st.write("Temporada 2026")
