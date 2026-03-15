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
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Gabriel's Luxury Store")

# 2. Diccionario de Productos (Simplificado)
# Las URLs son imágenes de ejemplo de alta calidad
productos = {
    "MacBook Pro": {"precio": 2500, "img": "https://m.media-amazon.com/images/I/618mS9vmSUL._AC_SL1500_.jpg"},
    "iPhone 15 Pro": {"precio": 1100, "img": "https://m.media-amazon.com/images/I/81SigFo7_LL._AC_SL1500_.jpg"},
    "AirPods Max": {"precio": 550, "img": "https://m.media-amazon.com/images/I/815mXvXQRAL._AC_SL1500_.jpg"},
    "Apple Watch": {"precio": 400, "img": "https://m.media-amazon.com/images/I/71LfnkS8SUL._AC_SL1500_.jpg"}
}

# Inicializar carrito de forma segura
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 3. Galería de Productos
cols = st.columns(4)
for i, (nombre, info) in enumerate(productos.items()):
    with cols[i]:
        st.markdown('<div class="product-box">', unsafe_allow_html=True)
        st.image(info["img"], use_container_width=True)
        st.subheader(nombre)
        st.write(f"Precio: **${info['precio']}**")
        if st.button(f"Añadir", key=f"add_{nombre}"):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"✅ {nombre} añadido")
        st.markdown('</div>', unsafe_allow_html=True)

# 4. Barra Lateral (Carrito)
with st.sidebar:
    st.header("🛒 Tu Compra")
    total = 0
    
    # Solo procesamos lo que está en nuestro diccionario actual
    items_en_carrito = list(st.session_state.carrito.items())
    
    if not items_en_carrito:
        st.write("Tu carrito está vacío.")
    else:
        for item, cant in items_en_carrito:
            if item in productos: # <-- ESTO EVITA EL ERROR DE LA FOTO
                subtotal = productos[item]["precio"] * cant
                total += subtotal
                st.write(f"**{item}** x{cant}: ${subtotal}")
        
        st.divider()
        st.write(f"## Total: ${total}")
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = {}
            st.rerun()
        
        if st.button("Pagar por WhatsApp"):
            st.balloons()
            st.success("¡Pedido enviado!")

    st.markdown("---")
    st.info("Creado por **Gabriel**")
