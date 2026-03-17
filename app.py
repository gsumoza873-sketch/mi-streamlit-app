import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Detector de Verdad 3000", page_icon="🕵️‍♂️")

# Estilo visual de terminal de inteligencia secreta
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0a0a;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    .stRadio > div {
        background-color: #1a1a1a;
        padding: 20px;
        border: 2px solid #00ff41;
        border-radius: 10px;
    }
    .status-box {
        border: 1px solid #00ff41;
        padding: 10px;
        margin: 10px 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📂 SISTEMA DE ANÁLISIS: CASO MANUEL")
st.write("---")
st.write("### 🚨 INSTRUCCIONES:")
st.write("Responde los siguientes acertijos de comportamiento para que la IA procese los datos.")

# --- ACERTIJOS ---

st.subheader("🔍 ACERTIJO 1: EL GUSTO")
a1 = st.radio("Se dice que Manuel ve a un hombre guapo en la calle y...", 
              ["Mira hacia otro lado (Miente)", "Disimula pero detalla", "Se le sale un suspiro"])

st.write("---")

st.subheader("🔍 ACERTIJO 2: EL SECRETO")
a2 = st.radio("¿Qué guarda Manuel en su 'carpeta secreta' del celular?", 
              ["Fotos de paisajes", "Memes de béisbol", "Fotos de tipos del gimnasio"])

st.write("---")

st.subheader("🔍 ACERTIJO 3: EL DESTINO")
a3 = st.radio("Si Manuel va a una fiesta, ¿hacia dónde gravita su mirada?", 
              ["Hacia la comida", "Hacia el televisor", "Hacia los pantalones ajustados"])

# --- PROCESAMIENTO FINAL ---
st.write("---")
if st.button("🧬 INICIAR ESCANEO DE ADN Y COMPORTAMIENTO"):
    
    with st.status("Analizando patrones de Manuel...", expanded=True) as status:
        st.write("Calculando niveles de estrógeno...")
        time.sleep(1)
        st.write("Revisando historial de miradas sospechosas...")
        time.sleep(1)
        st.write("Verificando atracción por el mismo sexo...")
        time.sleep(1)
        status.update(label="¡Análisis Completado!", state="complete", expanded=False)

    # El resultado final SIEMPRE es positivo
    st.markdown("""
        <div style='background-color: #ff0055; padding: 30px; border-radius: 15px; text-align: center; border: 5px solid white;'>
            <h1 style='color: white; font-size: 40px;'>⚠️ RESULTADO POSITIVO ⚠️</h1>
            <h2 style='color: white;'>LA IA HA HABLADO:</h2>
            <h1 style='color: yellow; font-size: 60px;'>🌈 MANUEL ES GAY 🌈</h1>
            <p style='color: white; font-size: 20px;'>Nivel de certeza: 100.9%</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    st.snow()

# Barra lateral
st.sidebar.title("📊 STATUS")
st.sidebar.write("Estado: **Escaneando...**")
st.sidebar.write("Objetivo: **Manuel**")
st.sidebar.markdown("---")
st.sidebar.info(f"Sistema desarrollado por el **Agente Gabriel**")
