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
SITE = "https://eddyndumia.github.io/"

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
    s.append(Paragraph("Software Developer - Nairobi, Kenya", styles["tagline"]))
    s.append(Paragraph(
        f'<link href="{SITE}">eddyndumia.github.io</link> | '
        '<link href="mailto:ndumiaeddy8@gmail.com">ndumiaeddy8@gmail.com</link> | '
        '<link href="https://github.com/eddyndumia">github.com/eddyndumia</link> | '
        '<link href="https://www.linkedin.com/in/eddyndumia/">linkedin.com/in/eddyndumia</link>',
        styles["contact"]
    ))
    s.append(rule())

    s.append(Paragraph("SUMMARY", styles["section"]))
    s.append(Paragraph(
        "Final-year Mathematics and Computer Science student at JKUAT (graduating December 2026). I build and run "
        "production web and mobile systems for businesses in Kenya: websites, internal business systems, payment "
        "records and mobile apps. Freelance since 2020, with data engineering work on AWS. Most interested in "
        "software for payments, finance and data.",
        styles["body"]
    ))

    s.append(Paragraph("EXPERIENCE", styles["section"]))

    s.append(Paragraph("Head of Technology and Digital Products - Famyard Enterprises", styles["role"]))
    s.append(Paragraph("2025 - Present | Land sales company, Nyeri and Laikipia", styles["date"]))
    s.append(Paragraph(
        "- Rebuilt famyard.co.ke in Next.js and moved it off WordPress, with every old URL redirected.",
        styles["bullet"]))
    s.append(Paragraph(
        "- Built the internal system the staff run the business on: plots and estates, enquiries and a sales "
        "pipeline, a payments ledger with numbered receipts and reversals instead of edits, the company email "
        "inbox, and role and department access with two-factor sign-in and encrypted backups.",
        styles["bullet"]))
    s.append(Paragraph(
        "- Built the engine for a one-plot tokenized land pilot planned for the CMA regulatory sandbox: investor "
        "checks, holder register, Hedera Token Service issuance, escrow and reconciliation. Runs on Hedera testnet.",
        styles["bullet"]))

    s.append(Paragraph("Developer - Apex AutoMobiles", styles["role"]))
    s.append(Paragraph("2026 - Present | Car import business, Nairobi", styles["date"]))
    s.append(Paragraph(
        "- Built the public website (about 1,700 cars, static pages on Cloudflare) and Apex Manager, the dealer "
        "system for stock, photos, preparation tasks and costs, with one-click publishing through GitHub Actions.",
        styles["bullet"]))
    s.append(Paragraph(
        "- Migrated 1,660 cars and 31,000 photos from the old WooCommerce site into the new system.",
        styles["bullet"]))

    s.append(Paragraph("Developer (contract) - GBL Capital", styles["role"]))
    s.append(Paragraph("2026 | Futures signals service", styles["date"]))
    s.append(Paragraph(
        "- Built the Flutter customer and desk apps and a TypeScript backend (Fastify, Postgres, public and admin "
        "APIs, worker) with Stripe billing and Firebase push alerts; shipped ten releases to 2.0.0 with about "
        "110 automated tests.",
        styles["bullet"]))

    s.append(Paragraph("Founder and Developer - Chukua", styles["role"]))
    s.append(Paragraph("2026 - Present | Own product", styles["date"]))
    s.append(Paragraph(
        "- Android app for giving things away to people nearby, live in Nairobi since October 2026 (v1.3.5). "
        "Flutter, Supabase and PostGIS, with the rules enforced in SQL and Row-Level Security, push alerts and "
        "in-app updates.",
        styles["bullet"]))

    s.append(Paragraph("Freelance Web and Full-Stack Developer", styles["role"]))
    s.append(Paragraph("2020 - Present | Kenya", styles["date"]))
    s.append(Paragraph(
        "- Websites and full-stack builds for small businesses, in WordPress or code.",
        styles["bullet"]))

    s.append(Paragraph("EDUCATION", styles["section"]))
    s.append(Paragraph("B.Sc. Mathematics and Computer Science - JKUAT", styles["role"]))
    s.append(Paragraph("2020 - 2026 (graduating December 2026)", styles["date"]))
    s.append(Paragraph("ALX / Holberton Software Engineering Programme", styles["role"]))
    s.append(Paragraph("2023 | C, algorithms, Linux", styles["date"]))

    s.append(Paragraph("OTHER PROJECTS", styles["section"]))
    projects = [
        ("Sales ETL Pipeline", "Messy sales export cleaned, tested and loaded into a constrained SQLite warehouse; six data-quality checks gate every run in CI."),
        ("Sales Demand Forecasting", "Seasonal-naive, SARIMA and XGBoost compared on a 90-day holdout."),
        ("Voice Forge", "Desktop audio app in Python; GPU jobs run on Kaggle through its API. In development."),
    ]
    for name, desc in projects:
        s.append(Paragraph(f"<b>{name}</b> - {desc}", styles["project"]))
    s.append(Paragraph(f'Write-ups and links: <link href="{SITE}projects/">eddyndumia.github.io/projects</link>', styles["note"]))

    s.append(Paragraph("SKILLS", styles["section"]))
    s.append(Paragraph("<b>Languages:</b> TypeScript, Python, Dart, SQL", styles["body"]))
    s.append(Paragraph("<b>Web and mobile:</b> Next.js, React, Flutter, Node.js (Fastify, Hono)", styles["body"]))
    s.append(Paragraph("<b>Data:</b> Postgres, PostGIS, Drizzle, Supabase, Neon, pandas, scikit-learn, statsmodels", styles["body"]))
    s.append(Paragraph("<b>Infrastructure:</b> AWS, Cloudflare (Workers, D1, R2), Render, Docker, GitHub Actions, Hedera Token Service", styles["body"]))

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
