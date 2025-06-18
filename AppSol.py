import streamlit as st
from PIL import Image

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="Sol Trainer", layout="centered")

# ESTILOS PERSONALIZADOS
st.markdown("""
    <style>
        .main {
            background-color: #a85ee0;
            border: 2px solid white;
            border-radius: 20px;
            padding: 2em;
        }
        .banner {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            border-radius: 12px;
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .stButton > button {
            background-color: white;
            color: #6A0DAD;
            font-size: 22px;
            border-radius: 10px;
            padding: 15px 50px;
            border: 2px solid #6A0DAD;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #6A0DAD;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# CONTENIDO
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Banner completo (sin texto adicional)
    banner = Image.open("banner.png")  # Renombrá la imagen que descargaste como 'banner.png'
    st.image(banner, use_column_width=True, caption=None)

    # Botón Comenzar
    st.markdown('<div class="button">', unsafe_allow_html=True)
    if st.button("Comenzar"):
        st.session_state.pagina = "menu"
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
