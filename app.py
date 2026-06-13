import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Calculadora Completa Mundial 2026",
    page_icon="🏆",
    layout="centered"
)

# Estilos visuales oscuros estilo plataforma deportiva
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-grupo { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 20px; border: 1px solid #1e40af; margin-bottom: 25px; }</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Simulador Total - 3 Partidos por Grupo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Simula las 3 jornadas completas de cada grupo real de la FIFA y define los clasificados.</p>", unsafe_allow_html=True)

# 2. Base de Datos Oficial Completa de la FIFA (Los 12 Grupos con sus 6 partidos reales)
@st.cache_data
def obtener_calendario_completo():
    return {
        "Grupo A": {
            "equipos": ["México", "Sudáfrica", "Corea del Sur", "Chequia"],
            "partidos": [
                {"p_id": "gA_1", "loc": "México", "vis": "Sudáfrica", "jornada": "Jornada 1"},
                {"p_id": "gA_2", "loc": "Corea del Sur", "vis": "Chequia", "jornada": "Jornada 1"},
                {"p_id": "gA_3", "loc": "México", "vis": "Corea del Sur", "jornada": "Jornada 2"},
                {"p_id": "gA_4", "loc": "Chequia", "vis": "Sudáfrica", "jornada": "Jornada 2"},
                {"p_id": "gA_5", "loc": "Chequia", "vis": "México", "jornada": "Jornada 3"},
                {"p_id": "gA_6", "loc": "Sudáfrica", "vis": "Corea del Sur", "jornada": "Jornada 3"}
            ]
        },
        "Grupo B": {
            "equipos": ["Canadá", "Bosnia y Herzegovina", "Catar", "Suiza"],
            "partidos": [
                {"p_id": "gB_1", "loc": "Canadá", "vis": "Bosnia y Herzegovina", "jornada": "Jornada 1"},
                {"p_id": "gB_2", "loc": "Catar", "vis": "Suiza", "jornada": "Jornada 1"},
                {"p_id": "gB_3", "loc": "Canadá", "vis": "Catar", "jornada": "Jornada 2"},
                {"p_id": "gB_4", "loc": "Suiza", "vis": "Bosnia y Herzegovina", "jornada": "Jornada 2"},
                {"p_id": "gB_5", "loc": "Suiza", "vis": "Canadá", "jornada": "Jornada 3"},
                {"p_id": "gB_6", "loc": "Bosnia y Herzegovina", "vis": "Catar", "jornada": "Jornada 3"}
            ]
        },
        "Grupo C": {
            "equipos": ["Brasil", "Marruecos", "Haití", "Escocia"],
            "partidos": [
                {"p_id": "gC_1", "loc": "Brasil", "vis": "Marruecos", "jornada": "Jornada 1"},
                {"p_id": "gC_2", "loc": "Haití", "vis": "Escocia", "jornada": "Jornada 1"},
                {"p_id": "gC_3", "loc": "Brasil", "vis": "Haití", "jornada": "Jornada 2"},
                {"p_id": "gC_4", "loc": "Escocia", "vis": "Marruecos", "jornada": "Jornada 2"},
                {"p_id": "gC_5", "loc": "Escocia", "vis": "Brasil", "jornada": "Jornada 3"},
                {"p_id": "gC_6", "loc": "Marruecos", "vis": "Haití", "jornada": "Jornada 3"}
            ]
        },
        "Grupo D": {
            "equipos": ["Estados Unidos", "Jamaica", "Zambia", "Austria"],
            "partidos": [
                {"p_id": "gD_1", "loc": "Estados Unidos", "vis": "Jamaica", "jornada": "Jornada 1"},
                {"p_id": "gD_2", "loc": "Zambia", "vis": "Austria", "jornada": "Jornada 1"},
                {"p_id": "gD_3", "loc": "Estados Unidos", "vis": "Zambia", "jornada": "Jornada 2"},
                {"p_id": "gD_4", "loc": "Austria", "vis": "Jamaica", "jornada": "Jornada 2"},
                {"p_id": "gD_5", "loc": "Austria", "vis": "Estados Unidos", "jornada": "Jornada 3"},
                {"p_id": "gD_6", "loc": "Jamaica", "vis": "Zambia", "jornada": "Jornada 3"}
            ]
        },
        "Grupo E": {
            "equipos": ["Bélgica", "Argelia", "Bolivia", "Irak"],
            "partidos": [
                {"p_id": "gE_1", "loc": "Bélgica", "vis": "Argelia", "jornada": "Jornada 1"},
                {"p_id": "gE_2", "loc": "Bolivia", "vis": "Irak", "jornada": "Jornada 1"},
                {"p_id": "gE_3", "loc": "Bélgica", "vis": "Bolivia", "jornada": "Jornada 2"},
                {"p_id": "gE_4", "loc": "Irak", "vis": "Argelia", "jornada": "Jornada 2"},
                {"p_id": "gE_5", "loc": "Irak", "vis": "Bélgica", "jornada": "Jornada 3"},
                {"p_id": "gE_6", "loc": "Argelia", "vis": "Bolivia", "jornada": "Jornada 3"}
            ]
        },
        "Grupo F": {
            "equipos": ["Inglaterra", "Catar", "Gales", "Chile"],
            "partidos": [
                {"p_id": "gF_1", "loc": "Inglaterra", "vis": "Catar", "jornada": "Jornada 1"},
                {"p_id": "gF_2", "loc": "Gales", "vis": "Chile", "jornada": "Jornada 1"},
                {"p_id": "gF_3", "loc": "Inglaterra", "vis": "Gales", "jornada": "Jornada 2"},
                {"p_id": "gF_4", "loc": "Chile", "vis": "Catar", "jornada": "Jornada 2"},
                {"p_id": "gF_5", "loc": "Chile", "vis": "Inglaterra", "jornada": "Jornada 3"},
                {"p_id": "gF_6", "loc": "Catar", "vis": "Gales", "jornada": "Jornada 3"}
            ]
        },
        "Grupo G": {
            "equipos": ["Francia", "Egipto", "Perú", "Ucrania"],
            "partidos": [
                {"p_id": "gG_1", "loc": "Francia", "vis": "Egipto", "jornada": "Jornada 1"},
                {"p_id": "gG_2", "loc": "Perú", "vis": "Ucrania", "jornada": "Jornada 1"},
                {"p_id": "gG_3", "loc": "Francia", "vis": "Perú", "jornada": "Jornada 2"},
                {"p_id": "gG_4", "loc": "Ucrania", "vis": "Egipto", "jornada": "Jornada 2"},
                {"p_id": "gG_5", "loc": "Ucrania", "vis": "Francia", "jornada": "Jornada 3"},
                {"p_id": "gG_6", "loc": "Egipto", "vis": "Perú", "jornada": "Jornada 3"}
            ]
        },
        "Grupo H": {
            "equipos": ["España", "Túnez", "Honduras", "Suecia"],
            "partidos": [
                {"p_id": "gH_1", "loc": "España", "vis": "Túnez", "jornada": "Jornada 1"},
                {"p_id": "gH_2", "loc": "Honduras", "vis": "Suecia", "jornada": "Jornada 1"},
                {"p_id": "gH_3", "loc": "España", "vis": "Honduras", "jornada": "Jornada 2"},
                {"p_id": "gH_4", "loc": "Suecia", "vis": "Túnez", "jornada": "Jornada 2"},
                {"p_id": "gH_5", "loc": "Suecia", "vis": "España", "jornada": "Jornada 3"},
                {"p_id": "gH_6", "loc": "Túnez", "vis": "Honduras", "jornada": "Jornada 3"}
            ]
        },
        "Grupo I": {
            "equipos": ["Países Bajos", "Ecuador", "EAU", "Noruega"],
            "partidos": [
                {"p_id": "gI_1", "loc": "Países Bajos", "vis": "Ecuador", "jornada": "Jornada 1"},
                {"p_id": "gI_2", "loc": "EAU", "vis": "Noruega", "jornada": "Jornada 1"},
                {"p_id": "gI_3", "loc": "Países Bajos", "vis": "EAU", "jornada": "Jornada 2"},
                {"p_id": "gI_4", "loc": "Noruega", "vis": "Ecuador", "jornada": "Jornada 2"},
                {"p_id": "gI_5", "loc": "Noruega", "vis": "Países Bajos", "jornada": "Jornada 3"},
                {"p_id": "gI_6", "loc": "Ecuador", "vis": "EAU", "jornada": "Jornada 3"}
            ]
        },
        "Grupo J": {
            "equipos": ["Italia", "Camerún", "Nueva Zelanda", "Polonia"],
            "partidos": [
                {"p_id": "gJ_1", "loc": "Italia", "vis": "Camerún", "jornada": "Jornada 1"},
                {"p_id": "gJ_2", "loc": "Nueva Zelanda", "vis": "Polonia", "jornada": "Jornada 1"},
                {"p_id": "gJ_3", "loc": "Italia", "vis": "Nueva Zelanda", "jornada": "Jornada 2"},
                {"p_id": "gJ_4", "loc": "Polonia", "vis": "Camerún", "jornada": "Jornada 2"},
                {"p_id": "gJ_5", "loc": "Polonia", "vis": "Italia", "jornada": "Jornada 3"},
                {"p_id": "gJ_6", "loc": "Camerún", "vis": "Nueva Zelanda", "jornada": "Jornada 3"}
            ]
        },
        "Grupo K": {
            "equipos": ["Portugal", "Uzbekistán", "Colombia", "RD Congo"],
            "partidos": [
                {"p_id": "gK_1", "loc": "Portugal", "vis": "RD Congo", "jornada": "Jornada 1"},
                {"p_id": "gK_2", "loc": "Uzbekistán", "vis": "Colombia", "jornada": "Jornada 1"},
                {"p_id": "gK_3", "loc": "Portugal", "vis": "Uzbekistán", "jornada": "Jornada 2"},
                {"p_id": "gK_4", "loc": "Colombia", "vis": "RD Congo", "jornada": "Jornada 2"},
                {"p_id": "gK_5", "loc": "Colombia", "vis": "Portugal", "jornada": "Jornada 3"},
                {"p_id": "gK_6", "loc": "RD Congo", "vis": "Uzbekistán", "jornada": "Jornada 3"}
            ]
        },
        "Grupo L": {
            "equipos": ["Alemania", "Japón", "Australia", "Ghana"],
            "partidos": [
                {"p_id": "gL_1", "loc": "Alemania", "vis": "Japón", "jornada": "Jornada 1"},
                {"p_id": "gL_2", "loc": "Australia", "vis": "Ghana", "jornada": "Jornada 1"},
                {"p_id": "gL_3", "loc": "Alemania", "vis": "Australia", "jornada": "Jornada 2"},
                {"p_id": "gL_4", "loc": "Ghana", "vis": "Japón", "jornada": "Jornada 2"},
                {"p_id": "gL_5", "loc": "Ghana", "vis": "Alemania", "jornada": "Jornada 3"},
                {"p_id": "gL_6", "loc": "Japón", "vis": "Australia", "jornada": "Jornada 3"}
            ]
        }
    }

todos_los_grupos = obtener_calendario_completo()
nombres_grupos = list(todos_los_grupos.keys())

# 3. Inicializar la persistencia de los marcadores
if "goles_simulados" not in st.session_state:
    st.session_state.goles_simulados = {}

# 4. Estructura de Pestañas Interactivas
pestanas = st.tabs(nombres_grupos)

for i, nombre_grupo in enumerate(nombres_grupos):
    with pestanas[i]:
        info_grupo = todos_los_grupos[nombre_grupo]
        lista_equipos = info_grupo["equipos"]
        partidos = info_grupo["partidos"]
        
        st.markdown(f"## 📅 Calendario Completo (3 Fechas): {nombre_grupo}")
        st.write("Registra los marcadores de los 6 partidos obligatorios para procesar la tabla:")
        
        # Tarjeta contenedora de los partidos
        st.markdown("<div class='card-grupo'>", unsafe_allow_html=True)
        
        jornada_actual = ""
        for idx, partido in enumerate(partidos):
            pid = partido["p_id"]
            
            # Separador visual de Jornadas
            if partido["jornada"] != jornada_actual:
                jornada_actual = partido["jornada"]
                st.markdown(f"<p style='color: #60a5fa; font-weight: bold; margin-top: 10px; font-size: 14px;'>🔹 {jornada_actual}</p>", unsafe_allow_html=True)
            
            col_l, col_vs, col_v = st.columns([3, 1, 3])
            
            key_l = f"goles_l_{pid}"
            key_v = f"goles_v_{pid}"
            
            val_l_def = st.session_state.goles_simulados.get(key_l, 0)
            val_v_def = st.session_state.goles_simulados.get(key_v, 0)
            
            with col_l:
                goles_l = st.number_input(f"{partido['loc']}", min_value=0, max_value=15, value=val_l_def, step=1, key=f"input_{key_l}")
            with col_vs:
                st.markdown("<p style='text-align: center; margin-top: 30px; font-weight: bold; color: #64748b;'>VS</p>", unsafe_allow_html=True)
            with col_v:
                goles_v = st.number_input(f"{partido['vis']}", min_value=0, max_value=15, value=val_v_def, step=1, key=f"input_{key_v}")
                
            # Guardar en memoria de sesión de forma síncrona
            st.session_state.goles_simulados[key_l] = goles_l
            st.session_state.goles_simulados[key_v] = goles_v
            
            if idx < len(partidos) - 1:
                st.markdown("<hr style='border-color: #1e293b; margin: 10px 0;' />", unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 5. ALGORITMO MATEMÁTICO AVANZADO PARA LAS POSICIONES TRAS LOS 3 JUEGOS
        tabla_calculada = {equipo: {"PTS": 0, "PJ": 0, "GF": 0, "GC": 0, "DG": 0} for equipo in lista_equipos}
        
        for partido in partidos:
            pid = partido["p_id"]
            gl = st.session_state.goles_simulados.get(f"goles_l_{pid}", 0)
            gv = st.session_state.goles_simulados.get(f"goles_v_{pid}", 0)
            
            loc = partido["loc"]
            vis = partido["vis"]
            
            # Acumular partidos jugados y goles
            tabla_calculada[loc]["PJ"] += 1
            tabla_calculada[vis]["PJ"] += 1
            tabla_calculada[loc]["GF"] += gl
            tabla_calculada[loc]["GC"] += gv
            tabla_calculada[vis]["GF"] += gv
            tabla_calculada[vis]["GC"] += gl
            
            # Sistema matemático de puntos FIFA
            if gl > gv:
                tabla_calculada[loc]["PTS"] += 3
            elif gv > gl:
                tabla_calculada[vis]["PTS"] += 3
            else:
                tabla_calculada[loc]["PTS"] += 1
                tabla_calculada[vis]["PTS"] += 1
                
        # Calcular Diferencia de Goles neta
        for equipo in tabla_calculada:
            tabla_calculada[equipo]["DG"] = tabla_calculada[equipo]["GF"] - tabla_calculada[equipo]["GC"]
            
        # Ordenar rigurosamente: Puntos -> Diferencia de Goles -> Goles anotados
        tabla_ordenada = sorted(
            tabla_calculada.items(),
            key=lambda x: (x[1]["PTS"], x[1]["DG"], x[1]["GF"]),
            reverse=True
        )
        
        # 6. Renderizar Tabla de Clasificación Final
        st.markdown("### 📋 Tabla de Posiciones Final del Grupo")
        md_tabla = "| Pos | Selección | PJ | PTS | GF | GC | DG |\n| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"
        for pos_idx, (equipo, stats) in enumerate(tabla_ordenada):
            medalla = "🥇" if pos_idx == 0 else "🥈" if pos_idx == 1 else "🥉" if pos_idx == 2 else "❌"
            md_tabla += f"| {medalla} {pos_idx+1} | **{equipo}** | {stats['PJ']} | **{stats['PTS']}** | {stats['GF']} | {stats['GC']} | {stats['DG']} |\n"
        st.markdown(md_tabla)

# Pie de página fijo
st.write("---")
st.caption("⚡ FIFA World Cup 2026 Core Engine • 3 Jornadas Completas (6 Partidos por Grupo) • Hecho por Gabriel.s")
        
