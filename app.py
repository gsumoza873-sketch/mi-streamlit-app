import streamlit as st
import time
import random

# 1. Configuración de la página (Estilo Portal de Prensa)
st.set_page_config(
    page_title="Diario Central - Edición Especial",
    page_icon="📰",
    layout="centered"
)

# 2. Estilos CSS para simular un Periódico Digital Serio (Fondo claro, tipografía de prensa)
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    .header-periodico {
        text-align: center;
        border-bottom: 3px double #1e293b;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    .nombre-diario {
        font-family: 'Times New Roman', Times, serif;
        font-size: 48px;
        font-weight: bold;
        color: #0f172a;
        letter-spacing: 1px;
        margin-bottom: 0px;
    }
    .meta-info {
        font-family: 'Courier New', monospace;
        font-size: 13px;
        color: #64748b;
        display: flex;
        justify-content: space-between;
        border-top: 1px solid #cbd5e1;
        padding-top: 5px;
        margin-top: 5px;
    }
    .titular-principal {
        font-family: 'Georgia', serif;
        font-size: 32px;
        font-weight: bold;
        color: #1e1b4b;
        line-height: 1.2;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .subtitulo-articulo {
        font-family: 'Georgia', serif;
        font-size: 18px;
        font-style: italic;
        color: #475569;
        margin-bottom: 25px;
    }
    .cuerpo-texto {
        font-family: 'Georgia', serif;
        font-size: 16px;
        line-height: 1.6;
        text-align: justify;
        color: #334155;
    }
    .seccion-nota {
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .subtitulo-seccion {
        font-family: 'Georgia', serif;
        color: #0f172a !important;
        border-bottom: 2px solid #f43f5e;
        padding-bottom: 5px;
        margin-top: 15px;
    }
    .resultado-editorial {
        background-color: #eff6ff;
        border-left: 5px solid #2563eb;
        padding: 15px;
        border-radius: 4px;
        margin-top: 20px;
        font-family: 'Georgia', serif;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabecera del Portal de Noticias
st.markdown("""
    <div class="header-periodico">
        <div class="nombre-diario">EL DIARIO CENTRAL</div>
        <div class="meta-info">
            <span>Sección: Crónica e Investigación Urbana</span>
            <span>Edición Digital</span>
            <span>Estado: Verificado ✔️</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Titular y Subtítulo del Artículo
st.markdown("""
    <div class="titular-principal">El fenómeno Ipia: Entre la estatura compacta, la recocha indomable y los visajes sospechosos</div>
    <div class="subtitulo-articulo">Un análisis exhaustivo sobre el comportamiento de Sebastián Ipia y los factores biológicos y sociales que definen su particular estilo de vida.</div>
""", unsafe_allow_html=True)

# 5. Cuerpo del Artículo (Estructura de noticia formal con la recocha implícita)
st.markdown("""
    <div class="cuerpo-texto">
        <p><b>REDACCIÓN CENTRAL.</b>— En los últimos meses, la comunidad ha venido haciendo un seguimiento detallado al ciudadano <b>Sebastián Ipia</b>, cuyas características físicas y conductuales han despertado profundos debates entre sus allegados. Expertos en comportamiento urbano intentan descifrar la fórmula detrás de un individuo que combina una estatura notablemente baja con un temperamento hiperactivo orientado a la recocha y un catálogo de ademanes que muchos califican de sumamente delicados.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 1: La Estatura
st.markdown("<h3 class=\"subtitulo-seccion\">📏 1. Anatomía de bolsillo: ¿Por qué tan abajo?</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>El primer eje de análisis es, sin duda, su estatura. La ciencia evalúa si el empaque compacto de Ipia se debe a factores genéticos severos o si, por el contrario, simplemente dejó de crecer para ahorrar espacio. Fuentes cercanas afirman que ver a Sebastián caminando rápido con sus tenis blancos inmaculados para no alcanzar el suelo húmedo genera una perspectiva visual extraña. Diversas teorías apuntan a que su centro de gravedad bajo es lo que le permite desplazarse con tanta agilidad cuando intenta esquivar sus responsabilidades académicas.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 2: La Recocha
st.markdown("<h3 class=\"subtitulo-seccion\">🤡 2. El síndrome de la recocha perpetua</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>No se puede hablar de Ipia sin mencionar su adicción al desorden. Su incapacidad para mantener la seriedad por más de treinta segundos consecutivos ha llevado a pensar que el sujeto sufre de un exceso de vibras alegres en el lóbulo frontal. Ya sea montando un show en plena vía pública, interrumpiendo conversaciones serias con apuntes sin sentido, o buscando llamar la atención de la pipol con payasadas, su nivel de recocha indomable parece ser un mecanismo de defensa para compensar los centímetros que le hicieron falta abajo.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 3: Los Modales Sospechosos
st.markdown("<h3 class=\"subtitulo-seccion\">🌈 3. La energía delicada y el quiebre de muñeca</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>Por último, el artículo aborda el enigma de su delicadeza. Aunque el sujeto insiste en camuflarse adoptando posturas rudas y usando expresiones gruesas para parecer un pez pesado, ciertos patrones cotidianos lo terminan delatando a los dos segundos. El sutil pero evidente quiebre de muñeca al gesticular, su extraña fascinación por analizar detalladamente el físico de otros manes en el gimnasio, y la sospechosa selección de temas musicales de Karol G o La Rosalía que tararea cuando cree que nadie lo está escuchando, configuran un cuadro clínico donde, según el argot popular, la canoa no solo se balancea, sino que navega con bandera desplegada.</p>
    </div>
""", unsafe_allow_html=True)

# 6. MÓDULO INTERACTIVO (Camuflado como buzón de aportes del lector)
st.write("---")
st.markdown("<h3 style='font-family: Georgia, serif; text-align: center;'>📥 Buzón de Aportes a la Investigación</h3>", unsafe_allow_html=True)
st.write("Como lector de este portal, puedes enviar tus observaciones directamente al equipo editorial para robustecer la nota periodística:")

# Inicialización de variables en session_state
if "procesado" not in st.session_state:
    st.session_state.procesado = False
if "resultado_actual" not in st.session_state:
    st.session_state.resultado_actual = ""

# Casilla donde el usuario redacta libremente (Se limpia sola tras enviar)
aporte_usuario = st.text_area(
    "Escribe aquí tu análisis o testimonio sobre las conductas, la estatura o la recocha de Ipia:",
    placeholder="Ej: Considero que su falta de estatura influye en que sea tan recochero, pero lo de la muñeca quebrada ya es de nacimiento...",
    key="input_aporte"
)

# Opciones de resultados periodísticos irónicos que saltarán aleatoriamente
conclusiones_prensa = [
    "📰 NOTA EDITORIAL ADJUNTA: Tras analizar el testimonio, el comité de prensa concluye que el sujeto mide lo mismo que un bafle mediano y bota más plumas que una almohada vieja. Caso confirmado.",
    "📰 ACTUALIZACIÓN DE ÚLTIMA HORA: Los datos de campo demuestran una correlación directa: a menor estatura, mayor es el visaje y la necesidad de cantar los temas de Karol G haciendo poses raras.",
    "📰 DICTAMEN DE CORRESPONSAL: Testigos aseguran que el camuflaje de Sebastián ha fallado. Su recocha no logra ocultar que camina empinado para verse más alto y que se le dobla la mano al saludar.",
    "📰 ARCHIVO CLASIFICADO: El algoritmo de redacción colapsó debido al exceso de evidencia sospechosa detectada. Veredicto final: Chiquito, recochero y recontra pato.",
    "📰 DECLARACIÓN COMPLEMENTARIA: El análisis textual confirma que a Sebastián se le moja la canoa de manera crónica e irreversible, sin importar los pantalones anchos que se ponga."
]

if st.button("📝 ENVIAR REPORTE AL EQUIPO DE REDACCIÓN", use_container_width=True):
    if not aporte_usuario:
        st.warning("⚠️ El buzón está vacío. Escribe tu aporte antes de enviarlo al servidor de prensa.")
    else:
        # Animación de procesamiento simulado al estilo periódico
        with st.spinner("📨 Transmitiendo texto al servidor central de noticias..."):
            time.sleep(1.2)
        with st.spinner("⚙️ Cotejando testimonio con el archivo biográfico de Ipia..."):
            time.sleep(1.0)
        with st.spinner("🗑️ Auto-eliminando registro para proteger la fuente anónima..."):
            time.sleep(0.8)
        
        # Guardar la conclusión aleatoria y forzar limpieza
        st.session_state.resultado_actual = random.choice(conclusiones_prensa)
        st.session_state.procesado = True
        st.rerun()

# Despliegue de los resultados
if st.session_state.procesado:
    st.markdown(f"""
        <div class="resultado-editorial">
            <strong>📊 RESOLUCIÓN INTERNA DEL DIARIO:</strong><br><br>
            {st.session_state.resultado_actual}
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Redactar otra columna de opinión"):
        st.session_state.procesado = False
        st.session_state.resultado_actual = ""
        st.rerun()

# Pie de página formal sin ubicaciones explícitas
st.write("---")
st.caption("📰 Servicio de Prensa Independiente • Sección de Análisis de Casos Especiales • Contenido estrictamente confidencial. 🤫")
