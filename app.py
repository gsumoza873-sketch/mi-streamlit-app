import streamlit as st

# Configuración
st.set_page_config(page_title="Trivia Médica para Fariana", page_icon="🩺")

st.title("🩺 ¡Bienvenida, Fariana!")
st.subheader("Demuestra tus conocimientos con estas 5 preguntas fáciles")

# Puntuación en la sesión
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0

# Pregunta 1
st.write("---")
p1 = st.radio("1. ¿Cuál es el órgano que bombea sangre a todo el cuerpo?", 
              ["Pulmones", "Cerebro", "Corazón", "Hígado"])

# Pregunta 2
st.write("---")
p2 = st.radio("2. ¿Cuántos litros de agua se recomienda beber al día aproximadamente?", 
              ["500 ml", "2 Litros", "10 Litros", "1 vaso"])

# Pregunta 3
st.write("---")
p3 = st.radio("3. ¿Cuál es el instrumento que usan los médicos para escuchar el corazón?", 
              ["Termómetro", "Estetoscopio", "Martillo de reflejos", "Bisturí"])

# Pregunta 4
st.write("---")
p4 = st.radio("4. ¿Qué nutriente nos da el sol principalmente?", 
              ["Vitamina C", "Hierro", "Vitamina D", "Calcio"])

# Pregunta 5
st.write("---")
p5 = st.radio("5. ¿Cuál es la temperatura normal promedio del cuerpo humano?", 
              ["30°C", "37°C", "42°C", "25°C"])

# Botón de resultados
st.write("---")
if st.button("Ver mi calificación 🏆"):
    nota = 0
    if p1 == "Corazón": nota += 1
    if p2 == "2 Litros": nota += 1
    if p3 == "Estetoscopio": nota += 1
    if p4 == "Vitamina D": nota += 1
    if p5 == "37°C": nota += 1
    
    if nota >= 4:
        st.success(f"¡Increíble Fariana! Sacaste {nota}/5. ¡Eres toda una experta!")
        st.balloons()
    else:
        st.warning(f"Buen intento, Fariana. Sacaste {nota}/5. ¡Sigue estudiando!")

st.sidebar.info("Minijuego creado por Gabriel.")
