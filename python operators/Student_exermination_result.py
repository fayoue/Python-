# Student Examination Results

student_name = input("Enter student name: ")
coursework_mark = float(input("Enter coursework mark out of 30: "))
examination_mark = float(input("Enter examination mark out of 70: "))

# Calculate total mark
total_mark = coursework_mark + examination_mark

# Determine whether the student has passed
passed = total_mark >= 40

# Display results
print("\nStudent Examination Results")
print("Student Name:", student_name)
print("Coursework Mark:", coursework_mark)
print("Examination Mark:", examination_mark)
print("Total Mark:", total_mark)
print("Passed:", passed)
