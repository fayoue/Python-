"""
Employee Status Program

This program stores and displays an employee's
basic information and active employment status.
"""

employee_name = "John"
employee_age = 25
employee_salary = 45000.50
employee_active = True

print("Employee Information")
print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: {employee_salary:.2f}")
print(f"Employee Active: {employee_active}")

# Convert a number to a string before concatenating
age_text = str(employee_age)
print("Employee age is " + age_text + " years old.")
