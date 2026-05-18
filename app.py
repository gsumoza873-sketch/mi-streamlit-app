import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="La Gaceta Tricolor | Edición Semanal",
    page_icon="🇻🇪",
    layout="wide"
)

# 2. Estilos CSS (Look tricolor con bandera y diseño de revista)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .top-left-flag {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 80px;
        z-index: 999;
        border: 2px solid white;
        border-radius: 4px;
    }
    .main-banner {
        background: linear-gradient(to right, #FFD700 33%, #0038A8 33% 66%, #CE1126 66%);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
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
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-bottom: 20px;
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
            <p style='color: white; font-size: 18px;'>Tu rincón digital para conocer la cultura, historia y el movimiento de Venezuela.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. ÉNFASIS SEMANAL
st.markdown("""
    <div class="aviso-semanal">
        <h4 style='color: #FFD700; margin: 0;'>📢 ¡Epa, pana! Activo aquí...</h4>
        <p style='color: #e2e8f0; margin: 5px 0 0 0; font-size: 16px;'>
            Esta es una página <b>100% dedicada a Venezuela</b>. Para que no te aburras, 
            <b>cada semana cambiaremos el contenido por completo</b>. ¡Un domingo vienes y lees de política, y al otro vienes por música o deportes! Actívate.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. Barra Lateral
st.sidebar.title("📅 Edición Actual")
st.sidebar.info("**Tema:** Política Contemporánea (1992 - 2024)")
st.sidebar.write("---")

st.sidebar.subheader("🔥 Próxima Semana")
st.sidebar.warning("🎵 **Historia Musical de Venezuela**")
st.sidebar.write("""
Hablaremos de:
* El fenómeno de **Oscar D'León** y la salsa.
* ¿Quién manda ahorita? El género urbano con **Akapellah**, **Micro TDH** y el legado de **Canserbero**.
* El rey actual de las plataformas.
""")

# 6. Menú de pestañas
tab_historia, tab_simbolos, tab_geografia = st.tabs(["📜 Edición de Hoy: Política", "🌿 Símbolos y Patria", "📍 Estados y Capitales"])

with tab_historia:
    st.header("Cronología Política: El Beta desde 1992")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="section-box">
            <h3>1992: El "Por Ahora"</h3>
            <p>El beta empezó fuerte el <b>4 de febrero de 1992</b>. Un Hugo Chávez joven se alzó contra Carlos Andrés Pérez. No llegó a Miraflores ese día, pero con su frase <i>"Por ahora"</i> se ganó a un gentío que estaba cansado de la misma guachafita de antes.</p>
        </div>
        <div class="section-box">
            <h3>1999-2012: El Comandante en el coroto</h3>
            <p>Chávez gana en el 98 y arranca la 5ta República. Cambió la Constitución, hubo un golpe en 2002 que duró lo que un suspiro (47 horas), y el petróleo subió tanto que el dinero corría por montones. Fue una época de misiones y mucha polarización.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Imagen de Chávez con link alternativo estable
        st.image("https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?w=400", caption="Reflexión de la Historia")

    col3, col4 = st.columns([2, 1])
    with col3:
        st.markdown("""
        <div class="section-box">
            <h3>2013-2023: La era de Maduro y el apretón</h3>
            <p>Muere Chávez y queda Maduro. Aquí la cosa se puso color de hormiga: la economía se fue al foso, comenzó el éxodo masivo de panas y surgieron figuras como Guaidó que al final no cuajaron. Sanciones, marchas y un país tratando de resolver como un guerrero.</p>
        </div>
        <div class="section-box">
            <h3>2024: Las Elecciones Recientes</h3>
            <p>Llegaron las elecciones presidenciales. La oposición se unió con María Corina Machado y Edmundo González. El CNE proclamó ganador a Maduro, pero los resultados han sido fuertemente cuestionados dentro y fuera del país, manteniendo una tensa disputa política por el mando.</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        # Imagen representativa de Caracas/Vzla estable
        st.image("https://images.unsplash.com/photo-1544913716-e570df4a5695?w=400", caption="Venezuela Contemporánea")

with tab_simbolos:
    st.header("Identidad y Corazón Nacional")
    
    st.subheader("🎵 Himno Nacional: Gloria al Bravo Pueblo")
    st.audio("https://upload.wikimedia.org/wikipedia/commons/3/30/Gloria_al_Bravo_Pueblo_instrumental.ogg")

    st.subheader("🌿 Nuestros Símbolos Naturales")
    c1, c2, c3 = st.columns(3)
    with c1:
        # Árbol/Naturaleza
        st.image("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400", caption="El Araguaney (Árbol Nacional - Representación)")
    with c2:
        # Ave/Fauna
        st.image("https://images.unsplash.com/photo-1444464666168-49d633b86797?w=400", caption="El Turpial (Ave Nacional - Representación)")
    with c3:
        # Flor
        st.image("https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?w=400", caption="La Orquídea (Flor Nacional - Representación)")

with tab_geografia:
    st.header("Estados y Capitales de Venezuela")
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
    st.table({"Estado": [i[0] for i in data], "Capital": [i[1] for i in data]})

st.write("---")
st.caption("La Gaceta Tricolor v1.6 • Revista Digital Semanal Educativa. ¡Mano, tengo fe! 🇻🇪")
