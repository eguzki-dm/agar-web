TRANSLATIONS = {
    # ─── Navigation ─────────────────────────────────────────────
    "nav.section.home": "Inicio",
    "nav.section.learn": "Aprender",
    "nav.section.more": "Más",
    "nav.home": "Inicio",
    "nav.how_it_works": "¿Cómo funciona?",
    "nav.kount": "μKount",
    "nav.detect": "μDetect",
    "nav.results": "Resultados",
    "nav.about": "Aspectos técnicos",
    "nav.cuora": "Cuora",
    "nav.future": "Funcionalidades Futuras",
    "nav.disclaimer": "Aviso Legal",
    "nav.acknowledgments": "Agradecimientos",
    "nav.faq": "FAQ",
    "nav.fundamentals": "Fundamentos",

    # ─── Sidebar ────────────────────────────────────────────────
    "sidebar.language": "Idioma / Language",
    "sidebar.restart": "🔄 Reiniciar pipeline",
    "sidebar.microbiology_cta": "Si quieres saber más sobre microbiología:",
    "sidebar.microbiology_handle": "lifeisaboutmicrobiology",

    # ─── Home ───────────────────────────────────────────────────
    "home.title": "μKount & μDetect",
    "home.subtitle": "Inteligencia Artificial para análisis de placas de agar",
    "home.intro": "Sistema de visión artificial para:",
    "home.bullet.detection": "Detección de colonias",
    "home.bullet.counting": "Conteo automático",
    "home.bullet.classification": "Clasificación microbiológica",

    "home.based_on.intro": "Basado en:",
    "home.based_on.kount": "μKount (YOLO) — Detección y conteo de colonias",
    "home.based_on.detect": "μDetect (CNN) — Clasificación de especies microbianas",

    "home.pipeline": "Pipeline visual",
    "home.pipeline.upload.title": "Cargar",
    "home.pipeline.upload.subtitle": "Imagen",
    "home.pipeline.kount.title": "μKount",
    "home.pipeline.kount.subtitle": "Detección con YOLO",
    "home.pipeline.crop.title": "Recorte y preparación",
    "home.pipeline.crop.subtitle": "Fondo negro",
    "home.pipeline.detect.title": "μDetect",
    "home.pipeline.detect.subtitle": "Clasificación CNN",
    "home.pipeline.results.title": "Resultados",
    "home.pipeline.results.subtitle": "Visualizaciones",

    "home.dataset": "Dataset AGAR",
    "home.dataset.images": "~18.000 imágenes de placas de agar",
    "home.dataset.annotations": "~337.000 anotaciones de colonias",
    "home.dataset.configs": "Múltiples configuraciones de captura y condiciones de iluminación",
    "home.dataset.source": "Dataset: AGAR dataset de NeuroSYS Research",
    "home.dataset.authors": "Investigadores: Majchrowska et al. (2021)",
    "home.dataset.title": "Título: AGAR a microbial colony dataset for deep learning detection",

    "home.supporting": (
        "Apoyando a microbiólogos mediante detección automatizada de colonias, "
        "recuento y clasificación preliminar."
    ),

    "home.whatis.title": "¿Qué es μKount & μDetect?",
    "home.whatis.content": (
        "μKount & μDetect es un proyecto de Inteligencia Artificial desarrollado como trabajo final "
        "de la formación LABORLAN 2026: IA & Data Tech — Inteligencia Artificial y Gestión de Proyectos Tecnológicos.\n\n"
        "La aplicación asiste en el análisis macroscópico de cultivos microbianos en placas de agar combinando visión por computador y deep learning.\n\n"
        "Realiza tres tareas principales:\n\n"
        "* 🔍 Detección automática de colonias\n"
        "* 🔢 Recuento automático de colonias\n"
        "* 🧫 Clasificación preliminar de colonias\n\n"
        "La clasificación representa la especie más compatible según la morfología y debe interpretarse como apoyo a la decisión, no como diagnóstico definitivo."
    ),

    "home.architecture.title": "Arquitectura de IA",
    "home.arch.kount": "### μKount (YOLO)\n\nDetección y recuento automático de colonias.",
    "home.arch.detect": "### μDetect (CNN)\n\nClasificación preliminar de colonias microbianas.",

    "home.scope.title": "Alcance del modelo",
    "home.scope.content": (
        "El modelo ha sido entrenado con:\n\n"
        "* Placas de agar TSA\n"
        "* Imágenes cenitales de alta resolución\n"
        "* Cinco especies microbianas:\n\n"
        "  * _Bacillus subtilis_\n"
        "  * _Candida albicans_\n"
        "  * _Escherichia coli_\n"
        "  * _Pseudomonas aeruginosa_\n"
        "  * _Staphylococcus aureus_\n\n"
        "Las predicciones fuera de estas condiciones pueden no ser fiables."
    ),

    "home.dataset.content": (
        "El modelo fue entrenado con ~1.800 imágenes (10% del dataset AGAR) "
        "y ~6.000 recortes de colonias.\n\n"
        "Dataset: AGAR Dataset (Majchrowska et al., 2021)"
    ),

    "home.notice.title": "Aviso científico",
    "home.notice.items": (
        "μKount & μDetect es una prueba de concepto.\n\n"
        "Los resultados:\n\n"
        "* son solo para investigación y educación\n"
        "* no constituyen diagnóstico microbiológico\n"
        "* requieren validación en laboratorio\n"
        "* deben interpretarse por personal cualificado\n"
        "* no sustituyen métodos estándar"
    ),

    # ─── Pipeline page ──────────────────────────────────────────
    "pipeline.title": "🔬 Pipeline de procesamiento",
    "pipeline.show_tutorial": "💡 Mostrar tutorial",

    "tutorial.demo.title": "Demo interactivo",
    "tutorial.demo.desc": "Observa el pipeline ejecutándose paso a paso sobre una imagen real.",
    "tutorial.demo.button": "Ejecutar demo con 11_CAAL.jpg",

    "tutorial.next": "Siguiente →",
    "tutorial.restart": "Reiniciar demo",

    "tutorial.step4.detail": "Cada colonia se recorta y se redimensiona con padding (224×224).",
    "tutorial.crop.raw": "Recorte original",
    "tutorial.crop.padded": "Redimensionado con padding (224×224)",

    "pipeline.tutorial.title": "Guía paso a paso",

    "pipeline.subtitle": "Flujo completo desde imagen hasta clasificación final.",

    # ─── μKount page ───────────────────────────────────────────
    "kount.title": "🔍 μKount — Detección de colonias",
    "kount.subtitle": "Detección de colonias basada en YOLO (You Only Look Once).",

    "kount.detection_mode.full": "⚡ Modo rápido (recomendado)",
    "kount.detection_mode.sahi": "🔍 Modo alta precisión",

    "kount.upload.guide.title": "📤 Subir imágenes para μKount",
    "kount.upload.guide.desc": "Usa imágenes bien enfocadas y de alta calidad.",

    # ─── μDetect page ──────────────────────────────────────────
    "detect.title": "🧫 μDetect — Clasificación de colonias",
    "detect.subtitle": "Clasifica cada colonia detectada por especie microbiana.",

    "detect.mode.flash": "⚡ Rápido (solo imagen)",
    "detect.mode.robust": "🧬 Robusto (multimodal)",

    # ─── Results page ───────────────────────────────────────────
    "results.title": "📊 Resultados globales",
    "results.subtitle": "Resumen completo del análisis de la placa de agar.",

    "results.download_pdf": "📄 Descargar PDF",

    # ─── About page ────────────────────────────────────────────
    "about.title": "⚙️ Aspectos técnicos",
    "about.subtitle": (
        "μKount & μDetect es un sistema de visión artificial para análisis de placas de agar "
        "desarrollado como proyecto final de LABORLAN 2026 (IA, Machine Learning y Deep Learning)."
    ),

    "about.training.detect": "**μDetect (MobileNetV2)** — Transfer Learning, 5 especies, 50 épocas.",

    "about.version.desc": "Versión inicial de prueba de concepto. Modelos en desarrollo.",

    # ─── Future Features page ───────────────────────────────────
    "future.title": "🚀 Funcionalidades futuras",

    # ─── Disclaimer page ────────────────────────────────────────
    "disclaimer.title": "⚠️ Aviso legal — Ético y científico",
    "disclaimer.banner.text": "NO debe usarse para diagnóstico clínico.",

    "disclaimer.version.desc": "Versión de prueba de concepto. Evolución en desarrollo.",

    # ─── Cuora ──────────────────────────────────────────────────
    "cuora.title": "🧠 Cuora",
    "cuora.subtitle": "Asistente especializado en microbiología.",
    "cuora.prompt": (
        "Eres un experto en microbiología. Solo respondes preguntas relacionadas con microbiología. "
        "Si no lo son, responde: 'Lo siento, solo puedo responder preguntas relacionadas con microbiología.' "
        "No inventes información. Responde siempre en el idioma del usuario."
    ),

    # ─── Learn ──────────────────────────────────────────────────
    "learn.title": "🧠 Aprende IA",
    "learn.subtitle": "Conceptos clave de inteligencia artificial explicados de forma sencilla.",

    # ─── FAQ ─────────────────────────────────────────────────────
    "faq.title": "Preguntas frecuentes",

    "faq.q1.answer": "μKount detecta colonias y μDetect las clasifica usando IA.",
    "faq.q3.answer": "YOLO es un modelo de detección de objetos en tiempo real.",

    # ─── Cards / Charts (mínimos ajustes) ───────────────────────
    "cards.disclaimer.short": (
        "⚠️ μKount & μDetect es una prueba de concepto. "
        "Resultados experimentales, no usar para diagnóstico clínico."
    ),

    "charts.distribution.title": "Distribución de especies",
}