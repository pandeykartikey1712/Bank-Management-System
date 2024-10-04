class InsufficientBalanceError(Exception):
    """Raised when the balance is insufficient for a transaction."""
    def __init__(self, message="Insufficient balance to complete this transaction."):
        self.message = message
        super().__init__(self.message)


class InvalidAmountError(Exception):
    """Raised when the amount entered is invalid (<= 0)."""
    def __init__(self, message="Invalid amount. Please enter a positive number."):
        self.message = message
        super().__init__(self.message)


class InvalidInputError(Exception):
    """Raised when the input is invalid."""
    def __init__(self, message="Invalid input. Please try again."):
        self.message = message
        super().__init__(self.message)
