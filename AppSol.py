import streamlit as st
from PIL import Image

def menu():
    # Fondo degradado para toda la app en menú
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #7b2ff7, #ff7e5f);
            min-height: 100vh;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Encabezado con columnas (flecha atrás, título, menú)
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        if st.button("←"):
            st.session_state.pagina = "inicio"
    with col2:
        st.markdown("<h2 style='text-align:center; margin: 0;'>Fitness</h2>", unsafe_allow_html=True)
    with col3:
        st.button("≡")  # Botón menú (sin funcionalidad por ahora)

    st.markdown("---")

    # Lista de opciones con íconos y subtítulos
    opciones = [
        ("💪 Hipertrofia", "Entrenamientos enfocados en el crecimiento muscular."),
        ("🔥 Pérdida de grasa", ""),
        ("🏋️‍♂️ Aumento de fuerza", ""),
        ("🏃‍♂️ Resistencia física", ""),
        ("🎯 Definición muscular", ""),
        ("🌿 Bienestar general", "")
    ]

    # Botones apilados verticalmente con subtítulos
    for titulo, subtitulo in opciones:
        if st.button(f"{titulo}", key=titulo, help=subtitulo):
            st.info(f"Seleccionaste: {titulo}")
        if subtitulo:
            st.markdown(f"<small style='color:rgba(255,255,255,0.75); margin-bottom:15px; display:block;'>{subtitulo}</small>", unsafe_allow_html=True)

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
