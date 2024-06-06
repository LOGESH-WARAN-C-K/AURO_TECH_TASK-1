# AURO_TECH_TASK 1

Here's a more detailed `README.md` file for your ATM interface project, covering all aspects thoroughly :

```markdown
# ATM Interface

This project is a console-based ATM interface implemented in Python. It allows users to perform various banking operations such as creating accounts, logging in, depositing funds, withdrawing funds, transferring funds, and viewing transaction history.

## Features

- **Create Account**: Create a new account with a unique user ID and PIN.
- **Login**: Secure login using user ID and PIN.
- **Deposit**: Add money to your account.
- **Withdraw**: Remove money from your account, subject to sufficient balance.
- **Transfer**: Send money to another user's account.
- **View Balance**: Check your current account balance.
- **View Transactions**: See the history of all transactions on your account.

## Classes Overview

### Account Class

Represents a single user's bank account.

- **Attributes**:
  - `user_id`: The unique identifier for the account.
  - `pin`: The PIN used for authentication.
  - `balance`: The current balance of the account.
  - `transactions`: A list of all transactions associated with the account.
  
- **Methods**:
  - `deposit(amount)`: Adds the specified amount to the balance.
  - `withdraw(amount)`: Deducts the specified amount from the balance if funds are sufficient.
  - `transfer(amount, recipient_account)`: Transfers the specified amount to another account if funds are sufficient.
  - `get_balance()`: Returns the current balance.
  - `get_transactions()`: Returns the transaction history.

### Bank Class

Manages multiple accounts.

- **Attributes**:
  - `accounts`: A dictionary of user IDs to `Account` objects.
  
- **Methods**:
  - `create_account(user_id, pin)`: Creates a new account with the specified user ID and PIN.
  - `get_account(user_id)`: Retrieves the account associated with the specified user ID.

### ATM Class

Handles the main ATM functionalities.

- **Attributes**:
  - `bank`: The `Bank` instance managing the accounts.
  - `current_account`: The account currently logged in.
  
- **Methods**:
  - `login(user_id, pin)`: Authenticates and logs in a user.
  - `logout()`: Logs out the current user.
  - `deposit(amount)`: Deposits an amount to the logged-in account.
  - `withdraw(amount)`: Withdraws an amount from the logged-in account.
  - `transfer(amount, recipient_user_id)`: Transfers an amount to another account.
  - `show_balance()`: Displays the current balance of the logged-in account.
  - `show_transactions()`: Displays the transaction history of the logged-in account.

### UserInterface Class

Handles user interaction.

- **Attributes**:
  - `atm`: The `ATM` instance that handles the functionalities.
  
- **Methods**:
  - `display_menu()`: Displays the menu options.
  - `run()`: Runs the main loop to interact with the user.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/atm-interface.git
    ```
2. Navigate to the project directory:
    ```bash
    cd atm-interface
    ```

## Usage

To run the ATM interface, execute the following command:
```bash
python atm_interface.py
```

### Menu Options

Upon running the program, you will be presented with the following menu:

```
1. Create account
2. Login
3. Deposit
4. Withdraw
5. Transfer
6. Show balance
7. Show transactions
8. Quit
```

#### Creating an Account

- Select option `1` to create a new account.
- Enter a unique user ID and a PIN when prompted.
- The account will be created if the user ID is not already taken.

#### Logging In

- Select option `2` to log in.
- Enter your user ID and PIN when prompted.
- You will be logged in if the credentials are correct.

#### Depositing Money

- Select option `3` to deposit money.
- Enter the amount you wish to deposit.
- The amount will be added to your account balance.

#### Withdrawing Money

- Select option `4` to withdraw money.
- Enter the amount you wish to withdraw.
- The amount will be deducted from your account balance if you have sufficient funds.

#### Transferring Money

- Select option `5` to transfer money to another account.
- Enter the amount and the recipient's user ID.
- The amount will be transferred if you have sufficient funds and the recipient's account exists.

#### Viewing Balance

- Select option `6` to view your current balance.

#### Viewing Transactions

- Select option `7` to view your transaction history.

#### Quitting

- Select option `8` to log out and quit the program.

## Example Usage

```
1. Create account
2. Login
3. Deposit
4. Withdraw
5. Transfer
6. Show balance
7. Show transactions
8. Quit

Enter choice: 1
Enter user ID: user1
Enter PIN: 1234
Account created for user user1.

Enter choice: 2
Enter user ID: user1
Enter PIN: 1234
Login successful.

Enter choice: 3
Enter amount to deposit: 1000
Deposited 1000. New balance is 1000.0.

Enter choice: 6
Current balance: 1000.0

Enter choice: 7
('Deposit', 1000, datetime.datetime(2024, 6, 6, 12, 0, 0))

Enter choice: 8
Logged out.
Thank you for using the ATM.
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is built using Python and is inspired by basic banking operations.
```

This `README.md` file provides a comprehensive overview of your ATM interface project, including setup instructions, usage details, class explanations, and an example usage scenario. Replace `https://github.com/your-username/atm-interface.git` with the actual URL of your GitHub repository.
