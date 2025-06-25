import streamlit as st
from PIL import Image

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

        # Banner en un div para poder aplicar estilos CSS
        try:
            banner = Image.open("banner.png")
            st.markdown('<div class="banner-container">', unsafe_allow_html=True)
            st.image(banner, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except:
            st.error("No se encuentra 'banner.png'. Verificá que esté en la carpeta correcta.")

        # Botón centrado con estilos arriba aplicados
        if st.button("Comenzar"):
            st.session_state.pagina = "menu"

    elif st.session_state.pagina == "menu":
        st.write("Aquí va el menú principal...")  # Simple placeholder

if __name__ == "__main__":
    main()
