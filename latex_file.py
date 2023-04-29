from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

from pylatex import Document, Section, Itemize, Subsection

def create_latex_pdf(name, date, location, equipment, task, process):

    # Create document
    doc = Document()

    # Add title and author
    doc.append(r"Technical Report")
    # use name as author
    doc.append(r"Technician: " + name)
    # use date as date
    doc.append(r"Date: " + str(date))

    # Add sections
    with doc.create(Subsection('Equipment')):
        doc.append(equipment)

    with doc.create(Subsection('Task')):
        doc.append(task)

    with doc.create(Subsection('Process')):
        doc.append(process)
    # Generate pdf
    doc.generate_pdf('documents/report', clean_tex=True, clean=True)
