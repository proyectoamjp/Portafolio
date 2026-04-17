# 🗂️ Portfolio Profesional — Streamlit

Dashboard de portafolio con 15 proyectos navegables, diseño dark mode profesional y navegación interna entre páginas.

## 🚀 Inicio rápido

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la app
streamlit run Home.py
```

## 📁 Estructura del proyecto

```
portfolio/
│
├── Home.py                    ← Página principal (dashboard)
│
├── pages/                     ← Las 15 páginas de proyectos
│   ├── 01_Análisis_Exploratorio_de_Datos.py
│   ├── 02_Modelo_de_Clasificación_ML.py
│   ├── 03_Predicción_de_Series_de_Tiempo.py
│   ├── 04_Procesamiento_de_Lenguaje_Natural.py
│   ├── 05_Visión_por_Computadora.py
│   ├── 06_Dashboard_de_Business_Intelligence.py
│   ├── 07_Sistema_de_Recomendación.py
│   ├── 08_API_REST_con_FastAPI.py
│   ├── 09_Análisis_de_Redes_Sociales.py
│   ├── 10_Detección_de_Anomalías.py
│   ├── 11_Generative_AI_—_Chatbot.py
│   ├── 12_Pipeline_de_Datos_ETL.py
│   ├── 13_Análisis_Geoespacial.py
│   ├── 14_Optimización_con_Algoritmos_Evolutivos.py
│   └── 15_Web_Scraping_&_Automatización.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py              ← ✏️ EDITA AQUÍ: tu nombre, bio, proyectos
│   ├── components.py          ← Componentes reutilizables y CSS global
│   └── generate_pages.py      ← Generador de páginas de proyecto
│
├── requirements.txt
└── README.md
```

## ✏️ Personalización

### 1. Editar tu perfil
Abre `utils/config.py` y modifica el diccionario `PROFILE`:
```python
PROFILE = {
    "name": "Tu Nombre Real",
    "role": "Tu Especialidad",
    "bio": "Tu descripción profesional...",
    "experience": "5+",
    "technologies": "20+",
    "location": "Tu Ciudad 🌎",
    "email": "tu@email.com",
}
```

### 2. Editar tus proyectos
En el mismo archivo, modifica la lista `PROJECTS` con los datos reales:
```python
{
    "id": 1,
    "title": "Nombre Real del Proyecto",
    "description": "Descripción real...",
    "icon": "📊",
    "category": "Data Analysis",
    "tags": ["Python", "Pandas", "Plotly"],
    "page": "pages/01_tu_pagina.py",  # ← ruta al archivo real
    "status": "Completado",
}
```

### 3. Editar las páginas existentes
Si ya tienes tus páginas creadas, simplemente:
1. Cópialas a la carpeta `pages/`
2. Actualiza el campo `"page"` en `config.py` con la ruta correcta
3. Agrega al inicio de cada página:
```python
from utils.components import inject_global_css
inject_global_css()
```

### 4. Redes sociales
En `config.py`, actualiza `SOCIAL_LINKS` con tus URLs reales.

## 🎨 Diseño

- **Tema**: Dark mode elegante
- **Fuentes**: Syne (títulos) + DM Sans (cuerpo) — Google Fonts
- **Colores**: Negro profundo, azul acento `#4f8ef7`, violeta `#a78bfa`
- **Animaciones**: Fade-in suave en carga, hover effects en tarjetas

## 💡 Tips

- Las tarjetas se filtran por categoría con el control segmentado
- Cada página de proyecto tiene un botón "← Volver al inicio"
- El CSS vive en `utils/components.py → inject_global_css()`
- Para agregar nuevas páginas, duplica cualquier archivo en `pages/`
