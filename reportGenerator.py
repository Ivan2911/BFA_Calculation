#from docx import Document

#document = Document() #Initiate document

#Header

#person_name = "kk"
#business_name = "Joko"

#Personal Credit Profile


#Cash Flow Analysis


#Bank Statement Analysis
#document.save("BFA Report for " + person_name + " " + business_name)

"""
from docx.shared import Inches
from docx import Document

#inititate Documents
document = Document()

#Heading
heading = document.add_heading('Business Funding Analysis', 0)

#Personal credit profile
personal = document.add_heading('Personal Credit Profile', level=1)
p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

#document.add_picture('monty-truth.png', width=Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

#document.add_page_break()

#document.save('demo.docx')