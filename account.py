from exceptions import InvalidInputError

# Function to create an account and validate inputs
def create_account():
    try:
        username = input("Enter your username: ")
        account_number = int(input("Enter your account number: "))
        balance = float(input("Enter your initial balance: "))
        if balance < 0:
            raise InvalidInputError("Balance cannot be negative.")
        return username, account_number, balance
    except ValueError:
        raise InvalidInputError("Invalid account details provided. Please check your input.")
