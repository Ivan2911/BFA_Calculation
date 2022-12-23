
from docx.shared import Inches
from docx import Document


def report_content(dict):
    
    #get infor details from dictionary
    name = dict["name"]
    company = dict["company"]
    person_debt = dict["person_debt"]
    business_debt= dict["business_debt"]
    person_income= dict["person_income"]
    person_year1= dict["person_year1"]
    person_year2= dict["person_year2"]
    person_year3= dict["person_year3"]
    business_income= dict["business_income"]
    business_year1= dict["business_year1"]
    business_year2= dict["business_year2"]
    business_year3= dict["business_year3"]
    DTO= dict["DTO"]
    DTI= dict["DTI"]
    GDSCR= dict["GDSCR"]
    capacity= dict["capacity"]
    balance= dict["balance"]
    ex= dict["ex"]
    eq = dict["eq"]
    tu = dict["tu"]

    #Initiate document
    document = Document()

    #Header
    document.add_picture('picture/wcf_logo.png', width=Inches(3))
    document.add_heading('Personal Business Financial Analysis', 0)
    document.add_paragraph('for '+ name)
    document.add_paragraph('Prepared by Wallace Capital Funding, LLC ')

    #Person Name

    #Business Name

    #Personal Credit Profile
    document.add_heading('Personal Credit Profile', level=1)
    document.add_paragraph('Credit Scores', style='List Bullet')
    records = (
        (name, ex, eq, tu)
    )
    table = document.add_table(rows=1, cols=4)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Name'
    hdr_cells[1].text = 'TU'
    hdr_cells[2].text = 'EQ'
    hdr_cells[3].text = 'EX'

    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = ex
    row_cells[2].text = eq
    row_cells[3].text = tu
    """
      for Name, TU, EQ, EX in records:
        row_cells = table.add_row().cells
        row_cells[0].text = Name
        row_cells[1].text = TU
        row_cells[2].text = EQ
        row_cells[3].text = EX
    
    """
  

    document.add_paragraph('PCW: '+ name, style='List Bullet')
    document.add_paragraph('   Debt-to-Owing Ratio (DTO):')
    document.add_paragraph('   Debt-to-Income Ratio (DTI):')
    
    #Cashflow analysis
    document.add_heading('Cash Flow Analysis ', level=1)
    document.add_paragraph('GDSCR', style='List Bullet')
    document.add_paragraph('   Using Global Cash Flow Sheet, we are able to calculate the total operating income and the total debt. We calculate the operating income from the data compiled from their balance sheet, profit & loss statement, and recent tax returns. We were able to calculate the total debt from recent credit report statements from Experian. Net operating income totaled to be $83,242 in 2016. That is a monthly income of 6,937. Total debt equal $24,528 with monthly debt payments of $3,515. That is a GDSCR of 3.39')
    
    #Bank Statement Analsyis
    document.add_heading('Bank Statement Analysis', level=1)
    document.add_paragraph('   We used (Business Name)’s most recent bank account statements, from Oct 2016- Jan 2017, to conduct the bank statement analysis. In the personal account, they have $33,605 in deposits and $47,415 in debits and a remaining balance of $224', style='List Bullet')
    
    #Recommendations
    document.add_heading('Recommendation', level=1)
    document.add_paragraph('   Keep the largest balance in business & checking accounts as possible ($500.00 to $1,000.00)- It helps with cash flow on the bank statements', style='List Bullet')
    
    return document
#document.add_page_break()
#document.save('\documents\demo.docx')

import os
import tempfile

def tmp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return(tempfile.gettempdir())

def generate_report(dict):

    #get name
    name = dict["name"]

    #Created temporary directory
    directory = tmp_dir()

    filename = name + ".docx"
    file_path = os.path.join(directory, filename)

    #Generate Report
    report = report_content(dict)

    #Save the report in temporary directory
    report.save(file_path)
    
    #file = open(file_path, "w")
    #file.write("you have realy good GDSCR "+ docName)
    #file.close()
    return file_path

