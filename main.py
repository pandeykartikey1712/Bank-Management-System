from bank import Bank
import bank

def main():
    while True:
        print("Welcome to the Bank Management System")
        print("1. Create a new account")
        print("2. Log into existing account")

        option = input("Select an option (1 or 2): ")
        if option == '1':
            # Create a new account
            username = input("Enter your username: ")
            account_number = input("Enter your account number: ")
            balance = float(input("Enter initial balance: "))
            account_type = input("Enter account type (Saving/Current): ")
            password = input("Create your password: ")
            # Create an instance of Bank class
            bank = Bank(username, account_number, balance, account_type, password)
            print("Account created successfully!")

        
        elif option == '2':
            # Log into an existing account
            username = input("Enter your username: ")
            password = input("Enter your password: ")

    # Authenticate user (Assume there's a method to verify username and password)
            authenticated = bank.verify_pass(password)
            if authenticated:
                print("Login successful!")
                # Call the main menu for further operations
                bank_main_menu(bank)
            else:
                print("Login failed. Please try again.")

    else:
        print("Invalid option. Please select either 1 or 2.")
        

def bank_main_menu(bank):
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. Exit")
        option = input("Select an option: ")

        if option == '1':
            print(f"Your current balance is: {bank.balance_enquiry()}")
            
        elif option == '2':
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(amount)
            print(f"Deposited {amount} successfully.")

        elif option == '3':
            amount = float(input("Enter amount to withdraw: "))
            if bank.verify_pass(input("Re-enter your password: ")):
                bank.withdraw(amount)

        elif option == '4':
            recipient_account = input("Enter recipient account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(recipient_account, amount)

        elif option == '5':
            print("Thank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()