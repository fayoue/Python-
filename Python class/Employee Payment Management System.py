class Employee:

  def __init__(self, employee_id, name, basic_salary, overtime_hours):
    self.employee_id = employee_id
    self.name = name
    self.basic_salary = basic_salary
    self.overtime_hours = overtime_hours

  def calculate_gross_salary(self):
    return self.basic_salary + (self.overtime_hours * 500)

  def calculate_tax(self):
    gross_salary = self.calculate_gross_salary()
    return gross_salary * 0.10

  def calculate_net_salary(self):
    gross_salary = self.calculate_gross_salary()
    tax = self.calculate_tax()
    return gross_salary - tax


# Create two employee objects based on the table data
emp1 = Employee("FA/STAFF/256", "Boneface", 50000, 10)
emp2 = Employee("FA/STAFF/690", "Adrian", 65000, 6)

# Display Employee 1 details
print(f"Employee: {emp1.name} ({emp1.employee_id})")
print(f"Gross Salary: KSh {emp1.calculate_gross_salary():,.2f}")
print(f"Tax (10%): KSh {emp1.calculate_tax():,.2f}")
print(f"Net Salary: KSh {emp1.calculate_net_salary():,.2f}\n")

# Display Employee 2 details
print(f"Employee: {emp2.name} ({emp2.employee_id})")
print(f"Gross Salary: KSh {emp2.calculate_gross_salary():,.2f}")
print(f"Tax (10%): KSh {emp2.calculate_tax():,.2f}")
print(f"Net Salary: KSh {emp2.calculate_net_salary():,.2f}")
