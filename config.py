"""
config.py — Datos del perfil y proyectos del portafolio.
Edita este archivo para personalizar toda la información.
"""

# ─────────────────────────────────────────
# PERFIL PROFESIONAL
# ─────────────────────────────────────────
PROFILE = {
    "name": "Ana Maria Jaramillo Padierna",
    "role": "Automatizadora de procesos · Desarrolladora Python",
    "bio": "Transformo datos complejos en decisiones inteligentes. Apasionado por la inteligencia artificial, el análisis de datos y la creación de soluciones tecnológicas de alto impacto.",
    "experience": "5+",
    "location": "Colombia 🇨🇴",
    "email": "proyectoamjp@gmail.com",
}

# ─────────────────────────────────────────
# REDES SOCIALES
# ─────────────────────────────────────────
SOCIAL_LINKS = {
    "GitHub": {"url": "https://github.com/proyectoamjp", "icon": "⬡"},
    "LinkedIn": {"url": "https://linkedin.com/in/ana-maria-jaramillo-p-0815b7213", "icon": "in"},
    "Email": {"url": "mailto:proyectoamjp@gmail.com", "icon": "@"},
}

# ─────────────────────────────────────────
# PROYECTOS (15 proyectos)
# Campos: title, description, icon, category, tags, page, status
# ─────────────────────────────────────────
PROJECTS = [
    {
        "id": 1,
        "title": "Generador de Dígitos con VAE",
        
        "description": "Modelo generativo basado en VAE que aprende la representación latente de MNIST para generar nuevos dígitos de forma interactiva.",
        "icon": "🔢",
        "category": "Data Science",
        "tags": ["Deep Learning", "Generative Models", "MNIST"],
        "page": "https://dajmzwg8esz24mxpr2sdfp.streamlit.app/#variational-autoencoder-interactivo-para-explorar-y-generar-digitos",
        "status": "Completado",
        "url": "https://dajmzwg8esz24mxpr2sdfp.streamlit.app/#variational-autoencoder-interactivo-para-explorar-y-generar-digitos",
    },
    {
        "id": 2,
        "title": "Chat LLM con Anthropic",
        "description": "Interfaz de chat interactiva con modelos de Anthropic que permite ajustar parámetros de generación y definir la personalidad del asistente en tiempo real.",
        "icon": "🧠",
        "category": "LLM App",
        "tags": ["Streamlit", "LLM", "Anthropic"],
        "page": "pages/02_Modelo_de_Clasificación_ML.py",
        "status": "Completado",
        "url": "https://antchamjp.streamlit.app/",
    },
    {
        "id": 3,
        "title": "Chat Inteligente con PDFs (RAG)",
        "description": "Aplicación RAG que permite analizar documentos PDF y responder preguntas mediante búsqueda semántica y modelos de lenguaje.",
        "icon": "📄",
        "category": "LLM App",
        "tags": ["RAG", "PDF Analysis", "Language Models"],
        "page": "https://chatpdf-3kqtg4ywonj7her8patdk8.streamlit.app/",
        "status": "Completado",
        "url": "https://chatpdf-3kqtg4ywonj7her8patdk8.streamlit.app/",
    },
    {
        "id": 4,
        "title": "Chat Personalizado con OpenAI",
        "description": "Aplicación de chat con modelos de OpenAI que permite ajustar la personalidad del asistente y mantener conversaciones dinámicas en tiempo real.",
        "icon": "💬",
        "category": "LLM App",
        "tags": ["OpenAI", "Chatbot", "Streamlit"],
        "page": "https://chatgptanmjp.streamlit.app/",
        "status": "Completado",
        "url": "https://chatgptanmjp.streamlit.app/",
    },
    {
        "id": 5,
        "title": "Explorador de Convoluciones (CNN)",
        "description": "Visualiza cómo los filtros convolucionales transforman imágenes y explora feature maps de redes neuronales como VGG16 en tiempo real.",
        "icon": "🔬",
        "category": "Deep Learning",
        "tags": ["Computer Vision", "CNN", "TensorFlow"],
        "page": "https://convolucionesesdia.streamlit.app/",
        "status": "Completado",
        "url": "https://convolucionesesdia.streamlit.app/",
    },
    {
        "id": 6,
        "title": "Explorador Inteligente de Datos",
        "description": "Aplicación interactiva que permite cargar archivos CSV o Excel y analizarlos con IA mediante consultas en lenguaje natural, generando insights, estadísticas y visualizaciones automáticamente.",
        "icon": "📊",
        "category": "Data Analysis",
        "tags": ["Python", "Streamlit", "LangChain", "Pandas", "OpenAI"],
        "page": "https://anadataagent.streamlit.app/",
        "status": "Completado",
        "url": "https://anadataagent.streamlit.app/",
    },
    {
        "id": 7,
        "title": "Text to Speech Studio",
        "description": "Aplicación interactiva que convierte texto en audio en múltiples idiomas, permitiendo escuchar y descargar narraciones generadas automáticamente a partir de cualquier contenido escrito.",
        "icon": "🔊",
        "category": "AI / Audio",
        "tags": ["Python", "Streamlit", "gTTS", "Text-to-Speech", "Audio Processing"],
        "page": "https://audiocuentos.streamlit.app/",
        "status": "Completado",
        "url": "https://audiocuentos.streamlit.app/",
    },
    {
        "id": 8,
        "title": "Generador de Texto con LSTM",
        "description": "Aplicación interactiva que genera texto carácter a carácter usando redes neuronales LSTM, permitiendo controlar creatividad mediante temperatura y explorar el comportamiento del modelo.",
        "icon": "🧠",
        "category": "AI / Deep Learning",
        "tags": ["Python", "Streamlit", "LSTM", "TensorFlow", "NLP"],
        "page": "https://convoluciones-u7sqpcgfp3rw5mqfjtndt8.streamlit.app/",
        "status": "Completado",
        "url": "https://convoluciones-u7sqpcgfp3rw5mqfjtndt8.streamlit.app/",
    },
    {
        "id": 9,
        "title": "Detector de Dígitos con CNN",
        "description": "Aplicación interactiva que reconoce dígitos escritos a mano usando una red neuronal convolucional entrenada con MNIST, permitiendo dibujar en tiempo real y visualizar predicciones y probabilidades.",
        "icon": "✍️",
        "category": "AI / Computer Vision",
        "tags": ["Python", "Streamlit", "TensorFlow", "CNN", "MNIST"],
        "page": "https://mnistpred-kbetruvxi6rpzbe4ckz3bv.streamlit.app/",
        "status": "Completado",
        "url": "https://mnistpred-kbetruvxi6rpzbe4ckz3bv.streamlit.app/",
    },
    {
        "id": 10,
        "title": "Predicción de Consumo Eléctrico con LSTM",
        "description": "Aplicación interactiva que predice el consumo eléctrico futuro utilizando redes neuronales LSTM, permitiendo cargar datos reales, entrenar el modelo en tiempo real y visualizar tendencias y pronósticos.",
        "icon": "🔮",
        "category": "AI / Time Series",
        "tags": ["Python", "Streamlit", "PyTorch", "LSTM", "Forecasting"],
        "page": "https://penergia.streamlit.app/",
        "status": "Completado",
        "url": "https://penergia.streamlit.app/",
    },
    {
        "id": 11,
        "title": "Predicción de Series Temporales con RNN",
        "description": "Aplicación interactiva que utiliza una red neuronal recurrente (RNN) para predecir la continuación de señales temporales, permitiendo cargar modelos entrenados, generar señales y analizar el comportamiento interno de la red.",
        "icon": "🧠",
        "category": "AI / Deep Learning",
        "tags": ["Python", "Streamlit", "PyTorch", "RNN", "Time Series"],
        "page": "https://rnnbasica2.streamlit.app/",
        "status": "Completado",
        "url": "https://rnnbasica2.streamlit.app/",
    },
    {
        "id": 12,
        "title": "Clasificador de Flores con Transfer Learning",
        "description": "Aplicación web que clasifica imágenes de flores utilizando un modelo basado en MobileNetV2, permitiendo cargar modelos entrenados, analizar imágenes y visualizar probabilidades por clase en tiempo real.",
        "icon": "🌸",
        "category": "AI / Computer Vision",
        "tags": ["Python", "Streamlit", "TensorFlow", "Transfer Learning", "MobileNetV2"],
        "page": "https://tlflores-43enjszlxacsjcpmyrnw62.streamlit.app/",
        "status": "Completado",
        "url": "https://tlflores-43enjszlxacsjcpmyrnw62.streamlit.app/",
    },
    {
        "id": 13,
        "title": "Reconocimiento de Imágenes en Tiempo Real",
        "description": "Aplicación interactiva que utiliza un modelo entrenado con Teachable Machine para clasificar imágenes capturadas desde la cámara, permitiendo realizar predicciones en tiempo real directamente desde el navegador.",
        "icon": "📷",
        "category": "AI / Computer Vision",
        "tags": ["Python", "Streamlit", "TensorFlow", "Computer Vision", "Teachable Machine"],
        "page": "https://reconocimiento.streamlit.app/",
        "status": "Completado",
        "url": "https://reconocimiento.streamlit.app/   ",
    },
    {
        "id": 14,
        "title": "Traductor de Voz Multilenguaje",
        "description": "Aplicación interactiva que permite capturar voz en tiempo real, traducirla a múltiples idiomas y reproducir el resultado como audio, integrando reconocimiento de voz, traducción automática y síntesis de voz.",
        "icon": "🎤",
        "category": "AI / NLP",
        "tags": ["Python", "Streamlit", "Speech Recognition", "Translation", "gTTS"],
        "page": "https://traductorestidia.streamlit.app/",
        "status": "Completado",
        "url": "https://traductorestidia.streamlit.app/",
    },
    {
        "id": 15,
        "title": "Detección de Objetos con YOLOv5",
        "description": "Aplicación interactiva que detecta objetos en imágenes capturadas en tiempo real utilizando YOLOv5, mostrando resultados visuales, conteo por categorías y métricas de confianza.",
        "icon": "🔍",
        "category": "AI / Computer Vision",
        "tags": ["Python", "Streamlit", "PyTorch", "YOLOv5", "Object Detection"],
        "page": "https://9hmrebxedbkpyjszhm4zwx.streamlit.app/",
        "status": "Completado",
        "url": "https://9hmrebxedbkpyjszhm4zwx.streamlit.app/",
    },
]
