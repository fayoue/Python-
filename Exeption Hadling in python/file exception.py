try:
    file = open("employees.txt", "r")
    contents = file.read()

    print(contents)
    file.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
