import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="La Gaceta Tricolor | Edición Semanal",
    page_icon="🇻🇪",
    layout="wide"
)

# 2. Estilos CSS (Estructura de Revista, Bandera reubicada y Tarjetas Estéticas)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .top-left-flag {
        position: fixed;
        top: 60px;
        left: 20px;
        width: 75px;
        z-index: 999;
        border: 2px solid rgba(255, 255, 255, 0.8);
        border-radius: 4px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }
    .main-banner {
        background: linear-gradient(to right, #FFD700 33%, #0038A8 33% 66%, #CE1126 66%);
        padding: 8px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 25px;
        border-radius: 8px;
    }
    .aviso-semanal {
        background-color: #1e1b4b;
        border: 2px dashed #FFD700;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 25px;
    }
    .section-box {
        background-color: #1e293b;
        padding: 22px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-bottom: 20px;
    }
    /* Tarjetas para Símbolos Patrios y Naturales */
    .simbolo-card {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 12px;
        border-top: 4px solid #0038A8;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    .simbolo-titulo {
        color: #FFD700;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .simbolo-sub {
        color: #94a3b8;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }
    .simbolo-desc {
        color: #e2e8f0;
        font-size: 15px;
        line-height: 1.6;
        text-align: justify;
    }
    .simbolo-desc ul {
        margin-top: 5px;
        padding-left: 20px;
    }
    h1, h2, h3 {
        color: #FFD700 !important;
    }
    </style>
    
    <img src="https://flagcdn.com/w160/ve.png" class="top-left-flag">
""", unsafe_allow_html=True)

# 3. Encabezado de la Revista
st.markdown("""
    <div class="main-banner">
        <div class="header-box">
            <h1>🇻🇪 LA GACETA TRICOLOR</h1>
            <p style='color: white; font-size: 18px; margin-top: 5px;'>Portal Digital de Análisis Político, Histórico y Geográfico de Venezuela</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. ÉNFASIS SEMANAL
st.markdown("""
    <div class="aviso-semanal">
        <h4 style='color: #FFD700; margin: 0;'>📢 Formato de Publicación Dinámica</h4>
        <p style='color: #e2e8f0; margin: 5px 0 0 0; font-size: 16px;'>
            Espacio formativo <b>100% dedicado a Venezuela</b>. Con el fin de ofrecer una cobertura integral, 
            <b>nuestro contenido principal se actualiza cada semana</b>. Transicionando de manera rotativa por la política, la historia musical, los movimientos artísticos y el deporte nacional.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. Barra Lateral Informativa
st.sidebar.title("📅 Edición en Curso")
st.sidebar.info("**Enfoque:** Evolución Política e Institucional Contemporánea (1992 - 2026)")
st.sidebar.write("---")

st.sidebar.subheader("🔥 Próxima Edición Semanal")
st.sidebar.warning("🎵 **Historia Musical de Venezuela**")
st.sidebar.write("""
Ejes temáticos preparados:
* **Grandes Maestros:** El desarrollo de la salsa brava y el impacto de *Oscar D'León*.
* **Movimiento Urbano Actual:** Línea de tiempo desde el legado lírico de *Canserbero* hasta referentes modernos como *Akapellah* y *Micro TDH*.
* **Métricas en Plataformas:** Análisis de los géneros más reproducidos en el país actualmente.
""")

# 6. Menú de pestañas de Contenido
tab_historia, tab_patrios, tab_naturales, tab_geografia = st.tabs([
    "📜 Crónica Política Actualizada", 
    "🛡️ Símbolos Patrios", 
    "🌿 Símbolos Naturales", 
    "📍 Organización Territorial"
])

# PESTAÑA 1: HISTORIA POLITICA
with tab_historia:
    st.header("Cronología de Hechos Políticos (1992 - Al día de hoy: Marzo 2026)")
    
    st.markdown("""
    <div class="section-box">
        <h3>1992: El Quiebre del Sistema Tradicional</h3>
        <p>El 4 de febrero de 1992 quedó marcado por la insurrección militar liderada por el Teniente Coronel Hugo Chávez Frías contra el gobierno de Carlos Andrés Pérez. A pesar de no lograr los objetivos militares inmediatos, la alocución televisiva del <i>"Por ahora"</i> fracturó el bipartidismo e inició el colapso definitivo de la Cuarta República.</p>
    </div>
    
    <div class="section-box">
        <h3>1999 - 2012: Refundación Constitucional y Consolidación Presidencial</h3>
        <p>Tras vencer en los comicios de 1998, Chávez impulsó la Asamblea Nacional Constituyente de 1999, dando nacimiento a la República Bolivariana de Venezuela. Este período se caracterizó por una profunda polarización social, eventos críticos como el golpe de Estado de abril de 2002, un prolongado paro petrolero y un posterior auge en los ingresos fiscales que financió programas de subsidios masivos (Misiones Sociales).</p>
    </div>
    
    <div class="section-box">
        <h3>2013 - 2024: Crisis Estructural, Conflictividad Extrema y Elecciones</h3>
        <p>A la muerte de Chávez in 2013, Nicolás Maduro Moros asumió el mando ejecutivo. El país enfrentó una severa contracción económica, hiperinflación, tensiones diplomáticas internacionales, sanciones institucionales y corrientes migratorias masivas. Tras años de reajustes complejos, el ciclo cerró con el complejo proceso electoral presidencial de julio de 2024, cuyos resultados oficiales emitidos por el CNE abrieron intensos debates sobre transparencia y legitimidad ante la comunidad internacional.</p>
    </div>
    
    <div class="section-box">
        <h3>2025 - Marzo 2026: El Escenario Político e Institucional de Hoy</h3>
        <p>Alcanzado el presente mes de <b>marzo de 2026</b>, la dinámica política venezolana se desenvuelve bajo un esquema de alta complejidad institucional. El gobierno de Nicolás Maduro sostiene la gestión gubernamental enfocada en la estabilización económica selectiva, la flexibilización de licencias comerciales y el control político interno, mientras los factores de oposición organizada insisten en canales de presión diplomática externa. El panorama nacional se mantiene en una tensa expectativa respecto al reconocimiento exterior y el desarrollo de nuevas agendas de diálogo social.</p>
    </div>
    """, unsafe_allow_html=True)

# PESTAÑA 2: SÍMBOLOS PATRIOS (Corregida con los 3 pilares, descripciones y sin audio)
with tab_patrios:
    st.header("Símbolos Patrios e Identidad Nacional")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        # LA BANDERA
        st.markdown("""
        <div class="simbolo-card">
            <div class="simbolo-titulo">🇻🇪 La Bandera Nacional</div>
            <div class="simbolo-sub">Emblema de Libertad y Soberanía</div>
            <div class="simbolo-desc">
                Inspirada en el diseño original traído por el Generalísimo Francisco de Miranda en 1806, la bandera actual está compuesta por tres franjas horizontales de igual tamaño con los colores amarillo, azul y rojo, un arco de ocho estrellas blancas y el escudo nacional opcional en la esquina superior izquierda.<br><br>
                <b>Significado de sus elementos:</b>
                <ul>
                    <li><b>Amarillo:</b> Representa las riquezas del suelo venezolano, el oro, el sol radiante y las virtudes de la justicia y clemencia.</li>
                    <li><b>Azul:</b> Simboliza el ancho mar Caribe, los ríos indomables y el cielo que cubre y separa a la patria de los opresores.</li>
                    <li><b>Rojo:</b> Evoca la sangre derramada por los próceres y mártires independentistas en los campos de batalla para conquistar la libertad.</li>
                    <li><b>Las 8 Estrellas:</b> Representan las provincias originales que firmaron el Acta de la Independencia, incluyendo la incorporación de la provincia de Guayana decretada por Simón Bolívar.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        # EL ESCUDO
        st.markdown("""
        <div class="simbolo-card">
            <div class="simbolo-titulo">🛡️ El Escudo de Armas</div>
            <div class="simbolo-sub">Heráldica Oficial de la República</div>
            <div class="simbolo-desc">
                El Escudo Nacional refleja la unión, el triunfo y la riqueza del pueblo a través de tres cuarteles heráldicos que llevan los colores de la bandera:<br><br>
                <ul>
                    <li><b>Cuartel Rojo (Izquierdo):</b> Contiene un manojo de 24 espigas de trigo que simbolizan la unión de los estados de la República y la riqueza de la producción agrícola del país.</li>
                    <li><b>Cuartel Amarillo (Derecho):</b> Muestra un conjunto de armas (espadas y lanzas) entrelazadas con una bandera nacional, representando el triunfo militar en las guerras independentistas.</li>
                    <li><b>Cuartel Azul (Base):</b> Aloja a un caballo blanco salvaje que corre indómito hacia la izquierda, símbolo absoluto de la libertad, el patriotismo y la soberanía nacional.</li>
                    <li><b>Cresta y Flancos:</b> En la cima sobresalen dos cornucopias cruzadas que derraman frutos de abundancia. A los lados, una rama de laurel (victoria) y una de palma (paz) se amarran abajo con una cinta tricolor que dicta las fechas históricas patrias.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # EL HIMNO NACIONAL (Abajo ocupando el ancho completo)
    st.markdown("""
    <div class="simbolo-card" style="border-top: 4px solid #CE1126;">
        <div class="simbolo-titulo">🎼 El Himno Nacional: Gloria al Bravo Pueblo</div>
        <div class="simbolo-sub">Letra de Vicente Salias • Música de Juan José Landaeta</div>
        <div class="simbolo-desc" style="text-align: center; font-size: 16px; line-height: 1.8;">
            Adoptado oficialmente el 25 de mayo de 1881 por decreto del presidente Antonio Guzmán Blanco. Su composición histórica data de los días posteriores al primer grito de independencia del 19 de abril de 1810, naciendo como un canto patriótico popular que incitaba a la unión de toda América contra la opresión colonial.<br><br>
            <hr style="border: 0; border-top: 1px solid #475569; margin: 20px 0;">
            <b>CORO</b><br>
            Gloria al bravo pueblo que el yugo lanzó<br>
            la Ley respetando la virtud y honor. (Bis)<br><br>
            
            <b>I</b><br>
            ¡Abajo cadenas! (Bis) gritaba el señor;<br>
            y el pobre en su choza Libertad pidió:<br>
            a este santo nombre tembló de pavor<br>
            el vil egoísmo que otra vez triunfó.<br><br>
            
            <b>II</b><br>
            Gritemos con brío: (Bis) ¡Muera la opresión!<br>
            Compatriotas fieles, la fuerza es la unión;<br>
            y desde el Empíreo el Supremo Autor,<br>
            un sublime aliento al pueblo infundió.<br><br>
            
            <b>III</b><br>
            Unida con lazos (Bis) que el cielo formó,<br>
            la América toda existe en nación;  <br>
            y si el despotismo levanta la voz,<br>
            seguid el ejemplo que Caracas dio.
        </div>
    </div>
    """, unsafe_allow_html=True)

# PESTAÑA 3: SÍMBOLOS NATURALES
with tab_naturales:
    st.header("Símbolos Naturales de la Nación (Fichas Descriptivas)")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="simbolo-card">
            <div class="simbolo-titulo">🌳 El Araguaney</div>
            <div class="simbolo-sub">Handroanthus chrysanthus</div>
            <div class="simbolo-desc">
                Declarado Árbol Nacional de Venezuela el 29 de mayo de 1948. Su nombre proviene de una voz indígena americana. Se caracteriza por una impresionante y densa floración de color amarillo dorado, la cual ocurre de manera sincronizada durante la transición de la época de sequía a las primeras lluvias, simbolizando la riqueza del suelo venezolano.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="simbolo-card">
            <div class="simbolo-titulo">🐦 El Turpial</div>
            <div class="simbolo-sub">Icterus icterus</div>
            <div class="simbolo-desc">
                Designado como el Ave Nacional el 23 de mayo de 1958. Es un pájaro cantor de hermoso plumaje contrastado en tonos amarillo-anaranjado, negro y detalles blancos en sus alas. Destaca por su potente, melodioso y característico canto que resuena al amanecer, habitando principalmente de forma solitaria o en parejas en zonas cálidas y sabanas del territorio.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="simbolo-card">
            <div class="simbolo-titulo">🌸 La Orquídea</div>
            <div class="simbolo-sub">Cattleya mossiae</div>
            <div class="simbolo-desc">
                Oficializada como Flor Nacional el 23 de mayo de 1951. Conocida popularmente como la "Flor de Mayo", debido a que históricamente se utilizaba para adornar las festividades de la Cruz de Mayo. Sus pétalos exhiben tonalidades violetas, lilas y rosadas con un centro purpúreo; representa la belleza natural y la biodiversidad de la Cordillera de la Costa.
            </div>
        </div>
        """, unsafe_allow_html=True)

# PESTAÑA 4: TERRITORIO
with tab_geografia:
    st.header("Organización Político-Territorial: Estados y Capitales")
    st.write("Configuración del mapa geográfico de la República de acuerdo con las leyes territoriales vigentes:")
    
    data = [
        ["Amazonas", "Puerto Ayacucho"], ["Anzoátegui", "Barcelona"], ["Apure", "San Fernando de Apure"],
        ["Aragua", "Maracay"], ["Barinas", "Barinas"], ["Bolívar", "Ciudad Bolívar"],
        ["Carabobo", "Valencia"], ["Cojedes", "San Carlos"], ["Delta Amacuro", "Tucupita"],
        ["Caracas (Distrito Capital)", "Caracas"], ["Falcón", "Coro"], ["Guárico", "San Juan de los Morros"],
        ["Lara", "Barquisimeto"], ["Mérida", "Mérida"], ["Miranda", "Los Teques"],
        ["Monagas", "Maturín"], ["Nueva Esparta", "La Asunción"], ["Portuguesa", "Guanare"],
        ["Sucre", "Cumaná"], ["Táchira", "San Cristóbal"], ["Trujillo", "Trujillo"],
        ["Vargas (La Guaira)", "La Guaira"], ["Yaracuy", "San Felipe"], ["Zulia", "Maracaibo"]
    ]
    st.table({"Estado Federal": [i[0] for i in data], "Capital Administrativa": [i[1] for i in data]})

st.write("---")
st.caption("La Gaceta Tricolor v3.5 • Revista Digital Semanal Educativa. Hecho por Gabriel Sumoza • ¡Mano, tengo fe! 🇻🇪")
