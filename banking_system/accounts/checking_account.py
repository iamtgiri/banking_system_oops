class CheckingAccount:
    """
    Represents a checking account with overdraft protection.
    """

    def __init__(self, account_number: str, account_holder: str, balance: float, overdraft_limit: float):
        """
        Initializes the checking account with account number, holder, balance and overdraft limit.
        """
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount: float):
        """
        Increases balance by the deposit amount if it is positive.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Rs.{amount} deposited to account {self.__account_number}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount: float):
        """
        Decreases balance by the withdraw amount, checking for overdraft limit.
        """
        if self.__balance - amount < -self.__overdraft_limit:
            print("Transaction declined. Overdraft limit exceeded.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_holder(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
