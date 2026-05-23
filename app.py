import streamlit as st
import time
import random

# 1. Configuración de la página (Estilo Portal de Prensa)
st.set_page_config(
    page_title="Diario G - Crónica Escolar",
    page_icon="📰",
    layout="centered"
)

# 2. Estilos CSS para simular la Columna de Opinión Periodística (Diario G)
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
        font-size: 52px;
        font-weight: bold;
        color: #0f172a;
        letter-spacing: 2px;
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
        font-size: 30px;
        font-weight: bold;
        color: #1e1b4b;
        line-height: 1.3;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .autor-columna {
        font-family: 'Georgia', serif;
        font-size: 15px;
        font-weight: bold;
        color: #f43f5e;
        margin-bottom: 5px;
    }
    .subtitulo-articulo {
        font-family: 'Georgia', serif;
        font-size: 16px;
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
    .subtitulo-seccion {
        font-family: 'Georgia', serif;
        color: #0f172a !important;
        border-bottom: 2px solid #6366f1;
        padding-bottom: 5px;
        margin-top: 25px;
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

# 3. Cabecera del Portal Informativo - DIARIO G
st.markdown("""
    <div class="header-periodico">
        <div class="nombre-diario">DIARIO G</div>
        <div class="meta-info">
            <span>Sección: Opinión y Convivencia Escolar</span>
            <span>Columna del Salón</span>
            <span>Estatus: Artículo de Opinión de los Panas</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Titular, Autor y Subtítulo
st.markdown("""
    <div class="titular-principal">Convivir con el misterio de Ipia: Una mirada desde el pupitre de al lado</div>
    <div class="autor-columna">Por: Un compañero de clase y amigo cercano</div>
    <div class="subtitulo-articulo">Crónica sincera sobre cómo es aguantarse el desorden diario de Sebastián, su estatura de llavero y esos gestos que nos hacen dudar a todos en el salón.</div>
""", unsafe_allow_html=True)

# 5. Cuerpo del Artículo
st.markdown("""
    <div class="cuerpo-texto">
        <p>Compartir el salón de clases con <b>Sebastián Ipia</b> es una experiencia que desafía las leyes de la lógica y la paciencia. Como amigo suyo y compañero que se la pasa sentado a pocos metros, he tenido el privilegio —y a veces el sufrimiento— de analizar de cerca los tres grandes misterios que componen a este personaje. No es un secreto para nadie en el colegio que tenerlo cerca implica estar en una montaña rusa de risas, dudas y un visaje constante que ya es imposible de ignorar.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 1: Estatura
st.markdown("<h3 class=\"subtitulo-seccion\">📏 Verlo hacia abajo: El misterio de su estatura</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>El primer tema que debatimos a diario es su formato compacto. A veces me pregunto si Sebastián no creció más porque le dio pereza o si el pupitre le queda grande a propósito. Uno lo ve llegar temprano, caminando rápido con sus tenis blancos impecables cuidando de no pisar el más mínimo charco, y parece un bafle mediano moviéndose por los pasillos. Su centro de gravedad bajo es una ventaja para esconderse detrás de los compañeros altos cuando el profesor empieza a pedir las tareas que él obviamente no trajo, pero ver el esfuerzo que hace para alcanzar los estantes del salón ya es parte de nuestra rutina cómica.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 2: La Recocha
st.markdown("<h3 class=\"subtitulo-seccion\">🤡 La recocha infinita como escudo</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>Otra realidad innegable es su incapacidad absoluta para mantenerse serio. Es imposible tener una conversación seria con este man; si el profesor está explicando el tema más complejo del examen, Ipia sale con un apunte sin sentido, hace una mueca o monta un show para hacer reír a la pipol. Nosotros, como sus amigos, sabemos que esa recocha perpetua y esas ganas de llamar la atención son su armadura para compensar los centímetros de altura que le faltaron. Básicamente, si no puede destacar por lo alto, destaca por el desorden que arma en cinco minutos.</p>
    </div>
""", unsafe_allow_html=True)

# Sección 3: Los Visajes Delicados
st.markdown("<h3 class=\"subtitulo-seccion\">🌈 La energía sospechosa que se le sale</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="cuerpo-texto">
        <p>Por último, está el tema del que todos hablamos a escondidas: sus conductas sospechosas. Ipia intenta dárselas de muy parado en el salón, usando palabras pesadas y diciéndole '¿Qué dice, mi pez?' a todo el mundo para fingir rudeza. Pero los que nos sentamos con él sabemos la firme. Ese quiebre de muñeca automático que le da cuando se emociona hablando, la forma tan sutil en la que analiza la contextura física de los demás manes en el gimnasio, o el hecho de que se sepa completas las canciones de Karol G y La Rosalía y las tararee en voz baja en mitad de clase, nos deja claro que a nuestro amigo se le moja la canoa de una manera monumental. Ningún pantalón ancho va a tapar la delicadeza con la que pestañea cuando está distraído.</p>
    </div>
""", unsafe_allow_html=True)

# 6. MÓDULO INTERACTIVO (Buzón de firmas del salón)
st.write("---")
st.markdown("<h3 style='font-family: Georgia, serif; text-align: center;'>✍️ Respaldar la Columna (Testimonios del Salón)</h3>", unsafe_allow_html=True)
st.write("Como compañero de clase o testigo de los visajes de Ipia, deja aquí tu aporte anónimo para validar esta investigación estudiantil:")

# Inicialización de variables en session_state
if "procesado" not in st.session_state:
    st.session_state.procesado = False
if "resultado_actual" not in st.session_state:
    st.session_state.resultado_actual = ""

# Casilla libre
aporte_usuario = st.text_area(
    "Tu testimonio o anécdota sobre Sebastián:",
    placeholder="Ej: Yo confirmo lo de los tenis blancos, ayer caminaba empinado para verse de la misma altura que el profe...",
    key="input_aporte"
)

# Resultados periodísticos irónicos
conclusiones_prensa = [
    "📰 REPORTE DEL DELEGADO DE CURSO: Tras recopilar tu testimonio, el comité del salón confirma que Ipia mide lo mismo que un bolso escolar y bota más plumas que una almohada vieja. El caso queda archivado como 'Recontra confirmado'.",
    "📰 OBSERVACIÓN DEL PUESTO DE ATRÁS: Se añade la evidencia al expediente. La ciencia del salón demuestra que entre más bajito es el estudiante, mayor es su necesidad de bailar los temas de Karol G haciendo poses raras frente al tablero.",
    "📰 VERDICTO DEL GRUPO DE EXPOSICIÓN: Testigos confirman que el camuflaje rudo de Sebastián falló. Su recocha ya no puede ocultar que camina en puntitas y que se le quiebra la muñeca solita al recibir un papel.",
    "📰 INFORME GENERAL DEL RECREO: Los datos enviados colaron el sistema por exceso de sospecha. Veredicto final de los panas: Es chiquito, desordenado y se le nota a leguas lo pato.",
    "📰 ACTA DE CONVIVENCIA NO OFICIAL: El análisis de tu aporte confirma de manera unánime que a nuestro amigo se le va la canoa de medio lado de forma irreversible, por más que hable grueso."
]

if st.button("📝 REGISTRAR MI TESTIMONIO EN LA COLUMNA", use_container_width=True):
    if not aporte_usuario:
        st.warning("⚠️ Escribe algo en el buzón para poder añadir tu firma al informe del salón.")
    else:
        # Animación de procesamiento
        with st.spinner("Compartiendo testimonio con el grupo..."):
            time.sleep(1.2)
        with st.spinner("Analizando evidencias..."):
            time.sleep(1.0)
        with st.spinner("Guardando en el archivo anónimo del salón..."):
            time.sleep(0.8)
        
        # Guardar conclusión y limpiar
        st.session_state.resultado_actual = random.choice(conclusiones_prensa)
        st.session_state.procesado = True
        st.rerun()

# Despliegue de los resultados
if st.session_state.procesado:
    st.markdown(f"""
        <div class="resultado-editorial">
            <strong>📊 NOTA ADICIONAL DEL COMITÉ DE COMPAÑEROS:</strong><br><br>
            {st.session_state.resultado_actual}
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Registrar un nuevo testimonio"):
        st.session_state.procesado = False
        st.session_state.resultado_actual = ""
        st.rerun()

st.write("---")
st.caption("📰 Diario G • Columna Estudiantil Independiente • Contenido para lectura exclusiva de los panas • Prohibido mostrárselo a Ipia 🤫")
