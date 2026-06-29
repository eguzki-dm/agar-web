from datetime import datetime
from fpdf import FPDF


def generate_pdf(detections: list, classifications: list, species_counts: dict, session_id: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "uKount & uDetect - Analysis Report", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Session: {session_id}", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(10)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 7, f"Total detections: {len(detections)}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Total classified: {len(classifications)}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    if species_counts:
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "Species Distribution", new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Helvetica", "B", 10)
        col_w = 60
        pdf.cell(col_w, 8, "Species", border=1)
        pdf.cell(col_w, 8, "Count", border=1)
        pdf.cell(col_w, 8, "Percentage", border=1)
        pdf.ln()

        pdf.set_font("Helvetica", "", 10)
        total = sum(species_counts.values())
        for species, count in sorted(species_counts.items()):
            pct = f"{(count / total * 100):.1f}%" if total > 0 else "0%"
            pdf.cell(col_w, 7, species, border=1)
            pdf.cell(col_w, 7, str(count), border=1)
            pdf.cell(col_w, 7, pct, border=1)
            pdf.ln()
        pdf.ln(5)

    if classifications:
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "Per-Colony Details", new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Helvetica", "B", 9)
        col_w = [15, 40, 25, 25, 25]
        headers = ["#", "Species", "Confidence", "Detection", "Details"]
        for w, h in zip(col_w, headers):
            pdf.cell(w, 8, h, border=1)
        pdf.ln()

        pdf.set_font("Helvetica", "", 9)
        for i, c in enumerate(classifications[:50]):
            pdf.cell(col_w[0], 7, str(i + 1), border=1)
            pdf.cell(col_w[1], 7, c["species"], border=1)
            pdf.cell(col_w[2], 7, f"{c['confidence']:.1%}", border=1)
            det_conf = detections[i]["confidence"] if i < len(detections) else 0
            pdf.cell(col_w[3], 7, f"{det_conf:.1%}", border=1)
            pdf.cell(col_w[4], 7, "...", border=1)
            pdf.ln()

        if len(classifications) > 50:
            pdf.cell(0, 7, f"... and {len(classifications) - 50} more colonies", new_x="LMARGIN", new_y="NEXT")

    return pdf.output()