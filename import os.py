import os
import datetime 
# Global variables 
MIN_SAVINGS_BALANCE = 100 
MIN_CURRENT_BALANCE = 500
# Function to display the main menu 
def display_menu(): 
    print("Welcome to the Pragratee Banking Service System") 
    print("1. You can Login") 
    print("2. You can Exit") 
    choice = input("Enter your choice -> : ") 
    return choice 
# Function for customer login 
def customer_login(): 
    account_number = input("Enter your account number please: ") 
    password = input("Enter your password please: ") 
    if os.path.exists("customer_account_hehe.txt"): 
         with open("customer_accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == account_number and data[2] == password:
                    print("Login successful!Hoorayy")
                    return True
            print("Invalid account number or password. Please try again. Hax!!")
            return False
    else:
        print("No customer accounts found. Please register first. Yeah realy quick my man")
        return False
# Function for deposit transaction
def deposit_transaction(account_number):
    amount = float(input("Enter the amount to deposit here:heehh "))
    # Validate if the amount is positive
    if amount <= 0:
        print("Invalid amount. Please enter a positive value here.")
        return
    # Check if the account exists
    if os.path.exists("customer_accounts_hehe.txt"):
        with open("customer_accounts_hehe.txt", "r") as file:
            lines = file.readlines()
        with open("customer_accounts_hehe.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == account_number:
                    current_balance = float(data[3])
                    new_balance = current_balance + amount
                    file.write(f"{data[0]},{data[1]},{data[2]},{new_balance}\n")
                    print(f"Deposit successful! Rich man Current balance: {new_balance}")
                else:
                    file.write(line)
    else:
        print("No customer accounts found Damn make a new one.")
# Function for withdrawal transaction
def withdrawal_transaction(account_number, account_type):
    amount = float(input("Enter the amount to withdraw Rich kid party: "))
    # Validate if the amount is positive
    if amount <= 0:
        print("Invalid amount. Please enter a positive value please.")
        return
    # Validate if the account exists
    if os.path.exists("customer_accounts_hehe.txt"):
        with open("customer_accounts_hehe.txt", "r") as file:
            lines = file.readlines()
        with open("customer_accounts_hehe.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == account_number:
                    current_balance = float(data[3])
                    if account_type == "Savings" and current_balance - amount < MIN_SAVINGS_BALANCE:
                        print("Withdrawal amount exceeds minimum balance for Savings account.Poor.")
                        return
                    elif account_type == "Current" and current_balance - amount < MIN_CURRENT_BALANCE:
                        print("Withdrawal amount exceeds minimum balance for Current account.Poor.")
                        return
                    else:
                        new_balance = current_balance - amount
                        file.write(f"{data[0]},{data[1]},{data[2]},{new_balance}\n")
                        print(f"Withdrawal successful! Party? Current balance: {new_balance}")
                else:
                    file.write(line)
    else:
        print("No customer accounts found.Make a new one i guess")
# Function to generate customer statement of account
def generate_statement(account_number):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    # Validate date format
    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return
    # Validate if start date is before end date
    if start_date > end_date:
        print("Start date cannot be after end date.")
        return
    # Check if the account exists
    if os.path.exists("customer_accounts.txt"):
        with open("customer_accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == account_number:
                    transactions = []
                    with open("customer_transactions.txt", "r") as transaction_file:
                        for transaction_line in transaction_file:
                            transaction_data = transaction_line.strip().split(",")
                            trans_date = datetime.datetime.strptime(transaction_data[1], "%Y-%m-%d")
                            if trans_date >= start_date and trans_date <= end_date:
                                transactions.append(transaction_data)
                    print(f"Statement of Account for Account Number: {account_number}")
                    print("Transaction Date\tType\tAmount")
                    total_deposit = 0
                    total_withdrawal = 0
                    for transaction in transactions:
                        print(f"{transaction[1]}\t{transaction[2]}\t{transaction[3]}")
                        if transaction[2] == "Deposit":
                            total_deposit += float(transaction[3])
                        elif transaction[2] == "Withdrawal":
                            total_withdrawal += float(transaction[3])
                    print(f"Total deposits: {total_deposit}")
                    print(f"Total withdrawals: {total_withdrawal}")
                    return
        print("Account number not found.")
    else:
        print("No customer accounts found.")
# Example usage:
# generate_statement("1234567890")
# Function to update customer password
def update_password(account_number):
    new_password = input("Enter your new password: ")
        # Check if the account exists
    if os.path.exists("customer_accounts.txt"):
        with open("customer_accounts.txt", "r") as file:
            lines = file.readlines()

        with open("customer_accounts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == account_number:
                    file.write(f"{data[0]},{data[1]},{new_password},{data[3]}\n")
                    print("Password updated successfully!")
                else:
                    file.write(line)
    else:
        print("No customer accounts found.")
# Example usage:
# update_password("1234567890")
# Function to validate minimum balance
def validate_balance(account_type, amount):
    # Define minimum balance for each account type
    min_balance = MIN_SAVINGS_BALANCE if account_type == "Savings" else MIN_CURRENT_BALANCE

    # Check if the withdrawal amount will result in a balance below the minimum balance
    if amount < min_balance:
        print(f"Withdrawal amount is below minimum balance for {account_type} account.")
        return False
    else:
        return True
# Example usage:
# validate_balance("Savings", 50)
# Main function
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            customer_login()
        elif choice == '2':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()