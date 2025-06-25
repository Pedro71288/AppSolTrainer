import streamlit as st
from PIL import Image

def menu():
    st.markdown(
        """
        <style>
            /* Fondo degradado de violeta a naranja */
            .menu-background {
                height: 100vh;
                background: linear-gradient(135deg, #7b2ff7, #ff7e5f);
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px 15px;
                box-sizing: border-box;
            }

            /* Encabezado */
            .menu-header {
                width: 100%;
                max-width: 400px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: white;
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

            /* Grilla de botones 2x3 */
            .menu-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(3, 1fr);
                gap: 20px;
                width: 100%;
                max-width: 400px;
            }

            /* Botones cuadrados, fondo semi-transparente blanco con borde blanco */
            .menu-button {
                background: rgba(255, 255, 255, 0.15);
                border: 1.5px solid white;
                border-radius: 20px;
                color: white;
                font-weight: 600;
                font-size: 18px;
                height: 100px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                cursor: pointer;
                user-select: none;
                transition: background 0.3s ease;
            }
            .menu-button:hover {
                background: rgba(255, 255, 255, 0.35);
            }

            /* Íconos grandes y blancos */
            .menu-icon {
                font-size: 36px;
                margin-bottom: 8px;
                line-height: 1;
            }

            /* Optimización para pantalla táctil */
            @media (max-width: 480px) {
                .menu-button {
                    height: 90px;
                    font-size: 16px;
                }
                .menu-icon {
                    font-size: 30px;
                }
            }
        </style>
        <div class="menu-background">
            <div class="menu-header">
                <div class="icon" id="back">←</div>
                <div>Fitness</div>
                <div class="icon" id="menu">≡</div>
            </div>
            <div class="menu-grid">
                <div class="menu-button" id="workout">
                    <div class="menu-icon">🏋️‍♂️</div>
                    Workout
                </div>
                <div class="menu-button" id="goals">
                    <div class="menu-icon">📊</div>
                    Goals
                </div>
                <div class="menu-button" id="cardio">
                    <div class="menu-icon">❤️‍🔥</div>
                    Cardio
                </div>
                <div class="menu-button" id="info">
                    <div class="menu-icon">ℹ️</div>
                    Info
                </div>
                <div class="menu-button" id="journal">
                    <div class="menu-icon">📄</div>
                    Journal
                </div>
                <div class="menu-button" id="profile">
                    <div class="menu-icon">👤</div>
                    Profile
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
                /* Fondo degradado violetas en toda la app */
                html, body, [data-testid="stAppViewContainer"] {
                    height: 100%;
                    margin: 0;
                    background: linear-gradient(135deg, #7b2ff7, #ac42f0, #c77aff);
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    padding-top: 40px;
                }

                /* Contenedor del banner para centrar y limitar tamaño */
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

                /* Botón centrado, tamaño y estilo para móviles */
                .stButton {
                    display: flex;
                    justify-content: center;
                    margin-bottom: 40px;
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
