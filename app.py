import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Simulator the World Cup",
    page_icon="🏆",
    layout="centered"
)

# Estilos visuales oscuros estilo plataforma deportiva
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-grupo { background: linear-gradient(145deg, #0f172a, #1e293b); border-radius: 12px; padding: 20px; border: 1px solid #1e40af; margin-bottom: 25px; }</style>", unsafe_allow_html=True)
st.markdown("<style>.card-eliminatoria { background: linear-gradient(145deg, #1e1b4b, #312e81); border-radius: 12px; padding: 15px; border: 1px solid #7c3aed; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

# Título Corregido Exacto: Simulator the World Cup
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Simulator the World Cup</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Simulador Dinámico: Configura las selecciones reales y calcula toda la Copa del Mundo.</p>", unsafe_allow_html=True)

# Secciones principales de la App
seccion_principal = st.radio("Selecciona la etapa del torneo a gestionar:", ["Fase de Grupos", "Fases Finales (Eliminación Directa)"])

# 2. Inicialización de los 12 grupos editables (Evita datos falsos fijos)
if "config_grupos" not in st.session_state:
    st.session_state.config_grupos = {
        f"Grupo {letra}": [f"Equipo 1 {letra}", f"Equipo 2 {letra}", f"Equipo 3 {letra}", f"Equipo 4 {letra}"]
        for letra in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    }
    # Sedes confirmadas por la organización
    st.session_state.config_grupos["Grupo A"][0] = "México"
    st.session_state.config_grupos["Grupo B"][0] = "Canadá"
    st.session_state.config_grupos["Grupo D"][0] = "Estados Unidos"

if "goles_simulados" not in st.session_state: st.session_state.goles_simulados = {}
if "fase_elim" not in st.session_state: st.session_state.fase_elim = {}

nombres_grupos = list(st.session_state.config_grupos.keys())

# --- BLOQUE 1: FASE DE GRUPOS ---
if seccion_principal == "Fase de Grupos":
    
    # Panel superior para ingresar los países reales en los inputs
    with st.expander("⚙️ Panel de Configuración: Digita las Selecciones Reales"):
        st.write("Escribe las selecciones de cada grupo para actualizar los partidos automáticamente:")
        grupo_sel = st.selectbox("Selecciona el grupo a rellenar:", nombres_grupos)
        eq_actuales = st.session_state.config_grupos[grupo_sel]
        
        col_ed1, col_ed2 = st.columns(2)
        with col_ed1:
            n_eq1 = st.text_input("Selección 1:", value=eq_actuales[0], key=f"edit_{grupo_sel}_1")
            n_eq2 = st.text_input("Selección 2:", value=eq_actuales[1], key=f"edit_{grupo_sel}_2")
        with col_ed2:
            n_eq3 = st.text_input("Selección 3:", value=eq_actuales[2], key=f"edit_{grupo_sel}_3")
            n_eq4 = st.text_input("Selección 4:", value=eq_actuales[3], key=f"edit_{grupo_sel}_4")
        
        st.session_state.config_grupos[grupo_sel] = [n_eq1, n_eq2, n_eq3, n_eq4]

    pestanas = st.tabs(nombres_grupos)
    for i, nombre_grupo in enumerate(nombres_grupos):
        with pestanas[i]:
            lista_equipos = st.session_state.config_grupos[nombre_grupo]
            
            # Fixture dinámico basado en las selecciones escritas
            partidos = [
                {"p_id": f"{nombre_grupo}_1", "loc": lista_equipos[0], "vis": lista_equipos[1], "jornada": "Jornada 1"},
                {"p_id": f"{nombre_grupo}_2", "loc": lista_equipos[2], "vis": lista_equipos[3], "jornada": "Jornada 1"},
                {"p_id": f"{nombre_grupo}_3", "loc": lista_equipos[0], "vis": lista_equipos[2], "jornada": "Jornada 2"},
                {"p_id": f"{nombre_grupo}_4", "loc": lista_equipos[3], "vis": lista_equipos[1], "jornada": "Jornada 2"},
                {"p_id": f"{nombre_grupo}_5", "loc": lista_equipos[3], "vis": lista_equipos[0], "jornada": "Jornada 3"},
                {"p_id": f"{nombre_grupo}_6", "loc": lista_equipos[1], "vis": lista_equipos[2], "jornada": "Jornada 3"}
            ]
            
            st.markdown(f"## 📅 Fixture de Partidos: {nombre_grupo}")
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
            
            # Tabla de Posiciones Matemática Proporcional
            tabla_calculada = {equipo: {"PJ": 0, "PTS": 0, "GF": 0, "GC": 0, "DG": 0} for equipo in lista_equipos}
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
            
            st.markdown("### 📋 Tabla de Posiciones en Tiempo Real")
            md_tabla = "| Pos | Selección | PJ | PTS | GF | GC | DG |\n| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"
            for pos, (equipo, stats) in enumerate(tabla_ordenada):
                med = "🥇" if pos == 0 else "🥈" if pos == 1 else "🥉" if pos == 2 else "❌"
                md_tabla += f"| {med} {pos+1} | **{equipo}** | {stats['PJ']} | **{stats['PTS']}** | {stats['GF']} | {stats['GC']} | {stats['DG']} |\n"
            st.markdown(md_tabla)

# --- BLOQUE 2: FASES ELIMINATORIAS ---
else:
    st.markdown("## ⚔️ Llaves de Eliminación Directa")
    st.write("Gestiona la fase final introduciendo los ganadores desde Cuartos de Final hasta la definición del torneo:")
    
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
            st.session_state.fase_elim["ganador_c1"] = c1_l if gc1_l >= gc1_v else c1_v
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 2</b>", unsafe_allow_html=True)
            c2_l = st.text_input("Equipo Local C2:", "Argentina", key="c2l")
            c2_v = st.text_input("Equipo Visitante C2:", "Francia", key="c2v")
            gc2_l = st.number_input(f"Goles {c2_l}:", min_value=0, value=0, key="gc2l")
            gc2_v = st.number_input(f"Goles {c2_v}:", min_value=0, value=0, key="gc2v")
            st.session_state.fase_elim["ganador_c2"] = c2_l if gc2_l >= gc2_v else c2_v
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 3</b>", unsafe_allow_html=True)
            c3_l = st.text_input("Equipo Local C3:", "Inglaterra", key="c3l")
            c3_v = st.text_input("Equipo Visitante C3:", "España", key="c3v")
            gc3_l = st.number_input(f"Goles {c3_l}:", min_value=0, value=0, key="gc3l")
            gc3_v = st.number_input(f"Goles {c3_v}:", min_value=0, value=0, key="gc3v")
            st.session_state.fase_elim["ganador_c3"] = c3_l if gc3_l >= gc3_v else c3_v
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card-eliminatoria'><b>Cuartos 4</b>", unsafe_allow_html=True)
            c4_l = st.text_input("Equipo Local C4:", "Colombia", key="c4l")
            c4_v = st.text_input("Equipo Visitante C4:", "Alemania", key="c4v")
            gc4_l = st.number_input(f"Goles {c4_l}:", min_value=0, value=0, key="gc4l")
            gc4_v = st.number_input(f"Goles {c4_v}:", min_value=0, value=0, key="gc4v")
            st.session_state.fase_elim["ganador_c4"] = c4_l if gc4_l >= gc4_v else c4_v
            st.markdown("</div>", unsafe_allow_html=True)

    with pestana_semi:
        st.markdown("### Llaves de Semifinales")
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
            st.session_state.fase_elim["finalista_1"] = sem1_l if gs1_l >= gs1_v else sem1_v
            st.markdown("</div>", unsafe_allow_html=True)
        with col_s2:
            st.markdown("<div class='card-eliminatoria'><b>Semifinal 2</b>", unsafe_allow_html=True)
            st.write(f"Match: {sem2_l} vs {sem2_v}")
            gs2_l = st.number_input(f"Goles {sem2_l}:", min_value=0, value=0, key="gs2l")
            gs2_v = st.number_input(f"Goles {sem2_v}:", min_value=0, value=0, key="gs2v")
            st.session_state.fase_elim["finalista_2"] = sem2_l if gs2_l >= gs2_v else sem2_v
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
        
        if gf_l != gf_v or (gf_l == 0 and gf_v == 0 and fin_l != "Finalista 1"):
            campeon = fin_l if gf_l > gf_v else fin_v
            if fin_l != "Finalista 1":
                st.markdown(f"<h1 style='text-align: center; color: #34d399; margin-top: 20px;'>🎉 ¡{campeon.upper()} CAMPEÓN DEL MUNDO! 🎉</h1>", unsafe_allow_html=True)
        else:
            st.info("Define un ganador en el marcador para coronar al Campeón del Mundo.")
        st.markdown("</div>", unsafe_allow_html=True)

# 3. Pie de página con tu firma exacta e intacta
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.2 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
            
