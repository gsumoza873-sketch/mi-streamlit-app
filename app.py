import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Tutor Musical Inteligente IA",
    page_icon="🎹",
    layout="centered"
)

# 2. Estilos CSS (Pantalla LED, Teclado Neón y Contenedor de la IA)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    /* Contenedor del Chat de la IA */
    .chat-ia {
        background-color: #1e1b4b;
        border-left: 4px solid #a855f7;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.25);
    }
    
    /* Pantalla Digital del Sintetizador */
    .pantalla-led {
        background: linear-gradient(145deg, #020617, #0f172a);
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
        font-family: 'Courier New', monospace;
    }
    .led-titulo {
        font-size: 11px;
        color: #60a5fa;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    .led-principal {
        font-size: 24px;
        font-weight: bold;
        color: #34d399;
        text-shadow: 0 0 8px rgba(52, 211, 153, 0.5);
    }
    .led-sub {
        font-size: 13px;
        color: #94a3b8;
        margin-top: 5px;
    }

    /* Contenedor del Piano */
    .piano-container {
        display: flex;
        justify-content: center;
        background-color: #1e293b;
        padding: 35px 15px;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        position: relative;
    }

    /* Teclas Blancas Animadas */
    .tecla-blanca {
        width: 52px;
        height: 190px;
        background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 90%, #e2e8f0 100%);
        border: 1px solid #cbd5e1;
        border-radius: 0 0 6px 6px;
        cursor: pointer;
        z-index: 1;
        display: flex;
        align-items: flex-end;
        
