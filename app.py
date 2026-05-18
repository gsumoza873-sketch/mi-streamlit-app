import streamlit as st

# 1. Configuración de la página (Pestaña del navegador)
st.set_page_config(
    page_title="La Gaceta Tricolor | Historia de Venezuela",
    page_icon="🇻🇪",
    layout="centered"
)

# 2. Estilos visuales personalizados (Colores representativos de la bandera con tonos elegantes)
st.markdown("""
    <style>
    /* Fondo general de la app */
    .stApp {
        background-color: #121214;
        color: #E2E8F0;
    }
    /* Banner principal tricolor */
    .banner-tricolor {
        border-top: 6px solid #FFD700;   /* Amarillo */
        border-bottom: 6px solid #CE1126; /* Rojo */
        background-color: #0038A8;        /* Azul */
        padding: 20px;
        text-align: center;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .banner-tricolor h1 {
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: bold;
        margin: 0;
        font-size: 26pt;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
    }
    .banner-tricolor p {
        color: #FFD700 !important;
        margin: 5px 0 0 0;
        font-size: 12pt;
        font-style: italic;
    }
    /* Tarjetas de las secciones cronológicas */
    .bloque-cronologico {
        background-color: #1E1E24;
        border-left: 5px solid #FFD700;
        padding: 15px 20px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 20px;
    }
    .bloque-cronologico h3 {
        color: #FFD700 !important;
        margin-top: 0;
    }
    /* Alertas o destacados con jerga */
    .nota-pana {
        background-color: #2D3748;
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #0038A8;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado de la interfaz
st.markdown("""
    <div class="banner-tricolor">
        <h1>🇻🇪 LA GACETA TRICOLOR</h1>
        <p>¡Epa, chamo! Siéntate y lée los beta políticos del país desde 1992 hasta hoy</p>
    </div>
""", unsafe_allow_html=True)

# Introducción con jerga
st.markdown("""
¡Qué más, pana! Si quieres entender de verdad cómo llegó Venezuela a la situación política actual, hay que echar el cassette hacia atrás completos. No te preocupes, aquí te lo explicamos sin rodeos, con pelos y señales, desde que empezó el movimiento de Hugo Chávez en el 92 hasta el panorama de hoy en día. ¡Ponte cómodo!
""")

st.write("---")

# 4. Cuerpo del Artículo Informativo
st.markdown("## 📖 Artículo: Radiografía de la Política Venezolana (1992 - Actualidad)")

# Sección 1
st.markdown("""
<div class="bloque-cronologico">
    <h3>1992: El Por Ahora y el Sacudón Militar</h3>
    <p>Todo este beta contemporáneo arranca formalmente el <b>4 de febrero de 1992</b>. Un teniente coronel llamado <b>Hugo Chávez Frías</b> comandó un golpe de Estado contra el presidente Carlos Andrés Pérez. El golpe fracasó militarmente, pero Chávez salió en televisión nacional diciendo una frase que quedó grabada en la historia: <i>"Por ahora los objetivos no fueron alcanzados"</i>. Ese mismo año, en noviembre, hubo otra intentona golpista. El país quedó completamente movido y la vieja política herida de muerte.</p>
</div>
""", unsafe_allow_html=True)

# Sección 2
st.markdown("""
<div class="bloque-cronologico">
    <h3>1999 - 2012: La Era del Chavismo y la "Revolución"</h3>
    <p>Tras salir de prisión y ganar las elecciones de 1998, Chávez asumió la presidencia en 1999. Lo primero que hizo fue meterle mano a las reglas del juego convocando una Asamblea Constituyente para cambiar la Constitución. Durante esta época, el país vivió una polarización brutal: el paro petrolero de 2002, un golpe de Estado de 47 horas que sacó a Chávez temporalmente, y un auge petrolero masivo en los años siguientes que financió las misiones sociales, pero que también concentró todo el poder del Estado en una sola figura.</p>
</div>
""", unsafe_allow_html=True)

# Sección 3
st.markdown("""
<div class="bloque-cronologico">
    <h3>2013 - 2018: La Transición a Nicolás Maduro y la Crisis</h3>
    <p>Tras la muerte de Chávez en marzo de 2013, <b>Nicolás Maduro</b> asumió el mando y ganó unas elecciones sumamente reñidas contra Henrique Capriles. En este periodo la economía se vino abajo debido al desplome de los precios del petróleo y los controles del Estado. El descontento social estalló en las calles con olas de protestas masivas en 2014 y 2017. La oposición ganó la Asamblea Nacional en 2015, lo que llevó al Gobierno a crear una Asamblea Constituyente paralela para neutralizar al parlamento opositor.</p>
</div>
""", unsafe_allow_html=True)

# Sección 4
st.markdown("""
<div class="bloque-cronologico">
    <h3>2019 - Presente: Desafíos Políticos y el Contexto Actual</h3>
    <p>En 2019 la crisis política escaló a nivel internacional cuando Juan Guaidó se juramentó como presidente interino, figura que fue perdiendo fuerza con los años. El panorama político dio un giro drástico en el año <b>2024</b> con las elecciones presidenciales. La oposición, unificada bajo la figura de María Corina Machado y el candidato Edmundo González Urrutia, se enfrentó en las urnas a Nicolás Maduro. El Consejo Nacional Electoral proclamó ganador a Maduro, un resultado fuertemente cuestionado por la oposición y gran parte de la comunidad internacional, lo que mantiene al país en una tensa disputa política y diplomática sobre la legitimidad del mando.</p>
</div>
""", unsafe_allow_html=True)

# Nota final o llamado a la reflexión con estilo venezolano
st.markdown("""
<div class="nota-pana">
    <h4 style='color: #FFD700; margin-top:0;'>💡 El dato del pana:</h4>
    <p style='margin-bottom:0;'>Esta es una cronología informativa objetiva para que conozcas los hechos clave que cambiaron la historia de Venezuela. ¡La política de nuestro país se mueve más rápido que un motorizado en plena autopista, así que mantente informado!</p>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.caption("La Gaceta Tricolor v1.0 - Hecho para el público de forma educativa.")
