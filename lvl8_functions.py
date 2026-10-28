class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.00

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def make_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def view_account_info(self):
        return {
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance
        }

    def quit_account(self):
        return True
    
def handle_deposit(account):
    while True:
        user_input = input("How much would you like to deposit? ")
        try:
            deposit_amount = float(user_input)
            if account.make_deposit(deposit_amount):
                print(f"Deposit successful. Current balance: ${account.balance:.2f}")
                break
            else:
                print("Invalid amount. Deposit must be greater than $0.00. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 50 or 25.50).")

def handle_withdrawal(account):
    while True:
        user_input = input("Enter the amount to withdraw: ")
        try:
            withdrawal_amount = float(user_input)
            if account.make_withdrawal(withdrawal_amount):
                print("Withdrawal successful. Current balance: ${:.2f}".format(account.balance))
                break
            else:
                print("Withdrawal failed. Insufficient funds. Current balance: ${:.2f}".format(account.balance))
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 50 or 25.50).")

def handle_view_account_info(account):
    account_info = account.view_account_info()
    print("Customer Name: {}".format(account_info["name"]))
    print("Account Number: {}".format(account_info["account_number"]))
    print("Current Balance: ${:.2f}".format(account_info["balance"]))

def handle_quit_account(account):
    account.quit_account()
