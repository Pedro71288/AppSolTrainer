import streamlit as st
from PIL import Image

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Sol Trainer", layout="wide")

# ESTILOS PERSONALIZADOS
st.markdown("""
    <style>
        body {
            background-color: #a85ee0 !important;
        }
        .container {
            padding: 3em;
            border-left: 10px solid white;
            border-right: 10px solid white;
            min-height: 100vh;
        }
        .banner {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            border-radius: 16px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 3em;
        }
        .stButton > button {
            background-color: white;
            color: #6A0DAD;
            font-size: 24px;
            border-radius: 12px;
            padding: 18px 60px;
            border: 2px solid #6A0DAD;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #6A0DAD;
            color: white;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# CONTENIDO PRINCIPAL
st.markdown('<div class="container">', unsafe_allow_html=True)

# Mostrar banner (imagen con el título integrado)
banner = Image.open("banner.png")  # Asegurate que este archivo esté en la misma carpeta
st.image(banner, use_column_width=True)

# Botón "Comenzar"
st.markdown('<div class="button">', unsafe_allow_html=True)
if st.button("Comenzar"):
    st.session_state.pagina = "menu"
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
