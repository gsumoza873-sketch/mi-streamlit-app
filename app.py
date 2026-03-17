import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Misión Secreta: El Enigma", page_icon="🕵️‍♂️", layout="centered")

# Estilo visual tipo Hacker/Misterio
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00FF00; /* Verde tipo Matrix */
        font-family: 'Courier New', Courier, monospace;
    }
    .stRadio > div {
        background-color: #111111;
        padding: 15px;
        border: 1px solid #00FF00;
        border-radius: 10px;
    }
    .pista-box {
        background-color: #002200;
        padding: 10px;
        border-left: 5px solid #00FF00;
        margin-top: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️‍♂️ EXPEDIENTE X: MANUEL")
st.write("### Resuelve los acertijos para desbloquear la verdad oculta...")

# --- LÓGICA DE LOS ACERTIJOS ---

# Acertijo 1
st.write("---")
st.subheader("Nivel 1: El Objeto")
a1 = st.radio("Soy algo que se rompe antes de usarse, ¿qué soy?", 
              ["Una piedra", "Un huevo", "Una promesa", "Un cristal"], key="a1")

if a1 == "Un huevo":
    st.markdown('<div class="pista-box">🔓 PISTA 1: A Manuel le gusta...</div>', unsafe_allow_html=True)
else:
    st.write("❌ Bloqueado: Respuesta incorrecta")

# Acertijo 2
st.write("---")
st.subheader("Nivel 2: La Acción")
a2 = st.radio("Si me tienes, quieres compartirme. Si me compartes, ya no me tienes. ¿Qué soy?", 
              ["Dinero", "Un secreto", "Comida", "Un bostezo"], key="a2")

if a2 == "Un secreto":
    st.markdown('<div class="pista-box">🔓 PISTA 2: ...mucho el brillo y...</div>', unsafe_allow_html=True)
else:
    st.write("❌ Bloqueado: Pista oculta")

# Acertijo 3
st.write("---")
st.subheader("Nivel 3: El Destino")
a3 = st.radio("Vuelo sin alas, lloro sin ojos. ¿Qué soy?", 
              ["Un fantasma", "El viento", "Una nube", "Un pensamiento"], key="a3")

if a3 == "Una nube":
    st.markdown('<div class="pista-box">🔓 PISTA 3: ...la compañía masculina.</div>', unsafe_allow_html=True)
else:
    st.write("❌ Bloqueado: Sigue intentando")

st.write("---")

# --- REVELACIÓN FINAL ---
if st.button("🔓 DESBLOQUEAR ARCHIVO FINAL"):
    if a1 == "Un huevo" and a2 == "Un secreto" and a3 == "Una nube":
        st.balloons()
        st.error("⚠️ ARCHIVO DESBLOQUEADO ⚠️")
        st.markdown("""
            <h1 style='text-align: center; color: #ff00ff; font-size: 50px;'>
            🌈 ¡CONFIRMADO! 🌈
            </h1>
            <h2 style='text-align: center; color: white;'>
            Manuel es 100% GAY.
            </h2>
            <p style='text-align: center;'>No hay dudas en el sistema.</p>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ ACCESO DENEGADO: Debes resolver todos los acertijos correctamente para ver la verdad.")

# Firma
st.sidebar.write("Investigación liderada por:")
st.sidebar.info(f"**Agente Gabriel**")
