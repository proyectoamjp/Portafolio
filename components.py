"""
components.py — Componentes reutilizables y estilos CSS globales.
"""

import streamlit as st


# ─────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────
def inject_global_css():
    """Inyecta el CSS global del portafolio."""
    st.markdown("""
    <style>
    /* ── IMPORTS ─────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

    /* ── VARIABLES ───────────────────────── */
    :root {
        --bg:        #f0f2f5;
        --bg-card:   #ffffff;
        --bg-hover:  #f5f8ff;
        --border:    rgba(0,0,0,0.08);
        --border-hover: rgba(37,99,235,0.35);
        --accent:    #2563eb;
        --accent-2:  #7c3aed;
        --text:      #111827;
        --text-muted:#6b7280;
        --radius:    14px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ── BASE ────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        color: var(--text);
    }
    .stApp, [data-testid="stAppViewContainer"] {
        background: var(--bg) !important;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1280px !important;
    }

    /* ── OCULTAR ELEMENTOS STREAMLIT ─────── */
    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display: none; }

    /* ── HERO ────────────────────────────── */
    .hero-section {
        text-align: center;
        padding: 3rem 1rem 2rem;
        position: relative;
    }
    .hero-tag {
        display: inline-block;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.2em;
        color: var(--accent);
        border: 1px solid rgba(79,142,247,0.3);
        padding: 0.3rem 0.9rem;
        border-radius: 100px;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
    }
    .hero-name {
        font-family: 'Syne', sans-serif !important;
        font-size: clamp(2rem, 10vw, 3.5rem) !important;
        font-weight: 800 !important;
        line-height: 1.05 !important;
        margin: 0 0 0.75rem !important;
        background: linear-gradient(135deg, #111827 20%, var(--accent) 70%, var(--accent-2) 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    .hero-role {
        font-size: 1rem;
        color: var(--text-muted);
        letter-spacing: 0.03em;
        margin-bottom: 1.2rem !important;
    }
    .hero-bio {
        max-width: 580px;
        margin: 0 auto 2rem !important;
        font-size: 1.05rem;
        color: var(--text-muted);
        line-height: 1.7;
    }
    .hero-divider {
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, var(--accent), var(--accent-2));
        margin: 0 auto;
        border-radius: 2px;
    }

    /* ── STATS BAR ───────────────────────── */
    .stats-bar {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.5rem;
        margin: 2rem 0;
    }
    .stat-item {
        text-align: center;
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }
    .stat-value {
        font-family: 'Syne', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--accent);
    }
    .stat-label {
        font-size: 0.78rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* ── SECTION HEADERS ─────────────────── */
    .section-title {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        margin-top: 2.5rem !important;
        margin-bottom: 0.4rem !important;
        color: var(--text) !important;
    }
    .section-subtitle {
        color: var(--text-muted) !important;
        font-size: 0.9rem !important;
        margin-bottom: 1.5rem !important;
    }

    /* ── CARDS ───────────────────────────── */
    .project-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.2rem;
        height: auto;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        transition: var(--transition);
        position: relative;
        overflow: visible;
        cursor: pointer;
        margin-bottom: 2rem;
    }
    .project-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent), var(--accent-2));
        opacity: 0;
        transition: var(--transition);
    }
    .project-card:hover {
        border-color: var(--border-hover);
        background: var(--bg-hover);
        transform: translateY(-3px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    .project-card:hover::before { opacity: 1; }

    .card-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: 0.6rem;
    }
    .card-icon {
        font-size: 1.8rem;
        line-height: 1;
    }
    .card-id {
        font-family: 'Syne', sans-serif;
        font-size: 0.7rem;
        color: var(--text-muted);
        letter-spacing: 0.1em;
    }
    .card-title {
        font-family: 'Syne', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.4rem;
        line-height: 1.2;
    }
    .card-description {
        font-size: 0.82rem;
        color: var(--text-muted);
        line-height: 1.5;
        margin-bottom: 0.8rem;
        flex-grow: 1;
    }
    .card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin-bottom: 0.8rem;
    }
    .card-tag {
        font-size: 0.68rem;
        color: var(--accent);
        background: rgba(79,142,247,0.1);
        border: 1px solid rgba(79,142,247,0.2);
        padding: 0.2rem 0.55rem;
        border-radius: 100px;
        letter-spacing: 0.03em;
    }
    .card-category {
        font-size: 0.68rem;
        color: var(--accent-2);
        background: rgba(167,139,250,0.1);
        border: 1px solid rgba(167,139,250,0.2);
        padding: 0.2rem 0.55rem;
        border-radius: 100px;
    }
    .card-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: auto;
        padding-top: 0.8rem;
        border-top: 1px solid var(--border);
    }
    .card-status {
        font-size: 0.68rem;
        color: #16a34a;
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    .card-status::before {
        content: '●';
        font-size: 0.5rem;
    }
    .card-button {
        font-size: 0.78rem;
        color: var(--accent);
        background: transparent;
        border: 1px solid rgba(79,142,247,0.3);
        padding: 0.3rem 0.9rem;
        border-radius: 8px;
        text-decoration: none;
        cursor: pointer;
        transition: var(--transition);
        font-weight: 500;
        letter-spacing: 0.03em;
        display: inline-block;
        text-decoration: none !important;
    }
    .card-button:hover {
        background: rgba(79,142,247,0.1);
        border-color: var(--accent);
        box-shadow: 0 0 20px rgba(79,142,247,0.15);
        text-decoration: none !important;
    }

    /* ── BOTONES ─────────────────────────── */
    .stButton > button {
        background: transparent !important;
        color: var(--accent) !important;
        border: 1px solid rgba(79,142,247,0.3) !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        padding: 0.3rem 0.9rem !important;
        letter-spacing: 0.03em !important;
        transition: var(--transition) !important;
        width: auto !important;
    }
    .stButton > button:hover {
        background: rgba(79,142,247,0.1) !important;
        border-color: var(--accent) !important;
        box-shadow: 0 0 20px rgba(79,142,247,0.15) !important;
    }

    /* ── BACK BUTTON ─────────────────────── */
    .back-btn > button {
        background: rgba(79,142,247,0.08) !important;
        color: var(--text-muted) !important;
        border: 1px solid var(--border) !important;
        font-size: 0.8rem !important;
    }

    /* ── SEGMENTED CONTROL ───────────────── */
    .stSegmentedControl {
        background: var(--bg-card) !important;
        border-radius: 10px !important;
    }

    /* ── SIDEBAR ─────────────────────────── */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: var(--bg-card) !important;
        border-right: 1px solid var(--border) !important;
    }
    .sidebar-nav-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.6rem 0.8rem;
        border-radius: 8px;
        cursor: pointer;
        transition: var(--transition);
        margin-bottom: 0.2rem;
        font-size: 0.85rem;
        color: var(--text-muted);
        text-decoration: none;
    }
    .sidebar-nav-item:hover {
        background: rgba(79,142,247,0.08);
        color: var(--text);
    }

    /* ── PROJECT PAGE ────────────────────── */
    .project-hero {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .project-hero::after {
        content: '';
        position: absolute;
        top: -50%; right: -10%;
        width: 300px; height: 300px;
        background: radial-gradient(circle, rgba(79,142,247,0.06) 0%, transparent 70%);
        pointer-events: none;
    }
    .project-big-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    .project-title {
        font-family: 'Syne', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.75rem !important;
    }
    .project-desc {
        color: var(--text-muted) !important;
        font-size: 1.05rem !important;
        line-height: 1.7 !important;
        max-width: 700px !important;
    }

    /* ── FOOTER ──────────────────────────── */
    .portfolio-footer {
        margin-top: 4rem;
        padding: 2rem;
        border-top: 1px solid var(--border);
        text-align: center;
        color: var(--text-muted);
        font-size: 0.82rem;
    }
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 1rem;
    }
    .footer-link {
        color: var(--text-muted);
        text-decoration: none;
        transition: color 0.2s;
        font-size: 0.85rem;
    }
    .footer-link:hover { color: var(--accent); }

    /* ── SCROLLBAR ───────────────────────── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(0,0,0,0.25); }

    /* ── ANIMACIONES ─────────────────────── */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .hero-section, .project-card {
        animation: fadeInUp 0.5s ease-out forwards;
    }

    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
# COMPONENTE: TARJETA DE PROYECTO
# ─────────────────────────────────────────
def render_card(project: dict):
    """Renderiza una tarjeta de proyecto con botón de navegación."""
    tags_html = "".join(
        f'<span class="card-tag">{tag}</span>' for tag in project["tags"][:2]
    )
    
    # Usar el campo url del proyecto
    project_url = project.get("url", "#")
    
    st.markdown(f"""
    <div class="project-card">
        <div class="card-header">
            <span class="card-icon">{project['icon']}</span>
            <span class="card-id">#{project['id']:02d}</span>
        </div>
        <div class="card-title">{project['title']}</div>
        <div class="card-description">{project['description']}</div>
        <div class="card-tags">
            <span class="card-category">{project['category']}</span>
            {tags_html}
        </div>
        <div class="card-footer">
            <span class="card-status">{project['status']}</span>
            <a href="{project_url}" target="_blank" class="card-button">Ver proyecto →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
# COMPONENTE: FOOTER
# ─────────────────────────────────────────
def render_footer(profile: dict, social_links: dict):
    """Renderiza el footer con links de contacto."""
    links_html = "".join(
        f'<a href="{data["url"]}" class="footer-link" target="_blank">{name}</a>'
        for name, data in social_links.items()
    )
    st.markdown(f"""
    <div class="portfolio-footer">
        <div class="footer-links">{links_html}</div>
        <div>✉ {profile['email']}</div>
        <div style="margin-top:0.5rem; opacity:0.5;">
            © 2025 {profile['name']} · Construido con Python & Streamlit
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
# COMPONENTE: HEADER DE PÁGINA DE PROYECTO
# ─────────────────────────────────────────
def render_project_header(project: dict):
    """Renderiza el encabezado de una página de proyecto individual."""
    tags_html = "".join(
        f'<span class="card-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(f"""
    <div class="project-hero">
        <span class="project-big-icon">{project['icon']}</span>
        <div class="section-title" style="font-size:2rem!important">{project['title']}</div>
        <div class="card-tags" style="margin:0.75rem 0 1rem">
            <span class="card-category">{project['category']}</span>
            {tags_html}
        </div>
        <p class="project-desc">{project['description']}</p>
    </div>
    """, unsafe_allow_html=True)
