from flask import Flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('bfaCalc.html')

@app.route("/handle_calculation", methods=['POST'])
def output_calc():
    return render_template('outputCalc.html')


if __name__ == "__main__":
    app.run(debug = True)
    