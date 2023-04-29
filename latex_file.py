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


def create_latex_pdf2(name, date, location, equipment, task, process):
    from pylatex import Document, Section, Command, Tabularx, NewPage, NoEscape, \
        Center, Foot, LineBreak, MiniPage, Package, PageStyle, Head

    geometry_options = {"margin": "1in", "paperwidth": "595pt", "paperheight": "842pt"}
    doc = Document(geometry_options=geometry_options)

    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('color'))
    doc.packages.append(Package('pxfonts'))
    doc.packages.append(Package('fix-cm'))
    doc.packages.append(Package('latexsym'))
    doc.packages.append(Package('ucs', options=['mathletters']))
    doc.packages.append(Package('fontenc', options='T1'))
    doc.packages.append(Package('inputenc', options='utf8x'))
    doc.packages.append(Package('pict2e'))
    doc.packages.append(Package('wasysym'))
    doc.packages.append(Package('babel', options='english'))
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('fancyhdr'))
    doc.packages.append(Package('tabularx'))
    doc.packages.append(Package('booktabs'))
    doc.packages.append(Package('geometry'))
    doc.packages.append(Package('enumitem'))

    #doc.preamble.append(Command('DeclareUnicodeCharacter', '46', arguments=['\\textperiodcentered']))

    # Page style
    with doc.create(PageStyle("fancy")):
        with doc.create(Head("R")):
            doc.append("Service Report: (Enter ID here)")
        with doc.create(Head("L")):
            doc.append("Technician: (Enter name here)")
        with doc.create(Foot("L")):
            with doc.create(MiniPage(width=NoEscape(r"\textwidth"), pos='c', align='l')):
                doc.append(NoEscape(
                    r"\scriptsize \textbf{Electro Volt GmbH}\\Karl-Ebert-Str. 1\\80555 München, Germany\\E-Mail: info@electrovolt.de\\"))
        #doc.append(Command('setlength', 'headheight', arguments=['40pt']))

    doc.append(Command('begin', 'document'))

    with doc.create(Center()):
        doc.append(Command('textbf', 'Project Report'))

    doc.append(LineBreak())

    with doc.create(Tabularx('l X')):
        doc.append(Command('textbf', 'Report Date:'))
        doc.append('&')
        doc.append(Command('today'))
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Report ID:'))
        doc.append('&')
        doc.append('[insert report ID]')
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Technician:'))
        doc.append('&')
        doc.append('[insert technician name]')
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Customer Name:'))
        doc.append('&')
        doc.append('[insert customer name]')
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Customer ID:'))
        doc.append('&')
        doc.append('[insert customer ID]')
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Issue Type:'))
        doc.append('&')
        doc.append('[insert issue type]')
        doc.append(LineBreak())
        doc.append(Command('textbf', 'Operation Successful:'))
        doc.append('&')
        doc.append('[insert Yes or No]')
        doc.append(LineBreak())

    doc.append(NewPage())

    with doc.create(Section('Problem Description')):
        pass

    doc.append(Command('vspace', '1em'))

    doc.append(Command('vspace', '1em'))

    with doc.create(Section('Reason of Problem and Solution Provided')):
        pass

    doc.append(Command('vspace', '1em'))

    doc.append(Command('vspace', '1em'))

    with doc.create(Section('Daily Report')):
        pass

    doc.append(Command('vspace', '1em'))

    doc.append(Command('vspace', '1em'))

    with doc.create(Section('Checks Performed')):
        pass

    doc.append(Command('vspace', '1em'))

    doc.append(Command('vspace', '1em'))

    with doc.create(Section('Project Summary')):
        pass

    doc.append(Command('vspace', '1em'))

    doc.append(Command('vspace', '1cm'))

    doc.append(Command('noindent'))

    doc.append(Command('textbf', 'Signature:'))

    doc.append(Command('vspace', '0.5cm'))

    doc.append('Supervisor: ')
    doc.append(Command('underline', options=['hspace', '5cm']))
    doc.append(Command('hfill'))
    doc.append('Technician: ')
    doc.append(Command('underline', options=['hspace', '5cm']))

    doc.generate_pdf('example', clean_tex=False)

if __name__ == '__main__':
    create_latex_pdf2("name", "date", "location", "equipment", "task", "process")