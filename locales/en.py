TRANSLATIONS = {
    # ─── Navigation ─────────────────────────────────────────────
    "nav.home": "Home",
    "nav.pipeline": "Pipeline",
    "nav.kount": "\u03bcKount",
    "nav.detect": "\u03bcDetect",
    "nav.results": "Results",
    "nav.about": "About",
    "nav.future": "Future Features",
    "nav.disclaimer": "Disclaimer",
    "nav.acknowledgments": "Acknowledgments",
    "nav.faq": "FAQ",

    # ─── Sidebar ────────────────────────────────────────────────
    "sidebar.language": "Language / Idioma",
    "sidebar.restart": "\U0001f504 Restart pipeline",

    # ─── Home ───────────────────────────────────────────────────
    "home.title": "\u03bcKount&\u03bcDetect",
    "home.subtitle": "Artificial Intelligence for Agar Plate Analysis",
    "home.intro": "Computer vision system for:",
    "home.bullet.detection": "Colony Detection",
    "home.bullet.counting": "Automatic Counting",
    "home.bullet.classification": "Microbiological Classification",
    "home.based_on.intro": "Based on:",
    "home.based_on.kount": "\u03bcKount (YOLO) \u2014 Colony detection and counting",
    "home.based_on.detect": "\u03bcDetect (CNN) \u2014 Microbial species classification",
    "home.pipeline": "Visual Pipeline",
    "home.pipeline.upload.title": "Upload",
    "home.pipeline.upload.subtitle": "Image",
    "home.pipeline.kount.title": "\u03bcKount",
    "home.pipeline.kount.subtitle": "YOLO Detection",
    "home.pipeline.crop.title": "Crop & Prep",
    "home.pipeline.crop.subtitle": "Black Background",
    "home.pipeline.detect.title": "\u03bcDetect",
    "home.pipeline.detect.subtitle": "CNN Classification",
    "home.pipeline.results.title": "Results",
    "home.pipeline.results.subtitle": "Visualizations",
    "home.dataset": "AGAR Dataset",
    "home.dataset.images": "~18,000 agar plate images",
    "home.dataset.annotations": "~337,000 colony annotations",
    "home.dataset.configs": "Multiple capture setups and lighting conditions",
    "home.dataset.source": "Dataset: AGAR dataset by NeuroSYS Research",
    "home.dataset.authors": "Researchers: Majchrowska et al. (2021)",
    "home.dataset.title": "Title: AGAR a microbial colony dataset for deep learning detection",

    # ─── Pipeline page ──────────────────────────────────────────
    "pipeline.title": "\U0001f52c Processing Pipeline",
    "pipeline.subtitle": "Complete \u03bcKount&\u03bcDetect flow diagram, from original image to final classification.",
    "pipeline.step1.title": "\U0001f4e4 Input Image",
    "pipeline.step1.desc": "The user uploads an agar plate image (PNG, JPG, JPEG). "
        "The image is converted to RGB and stored for processing.",
    "pipeline.step1.source": "services/preprocessing_service.py",
    "pipeline.step2.title": "\U0001f50d \u03bcKount (YOLO)",
    "pipeline.step2.desc": "YOLO-based detection model (You Only Look Once). "
        "Locates colonies in the image generating bounding boxes with associated confidence. "
        "Returns coordinates and confidence score for each detected colony.",
    "pipeline.step2.source": "services/detection_service.py",
    "pipeline.step3.title": "\U0001f4e6 Bounding Boxes",
    "pipeline.step3.desc": "Detected colonies are displayed with colored bounding boxes on the original image. "
        "Each box includes a numeric identifier and the detection confidence level.",
    "pipeline.step3.source": "detection_service.py \u2192 components/image_viewer.py",
    "pipeline.step4.title": "\u2702\ufe0f Crop Extraction",
    "pipeline.step4.desc": "Each detected colony is individually extracted from the original image "
        "using its bounding box coordinates. Crops are prepared for the classification phase.",
    "pipeline.step4.source": "services/preprocessing_service.py",
    "pipeline.step5.title": "\u2b1b Black Background",
    "pipeline.step5.desc": "A black background filter is applied to each crop: pixels with value "
        "above a threshold (light agar background) are converted to black, "
        "keeping only the colony visible. This improves CNN accuracy.",
    "pipeline.step5.source": "services/preprocessing_service.py",
    "pipeline.step6.title": "\U0001f9ea \u03bcDetect (CNN)",
    "pipeline.step6.desc": "CNN model based on Transfer Learning. Each black-background crop is classified "
        "into one of 5 supported species, returning a probability vector for each.",
    "pipeline.step6.source": "services/classification_service.py",
    "pipeline.step7.title": "\U0001f4ca Prediction + Results",
    "pipeline.step7.desc": "Final results: species distribution, per-colony metrics, "
        "probability map and interactive visualizations with Plotly.",
    "pipeline.step7.source": "pages/05_results.py + components/charts.py",

    # ─── μKount page ───────────────────────────────────────────
    "kount.title": "\U0001f50d \u03bcKount \u2014 Colony Detection",
    "kount.subtitle": "YOLO-based colony detection with Slicing Aided Hyper Inference.",
    "kount.tab.upload": "Upload Image",
    "kount.tab.examples": "Example Images",
    "kount.upload.label": "Select an agar plate image",
    "kount.status.loaded": "Image loaded successfully.",
    "kount.examples.select": "Select an example image below to load it:",
    "kount.examples.none": "No example images found.",
    "kount.download_json": "\U0001f4e5 Download JSON",
    "kount.detect.button": "\u25b6\ufe0f Run \u03bcKount",
    "kount.status.detected": "{count} colonies detected in {time} s.",
    "kount.next.button": "\u27a1\ufe0f Process with \u03bcDetect",
    "kount.no_image": "Upload an image to start.",
    "kount.loaded_image": "Loaded image",
    "kount.detection_result": "Detection result",

    # ─── μDetect page ──────────────────────────────────────────
    "detect.title": "\U0001f9ea \u03bcDetect \u2014 Colony Classification",
    "detect.subtitle": "Classifies each detected colony by microbial species.",
    "detect.warning.no_detections": "No previous detections. Run \u03bcKount first "
        "to detect colonies in an image.",
    "detect.button.back": "\u2190 Go to \u03bcKount",
    "detect.error.no_image": "No original image available. Go back to \u03bcKount and load an image.",
    "detect.status.ready": "{count} colonies detected ready for classification.",
    "detect.process.button": "\u25b6\ufe0f Run \u03bcDetect",
    "detect.step1.title": "Crop Extraction",
    "detect.step1.desc": "Extracting each colony from the original image using bounding box coordinates...",
    "detect.step2.title": "Black Background",
    "detect.step2.desc": "Applying black background to each crop to improve classification...",
    "detect.status.crops_extracted": "{count} crops extracted.",
    "detect.status.classified": "{count} colonies classified.",
    "detect.results.title": "Results per colony",
    "detect.colony.label": "Colony #{number}",
    "detect.colony.processed": "Processed crop",
    "detect.species.label": "Predicted species",
    "detect.confidence.label": "Confidence",
    "detect.detection_precision": "Detection precision",
    "detect.probabilities.title": "View detailed probabilities",
    "detect.info.run": "Press 'Run \u03bcDetect' to classify the colonies.",

    # ─── Results page ───────────────────────────────────────────
    "results.title": "\U0001f4ca Results \u2014 Global Results",
    "results.subtitle": "Complete summary of the agar plate analysis.",
    "results.warning.no_data": "No analysis data available. Run \u03bcKount and \u03bcDetect first.",
    "results.summary.title": "Analysis Summary",
    "results.species_distribution.title": "Species Distribution",
    "results.percentage.title": "Percentage Distribution",
    "results.probability_table.title": "Probabilities per Colony",
    "results.probability_map.title": "Probability Map",
    "results.species_info.title": "Detected Species Information",
    "results.no_classifications": "No classifications available. Run \u03bcDetect to classify the detected colonies.",
    "results.colony": "Colony",
    "results.predicted_species": "Predicted species",
    "results.description": "Description",
    "results.clinical_significance": "Clinical significance",
    "results.industrial_relevance": "Industrial relevance",
    "results.pharmaceutical_applications": "Pharmaceutical applications",
    "results.common_habitats": "Common habitats",
    "results.warnings": "Warnings",
    "results.biosafety_notes": "Biosafety",
    "results.references": "References",
    "results.not_available": "N/A",

    # ─── About page ────────────────────────────────────────────
    "about.title": "\u2139\ufe0f About \u2014 About \u03bcKount&\u03bcDetect",
    "about.subtitle": "\u03bcKount&\u03bcDetect (Artificial Intelligence for Agar Plate Analysis) is a "
        "computer vision system designed for detection, counting and classification of "
        "microbial colonies on agar plates. "
        "This project is the final capstone project of the Laborlan training program in AI, Machine Learning and Deep Learning",
    "about.kount.title": "\U0001f9eb \u03bcKount \u2014 Colony Detector",
    "about.kount.function": "Locate colonies in agar plate images, "
        "generate bounding boxes around each colony, "
        "provide automatic colony counting.",
    "about.kount.tech": "Architecture: YOLOv8, Framework: Ultralytics, "
        "Output format: coordinates (x1, y1, x2, y2) + confidence",
    "about.detect.title": "\U0001f9ea \u03bcDetect \u2014 Species Classifier",
    "about.detect.function": "Classify individual colonies into microbial species, "
        "provide probabilities for each supported species.",
    "about.detect.species": "*S. aureus, B. subtilis, P. aeruginosa, E. coli, C. albicans*",
    "about.detect.tech": "Architecture: CNN based on pre-trained models (MobileNet), "
        "Framework: TensorFlow / PyTorch (to be defined)",
    "about.dataset.title": "\U0001f4ca AGAR Dataset",
    "about.dataset.content": "~18,000 agar plate images, ~337,000 individual colony annotations, "
        "Multiple capture setups (lighting, angle, distance), "
        "Annotations by expert microbiologists. "
        "Images were acquired under controlled laboratory conditions "
        "and represent 5 different microbial species.",
    "about.architecture.title": "Project Architecture",

    # ─── Future Features page ───────────────────────────────────
    "future.title": "\U0001f680 Future Features",
    "future.subtitle": "Implemented and planned features for \u03bcKount&\u03bcDetect.",
    "future.phase2.title": "Phase 2 \u2014 Manual Detection Editing",
    "future.phase2.desc": "After \u03bcKount execution, the user can interact directly with detections:",
    "future.phase3.title": "Phase 3 \u2014 Detailed Microbiological Information",
    "future.phase3.desc": "Each detected species will display complete information in info cards:",
    "future.phase4.title": "Phase 4 \u2014 Specialized Chatbot",
    "future.phase4.desc": "A conversational AI assistant that will answer questions about:",
    "future.feature.move_boxes": "Move bounding boxes",
    "future.feature.move_boxes.desc": "Drag and drop detected boxes to adjust position if the model "
        "has not centered the colony correctly.",
    "future.feature.resize_boxes": "Resize bounding boxes",
    "future.feature.resize_boxes.desc": "Adjust the size of each bounding box manually, allowing "
        "correction of over-detections or under-detections.",
    "future.feature.delete_boxes": "Delete detections",
    "future.feature.delete_boxes.desc": "Select and remove false positives directly on the image "
        "before proceeding to classification.",
    "future.feature.add_boxes": "Add new detections",
    "future.feature.add_boxes.desc": "Draw new bounding boxes in areas where the model did not "
        "detect colonies to ensure complete coverage.",
    "future.feature.micro_description": "Microbiological description",
    "future.feature.micro_description.desc": "Detailed information on morphology, Gram stain, "
        "natural habitats and biological characteristics of each detected species.",
    "future.feature.clinical": "Clinical relevance",
    "future.feature.clinical.desc": "Description of associated pathologies, risk groups and "
        "necessary handling precautions.",
    "future.feature.industrial": "Industrial relevance",
    "future.feature.industrial.desc": "Applications in biotechnology, food industry, "
        "pharmaceutical and agricultural sectors.",
    "future.feature.pharma": "Pharmaceutical applications",
    "future.feature.pharma.desc": "Uses in production of antibiotics, enzymes, probiotics "
        "and other pharmaceutical compounds.",
    "future.feature.chatbot_micro": "Microorganism queries",
    "future.feature.chatbot_micro.desc": "Questions about detected species, their characteristics and meaning.",
    "future.feature.chatbot_results": "Result interpretation",
    "future.feature.chatbot_results.desc": "Help understanding analysis results and their relevance.",
    "future.feature.chatbot_safety": "Safety information",
    "future.feature.chatbot_safety.desc": "Queries about biosafety levels, precautions and sample handling.",
    "future.chatbot_warning": "Important note: Information generated by the chatbot is for "
        "guidance only and does not replace the judgment of a healthcare professional, "
        "microbiologist or specialist.",
    "future.roadmap.title": "Complete Roadmap",
    "future.roadmap.phase1": "Phase 1 \u2014 MVP Streamlit with mock services",
    "future.roadmap.phase2": "Phase 2 \u2014 \u03bcKount integration (real YOLO)",
    "future.roadmap.phase3": "Phase 3 \u2014 \u03bcDetect integration (real CNN)",
    "future.roadmap.phase4": "Phase 4 \u2014 Manual bounding box editing",
    "future.roadmap.phase5": "Phase 5 \u2014 Complete microbiological information",
    "future.roadmap.phase6": "Phase 6 \u2014 Specialized chatbot",
    "future.roadmap.phase7": "Phase 7 \u2014 Public deployment",
    "future.roadmap.completed": "Completed",
    "future.roadmap.pending": "Pending",

    # ─── Disclaimer page ────────────────────────────────────────
    "disclaimer.title": "\u26a0\ufe0f Disclaimer \u2014 Ethical and Scientific Notice",
    "disclaimer.banner.title": "\u03bcKount&\u03bcDetect is a Proof-of-Concept Research System",
    "disclaimer.banner.text": "Must NOT be used for clinical diagnosis.",
    "disclaimer.limitations.title": "System Limitations",
    "disclaimer.limitation1.title": "\U0001f52c Purely research purpose",
    "disclaimer.limitation1.desc": "\u03bcKount&\u03bcDetect is a research and development tool. It is not approved "
        "by any health authority (FDA, EMA, etc.) for diagnostic use.",
    "disclaimer.limitation2.title": "\U0001f9ea Does not replace gold-standard techniques",
    "disclaimer.limitation2.desc": "Conventional microbiological methods (culture, Gram stain, "
        "biochemical tests, MALDI-TOF) remain the reference standard. "
        "\u03bcKount&\u03bcDetect does not replace these methods.",
    "disclaimer.limitation3.title": "\u26a0\ufe0f Experimental results",
    "disclaimer.limitation3.desc": "Detection and classification models can produce errors. "
        "False positives, false negatives and incorrect classifications are "
        "possible and must be verified.",
    "disclaimer.limitation4.title": "\U0001f4cb Validation required",
    "disclaimer.limitation4.desc": "All results must be validated through appropriate "
        "laboratory procedures before making any decisions.",
    "disclaimer.limitation5.title": "\U0001f468\u200d\U0001f52c Professional interpretation required",
    "disclaimer.limitation5.desc": "Results must be interpreted exclusively by qualified "
        "personnel (microbiologists, biochemists, healthcare professionals).",
    "disclaimer.limitation6.title": "\U0001f916 No clinical judgment",
    "disclaimer.limitation6.desc": "The system does not incorporate clinical judgment or "
        "contextual patient knowledge. It cannot consider medical history "
        "or other variables relevant to diagnosis.",
    "disclaimer.responsible_use.title": "Responsible Use",
    "disclaimer.responsible_use.intro": "By using \u03bcKount&\u03bcDetect, the user agrees to:",
    "disclaimer.responsible_use.item1": "NOT use the results for clinical diagnosis without prior validation.",
    "disclaimer.responsible_use.item2": "NOT make medical decisions based solely on the system output.",
    "disclaimer.responsible_use.item3": "Verify all detections and classifications through conventional methods.",
    "disclaimer.responsible_use.item4": "Cite \u03bcKount&\u03bcDetect as a research tool in any publication using its results.",
    "disclaimer.responsible_use.footer": "Failure to comply with these conditions may have serious consequences "
        "in clinical contexts. The developers of \u03bcKount&\u03bcDetect are not responsible "
        "for misuse of the system.",
    "disclaimer.version.title": "Current Version",
    "disclaimer.version.info": "Version 1.0.0 \u2014 Cuora is alive! \U0001f9e0",
    "disclaimer.version.desc": "This initial version uses simulated data to demonstrate the architecture "
        "and workflow. Real models (YOLO, CNN) will be integrated in later phases.",
    "disclaimer.version.status": "Status: Proof of Concept / Functional Prototype",

    # ─── Cards ──────────────────────────────────────────────────
    "cards.disclaimer.title": "\u26a0\ufe0f IMPORTANT \u2014 ETHICAL AND SCIENTIFIC NOTICE",
    "cards.disclaimer.poc": "\u03bcKount&\u03bcDetect is currently a Proof of Concept.",
    "cards.disclaimer.warning": "Results generated by the models:",
    "cards.disclaimer.item1": "Do not constitute clinical diagnosis.",
    "cards.disclaimer.item2": "Do not replace gold-standard microbiological techniques.",
    "cards.disclaimer.item3": "Must be validated through appropriate laboratory procedures.",
    "cards.disclaimer.item4": "Must be interpreted by qualified personnel.",
    "cards.disclaimer.footer": "Automatic classification may contain errors and should be considered "
        "solely as a decision support tool.",
    "cards.disclaimer.short": "\u26a0\ufe0f \u03bcKount&\u03bcDetect is a Proof-of-Concept research system. Results are experimental "
        "and must not be used for clinical diagnosis. Always validate through "
        "standard microbiological methods.",
    "cards.species.full_name": "Full name",
    "cards.species.gram": "Gram",
    "cards.species.shape": "Morphology",
    "cards.species.description": "View full description",
    "cards.species.not_available": "Not available.",
    "cards.future.planned": "planned",
    "cards.future.in_progress": "in_progress",
    "cards.future.completed": "completed",

    # ─── Charts ─────────────────────────────────────────────────
    "charts.distribution.title": "Species Distribution",
    "charts.distribution.x_label": "Species",
    "charts.distribution.y_label": "Number of colonies",
    "charts.heatmap.title": "Probability Map per Colony",
    "charts.heatmap.x_label": "Species",
    "charts.heatmap.y_label": "Colony",
    "charts.heatmap.color_label": "Probability",
    "charts.table.colony": "Colony",
    "charts.table.predicted": "Predicted species",
    "charts.metrics.detected": "Detected colonies",
    "charts.metrics.classified": "Classified colonies",
    "charts.metrics.time_kount": "\u03bcKount time",
    "charts.metrics.time_detect": "\u03bcDetect time",

    # ─── Acknowledgments page ─────────────────────────────────────
    "ack.title": "\U0001f64f Acknowledgments",
    "ack.program.title": "\U0001f393 Training Program",
    "ack.program.desc": "This project was developed as the final applied project within the "
        "**LABORLAN 2026: IA & Data Tech (Artificial Intelligence and Technology Project Management)** program.",
    "ack.mentor.title": "\U0001f9d1\u200d\U0001f3eb Mentor",
    "ack.mentor.desc": "Special thanks to **[Aitor Donado](https://github.com/Aitor-Donado)** for his "
        "technical guidance and continuous support throughout the project development.",
    "ack.classmates.title": "\U0001f465 Classmates",
    "ack.classmates.desc": "To all my classmates, who generously acted as Spark Worker Nodes "
        "to process my thousands of images. Thank you from the bottom of my heart! \u2665\ufe0f",
    "ack.dataset.title": "\U0001f4ca AGAR Dataset",
    "ack.dataset.desc": "Thanks to **Majchrowska et al.** and **NeuroSYS Research** for providing the AGAR dataset, "
        "which has been the fundamental basis for training and validating the detection and classification models.",
    "ack.patch.title": "\U0001f9e9 Patch Preprocessing",
    "ack.patch.desc": "To **Jarek Paw\u0142owski** for his [GitHub repository](https://github.com/jarek-pawlowski/microbial-dataset-generation) "
        "on microbial dataset generation, which served as a reference for implementing colony preprocessing and patching.",
    "ack.staff.title": "\U0001f3eb Teaching Staff and Organizers",
    "ack.staff.desc": "We thank the teaching staff, mentors, and organizers of LABORLAN 2026 for their commitment "
        "and the learning environment that made this project possible.",
    "cuora.title": "\U0001f9e0 Cuora",
    "cuora.subtitle": "Your virtual microbiologist \u2014 Only answers questions about bacteriology, virology, mycology, parasitology, immunology and molecular biology.",
    "cuora.chat_placeholder": "Ask about microbiology...",
    "cuora.login_title": "Sign in with your Google account to talk to Cuora",
    "cuora.login_button": "Continue with Google",
    "cuora.login_error": "GOOGLE_CLIENT_ID not configured in secrets.toml",
    "cuora.oauth_missing": "streamlit-oauth not installed. Using development mode.",
    "cuora.dev_mode": "Development mode \u2014 no real OAuth",
    "cuora.username_label": "Username",
    "cuora.dev_login": "Enter (dev)",
    "cuora.clear_chat": "\U0001f5d1\ufe0f Clear chat",
    "cuora.export": "\U0001f4be Export",
    "cuora.logout": "Logout",
    "cuora.api_key_error": "GROQ_API_KEY not found in secrets.toml. Configure it to use Cuora.",
    # ─── FAQ ─────────────────────────────────────────────────────
    "faq.title": "Frequently Asked Questions",
    "faq.q1.question": "What is \u03bcKount & \u03bcDetect?",
    "faq.q1.answer": (
        "\u03bcKount & \u03bcDetect is an AI-powered system for analyzing agar plates "
        "used in microbiology. \u03bcKount detects and counts microbial colonies using "
        "YOLO object detection, while \u03bcDetect classifies colony species using "
        "a CNN-based classifier."
    ),
    "faq.q2.question": "How does the pipeline work?",
    "faq.q2.answer": (
        "The pipeline consists of four stages: (1) upload or generate an agar plate image, "
        "(2) \u03bcKount detects and counts colonies with bounding boxes, "
        "(3) \u03bcDetect classifies each colony by species, "
        "(4) results are displayed in an interactive dashboard with charts and metrics."
    ),
    "faq.q3.question": "What is YOLO?",
    "faq.q3.answer": (
        "YOLO (You Only Look Once) is a real-time object detection algorithm. "
        "It divides the image into a grid and predicts bounding boxes and class probabilities "
        "in a single pass. \u03bcKount uses a YOLO model fine-tuned on the AGAR dataset "
        "for colony detection."
    ),
    "faq.q4.question": "What is a CNN?",
    "faq.q4.answer": (
        "A CNN (Convolutional Neural Network) is a deep learning architecture specialized "
        "for image analysis. \u03bcDetect uses a CNN trained to classify microbial species "
        "(S. aureus, E. coli, P. aeruginosa, B. subtilis, C. albicans) from colony crops."
    ),
    "faq.q5.question": "What image types can I upload?",
    "faq.q5.answer": (
        "You can upload PNG, JPG, and JPEG images of agar plates. "
        "The system also provides synthetic plate generation for testing purposes."
    ),
    "faq.q6.question": "How accurate are the results?",
    "faq.q6.answer": (
        "The detection model was trained on ~18,000 agar plate images with ~337,000 annotations "
        "from the AGAR dataset. Classification accuracy depends on image quality, lighting "
        "conditions, and colony morphology. Always validate results with traditional "
        "microbiological methods."
    ),
    "faq.q7.question": "Why is this tool important?",
    "faq.q7.answer": (
        "Manual colony counting and classification is time-consuming, subjective, and prone "
        "to human error. \u03bcKount & \u03bcDetect automates this process, providing "
        "consistent, fast, and reproducible results, accelerating microbiological analysis "
        "in clinical, industrial, and research settings."
    ),

    "cuora.analyzing": "\u23f3 Analyzing...",
    "cuora.default_name": "User",
    "cuora.prompt": (
        "You are an expert microbiologist with deep knowledge of bacteriology, "
        "virology, mycology, parasitology, immunology and molecular biology. "
        "You will ONLY answer questions related to microbiology. "
        "If the question is NOT about microbiology, answer exactly: "
        "'I'm sorry, I can only answer questions related to microbiology.' "
        "Do not make up information. If you do not know the answer, say so clearly. "
        "Always respond in the same language as the user."
    ),
}
