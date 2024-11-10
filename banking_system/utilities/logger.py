from ..transactions import Transaction
import datetime

def log_transaction(transaction):
    """
    Logs transaction details to a file named 'transaction_log.txt'.
    
    Args:
        transaction (Transaction): The transaction object to log.
    """
    with open("transaction_log.txt", 'a') as file:
        text = f"""--------------------------------------------------------------
                Transaction Log Entry
--------------------------------------------------------------
Transaction ID        : {transaction.transaction_id}
Account Holder        : {transaction.account.account_holder} 
Account Number        : {transaction.account.account_number}
Transaction Type      : {transaction.transaction_type}
Amount                : {transaction.amount}
Transaction Date      : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
--------------------------------------------------------------
"""
        file.write(text)
