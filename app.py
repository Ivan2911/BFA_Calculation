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
    person_debt = request.form.get("person_debt")
    business_debt = request.form.get("business_debt")

    #Personal Income
    person_income = request.form.get("person_income")
    person_year_1 = request.form.get("person_year_1")
    person_year_2 = request.form.get("person_year_2")
    person_year_3 = request.form.get("person_year_3")


    #Business Income
    business_income = request.form.get("business_income")
    business_year_1 = request.form.get("business_year_1")
    business_year_2 = request.form.get("business_year_2")
    business_year_3 = request.form.get("business_year_3")

    #Debt Ratio
    DTO = request.form.get("DTO")
    DTI = request.form.get("DTI")
    #GDSCR = (person_income+business_income)/(person_debt+business_debt)
    

    #Bank Statement Info
    capacity = request.form.get("capacity")
    balance = request.form.get("balance")

    #Credit Score
    ex = request.form.get("ex")
    eq = request.form.get("eq")
    tu = request.form.get("tu")



    print(type(person_debt))
    return render_template('bfaReport.html')

@app.route("/business")
def output_calc():
    return render_template('business.html')


if __name__ == "__main__":
    app.run(debug = True)
    