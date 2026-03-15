import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Gabriel's Luxury Store", page_icon="💎", layout="wide")

# Estilo CSS para colores y diseño
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    h1 {
        color: #00d4ff;
        text-align: center;
        font-family: 'Arial';
    }
    .product-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #00d4ff;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Gabriel's Luxury Store")
st.write("<p style='text-align: center;'>Diseño exclusivo y elegante</p>", unsafe_allow_html=True)

# 2. Productos
productos = {
    "MacBook Pro": 2500,
    "iPhone 15": 1100,
    "AirPods Max": 550,
    "Apple Watch": 400
}

# Inicializar carrito
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 3. Mostrar productos
col1, col2, col3, col4 = st.columns(4)
columnas = [col1, col2, col3, col4]

for i, (nombre, precio) in enumerate(productos.items()):
    with columnas[i]:
        st.markdown(f"""
            <div class="product-box">
                <h3>{nombre}</h3>
                <p style="color: #00d4ff; font-size: 20px;"><b>${precio}</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Agregar", key=f"btn_{nombre}"):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"{nombre} añadido")

# 4. Barra Lateral
with st.sidebar:
    st.header("🛒 Tu Carrito")
    total = 0
    if not st.session_state.carrito:
        st.write("Está vacío")
    else:
        for item, cant in list(st.session_state.carrito.items()):
            if item in productos:
                sub = productos[item] * cant
                total += sub
                st.write(f"**{item}** (x{cant}): ${sub}")
        
        st.divider()
        st.write(f"## Total: ${total}")
        
        if st.button("Limpiar Carrito"):
            st.session_state.carrito = {}
            st.rerun()
            
    st.markdown("---")
    st.info("Creado por **Gabriel**")
