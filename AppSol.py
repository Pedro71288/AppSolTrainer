import streamlit as st
from PIL import Image
import base64

# --- Fondo degradado (usando CSS en Streamlit) ---
page_bg = """
<style>
body {
    background: linear-gradient(135deg, #536DFE, #5C6BC0);
    color: white;
}
.centered {
    text-align: center;
    margin-top: 100px;
}
button {
    border-radius: 25px;
    padding: 10px 40px;
    font-size: 16px;
    font-weight: bold;
}
.login-btn {
    background-color: white;
    color: red;
    border: none;
    margin-top: 15px;
}
.forgot {
    color: #eeeeee;
    font-size: 13px;
    margin-top: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Cargar el logo ---
logo = Image.open("logosol2.png")  # Asegurate de renombrar tu imagen a esto o ajustar el nombre

# --- Contenido centrado ---
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st.image(logo, width=100)

st.markdown("<h1 style='margin-bottom: 5px;'>Sol Trainer</h1>", unsafe_allow_html=True)
st.markdown("<p style='margin-top: 0;'>Logra lo que creías imposible</p>", unsafe_allow_html=True)

# Botón de login
login_btn = st.button("Login", key="login")

# Texto inferior
st.markdown("<p class='forgot'>¿Olvidaste tu contraseña?</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
