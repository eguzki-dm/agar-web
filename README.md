<div align="center">
  <img src="icons/icono.png" width="160" alt="AGAR-Web Logo">
  <h1>μKount & μDetect</h1>
  <p><em>AI-Assisted Microbiological Colony Analysis</em></p>
  <p>
    <a href="https://github.com/eguzki-dm">Eguzkiñe</a>
  </p>
</div>

---

**AGAR-Web** is a Streamlit-based web application that demonstrates a complete AI-assisted workflow for agar plate microbiological analysis. It combines computer vision and deep learning to detect, count, and classify microbial colonies — all from a single uploaded image.

> ⚠️ **Research prototype.** Not for clinical use.

---

## Workflow

```
Upload Image → μKount (Detection) → Crop → μDetect (Classification) → Results
```

| Step | Description |
|------|-------------|
| **📤 Upload** | Drag & drop or generate a synthetic agar plate |
| **🔍 μKount** | YOLO-based colony detection with bounding boxes |
| **✂️ Crop** | Isolate each colony with black background preprocessing |
| **🧪 μDetect** | CNN-based species classification (5 bacteria/fungi) |
| **📊 Results** | Metrics dashboard + species knowledge base |

---

## Preview

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="icons/uKount.png" width="300"><br><b>μKount</b><br><em>Colony Detection</em></td>
      <td align="center"><img src="icons/uDetect.png" width="300"><br><b>μDetect</b><br><em>Species Classification</em></td>
    </tr>
  </table>
</div>

---

## Features

- **🎯 Colony Detection** — Locate and count microbial colonies on agar plates
- **🔬 Species Classification** — Identify 5 species: *S. aureus*, *B. subtilis*, *P. aeruginosa*, *E. coli*, *C. albicans*
- **🌐 Bilingual** — Full English / Spanish support via dictionary-based i18n (229 keys each)
- **🧪 Mock Services** — All AI services are mock until real YOLO/CNN models are integrated
- **📖 Species Knowledge Base** — Bilingual descriptions, Gram stain, morphology, risk group
- **📊 Results Dashboard** — Metrics, charts, detection previews
- **🖼️ Synthetic Data** — Generate synthetic agar plates for testing
- **♿ Accessible** — Clean, responsive UI with hidden navigation

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **[Streamlit](https://streamlit.io)** (≥1.28) | Web framework |
| **Python** (≥3.10) | Language |
| **Pillow** | Image processing |
| **YOLOv8** (future) | Real colony detection |
| **CNN** (future) | Real species classification |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/eguzki-dm/agar-web.git
cd agar-web

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Project Structure

```
agar-web/
├── app.py                  # Entry point + sidebar
├── config/                 # Settings (species, mock flag, colors)
├── pages/                  # 8 Streamlit pages (Home, Pipeline, μKount, μDetect, Results, About, Future Features, Disclaimer)
├── services/               # Detection, classification, preprocessing (mock)
├── components/             # Cards, charts, image viewer
├── data/                   # species_info.json (bilingual knowledge base)
├── icons/                  # Branding icons
├── locales/                # i18n dictionaries (en.py, es.py)
├── utils/                  # Session state, i18n helper
├── .opencode/              # AI assistant config
├── .memory/                # Project memory
└── .streamlit/             # Streamlit Cloud config
```

---

## Meet Cuora 🧑‍🔬

<div align="center">
  <img src="icons/Cuora.png" width="240" alt="Cuora">
</div>

**Cuora** is the virtual microbiologist of AGAR-Web. Soon she will answer your questions about colonies, species, and lab techniques — making the app not just a tool, but a learning companion.

*Coming in a future phase.*

---

## Roadmap

| Phase | Status |
|-------|--------|
| **1 — MVP** Streamlit + mock services | ✅ Complete |
| **2 — μKount** Real YOLO detection | 🔄 Pending |
| **3 — μDetect** Real CNN classification | ⬜ Pending |
| **4 — Detection Editing** Manual box adjustment | ⬜ Pending |
| **5 — Rich Species Info** Morphology, pathology | ⬜ Pending |
| **6 — Chatbot** Cuora answers your questions | ⬜ Pending |
| **7 — Deployment** Streamlit Cloud / HF Spaces | ⬜ Pending |

---

## Resources

| Resource | Reference |
|----------|-----------|
| **AGAR dataset** | Majchrowska et al. 2021 |
| **Patch preprocessing** | Pawłowski et al. 2022 · [GitHub](https://github.com/jarek-pawlowski/microbial-dataset-generation) |

---

## Acknowledgments

This project was developed as the final applied project within the **LABORLAN 2026: IA & Data Tech (Artificial Intelligence and Technology Project Management)** program.

Special thanks to **Aitor Donado** for his technical guidance and support, and to all my classmates who generously acted as the Spark Worker Nodes to process my thousands of images! ♥️

We also thank the teaching staff, mentors, and organizers of LABORLAN 2026 for their commitment and the learning environment that made this project possible.

---

## Author

**Eguzkiñe** — [@eguzki-dm](https://github.com/eguzki-dm)

---

## Disclaimer

AGAR-Web is a **Proof-of-Concept research system**. All AI services are mock implementations. Results are experimental and must **not** be used for clinical diagnosis, treatment decisions, or any medical purpose. Always validate microbial identification through standard microbiological methods.
