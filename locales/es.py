TRANSLATIONS = {
    # ─── Navigation ─────────────────────────────────────────────
    "nav.home": "Inicio",
    "nav.pipeline": "Pipeline",
    "nav.kount": "\u03bcKount",
    "nav.detect": "\u03bcDetect",
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
    "sidebar.restart": "\U0001f504 Reiniciar pipeline",
    "sidebar.microbiology_cta": "Si quieres saber m\u00e1s sobre microbiolog\u00eda:",
    "sidebar.microbiology_handle": "lifeisaboutmicrobiology",

    # ─── Home ───────────────────────────────────────────────────
    "home.title": "\u03bcKount&\u03bcDetect",
    "home.subtitle": "Inteligencia Artificial para An\u00e1lisis de Placas de Agar",
    "home.intro": "Sistema de visi\u00f3n artificial para:",
    "home.bullet.detection": "Detecci\u00f3n de colonias",
    "home.bullet.counting": "Conteo autom\u00e1tico",
    "home.bullet.classification": "Clasificaci\u00f3n microbiol\u00f3gica",
    "home.based_on.intro": "Basado en:",
    "home.based_on.kount": "\u03bcKount (YOLO) \u2014 Detecci\u00f3n y conteo de colonias",
    "home.based_on.detect": "\u03bcDetect (CNN) \u2014 Clasificaci\u00f3n de especies microbianas",
    "home.pipeline": "Pipeline Visual",
    "home.pipeline.upload.title": "Cargar",
    "home.pipeline.upload.subtitle": "Imagen",
    "home.pipeline.kount.title": "\u03bcKount",
    "home.pipeline.kount.subtitle": "Detecci\u00f3n YOLO",
    "home.pipeline.crop.title": "Recorte y Prep",
    "home.pipeline.crop.subtitle": "Fondo Negro",
    "home.pipeline.detect.title": "\u03bcDetect",
    "home.pipeline.detect.subtitle": "Clasificaci\u00f3n CNN",
    "home.pipeline.results.title": "Resultados",
    "home.pipeline.results.subtitle": "Visualizaciones",
    "home.dataset": "Dataset AGAR",
    "home.dataset.images": "~18.000 im\u00e1genes de placas de agar",
    "home.dataset.annotations": "~337.000 anotaciones de colonias",
    "home.dataset.configs": "M\u00faltiples configuraciones de captura y condiciones de iluminaci\u00f3n",
    "home.dataset.source": "Dataset: AGAR dataset de NeuroSYS Research",
    "home.dataset.authors": "Investigadores: Majchrowska et al. (2021)",
    "home.dataset.title": "T\u00edtulo: AGAR a microbial colony dataset for deep learning detection",
    "home.supporting": (
        "Apoyando a microbi\u00f3logos mediante detecci\u00f3n automatizada de colonias, "
        "recuento y clasificaci\u00f3n preliminar de colonias."
    ),
    "home.whatis.title": "\u00bfQu\u00e9 es \u03bcKount & \u03bcDetect?",
    "home.whatis.content": (
        "\u03bcKount & \u03bcDetect es un proyecto de Inteligencia Artificial "
        "desarrollado como trabajo final de la formaci\u00f3n "
        "**LABORLAN 2026: IA&Data Tech \u2013 Inteligencia Artificial "
        "y Gesti\u00f3n de Proyectos Tecnol\u00f3gicos**.\n\n"
        "La aplicaci\u00f3n asiste en el **an\u00e1lisis macrosc\u00f3pico de cultivos microbianos** "
        "crecidos en placas de agar combinando t\u00e9cnicas de Computer Vision y Deep Learning.\n\n"
        "Realiza tres tareas principales:\n\n"
        "* \U0001f50d Detecci\u00f3n autom\u00e1tica de colonias\n"
        "* \U0001f522 Recuento autom\u00e1tico de colonias\n"
        "* \U0001f9eb Clasificaci\u00f3n preliminar de colonias\n\n"
        "La clasificaci\u00f3n proporcionada por el modelo representa la **especie m\u00e1s compatible "
        "seg\u00fan la morfolog\u00eda de la colonia** y debe considerarse como apoyo a la decisi\u00f3n, "
        "no como una identificaci\u00f3n microbiol\u00f3gica definitiva."
    ),
    "home.architecture.title": "Arquitectura de IA",
    "home.arch.kount": (
        "### \u03bcKount (YOLO)\n\nDetecci\u00f3n y recuento autom\u00e1tico de colonias."
    ),
    "home.arch.detect": (
        "### \u03bcDetect (CNN)\n\nClasificaci\u00f3n preliminar de colonias microbianas."
    ),
    "home.scope.title": "Alcance del Modelo",
    "home.scope.content": (
        "La versi\u00f3n actual ha sido entrenada utilizando:\n\n"
        "* Placas de agar TSA\n"
        "* Im\u00e1genes cenitales de alta resoluci\u00f3n\n"
        "* Cinco especies microbianas:\n\n"
        "  * _Bacillus subtilis_\n"
        "  * _Candida albicans_\n"
        "  * _Escherichia coli_\n"
        "  * _Pseudomonas aeruginosa_\n"
        "  * _Staphylococcus aureus_\n\n"
        "Las predicciones fuera de estas condiciones pueden no ser fiables."
    ),
    "home.dataset.content": (
        "Aproximadamente **18.000 im\u00e1genes de placas de agar** y **337.000 anotaciones "
        "de colonias** de m\u00faltiples configuraciones de captura y condiciones de iluminaci\u00f3n.\n\n"
        "Dataset: **AGAR Dataset** (Majchrowska et al., 2021)"
    ),
    "home.notice.title": "Aviso Cient\u00edfico",
    "home.notice.items": (
        "\u03bcKount & \u03bcDetect es actualmente un **Prueba de Concepto**.\n\n"
        "Los resultados generados por esta aplicaci\u00f3n:\n\n"
        "* est\u00e1n destinados exclusivamente a fines de investigaci\u00f3n y educativos;\n"
        "* no constituyen un diagn\u00f3stico microbiol\u00f3gico o cl\u00ednico;\n"
        "* no reemplazan las t\u00e9cnicas de identificaci\u00f3n est\u00e1ndar de laboratorio;\n"
        "* deben ser siempre interpretados por personal cualificado;\n"
        "* requieren confirmaci\u00f3n mediante m\u00e9todos microbiol\u00f3gicos convencionales "
        "(ej. pruebas bioqu\u00edmicas o MALDI-TOF)."
    ),

    # ─── Pipeline page ──────────────────────────────────────────
    "pipeline.title": "\U0001f52c Pipeline de Procesamiento",
    "pipeline.show_tutorial": "\U0001f4a1 Mostrar tutorial",
    "pipeline.tutorial.title": "Gu\u00eda paso a paso",
    "pipeline.tutorial.0": "**Sube una imagen de placa de agar** \u2014 El proceso "
        "comienza cuando subes una foto de una placa de agar. La app acepta "
        "formatos est\u00e1ndar como PNG, JPG y JPEG. Una vez cargada, la imagen "
        "se almacena en memoria y est\u00e1 lista para el siguiente paso.",
    "pipeline.tutorial.1": "**\u03bcKount (detecci\u00f3n YOLO)** \u2014 \u03bcKount utiliza un modelo "
        "YOLOv8 para escanear la imagen y localizar cada colonia. Por cada colonia "
        "encontrada, dibuja un bounding box y asigna un nivel de confianza. "
        "Puedes revisar los resultados antes de continuar.",
    "pipeline.tutorial.2": "**Bounding boxes** \u2014 Cada colonia detectada se resalta "
        "con una caja de color y un n\u00famero. El nivel de confianza (0\u20131) indica "
        "cu\u00e1n seguro est\u00e1 el modelo de haber encontrado una colonia real. "
        "Cuanto m\u00e1s alto, mejor.",
    "pipeline.tutorial.3": "**Extracci\u00f3n de recortes** \u2014 Cada bounding box se usa "
        "para recortar un cuadrado peque\u00f1o de la imagen original, aislando una "
        "sola colonia. Estos recortes son la entrada para la siguiente fase.",
    "pipeline.tutorial.4": "**Fondo negro** \u2014 Un filtro elimina el fondo brillante "
        "del agar, dejando solo la colonia visible sobre negro. Esto ayuda a la "
        "CNN a centrarse en la forma y textura de la colonia, mejorando la "
        "precisi\u00f3n de la clasificaci\u00f3n.",
    "pipeline.tutorial.5": "**\u03bcDetect (clasificaci\u00f3n CNN)** \u2014 Cada recorte con "
        "fondo negro se pasa por un modelo MobileNetV2 que predice la especie "
        "m\u00e1s probable. El resultado incluye una probabilidad para cada una de "
        "las 5 especies soportadas.",
    "pipeline.tutorial.6": "**Resultados e interpretaci\u00f3n** \u2014 La p\u00e1gina final "
        "muestra: un gr\u00e1fico de distribuci\u00f3n de especies, probabilidades por "
        "colonia, un mapa de calor y tarjetas detalladas para cada especie. "
        "**Recuerda**: esto es una prueba de concepto \u2014 los resultados deben "
        "verificarse en un laboratorio.",
    "pipeline.subtitle": "Diagrama del flujo completo de \u03bcKount&\u03bcDetect, desde la imagen original hasta la clasificaci\u00f3n final.",
    "pipeline.step1.title": "\U0001f4e4 Imagen de Entrada",
    "pipeline.step1.desc": "El usuario sube una imagen de placa de agar (formatos: PNG, JPG, JPEG). "
        "La imagen se convierte a RGB y se almacena para su procesamiento.",
    "pipeline.step1.source": "services/preprocessing_service.py",
    "pipeline.step2.title": "\U0001f50d \u03bcKount (YOLO)",
    "pipeline.step2.desc": "Modelo de detecci\u00f3n basado en YOLO (You Only Look Once). "
        "Localiza colonias en la imagen generando bounding boxes con confianza asociada. "
        "Devuelve coordenadas y puntuaci\u00f3n de confianza para cada colonia detectada.",
    "pipeline.step2.source": "services/detection_service.py",
    "pipeline.step3.title": "\U0001f4e6 Bounding Boxes",
    "pipeline.step3.desc": "Las colonias detectadas se visualizan con bounding boxes de colores sobre la imagen original. "
        "Cada caja incluye un identificador num\u00e9rico y el nivel de confianza de la detecci\u00f3n.",
    "pipeline.step3.source": "detection_service.py \u2192 components/image_viewer.py",
    "pipeline.step4.title": "\u2702\ufe0f Extracci\u00f3n de Recortes",
    "pipeline.step4.desc": "Cada colonia detectada se extrae individualmente de la imagen original "
        "utilizando las coordenadas de su bounding box. Los recortes se preparan para la fase de clasificaci\u00f3n.",
    "pipeline.step4.source": "services/preprocessing_service.py",
    "pipeline.step5.title": "\u2b1b Fondo Negro",
    "pipeline.step5.desc": "A cada recorte se le aplica un filtro de fondo negro: los p\u00edxeles con valor "
        "superior a un umbral (fondo de agar claro) se convierten a negro, "
        "manteniendo \u00fanicamente la colonia visible. Esto mejora la precisi\u00f3n de la CNN.",
    "pipeline.step5.source": "services/preprocessing_service.py",
    "pipeline.step6.title": "\U0001f9ea \u03bcDetect (CNN)",
    "pipeline.step6.desc": "Modelo CNN basado en Transfer Learning. Cada recorte con fondo negro se clasifica "
        "en una de las 5 especies soportadas, devolviendo un vector de probabilidades para cada una.",
    "pipeline.step6.source": "services/classification_service.py",
    "pipeline.step7.title": "\U0001f4ca Predicci\u00f3n + Resultados",
    "pipeline.step7.desc": "Resultados finales: distribuci\u00f3n de especies, m\u00e9tricas por colonia, "
        "mapa de probabilidades y visualizaciones interactivas con Plotly.",
    "pipeline.step7.source": "pages/05_results.py + components/charts.py",

    # ─── μKount page ───────────────────────────────────────────
    "kount.title": "\U0001f50d \u03bcKount \u2014 Detecci\u00f3n de Colonias",
    "kount.subtitle": "Detecci\u00f3n de colonias basada en YOLO con Slicing Aided Hyper Inference.",
    "kount.tab.upload": "Subir Imagen",
    "kount.tab.examples": "Im\u00e1genes de Ejemplo",
    "kount.upload.label": "Selecciona una imagen de placa de agar",
    "kount.status.loaded": "Imagen cargada correctamente.",
    "kount.examples.select": "Selecciona una imagen de ejemplo para cargarla:",
    "kount.examples.none": "No se encontraron im\u00e1genes de ejemplo.",
    "kount.download_json": "\U0001f4e5 Descargar JSON",
    "kount.confidence.label": "Umbral de confianza de detecci\u00f3n",
    "kount.filter.label": "Confianza m\u00ednima para mostrar",
    "kount.detect.button": "\u25b6\ufe0f Ejecutar \u03bcKount",
    "kount.status.detected": "{count} colonias detectadas en {time} s.",
    "kount.next.button": "\u27a1\ufe0f Procesar con \u03bcDetect",
    "kount.no_image": "Sube una imagen para comenzar.",
    "kount.loaded_image": "Imagen cargada",
    "kount.detection_result": "Resultado de detecci\u00f3n",
    "kount.detection_mode.title": "Modo de Detecci\u00f3n",
    "kount.detection_mode.full": "\u26a1 Modo Vibrio (Recomendado)",
    "kount.detection_mode.sahi": "\U0001f50d Modo Agar Explorer",
    "kount.detection_mode.full.desc": "Detecci\u00f3n r\u00e1pida de placa completa.",
    "kount.detection_mode.sahi.desc": "Detecci\u00f3n de alta resoluci\u00f3n para placas densas.",
    "kount.detection_mode.sahi.optimizing": "\u26a0\ufe0f Optimizaci\u00f3n en curso \u2014 optimizando para mejor calidad de resultados",
    "kount.upload.guide.title": "📤 Subir imágenes para μKount",
    "kount.upload.guide.desc": "Antes de subir, asegúrate de que tus imágenes sean **de alta calidad y estén bien enfocadas**.",
    "kount.upload.guide.example": "🔎 Búsqueda de ejemplo en Google:",
    "kount.upload.guide.example_query": "agar plate triptona soya agar",
    "kount.upload.guide.search_button": "🔍 Google Imágenes",
    "kount.upload.guide.tip_size": "📏 Tamaño de imagen: **Grande**",
    "kount.upload.guide.tip_clarity": "🧫 Placa de Petri clara / agar visible",
    "kount.upload.guide.tip_compression": "📸 Sin compresión pesada",

    # ─── μDetect page ──────────────────────────────────────────
    "detect.title": "\U0001f9ea \u03bcDetect \u2014 Clasificaci\u00f3n de Colonias",
    "detect.subtitle": "Clasifica cada colonia detectada por especie microbiana.",
    "detect.warning.no_detections": "No hay detecciones previas. Ejecuta \u03bcKount primero "
        "para detectar colonias en una imagen.",
    "detect.button.back": "\u2190 Ir a \u03bcKount",
    "detect.error.no_image": "No hay imagen original disponible. Regresa a \u03bcKount y carga una imagen.",
    "detect.status.ready": "{count} colonias detectadas listas para clasificaci\u00f3n.",
    "detect.process.button": "\u25b6\ufe0f Ejecutar \u03bcDetect",
    "detect.step1.title": "Extracci\u00f3n de Recortes",
    "detect.step1.desc": "Extrayendo cada colonia de la imagen original usando las coordenadas de los bounding boxes...",
    "detect.step2.title": "Fondo Negro",
    "detect.step2.desc": "Aplicando fondo negro a cada recorte para mejorar la clasificaci\u00f3n...",
    "detect.status.crops_extracted": "{count} recortes extra\u00eddos.",
    "detect.status.classified": "{count} colonias clasificadas.",
    "detect.toast.done": "\u00a1Listo! Tienes {count} colonias, las principales son: {species}",
    "detect.results.title": "Resultados por Colonia",
    "detect.colony.label": "Colonia #{number}",
    "detect.colony.processed": "Recorte procesado",
    "detect.species.label": "Especie predicha",
    "detect.confidence.label": "Confianza",
    "detect.detection_precision": "Precisi\u00f3n detecci\u00f3n",
    "detect.probabilities.title": "Ver probabilidades detalladas",
    "detect.info.run": "Presiona 'Ejecutar \u03bcDetect' para clasificar las colonias.",
    "detect.button.results": "\U0001f4ca Ir a Resultados",

    # ─── Results page ───────────────────────────────────────────
    "results.title": "\U0001f4ca Resultados \u2014 Resultados Globales",
    "results.subtitle": "Resumen completo del an\u00e1lisis de la placa de agar.",
    "results.warning.no_data": "No hay datos de an\u00e1lisis. Ejecuta \u03bcKount y \u03bcDetect primero.",
    "results.summary.title": "Resumen del An\u00e1lisis",
    "results.species_distribution.title": "Distribuci\u00f3n de Especies",
    "results.percentage.title": "Distribuci\u00f3n Porcentual",
    "results.probability_table.title": "Probabilidades por Colonia",
    "results.probability_map.title": "Mapa de Probabilidades",
    "results.species_info.title": "Informaci\u00f3n de Especies Detectadas",
    "results.no_classifications": "No hay clasificaciones. Ejecuta \u03bcDetect para clasificar las colonias detectadas.",
    "results.colony": "Colonia",
    "results.predicted_species": "Especie predicha",
    "results.description": "Descripci\u00f3n",
    "results.clinical_significance": "Relevancia cl\u00ednica",
    "results.industrial_relevance": "Relevancia industrial",
    "results.pharmaceutical_applications": "Aplicaciones farmac\u00e9uticas",
    "results.common_habitats": "H\u00e1bitats comunes",
    "results.warnings": "Advertencias",
    "results.biosafety_notes": "Bioseguridad",
    "results.references": "Referencias",
    "results.not_available": "N/D",
    "results.download_json": "\U0001f4e5 Descargar JSON",
    "results.download_pdf": "\U0001f4c4 Descargar PDF",
    "results.tab.kount": "\u03bcKount",
    "results.tab.detect": "\u03bcDetect",
    "results.cfu.title": "\U0001f9ee Calculadora de UFC",
    "results.cfu.subtitle": "Estima la concentraci\u00f3n microbiana de la muestra original a partir del n\u00famero de colonias detectadas.",
    "results.cfu.colony_count": "N\u00famero de colonias",
    "results.cfu.sample_type": "Tipo de muestra",
    "results.cfu.liquid": "Muestra l\u00edquida",
    "results.cfu.solid": "Muestra s\u00f3lida",
    "results.cfu.dilution": "Diluci\u00f3n",
    "results.cfu.volume": "Volumen sembrado (mL)",
    "results.cfu.calculate": "\U0001f9ee Calcular UFC",
    "results.cfu.result": "Concentraci\u00f3n estimada",
    "results.cfu.unit_ml": "UFC/mL",
    "results.cfu.unit_g": "UFC/g",
    "results.cfu.error.colonies": "El n\u00famero de colonias debe ser mayor que 0.",
    "results.cfu.error.volume": "El volumen debe ser mayor que 0.",
    "results.cfu.error.dilution": "Selecciona una diluci\u00f3n.",
    "results.cfu.validation.valid": "\U0001f7e2 Recuento v\u00e1lido (30\u2013300 colonias). Apto para estimaci\u00f3n de UFC.",
    "results.cfu.validation.low": "\U0001f7e1 Recuento bajo (<30 colonias). La estimaci\u00f3n puede ser imprecisa.",
    "results.cfu.validation.high": "\U0001f534 Demasiadas colonias (>300). Considera usar una diluci\u00f3n mayor.",
    "results.cfu.disclaimer": "Esta estimaci\u00f3n se basa en el n\u00famero de colonias detectadas y los par\u00e1metros de diluci\u00f3n proporcionados por el usuario. Los resultados tienen fines educativos y de investigaci\u00f3n y deben confirmarse mediante procedimientos microbiol\u00f3gicos est\u00e1ndar de laboratorio.",

    # ─── About page ────────────────────────────────────────────
    "about.title": "\u2699\ufe0f Aspectos t\u00e9cnicos",
    "about.subtitle": "\u03bcKount&\u03bcDetect (Artificial Intelligence for Agar Plate Analysis) es un sistema de "
        "visi\u00f3n artificial dise\u00f1ado para la detecci\u00f3n, conteo y clasificaci\u00f3n de "
        "colonias microbianas en placas de agar. "
        "Este proyecto es el proyecto final del programa de formación Laborlan en IA, Machine Learning y Deep Learning",
    "about.kount.title": "\U0001f9eb \u03bcKount \u2014 Detector de Colonias",
    "about.kount.function": "Localizar colonias en im\u00e1genes de placas de agar, "
        "generar bounding boxes alrededor de cada colonia, "
        "proporcionar un conteo autom\u00e1tico del n\u00famero de colonias.",
    "about.kount.tech": "Arquitectura: YOLOv8, Framework: Ultralytics, "
        "Formato de salida: coordenadas (x1, y1, x2, y2) + confianza",
    "about.detect.title": "\U0001f9ea \u03bcDetect \u2014 Clasificador de Especies",
    "about.detect.function": "Clasificar colonias individuales en especies microbianas, "
        "proporcionar probabilidades para cada especie soportada.",
    "about.detect.species": "*S. aureus, B. subtilis, P. aeruginosa, E. coli, C. albicans*",
    "about.detect.tech": "Arquitectura: CNN basada en modelos pre-entrenados (MobileNet), "
        "Framework: TensorFlow / PyTorch (pendiente de definir)",
    "about.dataset.title": "\U0001f4ca Dataset AGAR",
    "about.dataset.content": "~18.000 im\u00e1genes de placas de agar, ~337.000 anotaciones de colonias individuales, "
        "M\u00faltiples configuraciones de captura (iluminaci\u00f3n, \u00e1ngulo, distancia), "
        "Anotaciones realizadas por microbi\u00f3logos expertos. "
        "Las im\u00e1genes fueron adquiridas en condiciones controladas de laboratorio "
        "y representan 5 especies microbianas diferentes.",
    "about.env.title": "\u2699\ufe0f Entorno de Desarrollo",
    "about.env.content": "Python 3.11, Streamlit 1.38+, Ultralytics YOLOv8, "
        "TensorFlow 2.15, OpenCV 4.9, NumPy, Plotly, scikit-learn",
    "about.training.title": "\U0001f9e0 Entrenamiento del Modelo",
    "about.training.kount": "**\u03bcKount (YOLOv8m)** \u2014 Entrada: 640px, "
        "\u00c9pocas: 150, Batch: 16, Optimizador: AdamW, Hardware: NVIDIA RTX 3060 12GB",
    "about.training.detect": "**\u03bcDetect (MobileNetV2)** \u2014 Entrada: 224px, "
        "Transfer Learning, Especies: 5, \u00c9pocas: 50, Framework: TensorFlow",
    "about.paper.title": "\U0001f4c4 Referencia Acad\u00e9mica",
    "about.paper.content": "Majchrowska et al. (2021). AGAR: a microbial colony "
        "dataset for deep learning detection. *Scientific Reports*, 11, 23973. "
        "DOI: [10.1038/s41598-021-02912-2](https://doi.org/10.1038/s41598-021-02912-2)",
    "about.repository.title": "\U0001f4bb C\u00f3digo Fuente",
    "about.repository.content": "El c\u00f3digo fuente completo de este proyecto "
        "est\u00e1 disponible en:\n\n"
        "[https://github.com/eguzki-dm/agar-web](https://github.com/eguzki-dm/agar-web)",
    "about.architecture.title": "Arquitectura del Proyecto",

    # ─── Future Features page ───────────────────────────────────
    "future.title": "\U0001f680 Funcionalidades Futuras",
    "future.subtitle": "Funcionalidades implementadas y planificadas para \u03bcKount&\u03bcDetect.",
    "future.feature.edit_boxes": "Editar bounding boxes",
    "future.feature.edit_boxes.desc": "Mover, redimensionar, eliminar o a\u00f1adir cajas de "
        "detecci\u00f3n manualmente tras el procesamiento de \u03bcKount.",
    "future.feature.optimize_sahi": "Optimizar procesamiento SAHI slicing",
    "future.feature.optimize_sahi.desc": "Mejorar el rendimiento del pipeline de inferencia SAHI slicing para placas densas. Optimizar solapamiento de slices, procesamiento por lotes y post-procesado para reducir el tiempo de detecci\u00f3n manteniendo la sensibilidad para colonias peque\u00f1as.",
    "future.feature.improve_cnn": "Mejorar CNN para clasificaci\u00f3n de bacterias",
    "future.feature.improve_cnn.desc": "Reentrenar el modelo con m\u00e1s especies, distintos "
        "medios de cultivo y condiciones de iluminaci\u00f3n para mejorar la generalizaci\u00f3n.",

    # ─── Disclaimer page ────────────────────────────────────────
    "disclaimer.title": "\u26a0\ufe0f Aviso Legal \u2014 Aviso \u00e9tico y cient\u00edfico",
    "disclaimer.banner.title": "\u03bcKount&\u03bcDetect es un Sistema de Investigaci\u00f3n de Prueba de Concepto",
    "disclaimer.banner.text": "NO debe usarse para diagn\u00f3stico cl\u00ednico.",
    "disclaimer.limitations.title": "Limitaciones del Sistema",
    "disclaimer.limitation1.title": "\U0001f52c Prop\u00f3sito exclusivamente investigador",
    "disclaimer.limitation1.desc": "\u03bcKount&\u03bcDetect es una herramienta de investigaci\u00f3n y desarrollo. No est\u00e1 aprobada "
        "por ninguna autoridad sanitaria (FDA, EMA, etc.) para uso diagn\u00f3stico.",
    "disclaimer.limitation2.title": "\U0001f9ea No sustituye t\u00e9cnicas gold-standard",
    "disclaimer.limitation2.desc": "Los m\u00e9todos microbiol\u00f3gicos convencionales (cultivo, tinci\u00f3n Gram, "
        "pruebas bioqu\u00edmicas, MALDI-TOF) siguen siendo el est\u00e1ndar de referencia. "
        "\u03bcKount&\u03bcDetect no reemplaza estos m\u00e9todos.",
    "disclaimer.limitation3.title": "\u26a0\ufe0f Resultados experimentales",
    "disclaimer.limitation3.desc": "Los modelos de detecci\u00f3n y clasificaci\u00f3n pueden producir errores. "
        "Falsos positivos, falsos negativos y clasificaciones incorrectas son "
        "posibles y deben ser verificados.",
    "disclaimer.limitation4.title": "\U0001f4cb Validaci\u00f3n requerida",
    "disclaimer.limitation4.desc": "Todos los resultados deben ser validados mediante procedimientos de "
        "laboratorio adecuados antes de tomar cualquier decisi\u00f3n.",
    "disclaimer.limitation5.title": "\U0001f468\u200d\U0001f52c Interpretaci\u00f3n profesional necesaria",
    "disclaimer.limitation5.desc": "Los resultados deben ser interpretados exclusivamente por personal "
        "cualificado (microbi\u00f3logos, bioqu\u00edmicos, profesionales sanitarios).",
    "disclaimer.limitation6.title": "\U0001f916 Sin juicio cl\u00ednico",
    "disclaimer.limitation6.desc": "El sistema no incorpora juicio cl\u00ednico ni conocimiento contextual del "
        "paciente. No puede considerar el historial m\u00e9dico ni otras variables "
        "relevantes para un diagn\u00f3stico.",
    "disclaimer.responsible_use.title": "Uso Responsable",
    "disclaimer.responsible_use.intro": "Al utilizar \u03bcKount&\u03bcDetect, el usuario acepta:",
    "disclaimer.responsible_use.item1": "NO utilizar los resultados para diagn\u00f3stico cl\u00ednico sin validaci\u00f3n previa.",
    "disclaimer.responsible_use.item2": "NO tomar decisiones m\u00e9dicas bas\u00e1ndose \u00fanicamente en la salida del sistema.",
    "disclaimer.responsible_use.item3": "Verificar todas las detecciones y clasificaciones mediante m\u00e9todos convencionales.",
    "disclaimer.responsible_use.item4": "Citar \u03bcKount&\u03bcDetect como herramienta de investigaci\u00f3n en cualquier publicaci\u00f3n que utilice sus resultados.",
    "disclaimer.responsible_use.footer": "El incumplimiento de estas condiciones puede tener consecuencias graves en contextos "
        "cl\u00ednicos. Los desarrolladores de \u03bcKount&\u03bcDetect no se hacen responsables del uso indebido "
        "del sistema.",
    "disclaimer.version.title": "Versi\u00f3n Actual",
    "disclaimer.version.info": "Versi\u00f3n 1.0.0 \u2014 \u00a1Cuora est\u00e1 viva! \U0001f9e0",
    "disclaimer.version.desc": "Esta versi\u00f3n inicial utiliza datos simulados para demostrar la arquitectura y el "
        "flujo de trabajo. Los modelos reales (YOLO, CNN) se integrar\u00e1n en fases posteriores.",
    "disclaimer.version.status": "Estado: Proof of Concept / Prototipo funcional",

    # ─── Cards ──────────────────────────────────────────────────
    "cards.disclaimer.title": "\u26a0\ufe0f IMPORTANTE \u2014 AVISO \u00c9TICO Y CIENT\u00cdFICO",
    "cards.disclaimer.poc": "\u03bcKount&\u03bcDetect es actualmente una Prueba de Concepto (Proof of Concept).",
    "cards.disclaimer.warning": "Los resultados generados por los modelos:",
    "cards.disclaimer.item1": "No constituyen un diagn\u00f3stico cl\u00ednico.",
    "cards.disclaimer.item2": "No sustituyen t\u00e9cnicas microbiol\u00f3gicas gold-standard.",
    "cards.disclaimer.item3": "Deben ser validados mediante procedimientos de laboratorio adecuados.",
    "cards.disclaimer.item4": "Deben ser interpretados por personal cualificado.",
    "cards.disclaimer.footer": "La clasificaci\u00f3n autom\u00e1tica puede contener errores y debe considerarse \u00fanicamente como "
        "una herramienta de apoyo a la decisi\u00f3n.",
    "cards.disclaimer.short": "\u26a0\ufe0f \u03bcKount&\u03bcDetect es un sistema de investigaci\u00f3n de Prueba de Concepto. Los resultados son experimentales "
        "y no deben usarse para diagn\u00f3stico cl\u00ednico. Valide siempre mediante "
        "m\u00e9todos microbiol\u00f3gicos est\u00e1ndar.",
    "cards.species.full_name": "Nombre completo",
    "cards.species.gram": "Gram",
    "cards.species.shape": "Morfolog\u00eda",
    "cards.species.description": "Ver descripci\u00f3n completa",
    "cards.species.not_available": "No disponible.",
    "cards.future.planned": "planificado",
    "cards.future.in_progress": "en_progreso",
    "cards.future.completed": "completado",

    # ─── Charts ─────────────────────────────────────────────────
    "charts.distribution.title": "Distribuci\u00f3n de Especies",
    "charts.distribution.x_label": "Especie",
    "charts.distribution.y_label": "N\u00famero de colonias",
    "charts.heatmap.title": "Mapa de Probabilidades por Colonia",
    "charts.heatmap.x_label": "Especie",
    "charts.heatmap.y_label": "Colonia",
    "charts.heatmap.color_label": "Probabilidad",
    "charts.table.colony": "Colonia",
    "charts.table.predicted": "Especie predicha",
    "charts.metrics.detected": "Colonias detectadas",
    "charts.metrics.classified": "Colonias clasificadas",
    "charts.metrics.time_kount": "Tiempo \u03bcKount",
    "charts.metrics.time_detect": "Tiempo \u03bcDetect",

    # ─── Acknowledgments page ─────────────────────────────────────
    "ack.title": "\U0001f64f Agradecimientos",
    "ack.program.title": "\U0001f393 Programa de Formaci\u00f3n",
    "ack.program.desc": "Este proyecto fue desarrollado como proyecto final aplicado dentro del programa "
        "**LABORLAN 2026: IA & Data Tech (Artificial Intelligence and Technology Project Management)**.",
    "ack.mentor.title": "\U0001f9d1\u200d\U0001f3eb Tutor",
    "ack.mentor.desc": "Agradecimiento especial a **[Aitor Donado](https://github.com/Aitor-Donado)** por su "
        "gu\u00eda t\u00e9cnica y apoyo constante durante todo el desarrollo del proyecto.",
    "ack.classmates.title": "\U0001f465 Compa\u00f1eros",
    "ack.classmates.desc": "A todos mis compa\u00f1eros de clase, que generosamente actuaron como Spark Worker Nodes "
        "para procesar mis miles de im\u00e1genes. \u00a1Gracias de coraz\u00f3n! \u2665\ufe0f",
    "ack.dataset.title": "\U0001f4ca Dataset AGAR",
    "ack.dataset.desc": "Agradecimientos a **Majchrowska et al.** y a **NeuroSYS Research** por la cesi\u00f3n del dataset "
        "AGAR, que ha sido la base fundamental para el entrenamiento y validaci\u00f3n de los modelos de detecci\u00f3n y clasificaci\u00f3n.",
    "ack.patch.title": "\U0001f9e9 Preprocesamiento de Parches",
    "ack.patch.desc": "A **Jarek Paw\u0142owski** por su [repositorio en GitHub](https://github.com/jarek-pawlowski/microbial-dataset-generation) "
        "de generaci\u00f3n de dataset microbiano, que sirvi\u00f3 como referencia para implementar el preprocesamiento y parcheo de colonias.",
    "ack.staff.title": "\U0001f3eb Equipo Docente y Organizadores",
    "ack.staff.desc": "Agradecemos al equipo docente, mentores y organizadores de LABORLAN 2026 por su compromiso "
        "y el entorno de aprendizaje que hizo posible este proyecto.",
    "cuora.title": "\U0001f9e0 Cuora",
    "cuora.subtitle": "Tu microbi\u00f3loga virtual \u2014 Solo responde preguntas sobre bacteriolog\u00eda, virolog\u00eda, micolog\u00eda, parasitolog\u00eda, inmunolog\u00eda y biolog\u00eda molecular.",
    "cuora.chat_placeholder": "Pregunta sobre microbiolog\u00eda...",
    "cuora.login_title": "Accede con tu cuenta de Google para hablar con Cuora",
    "cuora.login_button": "Continuar con Google",
    "cuora.login_error": "GOOGLE_CLIENT_ID no configurado en secrets.toml",
    "cuora.oauth_missing": "streamlit-oauth no instalado. Usando modo desarrollo.",
    "cuora.dev_mode": "Modo desarrollo \u2014 sin OAuth real",
    "cuora.username_label": "Nombre de usuario",
    "cuora.dev_login": "Entrar (dev)",
    "cuora.clear_chat": "\U0001f5d1\ufe0f Limpiar chat",
    "cuora.export": "\U0001f4be Exportar",
    "cuora.logout": "Cerrar sesi\u00f3n",
    "cuora.api_key_error": "No se encontr\u00f3 GROQ_API_KEY en secrets.toml. Config\u00farala para usar Cuora.",

    # ─── Fundamentos del proyecto ────────────────────────────────
    "fundamentals.title": "Fundamentos del proyecto",
    "fundamentals.welcome": (
        "\u00a1Bienvenido a **\u03bcKount & \u03bcDetect**! "
        "Te presento \u03bcKount & \u03bcDetect, un proyecto desarrollado como trabajo final "
        "de la formaci\u00f3n **LABORLAN 2026: IA&Data Tech \u2013 Inteligencia Artificial "
        "y Gesti\u00f3n de Proyectos Tecnol\u00f3gicos**.\n\n"
        "\u03bcKount & \u03bcDetect es una herramienta dise\u00f1ada para asistir en el "
        "**an\u00e1lisis macrosc\u00f3pico de cultivos microbianos**. En otras palabras, "
        "ayuda a interpretar lo que observamos a simple vista en las placas de Petri "
        "donde se han cultivado muestras con posible presencia de microorganismos."
    ),
    "fundamentals.context.title": "\u00bfPor qu\u00e9 es importante?",
    "fundamentals.context.content": (
        "Cuando los microorganismos crecen sobre una placa de cultivo forman colonias, "
        "estructuras visibles a simple vista. En numerosas ocasiones estas colonias "
        "deben contarse, ya que su n\u00famero permite estimar las Unidades Formadoras "
        "de Colonias (UFC) presentes en la muestra original. Esta informaci\u00f3n "
        "resulta fundamental en m\u00faltiples \u00e1mbitos:"
    ),
    "fundamentals.industries": (
        "* **Industria alimentaria**, donde la carga microbiana puede ayudar "
        "a establecer la vida \u00fatil de un producto.\n"
        "* **Industria farmac\u00e9utica**, para verificar que un producto cumple "
        "los criterios microbiol\u00f3gicos exigidos antes de su comercializaci\u00f3n.\n"
        "* **Microbiolog\u00eda cl\u00ednica**, donde el n\u00famero de UFC puede aportar "
        "informaci\u00f3n sobre la gravedad de una infecci\u00f3n.\n"
        "* **Control de aguas**, en el que la presencia de determinados "
        "microorganismos, como _Escherichia coli_, es inaceptable por indicar "
        "contaminaci\u00f3n de origen fecal."
    ),
    "fundamentals.classification.title": "M\u00e1s all\u00e1 del recuento",
    "fundamentals.classification.content": (
        "Adem\u00e1s del recuento, tambi\u00e9n es importante la clasificaci\u00f3n de las colonias. "
        "Identificar qu\u00e9 microorganismo ha crecido proporciona informaci\u00f3n muy valiosa. "
        "Por ejemplo, detectar _Escherichia coli_ en una muestra de agua indica una "
        "contaminaci\u00f3n que requiere actuaci\u00f3n inmediata, mientras que la presencia "
        "de otros microorganismos puede ser aceptable siempre que no se superen "
        "los l\u00edmites microbiol\u00f3gicos establecidos."
    ),
    "fundamentals.limitations.title": "Limitaciones del modelo",
    "fundamentals.limitations.content": (
        "Para obtener resultados fiables es importante tener en cuenta que el modelo "
        "ha sido entrenado con im\u00e1genes muy espec\u00edficas:\n\n"
        "* Placas de agar TSA (Triptona Soja Agar)\n"
        "* Fotograf\u00edas tomadas desde un plano cenital (vista superior)\n"
        "* Im\u00e1genes de alta resoluci\u00f3n\n"
        "* Colonias compatibles \u00fanicamente con las siguientes especies:\n\n"
        "  * _Bacillus subtilis_\n"
        "  * _Candida albicans_\n"
        "  * _Escherichia coli_\n"
        "  * _Pseudomonas aeruginosa_\n"
        "  * _Staphylococcus aureus_\n\n"
        "Por ello, esta herramienta no identifica microorganismos de forma definitiva, "
        "sino que propone la especie m\u00e1s compatible con el aspecto macrosc\u00f3pico "
        "de la colonia, siempre dentro del conjunto de especies con las que ha sido "
        "entrenada. Si se utilizan im\u00e1genes obtenidas en otras condiciones de cultivo "
        "o pertenecientes a microorganismos diferentes, los resultados pueden no ser correctos."
    ),
    "fundamentals.support.title": "Un apoyo, no un sustituto del laboratorio",
    "fundamentals.support.content": (
        "Es importante recordar que \u03bcKount & \u03bcDetect no sustituye el diagn\u00f3stico "
        "microbiol\u00f3gico realizado en un laboratorio.\n\n"
        "La identificaci\u00f3n de un microorganismo requiere habitualmente la combinaci\u00f3n "
        "de distintas t\u00e9cnicas, como pruebas bioqu\u00edmicas, ensayos metab\u00f3licos, "
        "an\u00e1lisis de ant\u00edgenos y m\u00e9todos instrumentales avanzados, como la "
        "espectrometr\u00eda de masas MALDI-TOF. Estas t\u00e9cnicas permiten confirmar con "
        "gran precisi\u00f3n la identidad del microorganismo e incluso, en muchos casos, "
        "determinar su cepa.\n\n"
        "\u03bcKount & \u03bcDetect debe entenderse como una **herramienta de apoyo para el "
        "an\u00e1lisis macrosc\u00f3pico de colonias**. Su objetivo es facilitar el recuento "
        "y ofrecer una primera orientaci\u00f3n sobre la posible identidad de una colonia "
        "a partir de su apariencia. A medida que se incorporen nuevas im\u00e1genes, "
        "condiciones de cultivo y especies al entrenamiento del modelo, su utilidad "
        "y capacidad de generalizaci\u00f3n podr\u00e1n seguir aumentando.\n\n"
        "\u00bf**Te animas a probarlo**?"
    ),
    "fundamentals.cuora_caption": "Asistente de IA",
    "fundamentals.detection_strategies.title": "Estrategias de Detecci\u00f3n",
    "fundamentals.detection_strategies.intro": "\u03bcKount ofrece dos estrategias de detecci\u00f3n que pueden seleccionarse antes de ejecutar el an\u00e1lisis:",
    "fundamentals.detection_strategies.sahi": "**\U0001f52c SAHI + YOLO** \u2014 Dise\u00f1ado para im\u00e1genes de alta resoluci\u00f3n. Excelente para colonias peque\u00f1as en placas densas. Utiliza slicing para aumentar la sensibilidad de detecci\u00f3n.",
    "fundamentals.detection_strategies.full": "**\U0001f9eb YOLO a Imagen Completa** \u2014 Procesa la imagen completa sin slicing. Recomendado para placas con pocas colonias grandes. Evita duplicaciones derivadas del slicing.",

    # ─── FAQ ─────────────────────────────────────────────────────
    "faq.title": "Preguntas Frecuentes",
    "faq.q1.question": "\u00bfQu\u00e9 es \u03bcKount & \u03bcDetect?",
    "faq.q1.answer": (
        "\u03bcKount & \u03bcDetect es un sistema basado en inteligencia artificial "
        "para analizar placas de agar en microbiolog\u00eda. \u03bcKount detecta y cuenta "
        "colonias microbianas usando detecci\u00f3n de objetos YOLO, mientras que "
        "\u03bcDetect clasifica las especies de colonias usando un clasificador basado en CNN."
    ),
    "faq.q2.question": "\u00bfC\u00f3mo funciona el pipeline?",
    "faq.q2.answer": (
        "El pipeline consta de cuatro etapas: (1) subir una imagen de placa de agar "
        "o utilizar una imagen de ejemplo "
        "(el nombre del archivo indica el n\u00famero real de colonias y las especies presentes, "
        "ej. 17_ESCO.jpg = 17 colonias de E. coli), "
        "(2) \u03bcKount detecta y cuenta colonias con recuadros delimitadores, "
        "(3) \u03bcDetect clasifica cada colonia por especie, "
        "(4) los resultados se muestran en un panel interactivo con gr\u00e1ficos y m\u00e9tricas."
    ),
    "faq.q3.question": "\u00bfQu\u00e9 es YOLO?",
    "faq.q3.answer": (
        "YOLO (You Only Look Once) es un algoritmo de detecci\u00f3n de objetos en tiempo real. "
        "Divide la imagen en una cuadr\u00edcula y predice recuadros delimitadores y "
        "probabilidades de clase en una sola pasada. \u03bcKount usa un modelo YOLO "
        "ajustado en el dataset AGAR para detecci\u00f3n de colonias."
    ),
    "faq.q4.question": "\u00bfQu\u00e9 es una CNN?",
    "faq.q4.answer": (
        "Una CNN (Red Neuronal Convolucional) es una arquitectura de deep learning "
        "especializada en an\u00e1lisis de im\u00e1genes. \u03bcDetect usa una CNN entrenada "
        "para clasificar especies microbianas (S. aureus, E. coli, P. aeruginosa, "
        "B. subtilis, C. albicans) a partir de recortes de colonias."
    ),
    "faq.q5.question": "\u00bfQu\u00e9 tipos de imagen puedo subir?",
    "faq.q5.answer": (
        "Puedes subir im\u00e1genes PNG, JPG y JPEG de placas de agar. "
        "El sistema tambi\u00e9n ofrece generaci\u00f3n de placas sint\u00e9ticas para pruebas."
    ),
    "faq.q6.question": "\u00bfQu\u00e9 precisi\u00f3n tienen los resultados?",
    "faq.q6.answer": (
        "El modelo de detecci\u00f3n fue entrenado con ~18,000 im\u00e1genes de placas de agar "
        "con ~337,000 anotaciones del dataset AGAR. La precisi\u00f3n de clasificaci\u00f3n "
        "depende de la calidad de imagen, condiciones de iluminaci\u00f3n y morfolog\u00eda "
        "de las colonias. Siempre valida los resultados con m\u00e9todos microbiol\u00f3gicos tradicionales."
    ),
    "faq.q7.question": "\u00bfPor qu\u00e9 es importante esta herramienta?",
    "faq.q7.answer": (
        "El conteo y clasificaci\u00f3n manual de colonias es lento, subjetivo y propenso "
        "a errores humanos. \u03bcKount & \u03bcDetect automatiza este proceso, "
        "proporcionando resultados consistentes, r\u00e1pidos y reproducibles, acelerando "
        "el an\u00e1lisis microbiol\u00f3gico en entornos cl\u00ednicos, industriales y de investigaci\u00f3n."
    ),
    "faq.q8.question": "\u00bfQu\u00e9 significan las abreviaturas de los archivos de ejemplo?",
    "faq.q8.answer": (
        "Las im\u00e1genes de ejemplo incluyen en su nombre el n\u00famero de colonias "
        "y una abreviatura de las especies presentes:\n\n"
        "- ESCO = _Escherichia coli_\n"
        "- BASU = _Bacillus subtilis_\n"
        "- CAAL = _Candida albicans_\n"
        "- PSAE = _Pseudomonas aeruginosa_\n"
        "- STAU = _Staphylococcus aureus_"
    ),

    "cuora.analyzing": "\u23f3 Analizando...",
    "cuora.default_name": "Usuario",
    "cuora.prompt": (
        "Eres un experto en microbiolog\u00eda con conocimiento profundo en bacteriolog\u00eda, "
        "virolog\u00eda, micolog\u00eda, parasitolog\u00eda, inmunolog\u00eda y biolog\u00eda molecular. "
        "SOLO responder\u00e1s preguntas relacionadas con microbiolog\u00eda. "
        "Si la pregunta NO es sobre microbiolog\u00eda, responde exactamente: "
        "'Lo siento, solo puedo responder preguntas relacionadas con microbiolog\u00eda.' "
        "No inventes informaci\u00f3n. Si no sabes la respuesta, dilo claramente. "
        "Responde siempre en el mismo idioma del usuario."
    ),
}
