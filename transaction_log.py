import datetime

# Function to log a transaction
def log_transaction(account_number, remarks, amount):
    transaction = {
        "timedate": str(datetime.datetime.now()),
        "account_number": account_number,
        "remarks": remarks,
        "amount": amount
}
    print(f"Transaction logged: {transaction}")
    return transaction