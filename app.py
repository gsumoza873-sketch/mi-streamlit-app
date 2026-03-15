import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Gabriel's Luxury Store", page_icon="💎", layout="wide")

# Estilo CSS avanzado
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
        border: 1px solid rgba(0, 212, 255, 0.3);
        text-align: center;
        margin-bottom: 20px;
    }
    img {
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Gabriel's Luxury Store")

# 2. Productos con sus IMÁGENES
productos = {
    "MacBook Pro": {"precio": 2500, "img": "http://googleusercontent.com/image_collection/image_retrieval/18232227657584336958_0"},
    "iPhone 15 Pro": {"precio": 1100, "img": "http://googleusercontent.com/image_collection/image_retrieval/14091339336383696798_0"},
    "AirPods Max": {"precio": 550, "img": "http://googleusercontent.com/image_collection/image_retrieval/1541256072169642398_0"},
    "Apple Watch": {"precio": 400, "img": "http://googleusercontent.com/image_collection/image_retrieval/13117506816291691781_0"}
}

if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 3. Mostrar productos con FOTOS
cols = st.columns(4)
for i, (nombre, info) in enumerate(productos.items()):
    with cols[i]:
        st.markdown(f'<div class="product-box">', unsafe_allow_html=True)
        st.image(info["img"])
        st.subheader(nombre)
        st.write(f"**${info['precio']}**")
        if st.button(f"Comprar", key=nombre):
            st.session_state.carrito[nombre] = st.session_state.carrito.get(nombre, 0) + 1
            st.toast(f"✅ {nombre} añadido")
        st.markdown('</div>', unsafe_allow_html=True)

# 4. Carrito
with st.sidebar:
    st.header("🛒 Tu Carrito")
    total = 0
    for item, cant in st.session_state.carrito.items():
        sub = productos[item]["precio"] * cant
        total += sub
        st.write(f"{item} x{cant}: ${sub}")
    st.divider()
    st.write(f"### Total: ${total}")
    if st.button("Pagar Ahora"):
        st.balloons()
