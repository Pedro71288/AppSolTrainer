import streamlit as st
from PIL import Image

def menu():
    st.markdown(
        """
        <style>
            /* Fondo degradado de violeta a naranja */
            .menu-background {
                min-height: 100vh;
                background: linear-gradient(135deg, #7b2ff7, #ff7e5f);
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px 15px;
                box-sizing: border-box;
                color: white;
                font-family: Arial, sans-serif;
            }

            /* Encabezado */
            .menu-header {
                width: 100%;
                max-width: 480px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 25px;
                user-select: none;
            }
            .menu-header .icon {
                cursor: pointer;
                font-size: 28px;
                padding: 5px 10px;
                user-select: none;
            }

            /* Botones apilados verticalmente */
            .menu-button {
                background: rgba(255, 255, 255, 0.15);
                border: 1.5px solid white;
                border-radius: 20px;
                color: white;
                font-weight: 600;
                font-size: 18px;
                padding: 18px 20px;
                margin-bottom: 20px;
                width: 100%;
                max-width: 480px;
                box-sizing: border-box;
                cursor: pointer;
                user-select: none;
                display: flex;
                align-items: center;
                gap: 15px;
                transition: background 0.3s ease;
            }
            .menu-button:hover {
                background: rgba(255, 255, 255, 0.35);
            }

            /* Íconos grandes */
            .menu-icon {
                font-size: 32px;
                flex-shrink: 0;
            }

            /* Texto con título y subtítulo */
            .menu-text {
                display: flex;
                flex-direction: column;
            }
            .menu-text .title {
                font-size: 20px;
                font-weight: 700;
            }
            .menu-text .subtitle {
                font-size: 14px;
                font-weight: 400;
                opacity: 0.85;
                margin-top: 4px;
            }

            /* Responsive móvil */
            @media (max-width: 480px) {
                .menu-button {
                    font-size: 16px;
                    padding: 16px 15px;
                }
                .menu-icon {
                    font-size: 28px;
                }
                .menu-text .title {
                    font-size: 18px;
                }
                .menu-text .subtitle {
                    font-size: 13px;
                }
            }
        </style>

        <div class="menu-background">
            <div class="menu-header">
                <div class="icon" onclick="window.history.back()">←</div>
                <div>Fitness</div>
                <div class="icon">≡</div>
            </div>

            <div class="menu-button" id="hipertrofia">
                <div class="menu-icon">💪</div>
                <div class="menu-text">
                    <div class="title">Hipertrofia</div>
                    <div class="subtitle">Entrenamientos enfocados en el crecimiento muscular.</div>
                </div>
            </div>

            <div class="menu-button" id="perdida-grasa">
                <div class="menu-icon">🔥</div>
                <div class="menu-text">
                    <div class="title">Pérdida de grasa</div>
                    <div class="subtitle"></div>
                </div>
            </div>

            <div class="menu-button" id="aumento-fuerza">
                <div class="menu-icon">🏋️‍♂️</div>
                <div class="menu-text">
                    <div class="title">Aumento de fuerza</div>
                    <div class="subtitle"></div>
                </div>
            </div>

            <div class="menu-button" id="resistencia-fisica">
                <div class="menu-icon">🏃‍♂️</div>
                <div class="menu-text">
                    <div class="title">Resistencia física</div>
                    <div class="subtitle"></div>
                </div>
            </div>

            <div class="menu-button" id="definicion-muscular">
                <div class="menu-icon">🎯</div>
                <div class="menu-text">
                    <div class="title">Definición muscular</div>
                    <div class="subtitle"></div>
                </div>
            </div>

            <div class="menu-button" id="bienestar-general">
                <div class="menu-icon">🌿</div>
                <div class="menu-text">
                    <div class="title">Bienestar general</div>
                    <div class="subtitle"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(page_title="Sol Trainer", layout="centered")

    if "pagina" not in st.session_state:
        st.session_state.pagina = "inicio"

    if st.session_state.pagina == "inicio":
        st.markdown(
            """
            <style>
                html, body, [data-testid="stAppViewContainer"] {
                    height: 100%;
                    margin: 0;
                    background: linear-gradient(135deg, #7b2ff7, #ac42f0, #c77aff);
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    padding-top: 40px;
                    color: white;
                    font-family: Arial, sans-serif;
                }
                .banner-container {
                    width: 90vw;
                    max-width: 400px;
                    margin: 0 auto 2rem auto;
                    border-radius: 20px;
                    box-shadow: 0 8px 20px rgba(124, 41, 255, 0.25);
                    overflow: hidden;
                }
                .banner-container img {
                    width: 100% !important;
                    height: auto !important;
                    display: block;
                }
                .stButton > button {
                    background-color: #7b2ff7;
                    color: white;
                    font-size: 20px;
                    padding: 14px 60px;
                    border: none;
                    border-radius: 15px;
                    cursor: pointer;
                    box-shadow: 0 6px 15px rgba(124, 41, 255, 0.6);
                    transition: all 0.3s ease;
                    font-weight: 600;
                    min-width: 180px;
                    margin-bottom: 40px;
                }
                .stButton > button:hover {
                    background-color: white;
                    color: #7b2ff7;
                    border: 2px solid #7b2ff7;
                    box-shadow: 0 6px 20px rgba(124, 41, 255, 0.8);
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        try:
            banner = Image.open("banner.png")
            st.markdown('<div class="banner-container">', unsafe_allow_html=True)
            st.image(banner, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except:
            st.error("No se encuentra 'banner.png'. Verificá que esté en la carpeta correcta.")

        if st.button("Comenzar"):
            st.session_state.pagina = "menu"

    elif st.session_state.pagina == "menu":
        menu()

if __name__ == "__main__":
    main()
