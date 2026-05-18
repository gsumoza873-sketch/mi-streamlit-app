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

# 3. Banner de Bienvenida para Fariana
st.markdown("""
    <div class="main-card">
        <h1 class="titulo-principal">🧠 OPERATIVO EXPOSICIÓN: ¡FARIANA SACA 20!</h1>
        <p class="sub-titulo">Guía interactiva y express para dominar el cuello anterior sin morir en el intento</p>
    </div>
""", unsafe_allow_html=True)

# Consejo corregido según lo que me pediste
st.info("💡 **Un recordatorio para Fariana:** Si en plena exposición se te olvida algo por los nervios, no te preocupes. Respira profundo durante tres segundos, piensa con calma y retoma la idea. ¡Tú puedes con esto!")

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
