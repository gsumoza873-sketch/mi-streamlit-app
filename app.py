import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Roseline's Beauty Challenge", page_icon="💄", layout="centered")

# Estilo visual: Soft Pink & Gold (Estilo Sephora/Ulta)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff0f3 0%, #ffccd5 100%);
        color: #590d22;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    .beauty-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #ff4d6d;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #333;
    }

    .stButton>button {
        background: linear-gradient(90deg, #ff4d6d 0%, #c9184a 100%) !important;
        color: white !important;
        border-radius: 25px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        height: 3em !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💄 ROSELINE: BEAUTY GURU QUIZ")
st.write("---")
st.write("### ¿Eres una experta en maquillaje? ¡Demuéstralo!")

# --- CUESTIONARIO DE MAQUILLAJE ---

with st.container():
    st.markdown('<div class="beauty-card">', unsafe_allow_html=True)
    m1 = st.selectbox("1. ¿Qué producto se aplica para que el maquillaje dure todo el día?", 
                    ["Corrector", "Primer (Prebase)", "Iluminador", "Bronzer"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="beauty-card">', unsafe_allow_html=True)
    m2 = st.radio("2. ¿Para qué sirve el 'Baking' en el maquillaje?", 
                ["Para cocinar", "Para sellar el corrector con polvos traslúcidos", "Para limpiar las brochas", "Para hidratar la piel"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class
