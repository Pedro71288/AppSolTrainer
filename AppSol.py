import streamlit as st

# Configurar la página
st.set_page_config(page_title="Sol Trainer", layout="centered")

# CSS personalizado
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #6a5acd, #ff7f50);
    color: white;
    font-family: 'Arial', sans-serif;
}
h1, h2, h3 {
    color: white;
    text-align: center;
}
.center {
    display: flex;
    justify-content: center;
    align-items: center;
}
button {
    font-size: 18px;
}
.card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    padding: 1rem;
}
.card {
    background: rgba(255,255,255,0.2);
    border: 2px solid white;
    border-radius: 10px;
    width: 25%;
    min-width: 120px;
    max-width: 180px;
    aspect-ratio: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.3s;
}
.card:hover {
    background: rgba(255,255,255,0.3);
}
.card img {
    width: 50px;
    height: 50px;
    margin-bottom: 10px;
}
@media (max-width: 600px) {
    .card { width: 45%; margin: 0.5rem; }
}
</style>
""", unsafe_allow_html=True)

# Estado de navegación
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "inicio"

# ——— PÁGINA INICIAL ———
if st.session_state["pagina"] == "inicio":
    st.markdown("<h1>Sol Trainer</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Tu camino al cambio empieza aquí</h3>", unsafe_allow_html=True)
    st.write("💡 Consejo del día: Cada paso que das, te acerca a tu mejor versión.")
    if st.button("Comenzar", use_container_width=True):
        st.session_state["pagina"] = "menu"

# ——— MENÚ PRINCIPAL ———
elif st.session_state["pagina"] == "menu":
    st.markdown("<h2>Seleccioná tu objetivo principal</h2>", unsafe_allow_html=True)

    cards = [
        ("Hipertrofia", "💪", "hipertrofia"),
        ("Pérdida de grasa", "🔥", "perdida_grasa"),
        ("Aumento de fuerza", "🏋️‍♂️", "fuerza"),
        ("Resistencia física", "🏃‍♂️", "resistencia"),
        ("Definición muscular", "🎯", "definicion"),
        ("Bienestar general", "🌿", "bienestar"),
    ]

    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    for name, icon, key in cards:
        st.markdown(f"""
        <div class="card">
            <div style="font-size:2rem;">{icon}</div>
            <div style="margin-top:0.5rem; font-size:1.2rem;">{name}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
