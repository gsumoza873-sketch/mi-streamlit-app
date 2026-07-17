import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 1. Configuración de la App
st.set_page_config(
    page_title="Penalty Shootout Pro",
    page_icon="⚽",
    layout="centered"
)

# Estilo oscuro deportivo
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Penalty Shootout Pro</h1>", unsafe_allow_html=True)

# URL de tu Google Sheet (Debe estar compartida como "Cualquier persona con el enlace puede EDITAR")
URL_HOJA = "https://docs.google.com/spreadsheets/d/1OWjj8Rig4ENu2IhiuljqZtBRg3xq0np01qRFxO_Tehg/edit?usp=sharing"

# Conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Función segura para leer las puntuaciones reales
def cargar_puntuaciones():
    try:
        # Lee la hoja de cálculo
        df = conn.read(spreadsheet=URL_HOJA, ttl="0s") # ttl=0s evita que use memoria caché y siempre lea los datos reales
        # Si la hoja está vacía o no tiene las columnas correctas
        if df.empty or "Nombre" not in df.columns or "Goles" not in df.columns:
            return pd.DataFrame(columns=["Nombre", "Goles"])
        return df
    except Exception:
        return pd.DataFrame(columns=["Nombre", "Goles"])

# Función para añadir el nuevo puntaje a Google Sheets
def guardar_puntuacion(nombre, goles):
    try:
        # 1. Descargamos la tabla actual
        df_actual = cargar_puntuaciones()
        
        # 2. Creamos la nueva fila con tu amigo
        nueva_fila = pd.DataFrame([{"Nombre": str(nombre), "Goles": int(goles)}])
        
        # 3. Juntamos los datos viejos con el nuevo jugador
        df_actualized = pd.concat([df_actual, nueva_fila], ignore_index=True)
        
        # 4. Lo subimos de vuelta a Google Sheets
        conn.update(spreadsheet=URL_HOJA, data=df_actualized)
        st.cache_data.clear() # Limpiamos la caché de Streamlit para que muestre el cambio de inmediato
    except Exception as e:
        st.error(f"Error al guardar en Google Sheets: {e}")

# 2. Control de Estado del Jugador en la sesión
if "jugador" not in st.session_state:
    st.session_state.jugador = ""
if "partida_terminada" not in st.session_state:
    st.session_state.partida_terminada = False
if "goles_finales" not in st.session_state:
    st.session_state.goles_finales = 0

# --- PANTALLA DE REGISTRO ---
if not st.session_state.jugador:
    st.markdown("### 📝 Regístrate para Jugar")
    st.write("Ingresa tu nombre para iniciar tu tanda de 10 penaltis y guardar tu récord:")
    
    nombre_input = st.text_input("Tu Nombre:", placeholder="Ej. Gabriel", max_chars=15)
    
    if st.button("Empezar Desafío ⚽"):
        if nombre_input.strip():
            st.session_state.jugador = nombre_input.strip()
            st.session_state.partida_terminada = False
            st.session_state.goles_finales = 0
            st.query_params.clear()
            st.rerun()
        else:
            st.warning("Por favor, ingresa tu nombre para poder registrar tu puntuación.")

# --- PANTALLA DE JUEGO ---
else:
    goles_params = st.query_params.get("goles_final", None)
    
    if goles_params is not None and not st.session_state.partida_terminada:
        try:
            goles_guardar = int(goles_params)
        except ValueError:
            goles_guardar = 0
            
        st.session_state.goles_finales = goles_guardar
        st.session_state.partida_terminada = True
        
        # Guardar automáticamente en Google Sheets
        guardar_puntuacion(st.session_state.jugador, goles_guardar)
        st.balloons()

    # Si la tanda terminó, mostramos el resultado
    if st.session_state.partida_terminada:
        st.markdown(f"""
        <div style='background-color: #1e1b4b; border-radius: 12px; padding: 20px; text-align: center; border: 2px solid #7c3aed;'>
            <h2 style='color: #a78bfa;'>🏁 ¡Tanda Finalizada!</h2>
            <p style='font-size: 24px;'>Anotaste <b>{st.session_state.goles_finales}</b> de 10 penaltis.</p>
            <p style='color: #4ade80; font-weight: bold;'>¡Tu puntuación ha sido registrada en Google Sheets! 🎉</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Volver a jugar (Cambiar de jugador) 🔄"):
            st.session_state.jugador = ""
            st.session_state.partida_terminada = False
            st.session_state.goles_finales = 0
            st.query_params.clear()
            st.rerun()
            
    # Si sigue jugando, cargamos el estadio interactivo
    else:
        st.markdown(f"👤 Jugador: **{st.session_state.jugador}** | 🎯 Objetivo: **10 tiros máximos**")
        
        juego_html = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <style>
                body { background-color: #060d17; color: #f1f5f9; font-family: sans-serif; text-align: center; margin: 0; padding: 5px; }
                .estadio { position: relative; width: 100%; max-width: 550px; height: 320px; background: linear-gradient(to bottom, #1e3a8a 30%, #15803d 30%); margin: 0 auto; border-radius: 15px; border: 4px solid #1e40af; overflow: hidden; }
                .arco { position: absolute; top: 10%; left: 50%; transform: translateX(-50%); width: 280px; height: 110px; border: 5px solid #ffffff; border-bottom: none; background-color: rgba(255, 255, 255, 0.15); display: flex; }
                .zona-tiro { width: 33.3%; height: 100%; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 11px; color: rgba(255, 255, 255, 0.3); transition: 0.2s; }
                .zona-tiro:hover { background-color: rgba(59, 130, 246, 0.4); color: #fff; }
                .arquero { position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 45px; height: 75px; background-size: contain; background-repeat: no-repeat; background-position: bottom center; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23f43f5e'><path d='M12 2a2 2 0 1 1-2 2 2 2 0 0 1 2-2zm9 7h-6v11h-2v-6h-2v6H9V9H3V7h18z'/></svg>"); transition: all 0.5s ease-out; }
                .balon { position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); width: 26px; height: 26px; background-size: contain; background-repeat: no-repeat; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512' fill='%23ffffff'><path d='M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm0 416c-18.4 0-36.1-3.2-52.7-9.1l32.1-55.6c4.6-8 4.6-17.9 0-25.9L212 294.8c-4.6-8-13.2-12.9-22.4-12.9H121c-4.2-13.9-6.4-28.7-6.4-43.9s2.2-30 6.4-43.9h68.6c9.2 0 17.8-4.9 22.4-12.9L235.4 142c4.6-8 4.6-17.9 0-25.9l-32.1-55.6C219.9 54.5 237.6 51.3 256 51.3s36.1 3.2 52.7 9.1l-32.1 55.6c-4.6 8-4.6 17.9 0 25.9L300 178.4c4.6 8 13.2 12.9 22.4 12.9h68.6c4.2 13.9 6.4 28.7 6.4 43.9s-2.2 30-6.4 43.9h-68.6c-9.2 0-17.8 4.9-22.4 12.9L276.6 332c-4.6 8-4.6 17.9 0 25.9l32.1 55.6c-16.6 5.9-34.3 9.1-52.7 9.1z'/></svg>"); transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94); }
                .marcador { display: flex; justify-content: space-around; background-color: #0f172a; border-radius: 10px; padding: 10px; margin-top: 15px; border: 1px solid #1e293b; }
                .valor { font-size: 18px; font-weight: bold; color: #3b82f6; }
            </style>
        </head>
        <body>
            <div class="estadio">
                <div class="arco">
                    <div class="zona-tiro" onclick="patear('Izquierda')">IZQ</div>
                    <div class="zona-tiro" onclick="patear('Centro')">CENTRO</div>
                    <div class="zona-tiro" onclick="patear('Derecha')">DER</div>
                    <div id="arquero" class="arquero"></div>
                </div>
                <div id="balon" class="balon"></div>
            </div>

            <div class="marcador">
                <div>⚽ GOLES: <span id="goles-count" class="valor">0</span></div>
                <div>📊 INTENTOS: <span id="tiros-count" class="valor">0</span> / 10</div>
            </div>
            
            <div id="res" style="font-size: 16px; font-weight: bold; margin-top: 10px; min-height: 25px; color: #94a3b8;">
                ¡Apunta al arco y dispara!
            </div>

            <script>
                let goles = 0;
                let tiros = 0;
                let bloqueado = false;

                function patear(ladoUsuario) {
                    if (bloqueado || tiros >= 10) return;
                    bloqueado = true;

                    const balon = document.getElementById('balon');
                    const arquero = document.getElementById('arquero');
                    const res = document.getElementById('res');

                    const opciones = ['Izquierda', 'Centro', 'Derecha'];
                    const ladoArquero = opciones[Math.floor(Math.random() * opciones.length)];

                    // Animación del Arquero
                    if (ladoArquero === 'Izquierda') {
                        arquero.style.left = '25%';
                        arquero.style.transform = 'rotate(-45deg)';
                    } else if (ladoArquero === 'Derecha') {
                        arquero.style.left = '75%';
                        arquero.style.transform = 'rotate(45deg)';
                    } else {
                        arquero.style.left = '50%';
                        arquero.style.transform = 'translateY(-10px)';
                    }

                    // Animación del Balón
                    if (ladoUsuario === 'Izquierda') {
                        balon.style.bottom = '180px';
                        balon.style.left = '32%';
                    } else if (ladoUsuario === 'Derecha') {
                        balon.style.bottom = '180px';
                        balon.style.left = '68%';
                    } else {
                        balon.style.bottom = '200px';
                        balon.style.left = '50%';
                    }
                    balon.style.transform = 'scale(0.5)';

                    setTimeout(() => {
                        tiros++;
                        if (ladoUsuario === ladoArquero) {
                            res.innerHTML = "<span style='color: #f87171;'>🧤 ¡ATAJADA! El arquero se estiró bien.</span>";
                        } else {
                            goles++;
                            res.innerHTML = "<span style='color: #4ade80;'>🔥 ¡GOOOLAZO!</span>";
                        }

                        document.getElementById('goles-count').innerText = goles;
                        document.getElementById('tiros-count').innerText = tiros;

                        setTimeout(() => {
                            if (tiros < 10) {
                                balon.style.bottom = '30px';
                                balon.style.left = '50%';
                                balon.style.transform = 'scale(1)';
                                arquero.style.left = '50%';
                                arquero.style.transform = 'rotate(0deg)';
                                res.innerHTML = "¡Apunta otra vez y dispara!";
                                bloqueado = false;
                            } else {
                                res.innerHTML = "<span style='color: #7c3aed;'>⏱️ Registrando tu puntuación...</span>";
                                const url = new URL(window.parent.location.href);
                                url.searchParams.set("goles_final", goles);
                                window.parent.location.href = url.toString();
                            }
                        }, 1200);

                    }, 400);
                }
            </script>
        </body>
        </html>
        """
        st.components.v1.html(juego_html, height=440)

# --- 🏆 TABLA DE POSICIONES DESDE GOOGLE SHEETS ---
st.markdown("---")
st.markdown("## 🏆 Tabla de Puntuaciones (Líderes)")

df_puntuaciones = cargar_puntuaciones()

if not df_puntuaciones.empty:
    # Ordenamos de mayor a menor cantidad de goles
    df_ordenado = df_puntuaciones.sort_values(by="Goles", ascending=False)
    
    # Mostrar cada uno en el formato limpio solicitado
    for index, fila in df_ordenado.iterrows():
        st.markdown(f"• **{fila['Nombre']}** {fila['Goles']} de 10")
else:
    st.info("Aún no hay puntuaciones registradas. ¡Inicia una tanda y sé el primero!")

# Pie de página
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.3 • Hecho por Gabriel.s")
