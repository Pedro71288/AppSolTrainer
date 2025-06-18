import streamlit as st
from PIL import Image

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="Sol Trainer", layout="wide")

# INICIALIZACIÓN DE ESTADO
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# ESTILOS COMUNES
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #a85ee0;
            margin: 0;
            padding: 0;
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

# ==============================
# PANTALLA INICIAL
# ==============================
if st.session_state.pagina == "inicio":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    try:
        banner = Image.open("banner.png")
        st.image(banner, use_container_width=True)
    except:
        st.error("No se encuentra 'banner.png'. Verificá que esté en la carpeta correcta.")

    if st.button("Comenzar"):
        st.session_state.pagina = "menu"

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# PANTALLA MENÚ PRINCIPAL
# ==============================
elif st.session_state.pagina == "menu":
    st.markdown("""
        <style>
            .menu-container {
                background-color: white;
                padding: 3em;
                border-radius: 20px;
                max-width: 1000px;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #6A0DAD;
                margin-bottom: 40px;
            }
            .menu-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 2em;
            }
            .menu-item {
                background-color: #f5e9ff;
                border: 2px solid #6A0DAD;
                border-radius: 15px;
                padding: 2em;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                color: #6A0DAD;
                transition: 0.3s ease;
            }
            .menu-item:hover {
                background-color: #6A0DAD;
                color: white;
                cursor: pointer;
            }
        </style>
        <div class="menu-container">
            <h1>Menú Principal</h1>
            <div class="menu-grid">
                <div class="menu-item">🏋️ Rutinas</div>
                <div class="menu-item">🥗 Dietas</div>
                <div class="menu-item">💡 Consejos</div>
                <div class="menu-item">📞 Contacto</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
