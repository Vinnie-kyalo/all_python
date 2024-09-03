from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def create_pdf(filename):
    # Create a SimpleDocTemplate with the specified filename and letter page size
    pdf = SimpleDocTemplate(filename, pagesize=letter)

    # Create a list to hold the elements to be added to the PDF
    elements = []

    # Get a sample stylesheet
    styles = getSampleStyleSheet()

    # Create a title
    title = Paragraph("PDF Generator Example", styles['Title'])
    elements.append(title)

    # Add a spacer between elements
    elements.append(Spacer(1, 12))

    # Add some sample text
    text = "This is a simple PDF generator example using ReportLab."
    paragraph = Paragraph(text, styles['Normal'])
    elements.append(paragraph)

    # Add another spacer
    elements.append(Spacer(1, 12))

    # Add more text
    text2 = "ReportLab is a powerful library for creating PDFs in Python. You can add various elements like text, images, tables, and more."
    paragraph2 = Paragraph(text2, styles['Normal'])
    elements.append(paragraph2)

    # Add a final spacer
    elements.append(Spacer(1, 12))

    # Build the PDF
    pdf.build(elements)

# Call the function to create the PDF
create_pdf("sample.pdf")
