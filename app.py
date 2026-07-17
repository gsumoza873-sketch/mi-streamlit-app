import streamlit as st
import random
import time

# 1. Configuración de la pantalla
st.set_page_config(
    page_title="Penalty Shootout Pro",
    page_icon="⚽",
    layout="centered"
)

# Estilos oscuros deportivos
st.markdown("<style>.stApp { background-color: #050b14; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.marcador { background: linear-gradient(135deg, #1e293b, #0f172a); border-radius: 15px; padding: 15px; text-align: center; border: 1px solid #3b82f6; margin-bottom: 20px; }</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>⚽ Penalty Shootout Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Enfréntate al arquero controlado por la IA. ¡Elige tu dirección y dispara!</p>", unsafe_allow_html=True)

# 2. Inicializar variables del juego en memoria
if "goles" not in st.session_state: st.session_state.goles = 0
if "atajadas" not in st.session_state: st.session_state.atajadas = 0
if "tiros" not in st.session_state: st.session_state.tiros = 0
if "historial" not in st.session_state: st.session_state.historial = []

# Reiniciar juego
def reiniciar():
    st.session_state.goles = 0
    st.session_state.atajadas = 0
    st.session_state.tiros = 0
    st.session_state.historial = []

# 3. Marcador en pantalla
st.markdown(
    f"""
    <div class='marcador'>
        <span style='font-size: 24px; font-weight: bold;'>🏆 MARCADOR</span><br>
        <span style='font-size: 40px; color: #4ade80;'>{st.session_state.goles} Goles</span> 
        <span style='font-size: 30px; color: #64748b;'> vs </span> 
        <span style='font-size: 40px; color: #f87171;'>{st.session_state.atajadas} Atajadas</span><br>
        <span style='color: #94a3b8;'>Intentos totales: {st.session_state.tiros}</span>
    </div>
    """, 
    unsafe_allow_html=True
)

# 4. Mecánica de juego: Elección del disparo
st.markdown("### 🎯 ¿Hacia dónde vas a patear?")
col1, col2, col3 = st.columns(3)

direccion_disparo = None

with col1:
    if st.button("⬅️ Izquierda", use_container_width=True):
        direccion_disparo = "Izquierda"
with col2:
    if st.button("⬆️ Centro", use_container_width=True):
        direccion_disparo = "Centro"
with col3:
    if st.button("➡️ Derecha", use_container_width=True):
        direccion_disparo = "Derecha"

# 5. Lógica del arquero (IA) cuando disparas
if direccion_disparo:
    st.session_state.tiros += 1
    opciones_arquero = ["Izquierda", "Centro", "Derecha"]
    # El arquero tiene 80% de probabilidad de lanzarse bien o mal
    direccion_arquero = random.choice(opciones_arquero)
    
    st.write(f"🏃‍♂️ Pateas hacia la **{direccion_disparo}**...")
    with st.spinner("¡El arquero se lanza!..."):
        time.sleep(0.8)  # Pequeño delay para darle drama
    
    if direccion_disparo == direccion_arquero:
        st.error(f"🧤 ¡ATAJADA! El arquero se lanzó a la {direccion_arquero} y te lo tapó.")
        st.session_state.atajadas += 1
        st.session_state.historial.insert(0, "❌ Atajado")
    else:
        st.success(f"🔥 ¡GOOOOL! El arquero se tiró a la {direccion_arquero} y el balón entró.")
        st.session_state.goles += 1
        st.session_state.historial.insert(0, "⚽ Gol")

# 6. Barra lateral con Historial y Reset
with st.sidebar:
    st.markdown("### ⚙️ Opciones")
    if st.button("Resetear Partida", on_click=reiniciar):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📜 Últimos Tiros")
    for tiro in st.session_state.historial[:5]:
        st.write(tiro)

# Pie de página con tu firma
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.2 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
