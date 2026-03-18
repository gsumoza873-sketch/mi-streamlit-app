import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Detector de Verdad 3000", page_icon="⚾")

# Estilo visual y Animación de Pelotas
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Animación de pelotas cayendo */
    @keyframes falling {
        0% { transform: translateY(-100vh) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(360deg); }
    }

    .ball {
        position: fixed;
        top: -10%;
        font-size: 2rem;
        z-index: 9999;
        animation: falling 3s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📂 ANÁLISIS DE ADN: CASO MANUEL")
st.write("---")

# --- ACERTIJOS ---
st.subheader("🔍 ACERTIJO 1")
a1 = st.radio("¿Qué prefiere Manuel en un estadio?", 
              ["Ver el juego", "Ver a los jugadores en el dugout", "Que le den un 'strike'"])

st.subheader("🔍 ACERTIJO 2")
a2 = st.radio("Si Manuel atrapa una pelota, ¿qué hace?", 
              ["Se la guarda", "La regala a un niño", "Se emociona porque es 'redonda y dura'"])

# --- PROCESAMIENTO ---
if st.button("🧬 REALIZAR PRUEBA DE CAMPO"):
    
    with st.status("Procesando datos sospechosos...", expanded=True) as status:
        time.sleep(1)
        st.write("Verificando radar de 'bateo'...")
        time.sleep(1)
        st.write("Confirmando orientación...")
        time.sleep(1)
        status.update(label="¡ANÁLISIS COMPLETADO!", state="complete", expanded=False)

    # REVELACIÓN CON LLUVIA DE PELOTAS
    # Generamos 20 pelotas en posiciones aleatorias usando HTML
    balls_html = "".join([f'<div class="ball" style="left: {i*5}%; animation-delay: {i*0.2}s;">⚾</div>' for i in range(20)])
    st.markdown(balls_html, unsafe_allow_html=True)

    st.markdown("""
        <div style='background-color: #ff0055; padding: 30px; border-radius: 15px; text-align: center; border: 5px solid white;'>
            <h1 style='color: white; font-size: 40px;'>⚠️ RESULTADO POSITIVO ⚠️</h1>
            <h2 style='color: white;'>LA IA DE GABRIEL DETERMINA:</h2>
            <h1 style='color: yellow; font-size: 60px;'>🌈 MANUEL ES GAY 🌈</h1>
            <p style='color: white; font-size: 20px;'>¡Se ponchó! ⚾</p>
        </div>
    """, unsafe_allow_html=True)
    
    # También lanzamos nieve para que haya más movimiento
    st.snow()

# Barra lateral
st.sidebar.title("👨‍💻 LAB")
st.sidebar.info("Investigación: **Gabriel**")
