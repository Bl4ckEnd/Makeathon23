from fpdf import FPDF

# define a method that creates a pdf file from given inputs


def create_pdf(name, date, location, equipment, task, process):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Name: " + name, ln=1)
    pdf.cell(200, 10, txt="Date: " + str(date), ln=1)
    pdf.cell(200, 10, txt="Location: " + location, ln=1)
    pdf.cell(200, 10, txt="Equipment: " + equipment, ln=1)
    pdf.cell(200, 10, txt="Task: " + task, ln=1)
    pdf.cell(200, 10, txt="Process: " + process, ln=1)
    pdf.output("report.pdf")

