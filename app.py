import streamlit as st

# 1. Configuración de la página del Mundial
st.set_page_config(
    page_title="Predicciones Mundial 2026",
    page_icon="⚽",
    layout="centered"
)

# 2. Estilos CSS temáticos para el Mundial (Colores oscuros y detalles de fútbol)
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-partido { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 15px; margin-bottom: 20px; border: 1px solid #1e40af; box-shadow: 0 4px 10px rgba(30, 64, 175, 0.2); }</style>", unsafe_allow_html=True)
st.markdown("<style>.badge-prob { background-color: #1e3a8a; color: #60a5fa; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }</style>", unsafe_allow_html=True)
st.markdown("<style>.resultado-ok { background-color: #064e3b; border-left: 4px solid #10b981; padding: 10px; border-radius: 6px; margin-top: 10px; }</style>", unsafe_allow_html=True)

# 3. Encabezado de la app
st.markdown("<h1 style='text-align: center; color: #3b82f6; margin-bottom: 5px;'>🏆 Simulador Mundial 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 30px;'>Planifica partidos por continente, analiza probabilidades de la IA y deja tus predicciones en vivo.</p>", unsafe_allow_html=True)

# 4. Inicializar la memoria de predicciones si no existe
if "mis_predicciones" not in st.session_state:
    st.session_state.mis_predicciones = {}

# 5. Base de datos fija de partidos clave por Continente/Confederación
# Incluye probabilidades de victoria calculadas por rendimiento histórico
partidos_mundial = {
    "🌍 África / Europa": {
        "local": "Marruecos",
        "visitante": "Brasil",
        "prob_local": 28,
        "prob_empate": 22,
        "prob_visitante": 50,
        "id": "mar_bra"
    },
    "🌎 Sudamérica (CONMEBOL)": {
        "local": "Colombia",
        "visitante": "Argentina",
        "prob_local": 35,
        "prob_empate": 30,
        "prob_visitante": 45,
        "id": "col_arg"
    },
    "🌎 Norteamérica (CONCACAF)": {
        "local": "México",
        "visitante": "Estados Unidos",
        "prob_local": 42,
        "prob_empate": 28,
        "prob_visitante": 30,
        "id": "mex_usa"
    },
    "🌏 Asia / Europa": {
        "local": "Japón",
        "visitante": "España",
        "prob_local": 25,
        "prob_empate": 25,
        "prob_visitante": 50,
        "id": "jap_esp"
    }
}

# 6. Selector de continentes interactivo
st.markdown("### 🗺️ Selecciona el Continente / Zona del Partido")
continente_elegido = st.selectbox(
    "Elige una zona geográfica para desplegar los partidos agendados:",
    options=list(partidos_mundial.keys())
)

# 7. Cargar datos del partido seleccionado
datos_partido = partidos_mundial[continente_elegido]
loc = datos_partido["local"]
vis = datos_partido["visitante"]
p_id = datos_partido["id"]

# 8. Render de la tarjeta del partido con barra de probabilidades de la IA
st.markdown(f"""
<div class="card-partido">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <span style="color: #94a3b8; font-size: 13px; font-weight: bold;">Fase de Grupos • Programación Oficial</span>
        <span class="badge-prob">Análisis de Probabilidad IA</span>
    </div>
    <h3 style="text-align: center; margin: 15px 0; color: #ffffff; font-size: 22px;">⚽ {loc} vs {vis} ⚽</h3>
    <p style="margin-bottom: 5px; font-size: 14px; color: #cbd5e1; text-align: center;">📈 <b>Probabilidades de victoria:</b></p>
    <div style="display: flex; justify-content: space-around; text-align: center; background-color: #0b1329; padding: 10px; border-radius: 8px;">
        <div><b style="color: #60a5fa;">{loc}:</b> {datos_partido['prob_local']}%</div>
        <div><b style="color: #94a3b8;">Empate:</b> {datos_partido['prob_empate']}%</div>
        <div><b style="color: #f43f5e;">{vis}:</b> {datos_partido['prob_visitante']}%</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 9. Zona Interactiva de Predicciones del Usuario
st.markdown("### 🔮 Tu Panel de Predicción")
st.write(f"Introduce abajo el marcador exacto que crees que va a quedar en el partido de **{loc} vs {vis}**:")

col_loc, col_vs, col_vis = st.columns([2, 1, 2])

# Recuperar valores guardados si el usuario ya había predicho este partido
goles_loc_default = st.session_state.mis_predicciones.get(f"{p_id}_l", 0)
goles_vis_default = st.session_state.mis_predicciones.get(f"{p_id}_v", 0)

with col_loc:
    goles_local = st.number_input(f"Goles de {loc}:", min_value=0, max_value=20, value=goles_loc_default, step=1, key=f"num_l_{p_id}")

with col_vs:
    st.markdown("<h3 style='text-align: center; margin-top: 25px; color: #64748b;'>VS</h3>", unsafe_allow_html=True)

with col_vis:
    goles_visita = st.number_input(f"Goles de {vis}:", min_value=0, max_value=20, value=goles_vis_default, step=1, key=f"num_v_{p_id}")

# Botón para guardar la predicción de forma permanente
if st.button("💾 Guardar mi predicción en el boleto"):
    st.session_state.mis_predicciones[f"{p_id}_l"] = goles_local
    st.session_state.mis_predicciones[f"{p_id}_v"] = goles_visita
    st.success(f"¡Predicción guardada con éxito para el partido de {loc} vs {vis}!")

# 10. Mostrar el ticket o resumen de la predicción en pantalla si existe
if f"{p_id}_l" in st.session_state.mis_predicciones:
    pred_l = st.session_state.mis_predicciones[f"{p_id}_l"]
    pred_v = st.session_state.mis_predicciones[f"{p_id}_v"]
    
    # Determinar quién gana según el usuario para poner un texto dinámico
    if pred_l > pred_v:
        ganador_texto = f"Tu predicción dicta que **gana {loc}** por diferencia de goles."
    elif pred_v > pred_l:
        ganador_texto = f"Tu predicción dicta que **gana {vis}** por diferencia de goles."
    else:
        ganador_texto = "Tu predicción dicta un **empate cerrado** en el marcador."

    st.markdown(f"""
    <div class="resultado-ok">
        <span style="color: #34d399; font-weight: bold; font-size: 15px;">📝 Tu Boleto de Predicción Activo:</span><br>
        <p style="margin: 5px 0 0 0; font-size: 14.5px; color: #e2e8f0;">
            Has pronosticado un resultado final de: <b>{loc} {pred_l} - {pred_v} {vis}</b>.<br>
            <i>{ganador_texto}</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Panel inferior interactivo de resumen completo
st.write("---")
with st.expander("📊 Ver todas mis predicciones del Mundial acumuladas"):
    if len(st.session_state.mis_predicciones) == 0:
        st.info("Aún no has guardado ninguna predicción en este navegador.")
    else:
        for cont, info in partidos_mundial.items():
            pid = info["id"]
            if f"{pid}_l" in st.session_state.mis_predicciones:
                st.write(f"• **{info['local']}** {st.session_state.mis_predicciones[f'{pid}_l']} vs {st.session_state.mis_predicciones[f'{pid}_v']} **{info['visitante']}** ({cont})")

# Pie de página con tu firma intacta
st.caption("⚡ World Cup Predictor Engine 2026 • Base de Datos por Continente • Hecho por Gabriel.s")
    
