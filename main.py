#Create a Python banking program for a customer who wants to manage a simple bank account.
from lvl8_functions import BankAccount, handle_view_account_info, handle_deposit, handle_withdrawal, handle_quit_account
import random

customer_name = input("Enter your name: ")
account = BankAccount(customer_name, str(random.randint(1000000000, 9999999999)))

#The account should begin with a balance of $0.00.
#The customer should be able to:
print("Welcome to your bank account management system. How can I assist you today?")
while True:
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    choice = input("Enter your choice: ")
    #1. Make a deposit
    #When the customer makes a deposit, ask how much money they would like to add to the account.
    if choice == "1":
        handle_deposit(account)
        
    #2. Make a withdrawal
    #When the customer makes a withdrawal, ask how much money they would like to withdraw. The
    #program should not allow the customer to withdraw more money than they currently have in the
    #account.
    elif choice == "2":
        handle_withdrawal(account)
    #3. View account information
    #When the customer chooses to view account information, display: the customer’s name, account
    #number, and current balance.
    elif choice == "3":
        handle_view_account_info(account)
    elif choice == "4":
        #4. Quit
        #When the customer chooses to quit, exit the program.
        handle_quit_account(account)
        break
    else:
        print("Invalid choice. Please try again.")

handle_quit_account(account)
print("Thank you for using the bank account management system.")
exit()   