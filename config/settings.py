USE_MOCK = True

MAX_UPLOAD_MB = 20

SUPPORTED_FORMATS = ["png", "jpg", "jpeg"]

APP_NAME = "μKount & μDetect"
APP_VERSION = "1.0.0"

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

SYNTHETIC_IMAGE_WIDTH = 800
SYNTHETIC_IMAGE_HEIGHT = 600
SYNTHETIC_MIN_COLONIES = 5
SYNTHETIC_MAX_COLONIES = 15
