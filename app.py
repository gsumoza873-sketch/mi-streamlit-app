import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Trivia Médica para Fariana", page_icon="🩺")

st.title("🩺 ¡Bienvenida, Fariana!")
st.subheader("Responde y descubre cuánto sabes de medicina")
st.write("---")

# Definimos las preguntas y respuestas correctas
preguntas = [
    {
        "enunciado": "1. ¿Cuál es el órgano que bombea sangre a todo el cuerpo?",
        "opciones": ["Pulmones", "Cerebro", "Corazón", "Hígado"],
        "correcta": "Corazón"
    },
    {
        "enunciado": "2. ¿Cuántos litros de agua se recomienda beber al día aproximadamente?",
        "opciones": ["500 ml", "2 Litros", "10 Litros", "1 vaso"],
        "correcta": "2 Litros"
    },
    {
        "enunciado": "3. ¿Cuál es el instrumento que usan los médicos para escuchar el corazón?",
        "opciones": ["Termómetro", "Estetoscopio", "Martillo de reflejos", "Bisturí"],
        "correcta": "Estetoscopio"
    },
    {
        "enunciado": "4. ¿Qué nutriente nos da el sol principalmente?",
        "opciones": ["Vitamina C", "Hierro", "Vitamina D", "Calcio"],
        "correcta": "Vitamina D"
    },
    {
        "enunciado": "5. ¿Cuál es la temperatura normal promedio del cuerpo humano?",
        "opciones": ["30°C", "37°C", "42°C", "25°C"],
        "correcta": "37°C"
    }
]

# Guardamos las respuestas del usuario
respuestas_usuario = []
for i, p in enumerate(preguntas):
    res = st.radio(p["enunciado"], p["opciones"], key=f"pregunta_{i}")
    respuestas_usuario.append(res)
    st.write("---")

# Botón de resultados
if st.button("Finalizar y Revisar 🏆"):
    nota = 0
    st.write("### Resumen de tu examen:")
    
    for i, p in enumerate(preguntas):
        if respuestas_usuario[i] == p["correcta"]:
            st.success(f"Pregunta {i+1}: ¡Correcto! ({p['correcta']}) ✅")
            nota += 1
        else:
            st.error(f"Pregunta {i+1}: Incorrecto. Elegiste '{respuestas_usuario[i]}'. La respuesta correcta era: {p['correcta']} ❌")
    
    # Puntaje final
    if nota >= 4:
        st.balloons()
        st.write(f"## ¡Felicidades Fariana! Puntaje: {nota}/5")
    else:
        st.write(f"## Buen intento. Puntaje: {nota}/5. ¡A seguir practicando!")

# Barra lateral con tu crédito
st.sidebar.markdown("---")
st.sidebar.write("### 👨‍💻 Creado por:")
st.sidebar.info("**Gabriel**")
