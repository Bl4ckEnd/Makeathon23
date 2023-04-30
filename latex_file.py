from pylatex import Document, Command, NoEscape, Package, Figure


def create_latex_pdf(name, date, location, equipment, task, process):

    # Create document
    geometry_options = {"margin": "1in", "paperwidth": "595pt", "paperheight": "842pt"}
    doc = Document(geometry_options=geometry_options)

    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('color'))
    doc.packages.append(Package('pxfonts'))
    doc.packages.append(Package('latexsym'))
    doc.packages.append(Package('ucs', options=['mathletters']))
    doc.packages.append(Package('fontenc', options='T1'))
    doc.packages.append(Package('wasysym'))
    doc.packages.append(Package('babel', options='english'))
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('fancyhdr'))
    doc.packages.append(Package('tabularx'))
    doc.packages.append(Package('booktabs'))
    doc.packages.append(Package('geometry'))
    doc.packages.append(Package('enumitem'))
    doc.packages.append(Package('graphicx'))

    # Add title
    doc.preamble.append(Command('title', 'Technical Report'))
    # date
    doc.preamble.append(Command('date', NoEscape(f'{date}')))

    # make title
    doc.append(NoEscape(r'\maketitle'))

    # insert company logo
    with doc.create(Figure(position='h!')) as pic:
        pic.add_image('/Users/vale/Documents/Makeathon23/company_logo.png', width='200px')


# latex bold text
    doc.append(Command('noindent'))
    doc.append(Command('textbf', 'Electro Volt Technician: '))
    doc.append(name)
    doc.append(Command('vspace', '0.3cm'))
    doc.append(NoEscape(r"\\"))
    doc.append(Command('textbf', 'Equipment: '))
    doc.append(equipment)
    doc.append(Command('vspace', '0.3cm'))
    doc.append(NoEscape(r"\\"))
    doc.append(Command('textbf', 'Location: '))
    doc.append(location)
    doc.append(Command('vspace', '0.3cm'))
    doc.append(NoEscape(r"\\"))
    doc.append(Command('textbf', 'Task: '))
    doc.append(task)
    doc.append(Command('vspace', '0.3cm'))
    doc.append(NoEscape(r"\\"))
    doc.append(Command('newpage'))
    doc.append(Command('noindent'))
    doc.append(Command('textbf', 'Process: '))
    doc.append(NoEscape(r"\\"))
    doc.append(process)
    doc.append(Command('vspace', '3cm'))

    doc.append(NoEscape(r"\\"))
    doc.append(Command('textbf', 'Signature:'))
    doc.append(Command('vspace', '1cm'))
    doc.append(NoEscape(r"\\"))

    doc.append('Supervisor: ')
    doc.append(Command('hfill'))
    doc.append('Technician: ')
    doc.append(Command('hspace', '1cm'))

    doc.generate_pdf('documents/report', clean_tex=True, clean=True)


if __name__ == '__main__':
    create_latex_pdf("Valentin Goelz", "24.03.2022", "Straubing", "Windturbine", "Repairs", "A lot of stuff.")