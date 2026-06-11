from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(topic, report):

    filename = f"{topic.replace(' ', '_')}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(topic, styles["Title"])
    )

    elements.append(
        Spacer(1, 12)
    )

    for paragraph in report.split("\n"):

        if paragraph.strip():

            elements.append(
                Paragraph(paragraph, styles["BodyText"])
            )

            elements.append(
                Spacer(1, 6)
            )

    doc.build(elements)

    return filename