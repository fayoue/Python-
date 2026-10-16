# Employee Net Salary Program

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
deduction = float(input("Enter monthly deduction: "))

# Calculate housing allowance
housing_allowance = 0.10 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + housing_allowance

# Calculate net salary
net_salary = gross_salary - deduction

# Display results
print("\nEmployee Salary Details")
print("Employee Name:", employee_name)
print("Basic Salary: KSh", basic_salary)
print("Housing Allowance: KSh", housing_allowance)
print("Gross Salary: KSh", gross_salary)
print("Deduction: KSh", deduction)
print("Net Salary: KSh", net_salary)
