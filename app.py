import streamlit as st

# 1. Configuración de la App
st.set_page_config(
    page_title="Penalty Shootout Pro",
    page_icon="⚽",
    layout="centered"
)

# Estilo oscuro de fondo para la app de Streamlit
st.markdown("<style>.stApp { background-color: #060d17; color: #f1f5f9; }</style>", unsafe_allow_html=True)

# Encabezado principal
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>⚽ Penalty Shootout Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Apunta haciendo clic en las zonas del arco y patea el balón.</p>", unsafe_allow_html=True)

# 2. Juego Interactivo en HTML5, CSS y JavaScript incrustado en Streamlit
juego_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background-color: #060d17;
            color: #f1f5f9;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin: 0;
            padding: 10px;
        }
        
        /* Contenedor del Estadio */
        .estadio {
            position: relative;
            width: 100%;
            max-width: 600px;
            height: 380px;
            background: linear-gradient(to bottom, #1e3a8a 30%, #15803d 30%);
            margin: 0 auto;
            border-radius: 15px;
            border: 4px solid #1e40af;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        }

        /* Líneas de la cancha */
        .linea-meta {
            position: absolute;
            top: 30%;
            left: 0;
            width: 100%;
            height: 3px;
            background-color: rgba(255, 255, 255, 0.6);
        }

        /* El Arco de Fútbol */
        .arco {
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
            width: 320px;
            height: 120px;
            border: 6px solid #ffffff;
            border-bottom: none;
            background-color: rgba(255, 255, 255, 0.15);
            display: flex;
            justify-content: space-between;
        }

        /* Zonas del arco para hacer clic */
        .zona-tiro {
            width: 33%;
            height: 100%;
            cursor: pointer;
            transition: background-color 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 12px;
            color: rgba(255, 255, 255, 0.3);
        }
        .zona-tiro:hover {
            background-color: rgba(59, 130, 246, 0.4);
            color: #ffffff;
        }

        /* Silueta del Arquero */
        .arquero {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 85px;
            background-size: contain;
            background-repeat: no-repeat;
            background-position: bottom center;
            /* Silueta SVG limpia de un arquero con los brazos abiertos */
            background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23f43f5e'><path d='M12 2a2 2 0 1 1-2 2 2 2 0 0 1 2-2zm9 7h-6v11h-2v-6h-2v6H9V9H3V7h18z'/></svg>");
            transition: all 0.5s ease-out;
        }

        /* El Balón de Fútbol */
        .balon {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            background-size: contain;
            background-repeat: no-repeat;
            /* Silueta SVG de balón de fútbol clásico */
            background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512' fill='%23ffffff'><path d='M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm0 416c-18.4 0-36.1-3.2-52.7-9.1l32.1-55.6c4.6-8 4.6-17.9 0-25.9L212 294.8c-4.6-8-13.2-12.9-22.4-12.9H121c-4.2-13.9-6.4-28.7-6.4-43.9s2.2-30 6.4-43.9h68.6c9.2 0 17.8-4.9 22.4-12.9L235.4 142c4.6-8 4.6-17.9 0-25.9l-32.1-55.6C219.9 54.5 237.6 51.3 256 51.3s36.1 3.2 52.7 9.1l-32.1 55.6c-4.6 8-4.6 17.9 0 25.9L300 178.4c4.6 8 13.2 12.9 22.4 12.9h68.6c4.2 13.9 6.4 28.7 6.4 43.9s-2.2 30-6.4 43.9h-68.6c-9.2 0-17.8 4.9-22.4 12.9L276.6 332c-4.6 8-4.6 17.9 0 25.9l32.1 55.6c-16.6 5.9-34.3 9.1-52.7 9.1z'/></svg>");
            transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        /* Silueta del Pateador */
        .pateador {
            position: absolute;
            bottom: 30px;
            left: 38%;
            width: 60px;
            height: 100px;
            background-size: contain;
            background-repeat: no-repeat;
            /* Silueta SVG de futbolista a punto de patear */
            background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%233b82f6'><path d='M16.5 1.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM12 9l-4 3h2v8H8v-4H4v-2h4v-3H6.5c-.83 0-1.5-.67-1.5-1.5S5.67 8 6.5 8h5.6l2.1-2.1L16 7.4 13.4 10H12z'/></svg>");
            transform-origin: bottom center;
            transition: all 0.4s ease;
        }

        /* Interfaz de Marcador */
        .marcador {
            display: flex;
            justify-content: space-around;
            background-color: #0f172a;
            border-radius: 10px;
            padding: 10px;
            margin-top: 15px;
            border: 1px solid #1e293b;
        }

        .valor {
            font-size: 20px;
            font-weight: bold;
            color: #3b82f6;
        }

        .btn-reset {
            background-color: #3b82f6;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 10px;
        }
        .btn-reset:hover {
            background-color: #2563eb;
        }
    </style>
</head>
<body>

    <div class="estadio">
        <div class="linea-meta"></div>
        
        <!-- El Arco con sus Zonas Clickables -->
        <div class="arco">
            <div class="zona-tiro" onclick="patear('Izquierda')">IZQ</div>
            <div class="zona-tiro" onclick="patear('Centro')">CENTRO</div>
            <div class="zona-tiro" onclick="patear('Derecha')">DER</div>
            
            <!-- El Arquero dentro del arco -->
            <div id="arquero" class="arquero"></div>
        </div>

        <!-- El Jugador Pateador -->
        <div id="pateador" class="pateador"></div>

        <!-- El Balón -->
        <div id="balon" class="balon"></div>
    </div>

    <!-- Resultados en Vivo -->
    <div class="marcador">
        <div>⚽ GOLES: <span id="marcador-goles" class="valor">0</span></div>
        <div>🧤 ATAJADAS: <span id="marcador-atajadas" class="valor">0</span></div>
    </div>
    
    <div id="resultado-texto" style="font-size: 18px; font-weight: bold; margin-top: 10px; min-height: 25px;">
        ¡Selecciona un lado en el arco para disparar!
    </div>

    <button class="btn-reset" onclick="resetearJuego()">Reiniciar Marcador</button>

    <script>
        let goles = 0;
        let atajadas = 0;
        let pateando = false;

        function patear(ladoUsuario) {
            if (pateando) return; // Evita doble clic durante la animación
            pateando = true;

            const balon = document.getElementById('balon');
            const arquero = document.getElementById('arquero');
            const pateador = document.getElementById('pateador');
            const resultadoTexto = document.getElementById('resultado-texto');

            // 1. Animación del Pateador corriendo hacia el balón
            pateador.style.transform = "scale(1.1) translateX(40px)";

            setTimeout(() => {
                // 2. Definir lanzada del arquero (IA)
                const opciones = ['Izquierda', 'Centro', 'Derecha'];
                const ladoArquero = opciones[Math.floor(Math.random() * opciones.length)];

                // Mover visualmente al arquero
                if (ladoArquero === 'Izquierda') {
                    arquero.style.left = '25%';
                    arquero.style.transform = 'rotate(-45deg) translateY(10px)';
                } else if (ladoArquero === 'Derecha') {
                    arquero.style.left = '75%';
                    arquero.style.transform = 'rotate(45deg) translateY(10px)';
                } else {
                    arquero.style.left = '50%';
                    arquero.style.transform = 'translateY(-15px)'; // Salto vertical
                }

                // 3. Mover visualmente el balón hacia la zona elegida
                if (ladoUsuario === 'Izquierda') {
                    balon.style.bottom = '220px';
                    balon.style.left = '32%';
                } else if (ladoUsuario === 'Derecha') {
                    balon.style.bottom = '220px';
                    balon.style.left = '68%';
                } else {
                    balon.style.bottom = '240px';
                    balon.style.left = '50%';
                }
                balon.style.transform = 'scale(0.5)'; // Simular profundidad

                // 4. Evaluar resultado del penal
                setTimeout(() => {
                    if (ladoUsuario === ladoArquero) {
                        atajadas++;
                        document.getElementById('marcador-atajadas').innerText = atajadas;
                        resultadoTexto.innerHTML = `<span style="color: #f87171;">🧤 ¡ATAJADA! El arquero adivinó a la ${ladoArquero}.</span>`;
                    } else {
                        goles++;
                        document.getElementById('marcador-goles').innerText = goles;
                        resultadoTexto.innerHTML = `<span style="color: #4ade80;">🔥 ¡GOOOOLAZO! Rompiste la red por la ${ladoUsuario}.</span>`;
                    }

                    // 5. Resetear posiciones de la jugada después de 2 segundos para el siguiente tiro
                    setTimeout(() => {
                        balon.style.bottom = '40px';
                        balon.style.left = '50%';
                        balon.style.transform = 'translateX(-50%) scale(1)';
                        
                        arquero.style.left = '50%';
                        arquero.style.transform = 'translateX(-50%)';
                        
                        pateador.style.transform = 'none';
                        resultadoTexto.innerText = "¡Apunta y dispara otra vez!";
                        pateando = false;
                    }, 2000);

                }, 400);

            }, 300);
        }

        function resetearJuego() {
            goles = 0;
            atajadas = 0;
            document.getElementById('marcador-goles').innerText = 0;
            document.getElementById('marcador-atajadas').innerText = 0;
            document.getElementById('resultado-texto').innerText = "Marcador reiniciado. ¡Patea!";
        }
    </script>
</body>
</html>
"""

# Renderizar el componente interactivo directamente en Streamlit
st.components.v1.html(juego_html, height=560)

# 3. Tu firma reglamentaria intacta en el pie de página de Streamlit
st.write("---")
st.caption("⚡ AI Learning Music Engine v5.2 • Sistema de Guía Teórica Dinámica • Hecho por Gabriel.s")
