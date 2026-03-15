import streamlit as st

# 1. Configuración y Estilo Visual (CSS personalizado)
st.set_page_config(page_title="Gabriel's Luxury Store", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    /* Cambiar el fondo de la página */
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a40 100%);
        color: white;
    }
    
    /* Personalizar los títulos */
    h1 {
        color: #00d4ff;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Estilo para las tarjetas de productos */
    .product-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        background-color: rgba(255, 255, 255, 0.15);
    }

    /* Botones personalizados */
    .stButton>button {
        width: 100%;
        background-color: #00d4ff;
        color: black;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #008fb3;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado
st.title("💎 Gabriel's Luxury Store")
st.write("<p style='text-align: center; font-size: 1.2rem;'>La mejor tecnología con el mejor diseño.</p>", unsafe_allow_html=True)
st.write("---")

# 3. Datos de productos
productos = {
    "MacBook Pro": {"precio": 2500, "emoji": "💻"},
    "iPhone 15": {"precio": 1100, "emoji": "📱"},
    "AirPods Max": {"precio": 550, "emoji": "🎧"},
    "Apple Watch": {"precio": 400, "emoji": "⌚"}
}

# Carrito en el estado de la sesión
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 4. Diseño de la Galería (4 columnas)
cols = st.columns(4)

for i, (nombre, info) in enumerate(productos.items()):
    with cols[i]:
        st.markdown(f"""
            <div class="product-card">
                <h1 style="font-size: 50px; margin: 0;">{info['emoji']}</h1>
                <h3 style="color: white; margin-top: 10px;">{nombre}</h3>
                <p style="color: #00d4ff; font-size: 1.2rem;"><b>${info['precio']}</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Comprar {nombre}", key=nombre):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"✅ {nombre} añadido")

# 5. Barra Lateral (Diseño limpio)
with st.sidebar:
    st.header("🛒 Tu Compra")
    total = 0
    if not st.session_state.carrito:
        st.write("Carrito vacío.")
    else:
        for item, cant in st.session_state.carrito.items():
            sub = productos[item]['precio'] * cant
            total += sub
            st.write(f"**{item}** x{cant} = ${sub}")
        
        st.divider()
        st.write(f"## Total: ${total}")
        if st.button("Pagar Ahora"):
            st.balloons()
            st.success("¡Pedido realizado con éxito!")

    st.markdown("---")
    st.info("Diseño exclusivo por **Gabriel**")
