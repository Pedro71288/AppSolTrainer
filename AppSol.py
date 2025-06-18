import streamlit as st
from PIL import Image

def main():
    # Configuración general
    st.set_page_config(page_title="Sol Trainer", layout="wide")

    # Inicialización del estado
    if "pagina" not in st.session_state:
        st.session_state.pagina = "inicio"

    if st.session_state.pagina == "inicio":
        st.markdown("""
        <style>
            html, body, [data-testid="stAppViewContainer"] {
                height: 100%;
                margin: 0;
                background: linear-gradient(135deg, #7b2ff7, #ac42f0, #c77aff);
                display: flex;
                justify-content: center;
                align-items: flex-start;
                padding-top: 40px;
            }
            .main-container {
                background-color: white;
                border-radius: 25px;
                max-width: 1000px;
                width: 90%;
                box-shadow: 0 12px 30px rgba(124, 41, 255, 0.3);
                padding: 2rem 2rem 3rem 2rem;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .banner {
                width: 100%;
                max-width: 900px;
                border-radius: 20px 20px 0 0;
                object-fit: contain;
                box-shadow: 0 8px 20px rgba(124, 41, 255, 0.25);
                margin-bottom: 2rem;
            }
            .stButton > button {
                background-color: #7b2ff7;
                color: white;
                font-size: 22px;
                padding: 16px 70px;
                border: none;
                border-radius: 15px;
                cursor: pointer;
                box-shadow: 0 6px 15px rgba(124, 41, 255, 0.6);
                transition: all 0.3s ease;
                font-weight: 600;
            }
            .stButton > button:hover {
                background-color: white;
                color: #7b2ff7;
                border: 2px solid #7b2ff7;
                box-shadow: 0 6px 20px rgba(124, 41, 255, 0.8);
            }
        </style>
        <div class="main-container">
        """, unsafe_allow_html=True)

        try:
            banner = Image.open("banner.png")
            st.image(banner, use_container_width=True, clamp=True)
        except:
            st.error("No se encuentra 'banner.png'. Verificá que esté en la carpeta correcta.")

        if st.button("Comenzar"):
            st.session_state.pagina = "menu"

        st.markdown("</div>", unsafe_allow_html=True)

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
                text-align: center;
            }
            h1 {
                color: #6A0DAD;
                margin-bottom: 40px;
            }
            .menu-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 2em;
                justify-items: center;
            }
            .menu-item {
                background-color: #f5e9ff;
                border: 2px solid #6A0DAD;
                border-radius: 15px;
                padding: 2em;
                font-size: 18px;
                font-weight: bold;
                color: #6A0DAD;
                transition: 0.3s ease;
                cursor: pointer;
                width: 180px;
            }
            .menu-item:hover {
                background-color: #6A0DAD;
                color: white;
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

if __name__ == "__main__":
    main()
