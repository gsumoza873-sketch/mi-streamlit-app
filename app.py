import streamlit as st

# 1. Configuración
st.set_page_config(page_title="Gabriel's Luxury Store", page_icon="💎", layout="wide")

# Diseño Visual
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    .product-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #00d4ff;
        text-align: center;
        min-height: 400px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Gabriel's Luxury Store")

# 2. Productos con fotos de alta disponibilidad
productos = {
    "MacBook Pro": {"precio": 2500, "img": "https://images.unsplash.com/photo-1517336712461-83ad53ffbbdf?w=500&q=80"},
    "iPhone 15 Pro": {"precio": 1100, "img": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500&q=80"},
    "AirPods Max": {"precio": 550, "img": "https://images.unsplash.com/photo-1613040809024-b4ef7ba99bc3?w=500&q=80"},
    "Apple Watch": {"precio": 400, "img": "https://images.unsplash.com/photo-1546868871-70c122467d9b?w=500&q=80"}
}

if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 3. Galería de Productos
cols = st.columns(4)
for i, (nombre, info) in enumerate(productos.items()):
    with cols[i]:
        st.markdown('<div class="product-box">', unsafe_allow_html=True)
        # Usamos st.image de forma sencilla
        st.image(info["img"], caption=nombre, use_container_width=True)
        st.write(f"Precio: **${info['precio']}**")
        if st.button(f"Añadir al carrito", key=f"add_{nombre}"):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"✅ {nombre} añadido")
        st.markdown('</div>', unsafe_allow_html=True)

# 4. Barra Lateral
with st.sidebar:
    st.header("🛒 Tu Compra")
    total = 0
    items_en_carrito = list(st.session_state.carrito.items())
    
    if not items_en_carrito:
        st.write("Tu carrito está vacío.")
    else:
        for item, cant in items_en_carrito:
            if item in productos:
                subtotal = productos[item]["precio"] * cant
                total += subtotal
                st.write(f"**{item}** x{cant}: ${subtotal}")
        
        st.divider()
        st.write(f"## Total: ${total}")
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = {}
            st.rerun()

    st.markdown("---")
    st.info("Creado por **Gabriel**")
