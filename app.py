import urllib.parse
from pathlib import Path

import streamlit as st

# Número de WhatsApp de tu tienda: código de país + número, sin signos ni espacios.
WHATSAPP = "573000000000"
IMAGENES = Path(__file__).parent / "images"

PRODUCTOS = [
    {"id": 1, "nombre": "Licuadora 1,5 L 600 W", "cat": "Cocina", "precio": 129900, "antes": 159900, "desc": "Vaso de vidrio, 5 velocidades", "img": "licuadora.jpg"},
    {"id": 2, "nombre": "Freidora de aire 7,5 L", "cat": "Cocina", "precio": 299900, "antes": 399900, "desc": "Cabe un pollo de hasta 3,6 kg", "img": "freidora.jpg"},
    {"id": 3, "nombre": "Nevera No Frost 300 L", "cat": "Cocina", "precio": 1899900, "antes": None, "desc": "Eficiencia energética A+", "img": "nevera.jpg"},
    {"id": 4, "nombre": "Microondas 20 L", "cat": "Cocina", "precio": 289900, "antes": None, "desc": "700 W, 6 niveles de potencia", "img": "microondas.jpg"},
    {"id": 5, "nombre": "Cafetera espresso", "cat": "Cocina", "precio": 99900, "antes": 129900, "desc": "Con vaporizador para espumar leche", "img": "cafetera.jpg"},
    {"id": 6, "nombre": "Arrocera 1,8 L", "cat": "Cocina", "precio": 119900, "antes": None, "desc": "Mantiene caliente automáticamente", "img": "arrocera.jpg"},
    {"id": 7, "nombre": "Lavadora automática 17 kg", "cat": "Lavado", "precio": 1699900, "antes": 1999900, "desc": "Carga superior, 8 programas", "img": "lavadora.jpg"},
    {"id": 8, "nombre": "Plancha a vapor 1.800 W", "cat": "Lavado", "precio": 89900, "antes": None, "desc": "Base antiadherente", "img": "plancha.jpg"},
    {"id": 9, "nombre": "Aspiradora de mano para carro", "cat": "Lavado", "precio": 249900, "antes": None, "desc": "Con accesorios y bolsa de transporte", "img": "aspiradora.jpg"},
    {"id": 10, "nombre": "Ventilador de mesa", "cat": "Clima", "precio": 179900, "antes": 219900, "desc": "Cabeza inclinable y base estable", "img": "ventilador.jpg"},
    {"id": 11, "nombre": "Aire acondicionado de ventana", "cat": "Clima", "precio": 1599900, "antes": None, "desc": "Con control digital en el panel", "img": "aire.jpg"},
    {"id": 12, "nombre": "Smart TV 50″ 4K", "cat": "Entretenimiento", "precio": 1799900, "antes": 2199900, "desc": "Netflix, YouTube y más integrados", "img": "tv.jpg"},
]
POR_ID = {p["id"]: p for p in PRODUCTOS}
CATEGORIAS = ["Todos"] + list(dict.fromkeys(p["cat"] for p in PRODUCTOS))

st.set_page_config(page_title="Voltio · Artefactos eléctricos", page_icon="⚡", layout="wide")


def peso(n):
    return "$" + f"{n:,.0f}".replace(",", ".")


if "carrito" not in st.session_state:
    st.session_state.carrito = {}


def agregar(pid):
    st.session_state.carrito[pid] = st.session_state.carrito.get(pid, 0) + 1


def quitar(pid):
    st.session_state.carrito[pid] -= 1
    if st.session_state.carrito[pid] <= 0:
        del st.session_state.carrito[pid]


# ---------- Carrito (barra lateral) ----------
with st.sidebar:
    st.header("🛒 Tu carrito")
    carrito = st.session_state.carrito
    total, lineas = 0, []
    if not carrito:
        st.write("Tu carrito está vacío. Agrega un producto del catálogo para empezar.")
    for pid, cant in list(carrito.items()):
        p = POR_ID[pid]
        sub = cant * p["precio"]
        total += sub
        lineas.append(f"• {cant} x {p['nombre']} ({peso(sub)})")
        st.markdown(f"**{p['nombre']}**")
        c1, c2, c3 = st.columns([1, 1, 2])
        c1.button("−", key=f"menos{pid}", on_click=quitar, args=(pid,))
        c2.button("+", key=f"mas{pid}", on_click=agregar, args=(pid,))
        c3.write(f"{cant} · {peso(sub)}")
    st.divider()
    st.subheader(f"Total: {peso(total)}")
    if carrito:
        mensaje = "Hola, quiero hacer este pedido:\n" + "\n".join(lineas) + f"\nTotal: {peso(total)}"
        st.link_button("Pedir por WhatsApp", f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(mensaje)}")

# ---------- Página principal ----------
st.title("⚡ Voltio")
st.subheader("Todo lo eléctrico que tu casa necesita, al mejor precio.")
st.caption("Garantía de 12 meses · Envío en 2 a 5 días · Pago contra entrega")

categoria = st.radio("Categoría", CATEGORIAS, horizontal=True, label_visibility="collapsed")
busqueda = st.text_input("Buscar", placeholder="Busca una licuadora, nevera, TV…", label_visibility="collapsed")

lista = [
    p for p in PRODUCTOS
    if (categoria == "Todos" or p["cat"] == categoria) and busqueda.lower().strip() in p["nombre"].lower()
]

if not lista:
    st.info("No encontramos productos con esa búsqueda. Prueba con otra palabra o elige otra categoría.")

for i in range(0, len(lista), 4):
    cols = st.columns(4)
    for col, p in zip(cols, lista[i:i + 4]):
        with col, st.container(border=True):
            st.image(str(IMAGENES / p["img"]))
            st.markdown(f"**{p['nombre']}**")
            st.caption(p["desc"])
            if p["antes"]:
                descuento = round((1 - p["precio"] / p["antes"]) * 100)
                st.markdown(f"**{peso(p['precio'])}** ~~{peso(p['antes'])}~~ 🔥 -{descuento}%")
            else:
                st.markdown(f"**{peso(p['precio'])}**")
            st.button("Agregar al carrito", key=f"add{p['id']}", on_click=agregar, args=(p["id"],))
