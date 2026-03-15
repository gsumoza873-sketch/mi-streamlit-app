import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Saludo para Matías", page_icon="👋")

# Título principal
st.title("¡Hola Matías! ¿Cómo estás?")

# Casilla de respuesta (Input)
respuesta = st.text_input("Cuéntame cómo va tu día:", placeholder="Escribe aquí...")

# Botón y lógica de respuesta
if st.button("Enviar respuesta"):
    if respuesta.strip():
        st.success(f"¡Qué bueno saber de ti, Matías! Dijiste: '{respuesta}'")
        st.balloons()  # Esto lanza los globos
    else:
        st.warning("Por favor, escribe algo antes de enviar.")
