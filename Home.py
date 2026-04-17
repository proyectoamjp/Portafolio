"""
Portfolio Profesional - Página Principal
Autor: Ana Maria Jaramillo Padierna
Descripción: Dashboard central del portafolio con navegación a 15 proyectos.
"""

import streamlit as st
from utils.config import PROFILE, PROJECTS, SOCIAL_LINKS
from utils.components import render_card, render_footer, inject_global_css

# ─────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────
st.set_page_config(
    page_title=f"{PROFILE['name']} · Portfolio",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# ─────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-tag">PORTAFOLIO PROFESIONAL</div>
    <h1 class="hero-name">{name}</h1>
    <p class="hero-role">{role}</p>
    <p class="hero-bio">{bio}</p>
    <div class="hero-divider"></div>
</div>
""".format(**PROFILE), unsafe_allow_html=True)

# ─────────────────────────────────────────
# STATS BAR
# ─────────────────────────────────────────
st.markdown('<div class="stats-bar">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
stats = [
    ("15", "Proyectos"),
    (PROFILE["experience"], "Años de Experiencia"),
    (PROFILE["location"], "Ubicación"),
]
for col, (value, label) in zip([col1, col2, col3], stats):
    with col:
        st.markdown(f"""
        <div class="stat-item">
            <span class="stat-value">{value}</span>
            <span class="stat-label">{label}</span>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────
# SECCIÓN DE PROYECTOS
# ─────────────────────────────────────────
st.markdown('<h2 class="section-title">Proyectos Destacados</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Explora mi trabajo · Haz clic en cualquier tarjeta para ver el detalle</p>', unsafe_allow_html=True)

# Mostrar los 15 proyectos
filtered = PROJECTS[:15]

# Grid de tarjetas (3 columnas)
cols_per_row = 3
for i in range(0, len(filtered), cols_per_row):
    row = filtered[i:i + cols_per_row]
    cols = st.columns(cols_per_row)
    for col, project in zip(cols, row):
        with col:
            render_card(project)
    st.write("")  # Espaciado vertical entre filas

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
render_footer(PROFILE, SOCIAL_LINKS)
