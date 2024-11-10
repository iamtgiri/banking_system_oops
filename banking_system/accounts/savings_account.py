class SavingsAccount:
    """
    Represents a savings account with balance, interest rate and basic deposit/withdraw functionality.
    """

    def __init__(self, account_number: str, account_holder: str, balance: float, interest_rate: float):
        """
        Initializes the savings account with account number, holder's name, balance and interest rate.
        """
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__interest_rate = interest_rate

    def deposit(self, amount: float):
        """
        Increases balance by the deposit amount if it is positive.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount: float):
        """
        Decreases balance by the withdraw amount if funds are sufficient.
        """
        if amount <= 0:
            print("Invalid amount.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        """
        Returns the interest earned on the current balance.
        """
        return self.__balance * self.__interest_rate / 100

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_holder(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance
