import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# 1. Configuración de la App
st.set_page_config(
    page_title="Penalty Shootout Pro",
    page_icon="⚽",
    layout="centered"
)

# Estilo oscuro deportivo
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏆 Penalty Shootout Pro</h1>", unsafe_allow_html=True)

# Conexión a la base de datos de Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    conn = None

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
    st.write("Ingresa tu nombre o apodo para iniciar tu tanda de 10 penaltis y competir en el ranking:")
    
    nombre_input = st.text_input("Tu Nombre / Nickname:", placeholder="Ej. Gabriel_10", max_chars=15)
    
    if st.button("Empezar Desafío ⚽"):
        if nombre_input.strip():
            st.session_state.jugador = nombre_input.strip()
            st.session_state.partida_terminada = False
            st.session_state.goles_finales = 0
            # Limpiar parámetros de URL viejos al empezar
            st.query_params.clear()
            st.rerun()
        else:
            st.warning("Por favor, ingresa un nombre válido para registrar tu puntuación.")

# --- PANTALLA DE JUEGO ---
else:
    # Verificamos si JavaScript nos acaba de enviar el puntaje final por la URL
    goles_params = st.query_params.get("goles_final", None)
    
    if goles_params is not None and not st.session_state.partida_terminada:
        try:
            goles_guardar = int(goles_params)
        except ValueError:
            goles_guardar = 0
            
        st.session_state.goles_finales = goles_guardar
        st.session_state.partida_terminada = True
        
        # Guardar automáticamente en Google Sheets
        if conn:
            try:
                try:
                    df_actual = conn.read(ttl="0s")
                except Exception:
                    df_actual = pd.DataFrame(columns=["Nombre", "Goles", "Fecha"])
                
                if df_actual is None or df_actual.empty:
                    df_actual = pd.DataFrame(columns=["Nombre", "Goles", "Fecha"])

                nueva_fila = pd.DataFrame([{
                    "Nombre": st.session_state.jugador,
                    "Goles": goles_guardar,
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
                }])
                
                df_actualizado = pd.concat([df_actual, nueva_fila], ignore_index=True)
                conn.update(data=df_actualizado)
                st.balloons()
            except Exception as e:
                st.error("No se pudo guardar en la base de datos. Revisa tus Secrets de Streamlit.")

    # Si la tanda terminó, bloqueamos el juego y ofrecemos reiniciar
    if st.session_state.partida_terminada:
        st.markdown(f"""
        <div style='background-color: #1e1b4b; border-radius: 12px; padding: 20px; text-align: center; border: 2px solid #7c3aed;'>
            <h2 style='color: #a78bfa;'>🏁 ¡Tanda Finalizada!</h2>
            <p style='font-size: 24px;'>Anotaste <b>{st.session_state.goles_finales}</b> de 10 penaltis.</p>
            <p style='color: #4ade80; font-weight: bold;'>¡Tu puntuación ha sido guardada con éxito en la base de datos! 🎉</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Volver a jugar (Cambiar de jugador) 🔄"):
            st.session_state.jugador = ""
            st.session_state.partida_terminada = False
            st.session_state.goles_finales = 0
            st.query_params.clear()
            st.rerun()
            
    # Si sigue jugando, renderizamos el estadio dinámico
    else:
        st.markdown(f"👤 Jugador: **{st.session_state.jugador}** | 🎯 Objetivo: **10 tiros máximos**")
        
        # Todo el juego corre rápido en JS para evitar congelamientos
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

                        // Actualizar textos en caliente sin recargar
                        document.getElementById('goles-count').innerText = goles;
                        document.getElementById('tiros-count').innerText = tiros;

                        // Reiniciar posiciones para el siguiente tiro
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
                                // Tanda terminada: Enviar el resultado final de golpe a Streamlit
                                res.innerHTML = "<span style='color: #7c3aed;'>⏱️ Guardando tu puntuación...</span>";
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

# --- TABLA DE CLASIFICACIÓN (RANKING TOP 10) ---
st.markdown("---")
st.markdown("## 🏆 Tabla de Líderes (TOP 10)")

if conn:
    try:
        df = conn.read(ttl="0s")
        if df is not None and not df.empty:
            df_leaderboard = df.sort_values(by="Goles", ascending=False).head(10).reset_index(drop=True)
            
            tabla_html = "| Puesto | 👤 Jugador | ⚽ Goles de 10 | 📅 Fecha |\n| :---: | :--- | :---: | :---: |\n"
            for index, row in df_leaderboard.iterrows():
                medalla = "🥇" if index == 0 else "🥈" if index == 1 else "🥉" if index == 2 else "🏃‍♂️"
                tabla_html += f"| {medalla} {index+1} | **{row['Nombre']}** | **{row['Goles']}** / 10 | {row['Fecha']} |\n"
            
            st.markdown(tabla_html)
        else:
            st.info("Aún no hay puntuaciones registradas. ¡Sé el primero!")
    except Exception:
        st.warning("Conectando con la base de datos de líderes... (Revisa que tu Sheet esté configurado)")
else:
    st.info("Configura las credenciales de Google Sheets para activar el ranking en línea.")

# Pie de página
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.2 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
