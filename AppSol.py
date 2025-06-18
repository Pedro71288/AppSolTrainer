import streamlit as st
from PIL import Image

# CONFIGURACIÓN
st.set_page_config(page_title="Sol Trainer", layout="wide")

# CSS MEJORADO Y FUNCIONAL
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #a85ee0;
            padding: 0;
            margin: 0;
        }
        [data-testid="stAppViewContainer"] {
            display: flex;
            justify-content: center;
        }
        .main-container {
            width: 90%;
            max-width: 1000px;
            padding: 2em;
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        .banner {
            width: 100%;
            border-radius: 12px;
        }
        .stButton > button {
            background-color: #6A0DAD;
            color: white;
            font-size: 22px;
            padding: 16px 60px;
            border: none;
            border-radius: 12px;
            margin-top: 2em;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: white;
            color: #6A0DAD;
            border: 2px solid #6A0DAD;
        }
    </style>
""", unsafe_allow_html=True)

# CONTENEDOR PRINCIPAL
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# BANNER SUPERIOR (asegurate que se llame banner.png)
try:
    banner = Image.open("banner.png")
    st.image(banner, use_column_width=True, output_format="PNG")
except:
    st.error("No se encuentra la imagen 'banner.png'. Asegurate de que esté en la misma carpeta.")

# BOTÓN CENTRAL
if st.button("Comenzar"):
    st.session_state.pagina = "menu"

# CIERRE CONTENEDOR
st.markdown('</div>', unsafe_allow_html=True)
