TRANSLATIONS = {
    # ─── Navigation ─────────────────────────────────────────────
    "nav.home": "Inicio",
    "nav.pipeline": "Pipeline",
    "nav.kount": "\u03bcKount",
    "nav.detect": "\u03bcDetect",
    "nav.results": "Resultados",
    "nav.about": "Acerca de",
    "nav.future": "Funcionalidades Futuras",
    "nav.disclaimer": "Aviso Legal",
    "nav.acknowledgments": "Agradecimientos",

    # ─── Sidebar ────────────────────────────────────────────────
    "sidebar.language": "Idioma / Language",
    "sidebar.restart": "\U0001f504 Reiniciar pipeline",

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

    # ─── Pipeline page ──────────────────────────────────────────
    "pipeline.title": "\U0001f52c Pipeline de Procesamiento",
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
    "kount.tab.synthetic": "Generar Imagen Sint\u00e9tica",
    "kount.tab.examples": "Im\u00e1genes de Ejemplo",
    "kount.upload.label": "Selecciona una imagen de placa de agar",
    "kount.synthetic.width": "Ancho",
    "kount.synthetic.height": "Alto",
    "kount.synthetic.desc": "Genera una placa de agar sint\u00e9tica con colonias simuladas.",
    "kount.synthetic.button": "\U0001f3b2 Generar placa sint\u00e9tica",
    "kount.status.loaded": "Imagen cargada correctamente.",
    "kount.status.generated": "Placa sint\u00e9tica generada.",
    "kount.examples.select": "Selecciona una imagen de ejemplo para cargarla:",
    "kount.examples.none": "No se encontraron im\u00e1genes de ejemplo.",
    "kount.download_json": "\U0001f4e5 Descargar JSON",
    "kount.detect.button": "\u25b6\ufe0f Ejecutar \u03bcKount",
    "kount.status.detected": "{count} colonias detectadas en {time} ms.",
    "kount.next.button": "\u27a1\ufe0f Procesar con \u03bcDetect",
    "kount.no_image": "Sube una imagen o genera una placa sint\u00e9tica para comenzar.",
    "kount.loaded_image": "Imagen cargada",
    "kount.detection_result": "Resultado de detecci\u00f3n",

    # ─── μDetect page ──────────────────────────────────────────
    "detect.title": "\U0001f9ea \u03bcDetect \u2014 Clasificaci\u00f3n de Colonias",
    "detect.subtitle": "Clasifica cada colonia detectada por especie microbiana.",
    "detect.warning.no_detections": "No hay detecciones previas. Ejecuta \u03bcKount primero "
        "para detectar colonias en una imagen.",
    "detect.button.back": "\u2190 Ir a \u03bcKount",
    "detect.error.no_image": "No hay imagen original disponible. Regresa a \u03bcKount y carga una imagen.",
    "detect.status.ready": "{count} colonias detectadas listas para clasificaci\u00f3n.",
    "detect.process.button": "\u25b6\ufe0f Ejecutar \u03bcDetect (clasificaci\u00f3n mock)",
    "detect.step1.title": "Extracci\u00f3n de Recortes",
    "detect.step1.desc": "Extrayendo cada colonia de la imagen original usando las coordenadas de los bounding boxes...",
    "detect.step2.title": "Fondo Negro",
    "detect.step2.desc": "Aplicando fondo negro a cada recorte para mejorar la clasificaci\u00f3n...",
    "detect.status.crops_extracted": "{count} recortes extra\u00eddos.",
    "detect.status.classified": "{count} colonias clasificadas.",
    "detect.results.title": "Resultados por Colonia",
    "detect.colony.label": "Colonia #{number}",
    "detect.colony.processed": "Recorte procesado",
    "detect.species.label": "Especie predicha",
    "detect.confidence.label": "Confianza",
    "detect.detection_precision": "Precisi\u00f3n detecci\u00f3n",
    "detect.probabilities.title": "Ver probabilidades detalladas",
    "detect.info.run": "Presiona 'Ejecutar \u03bcDetect' para clasificar las colonias.",

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

    # ─── About page ────────────────────────────────────────────
    "about.title": "\u2139\ufe0f Acerca de \u2014 Sobre \u03bcKount&\u03bcDetect",
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
    "about.architecture.title": "Arquitectura del Proyecto",

    # ─── Future Features page ───────────────────────────────────
    "future.title": "\U0001f680 Funcionalidades Futuras",
    "future.subtitle": "Funcionalidades implementadas y planificadas para \u03bcKount&\u03bcDetect.",
    "future.phase2.title": "Fase 2 \u2014 Edici\u00f3n Manual de Detecciones",
    "future.phase2.desc": "Tras la ejecuci\u00f3n de \u03bcKount, el usuario podr\u00e1 interactuar directamente con las detecciones:",
    "future.phase3.title": "Fase 3 \u2014 Informaci\u00f3n Microbiol\u00f3gica Detallada",
    "future.phase3.desc": "Cada especie detectada mostrar\u00e1 informaci\u00f3n completa en tarjetas informativas:",
    "future.phase4.title": "Fase 4 \u2014 Chatbot Especializado",
    "future.phase4.desc": "Un asistente conversacional basado en IA que responder\u00e1 preguntas sobre:",
    "future.feature.move_boxes": "Mover bounding boxes",
    "future.feature.move_boxes.desc": "Arrastrar y soltar las cajas detectadas para ajustar su posici\u00f3n si el modelo no ha "
        "centrado correctamente la colonia.",
    "future.feature.resize_boxes": "Redimensionar bounding boxes",
    "future.feature.resize_boxes.desc": "Ajustar el tama\u00f1o de cada bounding box manualmente, permitiendo corregir "
        "sobredetecciones o subdetecciones.",
    "future.feature.delete_boxes": "Eliminar detecciones",
    "future.feature.delete_boxes.desc": "Seleccionar y eliminar falsos positivos directamente sobre la imagen antes de "
        "pasar a la fase de clasificaci\u00f3n.",
    "future.feature.add_boxes": "A\u00f1adir nuevas detecciones",
    "future.feature.add_boxes.desc": "Dibujar nuevas bounding boxes en zonas donde el modelo no detect\u00f3 colonias "
        "para asegurar una cobertura completa.",
    "future.feature.micro_description": "Descripci\u00f3n microbiol\u00f3gica",
    "future.feature.micro_description.desc": "Informaci\u00f3n detallada sobre morfolog\u00eda, Gram, h\u00e1bitats naturales y caracter\u00edsticas "
        "biol\u00f3gicas de cada especie detectada.",
    "future.feature.clinical": "Relevancia cl\u00ednica",
    "future.feature.clinical.desc": "Descripci\u00f3n de las patolog\u00edas asociadas, grupos de riesgo y precauciones necesarias "
        "para su manipulaci\u00f3n.",
    "future.feature.industrial": "Relevancia industrial",
    "future.feature.industrial.desc": "Aplicaciones en biotecnolog\u00eda, industria alimentaria, farmac\u00e9utica y agr\u00edcola.",
    "future.feature.pharma": "Aplicaciones farmac\u00e9uticas",
    "future.feature.pharma.desc": "Usos en producci\u00f3n de antibi\u00f3ticos, enzimas, probi\u00f3ticos y otros compuestos "
        "de inter\u00e9s farmac\u00e9utico.",
    "future.feature.chatbot_micro": "Consulta de microorganismos",
    "future.feature.chatbot_micro.desc": "Preguntas sobre las especies detectadas, sus caracter\u00edsticas y significado.",
    "future.feature.chatbot_results": "Interpretaci\u00f3n de resultados",
    "future.feature.chatbot_results.desc": "Ayuda para comprender los resultados del an\u00e1lisis y su relevancia.",
    "future.feature.chatbot_safety": "Informaci\u00f3n de seguridad",
    "future.feature.chatbot_safety.desc": "Consultas sobre niveles de bioseguridad, precauciones y manejo de muestras.",
    "future.chatbot_warning": "Aviso importante: La informaci\u00f3n generada por el chatbot es \u00fanicamente "
        "orientativa y no sustituye el criterio de un profesional sanitario, microbi\u00f3logo "
        "o especialista.",
    "future.roadmap.title": "Roadmap Completo",
    "future.roadmap.phase1": "Fase 1 \u2014 MVP Streamlit con servicios mock",
    "future.roadmap.phase2": "Fase 2 \u2014 Integraci\u00f3n \u03bcKount (YOLO real)",
    "future.roadmap.phase3": "Fase 3 \u2014 Integraci\u00f3n \u03bcDetect (CNN real)",
    "future.roadmap.phase4": "Fase 4 \u2014 Edici\u00f3n manual de bounding boxes",
    "future.roadmap.phase5": "Fase 5 \u2014 Informaci\u00f3n microbiol\u00f3gica completa",
    "future.roadmap.phase6": "Fase 6 \u2014 Chatbot especializado",
    "future.roadmap.phase7": "Fase 7 \u2014 Despliegue p\u00fablico",
    "future.roadmap.completed": "Completada",
    "future.roadmap.pending": "Pendiente",

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
