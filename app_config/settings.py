MAX_UPLOAD_MB = 20

SUPPORTED_FORMATS = ["png", "jpg", "jpeg"]

APP_NAME = "μKount & μDetect"
APP_VERSION = "1.1.0"

SPECIES = ["S. aureus", "B. subtilis", "C. albicans", "P. aeruginosa", "E. coli"]

SPECIES_DISPLAY = {
    "S. aureus": "Staphylococcus aureus",
    "B. subtilis": "Bacillus subtilis",
    "E. coli": "Escherichia coli",
    "C. albicans": "Candida albicans",
    "P. aeruginosa": "Pseudomonas aeruginosa",
}

NAV_PAGES = [
    "Home",
    "Pipeline",
    "μKount",
    "μDetect",
    "Results",
    "About",
    "Future Features",
    "Disclaimer",
]

DETECTION_COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

SLICE_SIZE = 640
SAHI_OVERLAP_RATIO = 0.3
SAHI_BATCH_SIZE = 16
POST_PROCESS_MATCH_THRESHOLD = 0.2

# ── μKount settings ──
YOLO_MODEL_PATH = "model/Kount/best_slicing.pt"
YOLO_MODEL_RESIZE_PATH = "model/Kount/best_resize.pt"
YOLO_CONFIDENCE_THRESHOLD = 0.25
YOLO_IOU_THRESHOLD = 0.45
LETTERBOX_SIZE = 2048

# ── μDetect settings ──
CLASSIFICATION_MODEL_PATH = "model/Detect/best_model.keras"
CLASSIFICATION_IMG_SIZE = 224
CLASSIFICATION_CONF_THRESHOLD = 0.50

EXAMPLE_IMAGES_DIR = "example"

RESULTS_DIR = "data/results"
