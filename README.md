# Bank Account Management System

This is a simple bank account management system implemented in Python. The program allows users to make deposits and withdrawals, view their account balance, and view a transaction log.

## Usage

1. Run the program by executing `python main.py` in the command line.
2. Choose an action from the menu by entering a number between 1 and 5.
3. Follow the prompts to complete the chosen action.

## Classes

### `BankAccount`

This class represents a bank account and has the following methods:

- `__init__(self, name, balance)`: Initializes the `BankAccount` object with a name and balance.
- `deposit(self, amount)`: Deposits the specified amount into the account.
- `withdraw(self, amount)`: Withdraws the specified amount from the account, if possible.
- `__str__(self)`: Returns a string representation of the account name and balance.

### `TransactionLog`

This class represents a transaction log and has the following methods:

- `__init__(self, name)`: Initializes the `TransactionLog` object with a name.
- `add_transaction(self, date, amount)`: Adds a transaction to the log with the specified date and amount.
- `write_to_file(self)`: Writes the transaction log to a text file.
- `__str__(self)`: Returns a string representation of the transaction log.

## Contributing

Feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
