import streamlit as st
from supabase import create_client

# 1. Configuración de la Conexión (Usando tus Secrets)
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except:
    st.error("Error: No se encontraron los Secrets. Revisa la configuración en Streamlit.")

# 2. Interfaz Estilo Futbolero
st.set_page_config(page_title="Fanático VIP", page_icon="⚽")

# Título con estilo
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>⚽ Cuestionario del Fanático Pro</h1>", unsafe_allow_html=True)
st.write("---")

# 3. Casilla para el Nombre (¡Aquí está lo que faltaba!)
st.subheader("👤 Registro de Jugador")
nombre_usuario = st.text_input("Escribe tu nombre o apodo futbolero:", placeholder="Ej: Gabriel el 10")

# 4. El Cuestionario
st.subheader("🏆 El Test del Hincha")

pregunta_1 = st.selectbox(
    "¿Cuál es el mejor equipo del mundo actualmente?",
    ["Real Madrid", "Manchester United", "Manchester City", "Tigres de Aragua", "Otro"]
)

pregunta_2 = st.radio(
    "¿Quién es el mejor de la historia?",
    ["Lionel Messi", "Cristiano Ronaldo", "Pelé", "Maradona"]
)

# 5. Botón de Enviar con Lógica de Guardado
st.write("---")
if st.button("🚀 ENVIAR RESULTADOS AL VAR"):
    if nombre_usuario:
        try:
            # Preparamos los datos para la tabla
            # 'resultado' guardará las dos respuestas combinadas
            res_combinado = f"Equipo: {pregunta_1} | Ídolo: {pregunta_2}"
            
            datos = {
                "nombre": nombre_usuario, 
                "resultado": res_combinado
            }
            
            # Guardamos en la tabla que creaste
            supabase.table("respuestas_test").insert(datos).execute()
            
            st.balloons()
            st.success(f"¡GOLAZO {nombre_usuario}! Tus datos se guardaron en la base de datos de Suramérica.")
            
        except Exception as e:
            st.error(f"Hubo un error al conectar con el VAR (Base de datos): {e}")
    else:
        st.warning("⚠️ ¡Tarjeta Amarilla! Tienes que poner tu nombre para poder jugar.")

# Pie de página
st.markdown("<br><p style='text-align: center; color: gray;'>Proyecto conectado a Supabase Cloud</p>", unsafe_allow_html=True)
