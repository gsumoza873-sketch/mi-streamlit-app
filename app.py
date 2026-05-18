# Agrega "tab_amiga" a tu lista de pestañas arriba en el código, por ejemplo:
# tab_historia, tab_patrios, tab_naturales, tab_geografia, tab_amiga = st.tabs([...])

with tab_amiga:
    st.header("🧠 ¡Operativo Salvación! - Guía de Estudio para la Exposición")
    st.write("Dile a tu amiga que respire hondo. Aquí está el beta de los **Músculos Infrahioideos** explicado para que no se le olvide ni con los nervios en frente del profesor.")

    # Alerta motivacional/chistosa
    st.warning("⚠️ **Regla de oro para la exposición:** Si te quedas en blanco, di 'Hioides' con mucha seguridad. Ese hueso es el jefe de la zona.")

    # 1. INTRODUCCIÓN CON HUMOR
    st.markdown("""
    <div class="section-box" style="border-left: 5px solid #0038A8;">
        <h3>📍 ¿Qué son los Músculos Infrahioideos?</h3>
        <p>Para decírselo al profe: Son 4 pares de músculos delgados que están <b>debajo del hueso hioides</b>. Su trabajo principal es bajar el hioides y la laringe cuando tragamos o hablamos.</p>
        <p><b>Para entenderlo en cristiano:</b> Son los encargados de que puedas pasar la comida sin ahogarte y de mover la caja de voz. Están organizados en dos pisos (planos musculares). ¡Vamos a ver quién vive en cada piso!</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. LOS PLANOS MUSCULARES
    st.subheader("🏢 El Edificio del Cuello: Planos Musculares")
    
    col_piso1, col_piso2 = st.columns(2)
    
    with col_piso1:
        st.markdown("""
        <div class="simbolo-card" style="border-top: 4px solid #FFD700;">
            <div class="simbolo-titulo">🚪 Plano Superficial (Primer Piso)</div>
            <div class="simbolo-sub">Los que se ven a primera vista</div>
            <div class="simbolo-desc">
                Aquí viven dos tipos que son los más largos de la zona:
                <ul>
                    <li><b>Esternocleidohioideo (o Esternohioideo):</b> El nombre asusta, pero su camino es fácil. Va desde el esternón y la clavícula directo hasta el hioides. Es el guardaespaldas principal del frente del cuello.</li>
                    <li><b>Omohioideo:</b> Este es el 'raro' del grupo porque tiene dos panzas (vientres) unidas por un tendón en el medio. Viene viajando desde el omóplato (en la espalda) y cruza todo el cuello de lado hasta llegar al hioides. ¡Un aventurero!</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_piso2:
        st.markdown("""
        <div class="simbolo-card" style="border-top: 4px solid #CE1126;">
            <div class="simbolo-titulo">🚪 Plano Profundo (Planta Baja)</div>
            <div class="simbolo-sub">Los que están escondidos abajo</div>
            <div class="simbolo-desc">
                Si quitas los dos anteriores, te encuentras a los que están pegados a la laringe y la tiroides:
                <ul>
                    <li><b>Esternotiroideo:</b> Este no llega hasta el hioides. Es flojo, arranca en el esternón y se cansa rápido, quedándose plantado en el cartílago tiroides.</li>
                    <li><b>Tirohioideo:</b> Este continúa el trabajo del anterior. Arranca justo donde el otro se cansó (cartílago tiroides) y sube hasta el hueso hioides. Básicamente es el ascensor que conecta la tiroides con el techo.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 3. LA IRRIGACIÓN
    st.markdown("""
    <div class="section-box" style="border-left: 5px solid #CE1126;">
        <h3>🩸 Tuberías Premium: La Irrigación Sanguínea</h3>
        <p>¿Quién le lleva los nutrientes y la sangre a todos estos señores y a los órganos del cuello? La red eléctrica y de agua está a cargo de dos arterias principales:</p>
        <ul>
            <li><b>Arteria Carótida Externa:</b> Es la tubería matriz del cuello y la cara. De ella sale una rama súper importante llamada <b>Arteria Tiroidea Superior</b>, que baja a irrigar la tiroides y a los músculos vecinos.</li>
            <li><b>Arteria Subclavia:</b> Pasa por debajo de la clavícula y manda una rama hacia arriba llamada <b>Arteria Tiroidea Inferior</b>.</li>
        </ul>
        <p>💡 <b>Dato para lucirse:</b> Las arterias tiroideas superior e inferior se unen en el cuello creando una <i>red de vasos sanguíneos</i> brutal para asegurarse de que a la laringe, la tráquea y la tiroides nunca les falte sangre.</p>
    </div>
    """, unsafe_allow_html=True)

    # 4. EL CUESTIONARIO INTERACTIVO (Las 3 preguntas con botones nativos de Streamlit)
    st.write("---")
    st.subheader("📝 ¡Quiz Relámpago! Pon a prueba a tu amiga antes de salir al ruedo")
    st.write("Selecciona la respuesta correcta para ver si estás lista para el 20 de nota:")

    # Pregunta 1
    p1 = st.radio(
        "1. ¿Cuál de estos músculos NO llega directamente al hueso hioides?",
        ["Esternocleidohioideo", "Omohioideo", "Esternotiroideo"],
        index=None,
        placeholder="Elige tu respuesta..."
    )
    if p1 == "Esternotiroideo":
        st.success("¡Excelente! Ese se queda flojo a mitad de camino en el cartílago tiroides. 🔥")
    elif p1 is not None:
        st.error("Nopo. Ese sí llega al hioides. ¡Acuérdate del que se cansa a mitad de camino!")

    # Pregunta 2
    p2 = st.radio(
        "2. ¿Qué músculo tiene la rareza de tener dos 'vientres' y venir desde el omóplato?",
        ["Tirohioideo", "Omohioideo", "Esternohioideo"],
        index=None,
        placeholder="Elige tu respuesta..."
    )
    if p2 == "Omohioideo":
        st.success("¡Brutal! El Omohioideo viaja desde el hombro cruzando todo el cuello. 🧠")
    elif p2 is not None:
        st.error("Incorrecto. Piensa en el que hace el viaje largo desde atrás ('Omo' de omóplato).")

    # Pregunta 3
    p3 = st.radio(
        "3. ¿De qué gran arteria nace la Arteria Tiroidea Superior que irriga esta zona anterior?",
        ["Arteria Carótida Externa", "Arteria Subclavia", "Arteria Aorta"],
        index=None,
        placeholder="Elige tu respuesta..."
    )
    if p3 == "Arteria Carótida Externa":
        st.balloons()  # ¡Efecto de celebración si saca la última buena!
        st.success("¡Coronaste! La Carótida Externa es la jefa que manda esa rama superior. ¡Lista para la exposición! 🎓")
    elif p3 is not None:
        st.error("Casi, pero no. La subclavia se encarga de la inferior, la superior viene de más arriba.")
