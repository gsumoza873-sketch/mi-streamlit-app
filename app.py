import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="La Gaceta Tricolor | Orgullo Venezolano",
    page_icon="🇻🇪",
    layout="wide"
)

# 2. Estilos CSS para el look tricolor y la bandera en la esquina
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    /* Bandera en la esquina superior izquierda */
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
        margin-bottom: 30px;
    }
    .header-box {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 8px;
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
    .stTable {
        background-color: #1e293b;
    }
    </style>
    
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Venezuela.svg" class="top-left-flag">
""", unsafe_allow_html=True)

# 3. Encabezado Principal
st.markdown("""
    <div class="main-banner">
        <div class="header-box">
            <h1>🇻🇪 LA GACETA TRICOLOR: CRÓNICA Y PATRIA</h1>
            <p style='color: white; font-size: 18px;'>¡Epa, chamo! El portal donde se cuenta el beta completo de nuestra historia y nuestra tierra.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Menú de navegación (Tabs)
tab_historia, tab_simbolos, tab_geografia = st.tabs(["📜 Historia Política", "🌿 Símbolos y Patria", "📍 Estados y Capitales"])

with tab_historia:
    st.header("Cronología: Del 92 hasta el Sol de Hoy")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="section-box">
            <h3>1992: El "Por Ahora"</h3>
            <p>El beta empezó fuerte el <b>4 de febrero de 1992</b>. Un Hugo Chávez joven se alzó contra Carlos Andrés Pérez. No llegó a Miraflores ese día, pero con su frase <i>"Por ahora"</i> se ganó a un gentío que estaba cansado de la misma guachafita de antes.</p>
        </div>
        
        <div class="section-box">
            <h3>1999-2012: El Comandante en el coroto</h3>
            <p>Chávez gana en el 98 y arranca la 5ta República. Cambió la Constitución, hubo un golpe en 2002 que duró lo que un suspiro (47 horas), y el petróleo subió tanto que el dinero corría por montones. Fue una época de misiones y mucha polarización: o eras chavista o eras opositor, no había punto medio, pana.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Hugo_Ch%C3%A1vez_%28FAPESP%29.jpg/800px-Hugo_Ch%C3%A1vez_%28FAPESP%29.jpg", caption="Hugo Chávez")

    col3, col4 = st.columns([2, 1])
    with col3:
        st.markdown("""
        <div class="section-box">
            <h3>2013-2023: La era de Maduro y el apretón</h3>
            <p>Muere Chávez y queda Maduro. Aquí la cosa se puso color de hormiga: la economía se fue al foso, la gente empezó a irse por el Darién o en avión y surgieron figuras como Guaidó que al final no cuajaron. Sanciones, marchas y un país tratando de sobrevivir como un guerrero.</p>
        </div>
        
        <div class="section-box">
            <h3>2024: ¿Qué es lo que hay?</h3>
            <p>Llegaron las elecciones de este año. La oposición se unió con María Corina Machado y Edmundo González. El CNE dio ganador a Maduro, pero el mundo y la oposición dicen que las actas cuentan otro cuento. Estamos en un limbo político esperando a ver qué decide el VAR internacional.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Nicolas_Maduro_2024.jpg/800px-Nicolas_Maduro_2024.jpg", caption="Nicolás Maduro")

with tab_simbolos:
    st.header("Identidad Nacional")
    
    st.subheader("🎵 Himno Nacional: Gloria al Bravo Pueblo")
    st.audio("https://upload.wikimedia.org/wikipedia/commons/3/30/Gloria_al_Bravo_Pueblo_instrumental.ogg")
    with st.expander("Ver letra del Himno"):
        st.write("""
        Coro: Gloria al bravo pueblo que el yugo lanzó, la ley respetando la virtud y honor...
        I: ¡Abajo cadenas! gritaba el señor; y el pobre en su choza Libertad pidió...
        """)

    st.subheader("🌿 Símbolos Naturales")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Tabebuia_chrysantha_Flower.jpg/800px-Tabebuia_chrysantha_Flower.jpg", caption="El Araguaney (Árbol Nacional)")
    with c2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Icterus_icterus_2.jpg/800px-Icterus_icterus_2.jpg", caption="El Turpial (Ave Nacional)")
    with c3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Cattleya_mossiae_01.jpg/800px-Cattleya_mossiae_01.jpg", caption="La Orquídea (Flor Nacional)")

with tab_geografia:
    st.header("Geografía Patria: Estados y Capitales")
    st.write("Para que no te pierdas en el mapa, aquí tienes la lista completa:")
    
    data = [
        ["Amazonas", "Puerto Ayacucho"], ["Anzoátegui", "Barcelona"], ["Apure", "San Fernando de Apure"],
        ["Aragua", "Maracay"], ["Barinas", "Barinas"], ["Bolívar", "Ciudad Bolívar"],
        ["Carabobo", "Valencia"], ["Cojedes", "San Carlos"], ["Delta Amacuro", "Tucupita"],
        ["Caracas (Distrito Capital)", "Caracas"], ["Falcón", "Coro"], ["Guárico", "San Juan de los Morros"],
        ["Lara", "Barquisimeto"], ["Mérida", "Mérida"], ["Miranda", "Los Teques"],
        ["Monagas", "Matunín"], ["Nueva Esparta", "La Asunción"], ["Portuguesa", "Guanare"],
        ["Sucre", "Cumaná"], ["Táchira", "San Cristóbal"], ["Trujillo", "Trujillo"],
        ["Vargas (La Guaira)", "La Guaira"], ["Yaracuy", "San Felipe"], ["Zulia", "Maracaibo"]
    ]
    
    st.table({"Estado": [i[0] for i in data], "Capital": [i[1] for i in data]})

st.write("---")
st.caption("Hecho por y para venezolanos. ¡Mano, tengo fe! 🇻🇪")
