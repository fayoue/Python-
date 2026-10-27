class BankAccount:

  def __init__(self, account_number, balance, date_of_opening, customer_name):
    self.account_number = account_number
    self.balance = balance
    self.date_of_opening = date_of_opening
    self.customer_name = customer_name

  def deposit(self, amount):
    self.balance += amount
    return amount  # Returns the amount deposited

  def withdraw(self, amount):
    if self.balance < amount:
      return "insufficient balance"
    else:
      self.balance -= amount
      return amount  # Returns the amount that has been withdrawn

  def check_balance(self):
    print(f"Current Balance: {self.balance}")

  def customer_details(self):
    print(f"Customer Name: {self.customer_name}")
    print(f"Account Number: {self.account_number}")
    print(f"Date of Opening: {self.date_of_opening}")
    print(f"Balance: {self.balance}")


# Example usage:
acc = BankAccount("Equitry", 20000, "2025-01-15", "Rael peterson")
acc.customer_details()
print("Deposited:", acc.deposit(1500))
print("Withdrawn:", acc.withdraw(2000))
acc.check_balance()
