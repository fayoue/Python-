
# Create a list containing five subject marks
marks = [78, 85, 67, 90, 72]

# Display all marks
print("Student marks:", marks)

# Calculate and display total marks
total = sum(marks)
print("Total marks:", total)

# Calculate and display average mark
average = total / len(marks)
print("Average mark:", average)

# Display highest and lowest marks
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

# Modify the mark of the third subject
marks[2] = 75

# Display the updated list
print("Updated marks:", marks)
