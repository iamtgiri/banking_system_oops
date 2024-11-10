
# Banking System Python Package

This repository contains a Python-based **Banking System** package designed to simulate basic banking operations, including account management, transaction processing, and logging. The package is organized into three main sub-packages: **accounts**, **transactions**, and **utilities**.

## Package Structure

- **accounts**: Contains classes for different types of bank accounts:
  - **SavingsAccount**: Allows deposits, withdrawals, and interest calculations.
  - **CheckingAccount**: Supports deposits, withdrawals, and overdraft protection.
  
- **transactions**: Defines a `Transaction` class that handles financial transactions (deposit and withdrawal) on bank accounts. Transactions are executed based on the type (deposit/withdraw).

- **utilities**: Includes utility functions for the project:
  - **log_transaction**: Logs each transaction into a text file, keeping a history of all banking activities.

## How It Works

In the **main.py** script, we demonstrate the creation of instances of **SavingsAccount** and **CheckingAccount**, perform various transactions like deposits and withdrawals, and calculate the interest for a savings account. The transactions are logged, and account balances are updated accordingly.

## Features

- Create and manage **SavingsAccount** and **CheckingAccount**.
- Perform **deposit** and **withdrawal** transactions.
- Log transaction details to a file for record-keeping.
- Calculate **interest** on savings account balances.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iamtgiri/banking_system.git
   ```

2. Navigate to the project folder:
   ```bash
   cd banking_system_oops
   ```

3. Run the main script to simulate transactions:
   ```bash
   python -m banking_system_oops.main
   ```

## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- File handling for transaction logs

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by real-world banking systems for educational purposes.
- Developed as part of an OOP assignment.

