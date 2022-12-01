from flask import Flask
from flask import Flask, render_template, request, redirect, session, send_file
import os
from reportGenerator import generate_report
app = Flask(__name__)


doc_dir = "documents/"   #Directory to save files/reports
fileName = "BFA_REPORT"  #To store the file name, default name is BFA Report


@app.route("/")
def home():
    return render_template('bfaReport.html')

@app.route("/handle_report", methods=['POST'])
def report_generator():
    #Initiate file name
    fileName = "BFA_REPORT" #To store the file name, default name is BFA Report
    #Delete any file in the directory
    for filename in os.listdir(doc_dir):
        os.remove(doc_dir+filename)

    #general information
    person_name = request.form.get("person_name")
    company_name = request.form.get("company_name")

    #Debt
    try:
        person_debt = float(request.form.get("person_debt"))
    except ValueError:
        person_debt = ""

    try:
        business_debt = float(request.form.get("business_debt"))
    except ValueError:
        business_debt = ""
    #Personal Income
    try:
        person_income = float(request.form.get("person_income"))
    except ValueError:
        person_income = ""
    person_year_1 = request.form.get("person_year_1")
    person_year_2 = request.form.get("person_year_2")
    person_year_3 = request.form.get("person_year_3")


    #Business Income
    try:
        business_income = float(request.form.get("business_income"))
    except ValueError:
        business_income = ""
    business_year_1 = request.form.get("business_year_1")
    business_year_2 = request.form.get("business_year_2")
    business_year_3 = request.form.get("business_year_3")

    #Debt Ratio
    try:
        DTO = float(request.form.get("DTO"))
    except ValueError:
        DTO = ""
    try:
        DTI = float(request.form.get("DTI"))
    except ValueError:
         DTI = ""
    try:     
        GDSCR = (person_income+business_income)/(person_debt+business_debt)
    except ValueError and TypeError:
        GDSCR = 0
    

    #Bank Statement Info
    try:
        capacity = float(request.form.get("capacity"))
    except ValueError:
        capacity = ""
    try:
        balance = float(request.form.get("balance"))
    except ValueError:
        balance = ""

    #Credit Score
    ex = request.form.get("ex")
    eq = request.form.get("eq")
    tu = request.form.get("tu")

    #Generate report
    if person_name != "":
        fileName = person_name
    generate_report(fileName)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(person_name)
    #print(GDSCR)
    return render_template('outputCalc.html')

@app.route("/download_file")
def download_file():
    file_path = "documents/"+fileName
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    print(file_path)
    return send_file(file_path, as_attachment=True)
   



if __name__ == "__main__":
    app.run(debug = True)
    