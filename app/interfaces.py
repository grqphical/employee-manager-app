"""Script for interfacing with the database"""

import sqlite3
from dotenv import load_dotenv
from os import environ, path
from app.employee import Employee

load_dotenv(path.join(path.dirname(__file__),"..", ".env"))

# Check if user set the program to store the database in memory
if environ.get("DEBUG").lower() == "true":
    connection = sqlite3.connect(':memory:', check_same_thread=False)
else:
    connection = sqlite3.connect(path.join(path.dirname(__file__), "..", 'data/employees.sqlite'), check_same_thread=False)

# Setup the connection's cursor
cursor = connection.cursor()

def add_employee(employee:Employee):
    """Takes in a first name, last name and salary and adds it to the database"""
    with connection:
        cursor.execute("INSERT INTO Employees VALUES (:first, :last, :pay, :email)", {"first": employee.firstName, 
        "last": employee.lastName, 
        "pay": employee.salary, 
        "email": employee.email})

def get_employees_by_last(lastname:str):
    """Takes in an employees last name and gets every entry with the same last name"""
    with connection:
        cursor.execute("SELECT * FROM Employees WHERE last=:last", {'last': lastname})
        return cursor.fetchall()

def get_employees():
    """Gets all active employees"""
    with connection:
        cursor.execute("SELECT * FROM Employees")
        return cursor.fetchall()
def update_pay(first:str, last:str, pay:int):
    """Updates an employee's salary"""
    with connection:
        employee = Employee(first, last, pay)
        cursor.execute("""UPDATE Employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': employee.firstName, 'last': employee.lastName, 'pay': employee.salary})
def remove_employee(employee:Employee):
    """Removes an employee from the database"""
    with connection:
        cursor.execute("DELETE from Employees WHERE first = :first AND last = :last",
                  {'first': employee.firstName, 'last': employee.lastName})
def remove_employee_by_name(first:str, last:str):
    """Removes an employee based on their name"""
    with connection:
        cursor.execute("DELETE from Employees WHERE first = :first AND last = :last",
                  {'first': first, 'last': last})
