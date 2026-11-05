try:
    amount = int(input("Enter withdrawal amount: "))
    print("Withdrawal amount:", amount)

except ValueError:
    print("Invalid amount. Please enter a number.")
