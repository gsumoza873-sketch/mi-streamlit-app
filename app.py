import urllib.parse

import streamlit as st

# Número de WhatsApp de tu tienda: código de país + número, sin signos ni espacios.
WHATSAPP = "573000000000"

# ---------- Figuras didácticas (dibujos vectoriales, sin fotos) ----------
A, Y, D, G, L, B = "#1f3fff", "#ffd23f", "#101a33", "#3b4a7a", "#dfe6ff", "#6f86ff"


def svg(interior):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 120 120">'
        f'<rect width="120" height="120" rx="16" fill="#eef2ff"/>{interior}</svg>'
    )


_ranuras = "".join(f'<rect x="20" y="{y}" width="64" height="4" rx="2" fill="{A}"/>' for y in (38, 47, 56, 65, 74))
_aspas = "".join(
    f'<ellipse cx="60" cy="28" rx="8" ry="15" transform="rotate({r} 60 44)"/>' for r in (0, 90, 180, 270)
)

FIGURAS = {
    "licuadora": svg(
        f'<polygon points="38,18 82,18 76,68 44,68" fill="white" stroke="{G}" stroke-width="3"/>'
        f'<polygon points="41,42 79,42 76,68 44,68" fill="{Y}"/>'
        f'<rect x="34" y="10" width="52" height="9" rx="4" fill="{A}"/>'
        f'<rect x="38" y="68" width="44" height="30" rx="7" fill="{A}"/>'
        f'<circle cx="60" cy="83" r="6" fill="{Y}"/>'
        f'<rect x="32" y="98" width="56" height="6" rx="3" fill="{G}"/>'
    ),
    "freidora": svg(
        f'<rect x="24" y="20" width="72" height="68" rx="14" fill="{A}"/>'
        f'<rect x="32" y="28" width="56" height="12" rx="4" fill="{D}"/>'
        f'<circle cx="42" cy="34" r="2.5" fill="{Y}"/><circle cx="52" cy="34" r="2.5" fill="{Y}"/>'
        f'<circle cx="62" cy="34" r="2.5" fill="{Y}"/>'
        f'<rect x="30" y="48" width="60" height="32" rx="8" fill="{L}"/>'
        f'<rect x="46" y="58" width="28" height="9" rx="4" fill="{Y}"/>'
        f'<rect x="32" y="88" width="14" height="8" rx="3" fill="{G}"/>'
        f'<rect x="74" y="88" width="14" height="8" rx="3" fill="{G}"/>'
    ),
    "nevera": svg(
        f'<rect x="34" y="8" width="52" height="102" rx="8" fill="{A}"/>'
        f'<rect x="34" y="44" width="52" height="4" fill="{D}"/>'
        f'<rect x="40" y="20" width="4" height="16" rx="2" fill="{Y}"/>'
        f'<rect x="40" y="54" width="4" height="24" rx="2" fill="{Y}"/>'
        f'<rect x="58" y="56" width="20" height="20" rx="4" fill="{L}"/>'
        f'<rect x="64" y="64" width="8" height="12" rx="2" fill="{D}"/>'
        f'<rect x="40" y="110" width="8" height="5" fill="{G}"/><rect x="72" y="110" width="8" height="5" fill="{G}"/>'
    ),
    "microondas": svg(
        f'<rect x="12" y="30" width="96" height="60" rx="9" fill="{A}"/>'
        f'<rect x="20" y="38" width="54" height="44" rx="6" fill="{D}"/>'
        '<path d="M28 46 L46 46 L34 74 L28 74 Z" fill="white" opacity="0.12"/>'
        f'<rect x="80" y="38" width="20" height="12" rx="3" fill="{L}"/>'
        f'<circle cx="85" cy="62" r="4" fill="{Y}"/><circle cx="95" cy="62" r="4" fill="{Y}"/>'
        f'<circle cx="85" cy="74" r="4" fill="{Y}"/><circle cx="95" cy="74" r="4" fill="{Y}"/>'
        f'<rect x="20" y="90" width="10" height="6" rx="2" fill="{G}"/><rect x="90" y="90" width="10" height="6" rx="2" fill="{G}"/>'
    ),
    "cafetera": svg(
        f'<rect x="22" y="94" width="76" height="9" rx="4" fill="{D}"/>'
        f'<rect x="28" y="16" width="22" height="78" rx="7" fill="{A}"/>'
        f'<rect x="28" y="16" width="58" height="26" rx="8" fill="{A}"/>'
        f'<rect x="48" y="44" width="26" height="8" rx="3" fill="{G}"/>'
        '<rect x="59" y="52" width="4" height="18" fill="#8a4b1f"/>'
        f'<path d="M50 68 H74 V82 A9 9 0 0 1 65 91 H59 A9 9 0 0 1 50 82 Z" fill="white" stroke="{G}" stroke-width="3"/>'
        '<rect x="52" y="76" width="20" height="8" rx="3" fill="#8a4b1f"/>'
        f'<path d="M86 40 H96 V62" fill="none" stroke="{D}" stroke-width="5" stroke-linecap="round"/>'
    ),
    "arrocera": svg(
        f'<rect x="22" y="48" width="76" height="48" rx="18" fill="{A}"/>'
        f'<path d="M24 50 A36 28 0 0 1 96 50 Z" fill="{L}"/>'
        f'<rect x="56" y="22" width="8" height="6" fill="{D}"/><circle cx="60" cy="19" r="6" fill="{Y}"/>'
        f'<rect x="12" y="58" width="12" height="10" rx="4" fill="{D}"/><rect x="96" y="58" width="12" height="10" rx="4" fill="{D}"/>'
        f'<rect x="50" y="72" width="20" height="14" rx="4" fill="{Y}"/>'
        f'<rect x="30" y="96" width="14" height="6" rx="3" fill="{G}"/><rect x="76" y="96" width="14" height="6" rx="3" fill="{G}"/>'
    ),
    "lavadora": svg(
        f'<rect x="22" y="10" width="76" height="100" rx="10" fill="{L}" stroke="{A}" stroke-width="4"/>'
        f'<path d="M22 20 A10 10 0 0 1 32 10 H88 A10 10 0 0 1 98 20 V32 H22 Z" fill="{A}"/>'
        f'<circle cx="36" cy="22" r="5" fill="{Y}"/><rect x="56" y="17" width="30" height="10" rx="3" fill="{D}"/>'
        f'<circle cx="60" cy="72" r="26" fill="{A}"/><circle cx="60" cy="72" r="19" fill="{D}"/>'
        f'<path d="M42 74 A18 18 0 0 0 78 74 Z" fill="{B}"/>'
    ),
    "plancha": svg(
        f'<path d="M18 82 H102 C102 60 90 46 70 46 H34 C24 46 20 56 20 64 Z" fill="{A}"/>'
        f'<rect x="16" y="82" width="90" height="9" rx="4" fill="{D}"/>'
        f'<path d="M36 46 C36 24 84 24 84 46" fill="none" stroke="{Y}" stroke-width="8" stroke-linecap="round"/>'
        f'<circle cx="90" cy="68" r="4" fill="{Y}"/>'
        f'<circle cx="44" cy="102" r="3" fill="{B}"/><circle cx="60" cy="106" r="3" fill="{B}"/><circle cx="76" cy="102" r="3" fill="{B}"/>'
    ),
    "aspiradora": svg(
        f'<rect x="30" y="42" width="58" height="32" rx="12" fill="{A}"/>'
        '<polygon points="30,50 8,57 8,67 30,66" fill="#94a3c8"/>'
        f'<rect x="48" y="50" width="28" height="16" rx="5" fill="{L}"/>'
        f'<path d="M42 42 C42 22 76 22 76 42" fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round"/>'
        f'<circle cx="82" cy="58" r="4" fill="{Y}"/>'
        f'<path d="M88 62 C108 62 104 88 82 92" fill="none" stroke="{G}" stroke-width="3"/>'
        f'<rect x="72" y="88" width="14" height="8" rx="2" fill="{D}"/>'
    ),
    "ventilador": svg(
        f'<ellipse cx="60" cy="106" rx="28" ry="6" fill="{G}"/><rect x="57" y="76" width="6" height="30" fill="{G}"/>'
        f'<circle cx="60" cy="44" r="34" fill="white" stroke="{A}" stroke-width="5"/>'
        f'<g fill="{A}">{_aspas}</g><circle cx="60" cy="44" r="7" fill="{Y}"/>'
    ),
    "aire": svg(
        f'<rect x="10" y="26" width="100" height="58" rx="9" fill="{L}" stroke="{A}" stroke-width="4"/>{_ranuras}'
        f'<rect x="90" y="36" width="12" height="40" rx="3" fill="{A}"/>'
        f'<circle cx="96" cy="45" r="3" fill="{Y}"/><circle cx="96" cy="57" r="3" fill="{B}"/>'
        f'<circle cx="28" cy="100" r="3" fill="{B}"/><circle cx="50" cy="106" r="3" fill="{B}"/>'
        f'<circle cx="72" cy="100" r="3" fill="{B}"/><circle cx="94" cy="106" r="3" fill="{B}"/>'
    ),
    "tv": svg(
        f'<rect x="10" y="22" width="100" height="64" rx="6" fill="{D}"/>'
        f'<rect x="15" y="27" width="90" height="54" rx="3" fill="{A}"/>'
        f'<polygon points="15,81 42,50 58,68 76,44 105,81" fill="{B}"/>'
        f'<circle cx="90" cy="40" r="6" fill="{Y}"/>'
        f'<polygon points="46,104 74,104 68,86 52,86" fill="{G}"/><rect x="38" y="102" width="44" height="6" rx="3" fill="{G}"/>'
    ),
}

PRODUCTOS = [
    {"id": 1, "nombre": "Licuadora 1,5 L 600 W", "cat": "Cocina", "precio": 129900, "antes": 159900, "desc": "Vaso de vidrio, 5 velocidades", "fig": "licuadora"},
    {"id": 2, "nombre": "Freidora de aire 7,5 L", "cat": "Cocina", "precio": 299900, "antes": 399900, "desc": "Cabe un pollo de hasta 3,6 kg", "fig": "freidora"},
    {"id": 3, "nombre": "Nevera No Frost 300 L", "cat": "Cocina", "precio": 1899900, "antes": None, "desc": "Eficiencia energética A+", "fig": "nevera"},
    {"id": 4, "nombre": "Microondas 20 L", "cat": "Cocina", "precio": 289900, "antes": None, "desc": "700 W, 6 niveles de potencia", "fig": "microondas"},
    {"id": 5, "nombre": "Cafetera espresso", "cat": "Cocina", "precio": 99900, "antes": 129900, "desc": "Con vaporizador para espumar leche", "fig": "cafetera"},
    {"id": 6, "nombre": "Arrocera 1,8 L", "cat": "Cocina", "precio": 119900, "antes": None, "desc": "Mantiene caliente automáticamente", "fig": "arrocera"},
    {"id": 7, "nombre": "Lavadora automática 17 kg", "cat": "Lavado", "precio": 1699900, "antes": 1999900, "desc": "Carga superior, 8 programas", "fig": "lavadora"},
    {"id": 8, "nombre": "Plancha a vapor 1.800 W", "cat": "Lavado", "precio": 89900, "antes": None, "desc": "Base antiadherente", "fig": "plancha"},
    {"id": 9, "nombre": "Aspiradora de mano para carro", "cat": "Lavado", "precio": 249900, "antes": None, "desc": "Con accesorios y bolsa de transporte", "fig": "aspiradora"},
    {"id": 10, "nombre": "Ventilador de mesa", "cat": "Clima", "precio": 179900, "antes": 219900, "desc": "Cabeza inclinable y base estable", "fig": "ventilador"},
    {"id": 11, "nombre": "Aire acondicionado de ventana", "cat": "Clima", "precio": 1599900, "antes": None, "desc": "Con control digital en el panel", "fig": "aire"},
    {"id": 12, "nombre": "Smart TV 50″ 4K", "cat": "Entretenimiento", "precio": 1799900, "antes": 2199900, "desc": "Netflix, YouTube y más integrados", "fig": "tv"},
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
            st.image(FIGURAS[p["fig"]])
            st.markdown(f"**{p['nombre']}**")
            st.caption(p["desc"])
            if p["antes"]:
                descuento = round((1 - p["precio"] / p["antes"]) * 100)
                st.markdown(f"**{peso(p['precio'])}** ~~{peso(p['antes'])}~~ 🔥 -{descuento}%")
            else:
                st.markdown(f"**{peso(p['precio'])}**")
            st.button("Agregar al carrito", key=f"add{p['id']}", on_click=agregar, args=(p["id"],))
