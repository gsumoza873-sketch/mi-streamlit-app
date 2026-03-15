import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Gabriel's Minimal Store", page_icon="🛍️", layout="wide")

# Estilo CSS para fondo blanco y diseño limpio
st.markdown("""
    <style>
    /* Fondo de la página en blanco */
    .stApp {
        background-color: #FFFFFF;
        color: #1E1E1E;
    }
    
    /* Títulos en negro elegante */
    h1, h2, h3 {
        color: #1E1E1E !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }

    /* Tarjetas de productos blancas con sombra suave */
    .product-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #eeeeee;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .product-box:hover {
        box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
        background-color: #ffffff;
    }

    /* Botones en un color azul moderno o negro */
    .stButton>button {
        background-color: #007AFF; /* Azul estilo iOS */
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }

    /* Ajuste para la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #f1f3f5;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛍️ Gabriel's Store")
st.write("<p style='text-align: center; color: #666666;'>Calidad y elegancia en cada detalle.</p>", unsafe_allow_html=True)
st.divider()

# 2. Productos
productos = {
    "MacBook Pro": 2500,
    "iPhone 15": 1100,
    "AirPods Max": 550,
    "Apple Watch": 400
}

if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 3. Mostrar productos
col1, col2, col3, col4 = st.columns(4)
columnas = [col1, col2, col3, col4]

for i, (nombre, precio) in enumerate(productos.items()):
    with columnas[i]:
        st.markdown(f"""
            <div class="product-box">
                <p style="font-size: 40px; margin: 0;">📦</p>
                <h3>{nombre}</h3>
                <p style="color: #007AFF; font-size: 22px;"><b>${precio}</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Añadir", key=f"btn_{nombre}"):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"¡{nombre} añadido!")

# 4. Barra Lateral
with st.sidebar:
    st.header("🛒 Mi Carrito")
    total = 0
    if not st.session_state.carrito:
        st.
