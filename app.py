import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Simulator de World Cup",
    page_icon="🏆",
    layout="centered"
)

# Estilos visuales oscuros estilo plataforma deportiva
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-grupo { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 20px; border: 1px solid #1e40af; margin-bottom: 25px; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-eliminatoria { background: linear-gradient(145deg, #1e1b4b, #312e81); border-radius: 12px; padding: 15px; border: 1px solid #7c3aed; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

# Título solicitado: Simulator de World Cup
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Simulator de World Cup</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Simula desde la fase de grupos hasta la Gran Final del mundo en un solo lugar.</p>", unsafe_allow_html=True)

# Secciones principales de la App: Grupos y Fase Final
seccion_principal = st.radio("Selecciona la etapa del torneo a gestionar:", ["Fase de Grupos", "Fases Finales (Eliminación Directa)"])

# 2. Base de Datos Oficial (12 Grupos)
@st.cache_data
def obtener_calendario_completo():
    return {
        "Grupo A": {"equipos": ["México", "Sudáfrica", "Corea del Sur", "Chequia"], "partidos": [{"p_id": "gA_1", "loc": "México", "vis": "Sudáfrica", "jornada": "Jornada 1"}, {"p_id": "gA_2", "loc": "Corea del Sur", "vis": "Chequia", "jornada": "Jornada 1"}, {"p_id": "gA_3", "loc": "México", "vis": "Corea del Sur", "jornada": "Jornada 2"}, {"p_id": "gA_4", "loc": "Chequia", "vis": "Sudáfrica", "jornada": "Jornada 2"}, {"p_id": "gA_5", "loc": "Chequia", "vis": "México", "jornada": "Jornada 3"}, {"p_id": "gA_6", "loc": "Sudáfrica", "vis": "Corea del Sur", "jornada": "Jornada 3"}]},
        "Grupo B": {"equipos": ["Canadá", "Bosnia", "Catar", "Suiza"], "partidos": [{"p_id": "gB_1", "loc": "Canadá", "vis": "Bosnia", "jornada": "Jornada 1"}, {"p_id": "gB_2", "loc": "Catar", "vis": "Suiza", "jornada": "Jornada 1"}, {"p_id": "gB_3", "loc": "Canadá", "vis": "Catar", "jornada": "Jornada 2"}, {"p_id": "gB_4", "loc": "Suiza", "vis": "Bosnia", "jornada": "Jornada 2"}, {"p_id": "gB_5", "loc": "Suiza", "vis": "Canadá", "jornada": "Jornada 3"}, {"p_id": "gB_6", "loc": "Bosnia", "vis": "Catar", "jornada": "Jornada 3"}]},
        "Grupo C": {"equipos": ["Brasil", "Marruecos", "Haití", "Escocia"], "partidos": [{"p_id": "gC_1", "loc": "Brasil", "vis": "Marruecos", "jornada": "Jornada 1"}, {"p_id": "gC_2", "loc": "Haití", "vis": "Escocia", "jornada": "Jornada 1"}, {"p_id": "gC_3", "loc": "Brasil", "vis": "Haití", "jornada": "Jornada 2"}, {"p_id": "gC_4", "loc": "Escocia", "vis": "Marruecos", "jornada": "Jornada 2"}, {"p_id": "gC_5", "loc": "Escocia", "vis": "Brasil", "jornada": "Jornada 3"}, {"p_id": "gC_6", "loc": "Marruecos", "vis": "Haití", "jornada": "Jornada 3"}]},
        "Grupo D": {"equipos": ["Estados Unidos", "Jamaica", "Zambia", "Austria"], "partidos": [{"p_id": "gD_1", "loc": "Estados Unidos", "vis": "Jamaica", "jornada": "Jornada 1"}, {"p_id": "gD_2", "loc": "Zambia", "vis": "Austria", "jornada": "Jornada 1"}, {"p_id": "gD_3", "loc": "Estados Unidos", "vis": "Zambia", "jornada": "Jornada 2"}, {"p_id": "gD_4", "loc": "Austria", "vis": "Jamaica", "jornada": "Jornada 2"}, {"p_id": "gD_5", "loc": "Austria", "vis": "Estados Unidos", "jornada": "Jornada 3"}, {"p_id": "gD_6", "loc": "Jamaica", "vis": "Zambia", "jornada": "Jornada 3"}]},
        "Grupo E": {"equipos": ["Bélgica", "Argelia", "Bolivia", "Irak"], "partidos": [{"p_id": "gE_1", "loc": "Bélgica", "vis": "Argelia", "jornada": "Jornada 1"}, {"p_id": "gE_2", "loc": "Bolivia", "vis": "Irak", "jornada": "Jornada 1"}, {"p_id": "gE_3", "loc": "Bélgica", "vis": "Bolivia", "jornada": "Jornada 2"}, {"p_id": "gE_4", "loc": "Irak", "vis": "Argelia", "jornada": "Jornada 2"}, {"p_id": "gE_5", "loc": "Irak", "vis": "Bélgica", "jornada": "Jornada 3"}, {"p_id": "gE_6", "loc": "Argelia", "vis": "Bolivia", "jornada": "Jornada 3"}]},
        "Grupo F": {"equipos": ["Inglaterra", "Catar", "Gales", "Chile"], "partidos": [{"p_id": "gF_1", "loc": "Inglaterra", "vis": "Catar", "jornada": "Jornada 1"}, {"p_id": "gF_2", "loc": "Gales", "vis": "Chile", "jornada": "Jornada 1"}, {"p_id": "gF_3", "loc": "Inglaterra", "vis": "Gales", "jornada": "Jornada 2"}, {"p_id": "gF_4", "loc": "Chile", "vis": "Catar", "jornada": "Jornada 2"}, {"p_id": "gF_5", "loc": "Chile", "vis": "Inglaterra", "jornada": "Jornada 3"}, {"p_id": "gF_6", "loc": "Catar", "vis": "Gales", "jornada": "Jornada 3"}]},
        "Grupo G": {"equipos": ["Francia", "Egipto", "Perú", "Ucrania"], "partidos": [{"p_id": "gG_1", "loc": "Francia", "vis": "Egipto", "jornada": "Jornada 1"}, {"p_id": "gG_2", "loc": "Perú", "vis": "Ucrania", "jornada": "Jornada 1"}, {"p_id": "gG_3", "loc": "Francia", "vis": "Perú", "jornada": "Jornada 2"}, {"p_id": "gG_4", "loc": "Ucrania", "vis": "Egipto", "jornada": "Jornada 2"}, {"p_id": "gG_5", "loc": "Ucrania", "vis": "Francia", "jornada": "Jornada 3"}, {"p_id": "gG_6", "loc": "Egipto", "vis": "Perú", "jornada": "Jornada 3"}]},
        "Grupo H": {"equipos": ["España", "Túnez", "Honduras", "Suecia"], "partidos": [{"p_id": "gH_1", "loc": "España", "vis": "Túnez", "jornada": "Jornada 1"}, {"p_id": "gH_2", "loc": "Honduras", "vis": "Suecia", "jornada": "Jornada 1"}, {"p_id": "gH_3", "loc": "España", "vis": "Honduras", "jornada": "Jornada 2"}, {"p_id": "gH_4", "loc": "Suecia", "vis": "Túnez", "jornada": "Jornada 2"}, {"p_id": "gH_5", "loc": "Suecia", "vis": "España", "jornada": "Jornada 3"}, {"p_id": "gH_6", "loc": "Túnez", "vis": "Honduras", "jornada": "Jornada 3"}]},
        "Grupo I": {"equipos": ["Países Bajos", "Ecuador", "EAU", "Noruega"], "partidos": [{"p_id": "gI_1", "loc": "Países Bajos", "vis": "Ecuador", "jornada": "Jornada 1"}, {"p_id": "gI_2", "loc": "EAU", "vis": "Noruega", "jornada": "Jornada 1"}, {"p_id": "gI_3", "loc": "Países Bajos", "vis": "EAU", "jornada": "Jornada 2"}, {"p_id": "gI_4", "loc": "Noruega", "vis": "Ecuador", "jornada": "Jornada 2"}, {"p_id": "gI_5", "loc": "Noruega", "vis": "Países Bajos", "jornada": "Jornada 3"}, {"p_id": "gI_6", "loc": "Ecuador", "vis": "EAU", "jornada": "Jornada 3"}]},
        "Grupo J": {"equipos": ["Italia", "Camerún", "Nueva Zelanda", "Polonia"], "partidos": [{"p_id": "gJ_1", "loc": "Italia", "vis": "Camerún", "jornada": "Jornada 1"}, {"p_id": "gJ_2", "loc": "Nueva Zelanda", "vis": "Polonia", "jornada": "Jornada 1"}, {"p_id": "gJ_3", "loc": "Italia", "vis": "Nueva Zelanda", "jornada": "Jornada 2"}, {"p_id": "gJ_4", "loc": "Polonia", "vis": "Camerún", "jornada": "Jornada 2"}, {"p_id": "gJ_5", "loc": "Polonia", "vis": "Italia", "jornada": "Jornada 3"}, {"p_id": "gJ_6", "loc": "Camerún", "vis": "Nueva Zelanda", "jornada": "Jornada 3"}]},
        "Grupo K": {"equipos": ["Portugal", "Uzbekistán", "Colombia", "RD Congo"], "partidos": [{"p_id": "gK_1", "loc": "Portugal", "vis": "RD Congo", "jornada": "Jornada 1"}, {"p_id": "gK_2", "loc": "Uzbekistán", "vis": "Colombia", "jornada": "Jornada 1"}, {"p_id": "gK_3", "loc": "Portugal", "vis": "Uzbekistán", "jornada": "Jornada 2"}, {"p_id": "gK_4", "loc": "Colombia", "vis": "RD Congo", "jornada": "Jornada 2"}, {"p_id": "gK_5", "loc": "Colombia", "vis": "Portugal", "jornada": "Jornada 3"}, {"p_id": "gK_6", "loc": "RD Congo", "vis": "Uzbekistán", "jornada": "Jornada 3"}]},
        "Grupo L": {"equipos": ["Alemania", "Japón", "Australia", "Ghana"], "partidos": [{"p_id": "gL_1", "loc": "Alemania", "vis": "Japón", "jornada": "Jornada 1"}, {"p_id": "gL_2", "loc": "Australia", "vis": "Ghana", "jornada": "Jornada 1"}, {"p_id": "gL_3", "loc": "Alemania", "vis": "Australia", "jornada": "Jornada 2"}, {"p_id": "gL_4", "loc": "Ghana", "vis": "Japón", "jornada": "Jornada 2"}, {"p_id": "gL_5", "loc": "Ghana", "vis": "Alemania", "jornada": "Jornada 3"}, {"p_id": "gL_6", "loc": "Japón", "vis": "Australia", "jornada": "Jornada 3"}]}
    }

todos_los_grupos = obtener_calendario_completo()
nombres_grupos = list(todos_los_grupos.keys())

# Inicializar estados de memoria
if "goles_simulados" not in st.session_state: st.session_state.goles_simulados = {}
if "fase_elim" not in st.session_state: st.session_state.fase_elim = {}

# --- BLOQUE 1: FASE DE GRUPOS ---
if seccion_principal == "Fase de Grupos":
    pestanas = st.tabs(nombres_grupos)
    for i, nombre_grupo in enumerate(nombres_grupos):
        with pestanas[i]:
            info_grupo = todos_los_grupos[nombre_grupo]
            lista_equipos = info_grupo["equipos"]
            partidos = info_grupo["partidos"]
            
            st.markdown(f"## 📅 Calendario Completo (3 Fechas): {nombre_grupo}")
            st.markdown("<div class='card-grupo'>", unsafe_allow_html=True)
            
            jornada_actual = ""
            for idx, partido in enumerate(partidos):
                pid = partido["p_id"]
                if partido["jornada"] != jornada_actual:
                    jornada_actual = partido["jornada"]
                    st.markdown(f"<p style='color: #60a5fa; font-weight: bold; margin-top: 10px;'>🔹 {jornada_actual}</p>", unsafe_allow_html=True)
                
                col_l, col_vs, col_v = st.columns([3, 1, 3])
                key_l, key_v = f"goles_l_{pid}", f"goles_v_{pid}"
                
                with col_l: goles_l = st.number_input(f"{partido['loc']}", min_value=0, max_value=15, value=st.session_state.goles_simulados.get(key_l, 0), step=1, key=f"in_{key_l}")
                with col_vs: st.markdown("<p style='text-align: center; margin-top: 30px; color: #64748b;'>VS</p>", unsafe_allow_html=True)
                with col_v: goles_v = st.number_input(f"{partido['vis']}", min_value=0, max_value=15, value=st.session_state.goles_simulados.get(key_v, 0), step=1, key=f"in_{key_v}")
                
                st.session_state.goles_simulados[key_l] = goles_l
                st.session_state.goles_simulados[key_v] = goles_v
                if idx < len(partidos) - 1: st.markdown("<hr style='border-color: #1e293b; margin: 10px 0;' />", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Procesar posiciones
            tabla_calculada = {equipo: {"PTS": 0, "PJ": 0, "GF": 0, "GC": 0, "DG": 0} for equipo in lista_equipos}
            for partido in partidos:
                pid = partido["p_id"]
                gl = st.session_state.goles_simulados.get(f"goles_l_{pid}", 0)
                gv = st.session_state.goles_simulados.get(f"goles_v_{pid}", 0)
                loc, vis = partido["loc"], partido["vis"]
                tabla_calculada[loc]["PJ"] += 1; tabla_calculada[vis]["PJ"] += 1
                tabla_calculada[loc]["GF"] += gl; tabla_calculada[loc]["GC"] += gv
                tabla_calculada[vis]["GF"] += gv; tabla_calculada[vis]["GC"] += gl
                if gl > gv: tabla_calculada[loc]["PTS"] += 3
                elif gv > gl: tabla_calculada[vis]["PTS"] += 3
                else: tabla_calculada[loc]["PTS"] += 1; tabla_calculada[vis]["PTS"] += 1
            
            for eq in tabla_calculada: tabla_calculada[eq]["DG"] = tabla_calculada[eq]["GF"] - tabla_calculada[eq]["GC"]
            tabla_ordenada = sorted(tabla_calculada.items(), key=lambda x: (x[1]["PTS"], x[1]["DG"], x[1]["GF"]), reverse=True)
            
            st.markdown("### 📋 Tabla de Posiciones Real")
            md_tabla = "| Pos | Selección | PJ | PTS | GF | GC | DG |\n| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"
            for pos, (equipo, stats) in enumerate(tabla_ordenada):
                med = "🥇" if pos == 0 else "🥈" if pos == 1 else "🥉" if pos == 2 else "❌"
                md_tabla += f"| {med} {pos+1} | **{equipo}** | {stats['PJ']} | **{stats['PTS']}** | {stats['GF']} | {stats['GC']} | {stats['DG']} |\n"
            st.markdown(md_tabla)

# --- BLOQUE 2: FASES ELIMINATORIAS ---
else:
    st.markdown("## ⚔️ Cuadro de Eliminación Directa")
    st.write("Escribe los equipos que logren clasificar en cada etapa y simula el camino a la gloria:")
    
    # Pestañas internas para llevar el orden cronológico estricto que pediste
    pestana_cuartos, pestana_semi, pestana_final = st.tabs(["📊 Cuartos de Final", "🤝 Semifinales", "👑 Gran Final"])
    
    with pestana_cuartos:
        st.markdown("### Llaves de Cuartos de Final")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 1</b>", unsafe_allow_html=True)
            c1_l = st.text_input("Equipo Local C1:", "México", key="c1l")
            c1_v = st.text_input("Equipo Visitante C1:", "Brasil", key="c1v")
            gc1_l = st.number_input(f"Goles {c1_l}:", min_value=0, value=0, key="gc1l")
            gc1_v = st.number_input(f"Goles {c1_v}:", min_value=0, value=0, key="gc1v")
            st.session_state.fase_elim["ganador_c1"] = c1_l if gc1_l >= gc1_l else c1_v # Manejo simple de pase
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 2</b>", unsafe_allow_html=True)
            c2_l = st.text_input("Equipo Local C2:", "Argentina", key="c2l")
            c2_v = st.text_input("Equipo Visitante C2:", "Francia", key="c2v")
            gc2_l = st.number_input(f"Goles {c2_l}:", min_value=0, value=0, key="gc2l")
            gc2_v = st.number_input(f"Goles {c2_v}:", min_value=0, value=0, key="gc2v")
            st.session_state.fase_elim["ganador_c2"] = c2_l if gc2_l > gc2_v else c2_v
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 3</b>", unsafe_allow_html=True)
            c3_l = st.text_input("Equipo Local C3:", "Inglaterra", key="c3l")
            c3_v = st.text_input("Equipo Visitante C3:", "España", key="c3v")
            gc3_l = st.number_input(f"Goles {c3_l}:", min_value=0, value=0, key="gc3l")
            gc3_v = st.number_input(f"Goles {c3_v}:", min_value=0, value=0, key="gc3v")
            st.session_state.fase_elim["ganador_c3"] = c3_l if gc3_l > gc3_v else c3_v
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 4</b>", unsafe_allow_html=True)
            c4_l = st.text_input("Equipo Local C4:", "Colombia", key="c4l")
            c4_v = st.text_input("Equipo Visitante C4:", "Alemania", key="c4v")
            gc4_l = st.number_input(f"Goles {c4_l}:", min_value=0, value=0, key="gc4l")
            gc4_v = st.number_input(f"Goles {c4_v}:", min_value=0, value=0, key="gc4v")
            st.session_state.fase_elim["ganador_c4"] = c4_l if gc4_l > gc4_v else c4_v
            st.markdown("</div>", unsafe_allow_html=True)

    with pestana_semi:
        st.markdown("### Llaves de Semifinales")
        # Trae automáticamente los ganadores definidos en la pestaña anterior
        sem1_l = st.session_state.fase_elim.get("ganador_c1", "Ganador C1")
        sem1_v = st.session_state.fase_elim.get("ganador_c2", "Ganador C2")
        sem2_l = st.session_state.fase_elim.get("ganador_c3", "Ganador C3")
        sem2_v = st.session_state.fase_elim.get("ganador_c4", "Ganador C4")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("<div class='card-eliminatoria'><b>Semifinal 1</b>", unsafe_allow_html=True)
            st.write(f"Match: {sem1_l} vs {sem1_v}")
            gs1_l = st.number_input(f"Goles {sem1_l}:", min_value=0, value=0, key="gs1l")
            gs1_v = st.number_input(f"Goles {sem1_v}:", min_value=0, value=0, key="gs1v")
            st.session_state.fase_elim["finalista_1"] = sem1_l if gs1_l > gs1_v else sem1_v
            st.markdown("</div>", unsafe_allow_html=True)
        with col_s2:
            st.markdown("<div class='card-eliminatoria'><b>Semifinal 2</b>", unsafe_allow_html=True)
            st.write(f"Match: {sem2_l} vs {sem2_v}")
            gs2_l = st.number_input(f"Goles {sem2_l}:", min_value=0, value=0, key="gs2l")
            gs2_v = st.number_input(f"Goles {sem2_v}:", min_value=0, value=0, key="gs2v")
            st.session_state.fase_elim["finalista_2"] = sem2_l if gs2_l > gs2_v else sem2_v
            st.markdown("</div>", unsafe_allow_html=True)

    with pestana_final:
        st.markdown("### 👑 Partido de la Gran Final")
        fin_l = st.session_state.fase_elim.get("finalista_1", "Finalista 1")
        fin_v = st.session_state.fase_elim.get("finalista_2", "Finalista 2")
        
        st.markdown("<div class='card-grupo' style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown(f"<h2>⚽ {fin_l} vs {fin_v} ⚽</h2>", unsafe_allow_html=True)
        
        col_fl, col_fv = st.columns(2)
        with col_fl: gf_l = st.number_input(f"Goles de {fin_l}:", min_value=0, value=0, key="gfl")
        with col_fv: gf_v = st.number_input(f"Goles de {fin_v}:", min_value=0, value=0, key="gfv")
        
        if gf_l != gf_v:
            campeon = fin_l if gf_l > gf_v else fin_v
            st.markdown(f"<h1 style='text-align: center; color: #34d399; margin-top: 20px;'>🎉 ¡{campeon.upper()} CAMPEÓN DEL MUNDO! 🎉</h1>", unsafe_allow_html=True)
        else:
            st.info("Define un ganador en el marcador para coronar al Campeón del Mundo.")
        st.markdown("</div>", unsafe_allow_html=True)

# 3. Pie de página con tu firma exacta
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.2 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
                                                                                           
