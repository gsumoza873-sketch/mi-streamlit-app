import streamlit as st
import time
import random

# 1. Configuración de la página (Estilo Portal de Prensa)
st.set_page_config(
    page_title="El Vocero Estudiantil",
    page_icon="📰",
    layout="centered"
)

# 2. Estilos CSS para simular una Columna de Opinión Periodística seria
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
        font-size: 42px;
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

# 3. Cabecera del Portal Informativo
st.markdown("""
    <div class="header-periodico">
        <div class="nombre-diario">EL DIARIO CENTRAL</div>
        <div class="meta-info">
            <span>Sección: Opinión y Convivencia Escolar</span>
            <span>Columna del Salón</span>
            <span>Estatus: Artículo de Opinión</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Titular, Autor y Subtítulo
st.markdown("""
    <div class="titular-principal">Convivir con el misterio de Ipia: Una mirada desde el pupitre de al lado</div>
    <div class="autor-columna">Por: Un compañero de clase y amigo cercano</div>
    <div class="subtitulo-articulo">Crónica sincera sobre cómo es aguantarse el desorden diario de Sebastián, su estatura de llavero y esos gestos que nos hacen dudar a todos en el salón.</div>
""", unsafe_allow_html=True)

# 5. Cuerpo del Artículo (Desde tu perspectiva)
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
st.
