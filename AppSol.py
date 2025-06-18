import streamlit as st
from PIL import Image

# Logo como banner
img = Image.open("logosol2.png")
st.image(img, use_column_width=True)

# CSS personalizado
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    .title {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 0px;
        color: #6A0DAD;
    }
    .subtitle {
        text-align: center;
        font-style: italic;
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        color: #a85ee0;
        margin-top: 5px;
        margin-bottom: 40px;
    }
    .menu-button {
        background-color: #6A0DAD;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 20px;
        padding: 15px 50px;
        margin: 10px auto;
        display: block;
        width: 60%;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.markdown('<h1 class="title">Sol Trainer</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subtitle">Logra lo que creías imposible</h3>', unsafe_allow_html=True)

# Control de navegación
if 'menu' not in st.session_state:
    st.session_state.menu = False

if not st.session_state.menu:
    if st.button("Comenzar"):
        st.session_state.menu = True
        st.experimental_rerun()
else:
    st.markdown("## Menú Principal")
    st.markdown("### Elegí una sección:", unsafe_allow_html=True)

    st.markdown('<button class="menu-button">🏋️‍♀️ Rutinas</button>', unsafe_allow_html=True)
    st.markdown('<button class="menu-button">🍽️ Dietas</button>', unsafe_allow_html=True)
    st.markdown('<button class="menu-button">💡 Consejos</button>', unsafe_allow_html=True)
    st.markdown('<button class="menu-button">📞 Contacto</button>', unsafe_allow_html=True)
