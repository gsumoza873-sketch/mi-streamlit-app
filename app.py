import streamlit as st

# 1. Configuración de la tienda
st.set_page_config(page_title="Mi Tienda Virtual", page_icon="🛒")

st.title("🛒 Mi Mini Tienda Virtual")
st.write(f"Bienvenido a la tienda de **Gabriel**. ¡Elige tus productos!")

# 2. Base de datos de productos (puedes cambiar los nombres y precios)
productos = {
    "Laptop Gamer": 1200,
    "Audífonos Bluetooth": 50,
    "Mouse Inalámbrico": 25,
    "Monitor 4K": 300,
    "Teclado Mecánico": 80
}

# 3. Creación del Carrito de Compras en la barra lateral
st.sidebar.header("🛒 Tu Carrito")
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# 4. Mostrar productos en la página principal
col1, col2 = st.columns(2)

for i, (nombre, precio) in enumerate(productos.items()):
    # Alternamos entre columna 1 y columna 2 para que se vea como galería
    contenedor = col1 if i % 2 == 0 else col2
    
    with contenedor:
        st.subheader(nombre)
        st.write(f"Precio: **${precio}**")
        if st.button(f"Añadir {nombre}", key=nombre):
            if nombre in st.session_state.carrito:
                st.session_state.carrito[nombre] += 1
            else:
                st.session_state.carrito[nombre] = 1
            st.toast(f"¡{nombre} añadido!")

# 5. Lógica del Carrito (Barra lateral)
total = 0
if not st.session_state.carrito:
    st.sidebar.write("El carrito está vacío.")
else:
    for item, cantidad in st.session_state.carrito.items():
        subtotal = productos[item] * cantidad
        total += subtotal
        st.sidebar.write(f"{item} (x{cantidad}): **${subtotal}**")
    
    st.sidebar.write("---")
    st.sidebar.write(f"### Total: **${total}**")
    
    if st.sidebar.button("Vaciar Carrito"):
        st.session_state.carrito = {}
        st.rerun()

    if st.sidebar.button("Finalizar Compra"):
        st.balloons()
        st.sidebar.success(f"¡Gracias por tu compra de ${total}!")

# Firma
st.sidebar.markdown("---")
st.sidebar.info("Creado por **Gabriel**")
