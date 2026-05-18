import streamlit as st

# 1. Configuración de la página única
st.set_page_config(
    page_title="Operativo Salvación: Anatomía",
    page_icon="🧠",
    layout="centered"
)

# 2. Estilos CSS personalizados para el ambiente de estudio de Fariana
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .main-card {
        background-color: #1e293b;
        padding: 30px;
        border-radius: 15px;
        border-top: 6px solid #3b82f6;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
    }
    .titulo-principal {
        color: #3b82f6 !important;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-titulo {
        color: #94a3b8;
        text-align: center;
        font-size: 16px;
        margin-bottom: 30px;
    }
    .bloque-explicacion {
        background-color: #334155;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin-bottom: 20px;
    }
    .musculo-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #475569;
        margin-bottom: 15px;
    }
    .musculo-nombre {
        color: #f59e0b;
        font-size: 18px;
        font-weight: bold;
    }
    h2, h3 {
        color: #3b82f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Banner de Bienvenida y Humor para Fariana
st.markdown("""
    <div class="main-card">
        <h1 class="titulo-principal">🧠 OPERATIVO EXPOSICIÓN: ¡FARIANA SACA 20!</h1>
        <p class="sub-titulo">Guía interactiva y express para dominar el cuello anterior sin morir en el intento</p>
    </div>
""", unsafe_allow_html=True)

st.warning("⚠️ **Estrategia mental para Fariana:** Si en plena exposición te da pánico y te quedas en blanco, mira fijamente al profesor con mucha seguridad y di 'Hueso Hioides'. Eso te da +5 puntos de confianza automáticamente.")

# 4. Tema 1: Músculos Infrahioideos
st.markdown("## 🏢 El Edificio del Cuello: Músculos Infrahioideos")
st.markdown("""
<div class="bloque-explicacion">
    <b>¿Qué son en cristiano?</b> Son 4 pares de músculos delgados que están <b>debajo del hueso hioides</b>. 
    Su trabajo es bajar el hioides y la laringe cuando tragamos comida o cuando hablamos. Para que no se te olviden, están organizados en dos pisos (planos musculares).
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚪 Primer Piso (Plano Superficial)")
    st.write("Los que se ven a primera vista al quitar la piel:")
    
    st.markdown("""
    <div class="musculo-card">
        <div class="musculo-nombre">1. Esternocleidohioideo</div>
        <p style='font-size: 14px; color: #e2e8f0; margin-top:5px;'>
            El nombre es un trabalenguas, pero su ruta es fácil: Nace en el <b>esternón</b> y la clavícula, y sube derechito en línea recta hasta insertarse en el <b>hioides</b>. Es el guardaespaldas principal del frente.
        </p>
    </div>
    <div class="musculo-card">
        <div class="musculo-nombre">2. Omohioideo</div>
        <p style='font-size: 14px; color: #e2e8f0; margin-top:5px;'>
            Este es el 'viajero rumbero' porque tiene <b>dos vientres musculares</b> unidos por un tendón en el medio. Hace el viaje largo: viene en diagonal desde el <b>omóplato</b> (atrás en la espalda) cruzando todo el cuello hasta llegar al hioides.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🚪 Planta Baja (Plano Profundo)")
    st.write("Los que están escondidos abajo protegiendo los órganos:")
    
    st.markdown("""
    <div class="musculo-card">
        <div class="musculo-nombre">3. Esternotiroideo</div>
        <p style='font-size: 14px; color: #e2e8f0; margin-top:5px;'>
            Empieza abajo en el <b>esternón</b> pero le dio flojera y se cansó a mitad de camino, plantándose únicamente en el <b>cartílago tiroides</b>. ¡Este no llega al hioides!
        </p>
    </div>
    <div class="musculo-card">
        <div class="musculo-nombre">4. Tirohioideo</div>
        <p style='font-size: 14px; color: #e2e8f0; margin-top:5px;'>
            Es el relevo del flojo. Arranca justo donde el anterior se rindió (en el <b>cartílago tiroides</b>) y sube el tramo final que faltaba hasta el hueso <b>hioides</b>. Básicamente es el ascensor de conexión.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Tema 2: Irrigación
st.markdown("## 🩸 El Sistema de Tuberías: La Irrigación Sanguínea")
st.markdown("""
<div class="bloque-explicacion">
    ¿Quién le lleva los nutrientes y el oxígeno a todos estos músculos y órganos vitales (como la tiroides y la laringe)? El agua y la luz corren por cuenta de dos arterias principales que trabajan en equipo:
    <ul>
        <li><b>Arteria Carótida Externa:</b> Es la manguera principal que sube por el cuello. De ella sale una rama clave llamada <b>Arteria Tiroidea Superior</b>, que baja a encargarse de la parte alta de la tiroides y los músculos del frente.</li>
        <li><b>Arteria Subclavia:</b> Pasa por debajo de la clavícula y despacha hacia arriba otra rama llamada <b>Arteria Tiroidea Inferior</b>.</li>
    </ul>
    💡 <b>Dato pro para lucirse con el profe:</b> La arteria tiroidea superior y la inferior se unen en el cuello (hacen una <i>anastomosis</i>). Así arman una red de seguridad brutal para que a la tiroides y a la laringe jamás les falte sangre.
</div>
""", unsafe_allow_html=True)

# 6. El Cuestionario de 3 preguntas para Fariana (Versión Ultra-Compatible)
st.write("---")
st.markdown("## 📝 ¡Quiz de Control para Fariana!")
st.write("Elige una opción en cada pregunta para comprobar tus conocimientos:")

# Pregunta 1
p1 = st.radio(
    "1. ¿Cuál de estos músculos se frena a mitad de camino y NO toca el hueso hioides?",
    ["--- Selecciona una opción ---", "Esternocleidohioideo", "Omohioideo", "Esternotiroideo"]
)
if p1 == "Esternotiroideo":
    st.success("¡Brutal, Fariana! Ese se rinde antes, en el cartílago tiroides. ¡Llevas un punto! 🔥")
elif p1 != "--- Selecciona una opción ---":
    st.error("Nop. Ese sí completa la ruta hasta arriba. ¡Acuérdate del que se frena a mitad de camino!")

# Pregunta 2
p2 = st.radio(
    "2. ¿Qué músculo es el 'raro' que tiene dos vientres y viaja desde el omóplato?",
    ["--- Selecciona una opción ---", "Tirohioideo", "Omohioideo", "Esternohioideo"]
)
if p2 == "Omohioideo":
    st.success("¡Excelente! El prefijo 'Omo' viene de hombro/omóplato. ¡Dominado! 🧠")
elif p2 != "--- Selecciona una opción ---":
    st.error("Incorrecto. Piensa en el aventurero que hace el viaje largo en diagonal desde la espalda.")

# Pregunta 3
p3 = st.radio(
    "3. ¿De qué arteria principal nace la Arteria Tiroidea Superior que nutre esta zona?",
    ["--- Selecciona una opción ---", "Arteria Carótida Externa", "Arteria Subclavia", "Arteria Aorta"]
)
if p3 == "Arteria Carótida Externa":
    st.balloons()  # ¡Lluvia de globos virtuales!
    st.success("¡Coronaste! La Carótida Externa es la mamá de la rama superior. ¡Lista para destrozar esa exposición! 🎓")
elif p3 != "--- Selecciona una opción ---":
    st.error("Casi, pero esa manda la inferior. La superior viene desde más arriba (la carótida).")

st.write("---")
st.caption("Guía de Estudio Interactiva Especial • Hecho por Gabriel Sumoza para Fariana • ¡Mano, tengo fe! 🇻🇪")
