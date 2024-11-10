from banking_system.accounts import SavingsAccount, CheckingAccount

class Transaction:
    """
    Represents a financial transaction on a bank account with a type of "withdraw" or "deposit".
    """

    def __init__(self, transaction_id, account, amount, transaction_type):
        """
        Initializes a transaction with an ID, associated account, amount, and type.
        """
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def execute(self):
        """
        Executes the transaction by calling the appropriate method on the associated account.
        """
        if self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        elif self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        else:
            print("Error! Could not recognize transaction type.")
