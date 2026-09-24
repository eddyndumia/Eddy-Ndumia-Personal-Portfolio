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
# Live site. Change here when the portfolio moves to its own domain.
SITE = "https://eddyndumia.github.io/Eddy-Ndumia-Personal-Portfolio/"

styles = {
    "name": ParagraphStyle("name", fontName="Times-Bold", fontSize=24, leading=28, spaceAfter=2),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica", fontSize=10.5, leading=13, spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=12, textColor="#333333", spaceAfter=6),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceBefore=5, spaceAfter=2, textColor="#111111"),
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
    s.append(Paragraph("Developer and data engineer (AWS) - Maths &amp; Computer Science, JKUAT - Nairobi, Kenya", styles["tagline"]))
    s.append(Paragraph(
        f'<link href="{SITE}">eddyndumia.github.io/Eddy-Ndumia-Personal-Portfolio</link> | '
        '<link href="https://github.com/eddyndumia">github.com/eddyndumia</link> | '
        '<link href="https://www.linkedin.com/in/eddyndumia/">linkedin.com/in/eddyndumia</link>',
        styles["contact"]
    ))
    s.append(rule())

    s.append(Paragraph("SUMMARY", styles["section"]))
    s.append(Paragraph(
        "Mathematics and Computer Science student at JKUAT, finishing December 2026. I've built websites and "
        "full-stack apps for small businesses since 2020, and I do data engineering on AWS: cleaning messy data "
        "and building pipelines that don't break. Most interested in finance, crypto and AI.",
        styles["body"]
    ))

    s.append(Paragraph("EXPERIENCE", styles["section"]))

    s.append(Paragraph("Freelance Web Developer - Kenya", styles["role"]))
    s.append(Paragraph("2020 - Present", styles["date"]))
    s.append(Paragraph(
        "- Famyard Enterprises (land sales, Nyeri/Laikipia): rebuilt their site in Next.js on Cloudflare Pages, plus a "
        "custom CMS (Postgres, role-based login, inquiries inbox) so staff manage plots and content without WordPress.",
        styles["bullet"]
    ))
    s.append(Paragraph(
        "- Sites and full-stack builds for other small businesses, in WordPress or code.",
        styles["bullet"]
    ))


    s.append(Paragraph("EDUCATION &amp; TRAINING", styles["section"]))
    s.append(Paragraph("B.Sc. Mathematics and Computer Science - JKUAT", styles["role"]))
    s.append(Paragraph("2020 - 2026 (graduating December 2026)", styles["date"]))
    s.append(Paragraph("ALX / Holberton Software Engineering Program", styles["role"]))
    s.append(Paragraph("2023 - low-level programming in C, algorithms, Linux/DevOps", styles["date"]))

    s.append(Paragraph("SELECTED PROJECTS", styles["section"]))
    projects = [
        ("Sales ETL Pipeline", "Messy raw sales data cleaned, tested, and loaded into a quality-gated SQLite warehouse; 6 automated data-quality checks gate every run."),
        ("Sales Demand Forecasting", "Seasonal-naive vs. SARIMA vs. XGBoost on a 90-day holdout; XGBoost's calendar features catch the yearly retail spikes SARIMA misses."),
    ]
    for name, desc in projects:
        s.append(Paragraph(f"<b>{name}</b> - {desc}", styles["project"]))
    s.append(Paragraph(f'Full write-ups and repo links: <link href="{SITE}projects/">eddyndumia.github.io/Eddy-Ndumia-Personal-Portfolio/projects</link>', styles["note"]))

    s.append(Paragraph("SKILLS", styles["section"]))
    s.append(Paragraph("<b>Languages:</b> Python, TypeScript, JavaScript/Node.js, Dart, SQL", styles["body"]))
    s.append(Paragraph("<b>Data:</b> Pandas, NumPy, Scikit-learn, XGBoost, statsmodels, Airflow", styles["body"]))
    s.append(Paragraph("<b>Infra:</b> Postgres, PostGIS, Supabase, Docker, AWS", styles["body"]))
    s.append(Paragraph("<b>Web &amp; mobile:</b> React, Next.js, Flutter, WordPress", styles["body"]))

    return s


def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.35 * inch, bottomMargin=0.25 * inch,
        title="Eddy Ndumia - Resume",
    )
    doc.build(build_story())
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
