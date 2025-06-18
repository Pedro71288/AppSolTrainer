import streamlit as st
from PIL import Image

# CONFIGURACIÓN
st.set_page_config(page_title="Sol Trainer", layout="wide")

# CSS PERSONALIZADO
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
            text-align: center;
        }
        .banner {
            width: 100%;
            border-radius: 12px;
        }
        .stButton {
            display: flex;
            justify-content: center;
            margin-top: 2em;
        }
        .stButton > button {
            background-color: #6A0DAD;
            color: white;
            font-size: 22px;
            padding: 16px 60px;
            border: none;
            border-radius: 12px;
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

# BANNER
try:
    banner = Image.open("banner.png")
    st.image(banner, use_container_width=True)
except:
    st.error("No se encuentra 'banner.png'. Verificá que esté en la carpeta correcta.")

# BOTÓN CENTRADO
if st.button("Comenzar"):
    st.session_state.pagina = "menu"

# CIERRE CONTENEDOR
st.markdown('</div>', unsafe_allow_html=True)
