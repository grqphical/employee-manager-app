"""Script that runs the web interface"""
from flask import Flask, render_template, request, redirect, url_for
import app.interfaces
from app.employee import Employee

fapp = Flask(__name__)


name = None

# Home page
@fapp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", employees=app.interfaces.get_employees())

# View to add employee
@fapp.route("/add-employee", methods=["POST", "GET"])
def add_employee_view():
    if request.method == "GET":
        return render_template("add_employee.html")
    elif request.method == "POST":
        first = request.form.get('first')
        last = request.form.get('last')
        salary = request.form.get('salary')

        app.interfaces.add_employee(Employee(first, last , salary))
        return redirect("/")

# View to remove employees
@fapp.route("/remove-employee", methods=["POST", "GET"])
def remove_employee_view():
    if request.method == 'GET':
        return render_template("remove_employee.html", employees=app.interfaces.get_employees())
    else:
        select = request.form.get("employee")
        first, last = str(select).split()
        app.interfaces.remove_employee_by_name(first, last)
        return redirect("/")
# View to modify employee
@fapp.route("/modify-employee/<employee>", methods=['GET'])
def modify_employee_view(employee):
    global name
    if request.method == "GET":
        name = employee.replace("(", "")
        name = name.replace(")", "")
        name = name.replace('\'', "")
        name = name.replace(" ", "")

        name = name.split(",")
        
        return render_template("modify_employee.html", employee=name)

@fapp.route("/modify-employee", methods=["POST"])
def apply_employee_edit():
    global name
    pay = request.form.get("salary")
    app.interfaces.update_pay(name[0], name[1], pay)
    return redirect("/")

def main():
    fapp.run()