from flask import Flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('bfaReport.html')

@app.route("/handle_report", methods=['POST'])
def report_generator():
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
    #GDSCR = (person_income+business_income)/(person_debt+business_debt)
    

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



    print(type(person_debt),person_debt)
    return render_template('outputCalc.html')

@app.route("/business")
def output_calc():
    return render_template('business.html')


if __name__ == "__main__":
    app.run(debug = True)
    