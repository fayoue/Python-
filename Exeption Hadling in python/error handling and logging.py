
import logging

# Configure logging to save errors in a file
logging.basicConfig(
    filename="bank_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define a custom exception
class InsufficientFundsError(Exception):
    pass


# Banking withdrawal function
def withdraw_money(balance):

    try:
        # Ask user to enter withdrawal amount
        amount = float(input("Enter amount to withdraw: KSh "))

        # Check if withdrawal amount is positive
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Check if there is enough money
        if amount > balance:
            raise InsufficientFundsError(
                "Insufficient funds in your account."
            )

    except ValueError as e:
        print("Invalid input:", e)
        logging.error("ValueError: %s", e)

    except InsufficientFundsError as e:
        print(e)
        logging.error("InsufficientFundsError: %s", e)

    else:
        # Execute when no exception occurs
        balance = balance - amount

        print("Withdrawal successful!")
        print("Amount withdrawn: KSh", amount)
        print("Remaining balance: KSh", balance)

    finally:
        # Always execute
        print("Thank you for using our banking service. Goodbye!")


# Main program
account_balance = 10000

print("Welcome to the Banking Application")
print("Account balance: KSh", account_balance)

withdraw_money(account_balance)
