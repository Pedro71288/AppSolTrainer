import streamlit as st
from PIL import Image

# Función para mostrar pantalla inicial
def pantalla_inicio():
    img = Image.open("logosol2.png")
    st.image(img, use_column_width=True)

    st.markdown("""
        <style>
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
        .start-button {
            background-color: #6A0DAD;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 20px;
            padding: 15px 50px;
            margin: 0 auto;
            display: block;
            width: 60%;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">Sol Trainer</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Logra lo que creías imposible</h3>', unsafe_allow_html=True)

    if st.button("Comenzar"):
        st.session_state.pagina = "menu"

# Función para mostrar menú principal
def pantalla_menu():
    st.markdown("""
        <style>
        .menu-title {
            text-align: center;
            font-family: 'Georgia', serif;
            font-size: 36px;
            color: #6A0DAD;
            margin-bottom: 20px;
        }
        .menu-button {
            background-color: #6A0DAD;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 24px;
            padding: 15px 40px;
            margin: 15px auto;
            display: block;
            width: 50%;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="menu-title">Menú Principal</h2>', unsafe_allow_html=True)

    if st.button("🏋️‍♀️ Rutinas"):
        st.write("Aquí van las rutinas...")

    if st.button("🍽️ Dietas"):
        st.write("Aquí van las dietas...")

    if st.button("💡 Consejos"):
        st.write("Aquí van los consejos...")

    if st.button("📞 Contacto"):
        st.write("Aquí va el contacto...")

    if st.button("Volver al Inicio"):
        st.session_state.pagina = "inicio"


# Inicialización variable de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = "inicio"

# Control de navegación
if st.session_state.pagina == "inicio":
    pantalla_inicio()
elif st.session_state.pagina == "menu":
    pantalla_menu()
