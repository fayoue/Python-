# Basic class
class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    # Method to display personal details
    def display_details(self):
        print("Person ID:", self.person_id)
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class Student
class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)
        self.course = course
        self.marks = marks

    
    def calculate_grade(self):
        if self.marks >= 70:
            return "Grade A"
        elif self.marks >= 60:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Grade D"

    
    def display_details(self):
        super().display_details()
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())

# Derived class Lecturer
class Lecturer(Person):
    def __init__(self, person_id, name, age, department, monthly_salary):
        super().__init__(person_id, name, age)
        self.department = department
        self.monthly_salary = monthly_salary

   
    def calculate_annual_salary(self):
        return self.monthly_salary * 12

   
    def display_details(self):
        super().display_details()
        print("Department:", self.department)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.calculate_annual_salary())


# Create Student object
student1 = Student(97845, "Faith", 21, "Information Technology", 75)

# Create Lecturer object
lecturer1 = Lecturer(6871, "Daniel", 35, "Computer Science", 50000)



print("----- STUDENT DETAILS -----")
student1.display_details()

print("\n----- LECTURER DETAILS -----")
lecturer1.display_details()
