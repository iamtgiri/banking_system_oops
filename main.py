from banking_system import SavingsAccount, CheckingAccount, Transaction, log_transaction

# Create instances of SavingsAccount and CheckingAccount
savings_account = SavingsAccount("SA12345", "Rajesh Kumar", 50000.0, 5.5)
checking_account = CheckingAccount("CA67890", "Amit Sharma", 20000.0, 5000.0)

# Perform transactions (Deposits and Withdrawals)
deposit_transaction_savings = Transaction("T001", savings_account, 15000, "deposit")
deposit_transaction_savings.execute()
log_transaction(deposit_transaction_savings)

withdraw_transaction_savings = Transaction("T002", savings_account, 10000, "withdraw")
withdraw_transaction_savings.execute()
log_transaction(withdraw_transaction_savings)

deposit_transaction_checking = Transaction("T003", checking_account, 5000, "deposit")
deposit_transaction_checking.execute()
log_transaction(deposit_transaction_checking)

withdraw_transaction_checking = Transaction("T004", checking_account, 7000, "withdraw")
withdraw_transaction_checking.execute()
log_transaction(withdraw_transaction_checking)

# Calculate and display the interest for SavingsAccount
interest_earned = savings_account.calculate_interest()
print(f"Interest earned on Savings Account {savings_account.account_number} is Rs.{interest_earned:.2f}")

# Display account balances after transactions
print(f"Balance of Savings Account {savings_account.account_number}: Rs.{savings_account.balance}")
print(f"Balance of Checking Account {checking_account.account_number}: Rs.{checking_account.balance}")
