import streamlit as st

st.title("Conversación")

st.write("¿Hola Sofia, por qué eres tan fea?")

respuesta = st.text_input("Sofia responde:")

if respuesta:
    if respuesta.lower() == "porque si":
        st.write("y punto")
    else:
        st.write("Respuesta no válida")