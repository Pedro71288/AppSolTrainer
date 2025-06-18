import streamlit as st
from PIL import Image

# Cargar el logo como banner (ajustado al ancho)
img = Image.open("logosol2.png")
st.image(img, use_column_width=True)

# Aplicar estilos CSS para texto y botón
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        font-style: italic;
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        color: #555;
        margin-top: 5px;
        margin-bottom: 40px;
    }
    .stButton > button {
        font-size: 24px;
        padding: 15px 60px;
        border-radius: 10px;
        display: block;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo con estilo
st.markdown('<h1 class="title">Sol Trainer</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subtitle">Logra lo que creías imposible</h3>', unsafe_allow_html=True)

# Control de navegación con session_state
if 'menu' not in st.session_state:
    st.session_state.menu = False

if not st.session_state.menu:
    if st.button("Comenzar"):
        st.session_state.menu = True
        st.experimental_rerun()
else:
    st.header("Menú Principal")
    st.write("Elegí una sección para comenzar:")

    # Secciones de ejemplo
    if st.button("Rutinas"):
        st.success("Aquí irán las rutinas personalizadas.")
    if st.button("Dieta"):
        st.info("Aquí estará tu plan alimenticio.")
    if st.button("Progreso"):
        st.warning("Aquí podrás ver tu evolución.")
