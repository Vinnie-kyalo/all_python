from fpdf import FPDF

def create_pdf(input_text, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=input_text, ln=True)
    pdf.output(output_filename)
    
create_pdf("My name is Vincent Kyalo", "vinnie.pdf")
