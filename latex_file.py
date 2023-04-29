from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

# Create a new document
doc = Document()

# Add a title
doc.preamble.append(Command('title', 'My LaTeX Document'))
doc.preamble.append(Command('author', 'John Doe'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(Command('maketitle'))

# Add a section
with doc.create(Section('Section Title')):
    # Add a subsection
    with doc.create(Subsection('Subsection Title')):
        doc.append('Some text here.')

    # Add some italicized text
    doc.append(italic('Some italicized text.'))

# Add a custom command
doc.append(Command('mycommand', 'Some custom command.'))

# Generate the PDF
doc.generate_pdf('documents/my_document', clean=True, clean_tex=True, silent=True, compiler='latexmk')