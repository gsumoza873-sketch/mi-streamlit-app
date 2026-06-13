import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Calculadora de Grupos Mundial 2026",
    page_icon="🏆",
    layout="centered"
)

# Estilos visuales oscuros estilo plataforma deportiva
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-grupo { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 20px; border: 1px solid #1e40af; margin-bottom: 25px; }</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Calculadora Real - Fase de Grupos 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Simula los marcadores exactos de los partidos de la FIFA y calcula la tabla de posiciones al instante.</p>", unsafe_allow_html=True)

# 2. Base de Datos Oficial de la FIFA (Grupos y Partidos de la Jornada Inicial)
@st.cache_data
def obtener_datos_mundial():
    return {
        "Grupo A": {
            "equipos": ["México", "Sudáfrica", "Corea del Sur", "Chequia"],
            "partidos": [
                {"p_id": "gA_p1", "loc": "México", "vis": "Sudáfrica"},
                {"p_id": "gA_p2", "loc": "Corea del Sur", "vis": "Chequia"}
            ]
        },
        "Grupo B": {
            "equipos": ["Canadá", "Bosnia y Herzegovina", "Catar", "Suiza"],
            "partidos": [
                {"p_id": "gB_p1", "loc": "Canadá", "vis": "Bosnia y Herzegovina"},
                {"p_id": "gB_p2", "loc": "Catar", "vis": "Suiza"}
            ]
        },
        "Grupo C": {
            "equipos": ["Brasil", "Marruecos", "Haití", "Escocia"],
            "partidos": [
                {"p_id": "gC_p1", "loc": "Brasil", "vis": "Marruecos"},
                {"p_id": "gC_p2", "loc": "Haití", "vis": "Escocia"}
            ]
        },
        "Grupo K (Verdadero Grupo de Colombia)": {
            "equipos": ["Portugal", "Uzbekistán", "Colombia", "RD Congo"],
            "partidos": [
                {"p_id": "gK_p1", "loc": "Portugal", "vis": "RD Congo"},
                {"p_id": "gK_p2", "loc": "Uzbekistán", "vis": "Colombia"}
            ]
        }
    }

datos_mundial = obtener_datos_mundial()

# 3. Selector de Grupo
st.markdown("### 🗂️ Selecciona el Grupo a Calcular")
grupo_seleccionado = st.selectbox("Elige un grupo para gestionar la simulación:", list(datos_mundial.keys()))

info_grupo = datos_mundial[grupo_seleccionado]
lista_equipos = info_grupo["equipos"]
partidos = info_grupo["partidos"]

# 4. Inicializar estructura de puntos en el estado de la sesión
# Diccionario para guardar los goles ingresados por el usuario
if "goles_simulados" not in st.session_state:
    st.session_state.goles_simulados = {}

st.markdown(f"## 📊 Simulador de Resultados: {grupo_seleccionado}")
st.write("Modifica los marcadores de abajo para alterar el orden de la tabla matemática:")

# 5. Formulario de ingreso de marcadores
with st.container():
    st.markdown("<div class='card-grupo'>", unsafe_allow_html=True)
    
    for idx, partido in enumerate(partidos):
        pid = partido["p_id"]
        col_l, col_vs, col_v = st.columns([3, 1, 3])
        
        # Llaves únicas para la persistencia de datos
        key_l = f"goles_l_{pid}"
        key_v = f"goles_v_{pid}"
        
        # Recuperar valores si ya existen en la sesión
        val_l_def = st.session_state.goles_simulados.get(key_l, 0)
        val_v_def = st.session_state.goles_simulados.get(key_v, 0)
        
        with col_l:
            goles_l = st.number_input(f"{partido['loc']}", min_value=0, max_value=15, value=val_l_def, step=1, key=f"input_{key_l}")
        with col_vs:
            st.markdown("<p style='text-align: center; margin-top: 30px; font-weight: bold; color: #64748b;'>VS</p>", unsafe_allow_html=True)
        with col_v:
            goles_v = st.number_input(f"{partido['vis']}", min_value=0, max_value=15, value=val_v_def, step=1, key=f"input_{key_v}")
            
        # Guardar cambios inmediatamente en el diccionario del estado
        st.session_state.goles_simulados[key_l] = goles_l
        st.session_state.goles_simulados[key_v] = goles_v
        
        if idx < len(partidos) - 1:
            st.markdown("<hr style='border-color: #1e293b;' />", unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)

# 6. ALGORITMO MATEMÁTICO: Procesar Tabla de Posiciones
# Inicializamos las métricas vacías para el grupo activo
tabla_calculada = {equipo: {"PTS": 0, "GF": 0, "GC": 0, "DG": 0} for equipo in lista_equipos}

for partido in partidos:
    pid = partido["p_id"]
    gl = st.session_state.goles_simulados.get(f"goles_l_{pid}", 0)
    gv = st.session_state.goles_simulados.get(f"goles_v_{pid}", 0)
    
    loc = partido["loc"]
    vis = partido["vis"]
    
    # Sumar goles a favor y en contra
    tabla_calculada[loc]["GF"] += gl
    tabla_calculada[loc]["GC"] += gv
    tabla_calculada[vis]["GF"] += gv
    tabla_calculada[vis]["GC"] += gl
    
    # Calcular puntos y lógica del resultado
    if gl > gv:
        tabla_calculada[loc]["PTS"] += 3
    elif gv > gl:
        tabla_calculada[vis]["PTS"] += 3
    else:
        tabla_calculada[loc]["PTS"] += 1
        tabla_calculada[vis]["PTS"] += 1

# Calcular Diferencia de Goles (DG = GF - GC)
for equipo in tabla_calculada:
    tabla_calculada[equipo]["DG"] = tabla_calculada[equipo]["GF"] - tabla_calculada[equipo]["GC"]

# Convertir a lista y ordenar por Puntos, luego por Diferencia de Goles, y luego por Goles a Favor
tabla_ordenada = sorted(
    tabla_calculada.items(),
    key=lambda x: (x[1]["PTS"], x[1]["DG"], x[1]["GF"]),
    reverse=True
)

# 7. Desplegar la Tabla de Posiciones resultante en Interfaz Limpia
st.markdown("### 📋 Clasificación del Grupo en Tiempo Real")
st.write("El orden se reestructura de forma matemática según tus predicciones de arriba:")

# Construcción de la tabla usando Markdown estándar para evitar bugs de recarga
md_tabla = "| Pos | Selección | PTS | GF | GC | DG |\n| :---: | :--- | :---: | :---: | :---: | :---: |\n"
for i, (equipo, stats) in enumerate(tabla_ordenada):
    medalla = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "❌"
    md_tabla += f"| {medalla} {i+1} | **{equipo}** | **{stats['PTS']}** | {stats['GF']} | {stats['GC']} | {stats['DG']} |\n"

st.markdown(md_tabla)

st.write("---")
st.caption("⚡ FIFA World Cup 2026 Core Engine • Datos Oficiales • Hecho por Gabriel.s")
    
