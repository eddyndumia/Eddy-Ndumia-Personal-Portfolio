"""
Generates Eddy_Ndumia_Resume.pdf from scratch with reportlab.

Kept as a real, runnable script (not a one-off) so the resume can be
regenerated whenever content/projects/*.md gains something worth adding,
rather than hand-editing a binary PDF each time. Run from this directory:

    python generate_resume.py

Style notes carried over from the prior version of this file:
- Avoid literal em-dashes and &nbsp; entities - they mangle in reportlab's
  Standard-14 font text layer. Use a plain hyphen surrounded by spaces.
- Verify single-page output and that the text layer extracts cleanly
  before committing the regenerated PDF.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = "Eddy_Ndumia_Resume.pdf"

styles = {
    "name": ParagraphStyle("name", fontName="Times-Bold", fontSize=24, leading=28, spaceAfter=2),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica", fontSize=10.5, leading=13, spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=12, textColor="#333333", spaceAfter=6),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceBefore=6, spaceAfter=2, textColor="#111111"),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.2, leading=11.8, spaceAfter=2),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.4, leading=11.8, spaceAfter=0),
    "date": ParagraphStyle("date", fontName="Helvetica-Oblique", fontSize=8.5, leading=10.3, spaceAfter=2, textColor="#444444"),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.0, leading=11.3, leftIndent=10, spaceAfter=1.5),
    "project": ParagraphStyle("project", fontName="Helvetica", fontSize=8.8, leading=11.0, spaceAfter=1.5),
    "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.5, leading=11, spaceAfter=2, textColor="#444444"),
}


def rule():
    return HRFlowable(width="100%", thickness=0.6, color="#999999", spaceBefore=2, spaceAfter=6)


def build_story():
    s = []
    s.append(Paragraph("Eddy Ndumia", styles["name"]))
    s.append(Paragraph("AI enthusiast &amp; data engineer (AWS) - Mathematics &amp; Computer Science, JKUAT", styles["tagline"]))
    s.append(Paragraph(
        "ndumia.netlify.app | github.com/eddyndumia | linkedin.com/in/eddyndumia | Nairobi, Kenya",
        styles["contact"]
    ))
    s.append(rule())

    s.append(Paragraph("SUMMARY", styles["section"]))
    s.append(Paragraph(
        "AI enthusiast with data engineering experience on AWS, turning raw, messy data into pipelines and models "
        "that hold up in production. Currently building PesaScore, a fintech platform that scores creditworthiness "
        "from alternative data (M-Pesa statements) instead of a traditional credit bureau, and Capstone, an AI lead "
        "assistant for real estate agents. Freelance web developer since 2020.",
        styles["body"]
    ))

    s.append(Paragraph("EXPERIENCE", styles["section"]))

    s.append(Paragraph("Independent Builder - PesaScore, Capstone, Chukua &amp; Kwetu", styles["role"]))
    s.append(Paragraph("2026 - Present", styles["date"]))
    s.append(Paragraph(
        "- PesaScore: alt-data credit scoring from M-Pesa statements - consumer app, lender dashboard, real PDF "
        "parsing and scoring, Supabase Auth + Postgres Row-Level Security for tenant isolation.",
        styles["bullet"]
    ))
    s.append(Paragraph(
        "- Capstone: AI agent handling WhatsApp/Instagram DMs for real estate agencies - qualifies leads, books "
        "viewings, hands off to a human when it should. FastAPI + Postgres backend, Next.js dashboard.",
        styles["bullet"]
    ))
    s.append(Paragraph(
        "- Chukua: Flutter app for giving away free stuff nearby, with AI value estimates and M-Pesa claim fees. "
        "Supabase + PostGIS, atomic claim holds, Row-Level Security keeping givers' phones private.",
        styles["bullet"]
    ))
    s.append(Paragraph(
        "- Kwetu: Flutter app for people abroad to buy electronics for family in Kenya, paid in USDT/USDC.",
        styles["bullet"]
    ))

    s.append(Paragraph("Freelance Web Developer - Kenya", styles["role"]))
    s.append(Paragraph("2020 - Present", styles["date"]))
    s.append(Paragraph(
        "- Responsive, data-driven sites and custom full-stack builds for small businesses - WordPress and "
        "code-first, depending on the client.",
        styles["bullet"]
    ))

    s.append(Paragraph("Project Lead, Web Housing Management System - JKUAT", styles["role"]))
    s.append(Paragraph("Sept - Dec 2022", styles["date"]))
    s.append(Paragraph(
        "- Led a university team building a cloud-backed system for tenants, properties, and admin tasks - auth, "
        "data tracking, reporting dashboards.",
        styles["bullet"]
    ))

    s.append(Paragraph("EDUCATION &amp; TRAINING", styles["section"]))
    s.append(Paragraph("B.Sc. Mathematics and Computer Science - JKUAT", styles["role"]))
    s.append(Paragraph("2020 - 2026 (graduating December 2026)", styles["date"]))
    s.append(Paragraph("ALX / Holberton Software Engineering Program", styles["role"]))
    s.append(Paragraph("2023 - low-level programming in C, algorithms, Linux/DevOps", styles["date"]))
    s.append(Paragraph("HackRU IX Hackathon", styles["role"]))
    s.append(Paragraph(
        "2022 - patient-connection platform for the NY-Presbyterian/Morgan Stanley Children's Hospital Challenge",
        styles["date"]
    ))
    s.append(Paragraph("Certifications", styles["role"]))
    s.append(Paragraph(
        "Data Science with Python (JKUAT) | Cisco Networking Level 1 (JKUAT) | Web &amp; Mobile Application "
        "Development (eMobilis Technology Training Institute)",
        styles["date"]
    ))

    s.append(Paragraph("SELECTED PROJECTS", styles["section"]))
    projects = [
        ("Sales ETL Pipeline", "Messy raw sales data cleaned, tested, and loaded into a quality-gated SQLite warehouse; 6 automated data-quality checks gate every run."),
        ("Customer Churn Classification", "Imbalance-aware model comparison (class weighting vs. SMOTE across 3 model types) translated into an estimated $112k business impact, not just an accuracy score."),
        ("Sales Pipeline Funnel Analytics", "6 SQL queries answering real sales-ops questions: funnel drop-off, rep and lead-source win rates, deal velocity by segment, stage-weighted revenue forecasting."),
        ("Sales Demand Forecasting", "Seasonal-naive vs. SARIMA vs. XGBoost on a 90-day holdout; found and explained why single-seasonality SARIMA misses yearly retail spikes XGBoost catches via calendar features."),
        ("Lead Scoring App", "Gradient-boosting lead scorer deployed as a Streamlit app, with precision/recall thresholds tied to real sales team capacity (~1.9x lift over random contact at 25% capacity)."),
        ("PropFire", "Trading timer and journal for forex traders timing entries around high-impact news releases."),
        ("RAG Chatbot", "LangChain-based retrieval-augmented chatbot for querying custom text datasets."),
    ]
    for name, desc in projects:
        s.append(Paragraph(f"<b>{name}</b> - {desc}", styles["project"]))
    s.append(Paragraph("Full write-ups and repo links: ndumia.netlify.app/projects", styles["note"]))

    s.append(Paragraph("SKILLS", styles["section"]))
    s.append(Paragraph("<b>Languages:</b> Python, TypeScript, JavaScript/Node.js, Dart, Kotlin, SQL", styles["body"]))
    s.append(Paragraph("<b>Data &amp; ML:</b> Pandas, NumPy, Scikit-learn, XGBoost, statsmodels, TensorFlow, LangChain / RAG", styles["body"]))
    s.append(Paragraph("<b>Infra:</b> Postgres, PostGIS, Supabase, Docker, AWS", styles["body"]))
    s.append(Paragraph("<b>Web &amp; mobile:</b> React, Next.js, Flutter, FastAPI, Streamlit, WordPress", styles["body"]))

    return s


def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.4 * inch, bottomMargin=0.25 * inch,
        title="Eddy Ndumia - Resume",
    )
    doc.build(build_story())
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
