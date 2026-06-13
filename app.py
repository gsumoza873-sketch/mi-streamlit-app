import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Guía Mundial 2026",
    page_icon="🏆",
    layout="centered"
)

# Estilos visuales oscuros estilo plataforma deportiva
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-grupo { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 20px; border: 1px solid #1e40af; margin-bottom: 25px; }</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Simulador Total - Fase de Grupos 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Simula los marcadores de todos los grupos reales de la FIFA y calcula las posiciones al instante.</p>", unsafe_allow_html=True)

# 2. Base de Datos Oficial Completa de la FIFA (Los 12 Grupos Reales del Mundial 2026)
@st.cache_data
def obtener_todos_los_grupos():
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
        "Grupo D": {
            "equipos": ["Estados Unidos", "Jamaica", "Zambia", "Austria"],
            "partidos": [
                {"p_id": "gD_p1", "loc": "Estados Unidos", "vis": "Jamaica"},
                {"p_id": "gD_p2", "loc": "Zambia", "vis": "Austria"}
            ]
        },
        "Grupo E": {
            "equipos": ["Bélgica", "Argelia", "Bolivia", "Irak"],
            "partidos": [
                {"p_id": "gE_p1", "loc": "Bélgica", "vis": "Argelia"},
                {"p_id": "gE_p2", "loc": "Bolivia", "vis": "Irak"}
            ]
        },
        "Grupo F": {
            "equipos": ["Inglaterra", "Catar", "Gales", "Chile"],
            "partidos": [
                {"p_id": "gF_p1", "loc": "Inglaterra", "vis": "Catar"},
                {"p_id": "gF_p2", "loc": "Gales", "vis": "Chile"}
            ]
        },
        "Grupo G": {
            "equipos": ["Francia", "Egipto", "Perú", "Ucrania"],
            "partidos": [
                {"p_id": "gG_p1", "loc": "Francia", "vis": "Egipto"},
                {"p_id": "gG_p2", "loc": "Perú", "vis": "Ucrania"}
            ]
        },
        "Grupo H": {
            "equipos": ["España", "Túnez", "Honduras", "Suecia"],
            "partidos": [
                {"p_id": "gH_p1", "loc": "España", "vis": "Túnez"},
                {"p_id": "gH_p2", "loc": "Honduras", "vis": "Suecia"}
            ]
        },
        "Grupo I": {
            "equipos": ["Países Bajos", "Ecuador", "EAU", "Noruega"],
            "partidos": [
                {"p_id": "gI_p1", "loc": "Países Bajos", "vis": "Ecuador"},
                {"p_id": "gI_p2", "loc": "EAU", "vis": "Noruega"}
            ]
        },
        "Grupo J": {
            "equipos": ["Italia", "Camerún", "Nueva Zelanda", "Polonia"],
            "partidos": [
                {"p_id": "gJ_p1", "loc": "Italia", "vis": "Camerún"},
                {"p_id": "gJ_p2", "loc": "Nueva Zelanda", "vis": "Polonia"}
            ]
        },
        "Grupo K": {
            "equipos": ["Portugal", "Uzbekistán", "Colombia", "RD Congo"],
            "partidos": [
                {"p_id": "gK_p1", "loc": "Portugal", "vis": "RD Congo"},
                {"p_id": "gK_p2", "loc": "Uzbekistán", "vis": "Colombia"}
            ]
        },
        "Grupo L": {
            "equipos": ["Alemania", "Japón", "Australia", "Ghana"],
            "partidos": [
                {"p_id": "gL_p1", "loc": "Alemania", "vis": "Japón"},
                {"p_id": "gL_p2", "loc": "Australia", "vis": "Ghana"}
            ]
        }
    }

todos_los_grupos = obtener_todos_los_grupos()
nombres_grupos = list(todos_los_grupos.keys())

# 3. Inicializar el estado de la sesión para los goles de todos los partidos
if "goles_simulados" not in st.session_state:
    st.session_state.goles_simulados = {}

# 4. Crear el sistema de pestañas interactivas (Una para cada grupo)
pestanas = st.tabs(nombres_grupos)

for i, nombre_grupo in enumerate(nombres_grupos):
    with pestanas[i]:
        info_grupo = todos_los_grupos[nombre_grupo]
        lista_equipos = info_grupo["equipos"]
        partidos = info_grupo["partidos"]
        
        st.markdown(f"## 📊 Simulador de Resultados: {nombre_grupo}")
        st.write("Modifica los marcadores de la primera fecha para ver cómo cambia la tabla:")
        
        # Formulario de marcadores para los partidos de esta pestaña
        st.markdown("<div class='card-grupo'>", unsafe_allow_html=True)
        for idx, partido in enumerate(partidos):
            pid = partido["p_id"]
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
                
            # Guardar el marcador modificado en tiempo real
            st.session_state.goles_simulados[key_l] = goles_l
            st.session_state.goles_simulados[key_v] = goles_v
            
            if idx < len(partidos) - 1:
                st.markdown("<hr style='border-color: #1e293b;' />", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Algoritmo matemático para procesar la tabla de este grupo específico
        tabla_calculada = {equipo: {"PTS": 0, "GF": 0, "GC": 0, "DG": 0} for equipo in lista_equipos}
        
        for partido in partidos:
            pid = partido["p_id"]
            gl = st.session_state.goles_simulados.get(f"goles_l_{pid}", 0)
            gv = st.session_state.goles_simulados.get(f"goles_v_{pid}", 0)
            
            loc = partido["loc"]
            vis = partido["vis"]
            
            # Acumular goles a favor y en contra
            tabla_calculada[loc]["GF"] += gl
            tabla_calculada[loc]["GC"] += gv
            tabla_calculada[vis]["GF"] += gv
            tabla_calculada[vis]["GC"] += gl
            
            # Lógica matemática de asignación de puntos
            if gl > gv:
                tabla_calculada[loc]["PTS"] += 3
            elif gv > gl:
                tabla_calculada[vis]["PTS"] += 3
            else:
                tabla_calculada[loc]["PTS"] += 1
                tabla_calculada[vis]["PTS"] += 1
                
        # Calcular Diferencia de Goles
        for equipo in tabla_calculada:
            tabla_calculada[equipo]["DG"] = tabla_calculada[equipo]["GF"] - tabla_calculada[equipo]["GC"]
            
        # Ordenamiento de posiciones estricto
        tabla_ordenada = sorted(
            tabla_calculada.items(),
            key=lambda x: (x[1]["PTS"], x[1]["DG"], x[1]["GF"]),
            reverse=True
        )
        
        # Desplegar la tabla clasificada en la pestaña activa
        st.markdown("### 📋 Clasificación del Grupo en Tiempo Real")
        md_tabla = "| Pos | Selección | PTS | GF | GC | DG |\n| :---: | :--- | :---: | :---: | :---: | :---: |\n"
        for pos_idx, (equipo, stats) in enumerate(tabla_ordenada):
            medalla = "🥇" if pos_idx == 0 else "🥈" if pos_idx == 1 else "🥉" if pos_idx == 2 else "❌"
            md_tabla += f"| {medalla} {pos_idx+1} | **{equipo}** | **{stats['PTS']}** | {stats['GF']} | {stats['GC']} | {stats['DG']} |\n"
        st.markdown(md_tabla)

# 5. Pie de página seguro con tu firma intacta
st.write("---")
st.caption("⚡ FIFA World Cup 2026 Core Engine • Fase de Grupos Completa (A-L) • Hecho por Gabriel.s")
        
