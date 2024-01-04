#ABC Banking System
class Bank:
    def __init__(self):
        # Use a dictionary to store account details,
         # key is the account number and the value are account holder name and initial balance for exsisting customer
        self.accounts = {100100: {'name': 'Anu', 'balance': 500.00},100101: {'name': 'Nimi', 'balance': 1000.00}}
    #login Session
    def login(self, accountno, name):
        if accountno in self.accounts and name == self.accounts[accountno]['name']:
            print("\033[1;36m"+"Welcome to ABC Banking System",name +"\033[0m")
            return True
        else:
            print("Sorry, Account not found. Creating a new account with ABC banking.")
            self.create_account(accountno, name)
            return True

    #Account Creation if login failed
    def create_account(self, accountno, name):
        if accountno not in self.accounts:
            try:
                initial_balance = float(input("Enter initial balance for the new account: "))
                self.accounts[accountno] = {'name': name, 'balance': initial_balance}
            except ValueError:
                print("Invalid Amount . Please Enter a Correct Amount ")
                exit()

            print("\033[1;36m"+"Account created successfully".center(80)+ "\033[0m""\n")
            print("\033[1m"+f"Your Account Number:{accountno}\nName:{name}\nInitial balance: {initial_balance}\n")
            return self.accounts[accountno]
        else:
            print("Account already exists with the same Account Number.Try Again.")
            print("Thank you")
            exit()
    #Deposit Amount After Login
    def deposit(self, accountno, amount):
        if accountno in self.accounts:
            try:
                if amount<=0:
                    print("\033[1;36m" + "Invalid amount. Please enter a valid amount" + "\033[0m""\n")
                    return True
                self.accounts[accountno]['balance'] += amount
                print(f"Amount {amount} deposited successfully.\nNew balance: {self.accounts[accountno]['balance']}.\n")
                print("\033[1;36m"+"Thank you for choosing ABC Banking System"+ "\033[0m""\n")
            except ValueError:
                print("Invalid Amount . Please Enter a Correct Amount ")
        else:
            print("Account not found. Please log in first.")
    #Withdraw Amount
    def withdraw(self, accountno, amount):
        if accountno in self.accounts:
            try:
                if amount<=0:
                    print("\033[1;36m" + "Invalid amount. Please enter a valid amount" + "\033[0m""\n")
                    return True
                if self.accounts[accountno]['balance'] >= amount:
                    self.accounts[accountno]['balance'] -= amount
                    print(f"Transaction of {amount} successful.\nNew balance: {self.accounts[accountno]['balance']}.\n")
                    print("\033[1;36m" + "Thank you for choosing ABC Banking System" + "\033[0m""\n")
                else:
                    print("Insufficient fund.")
                    print("\033[1;36m" + "Thank you for choosing ABC Banking System" + "\033[0m""\n")
            except ValueError:
                print("Invalid Amount . Please Enter a Correct Amount ")
        else:
            print("Account not found. Please log in first.")
    #Display Account Details
    def display(self,accountno,name):
        #print("ABC Banking System".center(80))
        print(f"Welcome  {name} \n Available Balance is {self.accounts[accountno]['balance']}")
        print("\033[1;36m" + "Thank you for choosing ABC Banking System" + "\033[0m""\n")

#Create a Bank Class Object
bank = Bank()
# Login or create account
print("\033[1;41m"+"******ABC Banking System******".center(80)+ "\033[0m")
print("\033[1m"+"Please Login for continue"+"\033[0m")
try:
    user_account_number = int(input("\033[1m"+"Enter your account number:"))
except ValueError:
    print("Invalid Account Number Format . Please Enter a Valid Number ")
    exit()
user_account_name = input("Enter your name:")
bank.login(user_account_number, user_account_name)
# Take user input for choosing a method
try:
    choice = int(input("\033[1m"+"Choose an option (1: Deposit, 2: Withdraw, 3: Display Account Details, 4: exit): "))
except ValueError:
    print("Invalid Choice . Please Enter a Valid Choice ")
    exit()
if choice==1:
    # Deposit Amount
    try:
        deposit_amount = float(input("Enter the amount to deposit:"))
    except ValueError:
        print("Invalid  Amount format . Please Enter a Valid Amount ")
        exit()
    bank.deposit(user_account_number, deposit_amount)

elif choice==2:
    try:
        withdraw_amount = float(input("Enter the amount to withdraw:"))
    except ValueError:
        print("Invalid Amount format . Please Enter a Valid Amount ")
        exit()
    bank.withdraw(user_account_number, withdraw_amount)
elif choice==3:
    bank.display(user_account_number,user_account_name)
elif choice==4:
    exit()
else:
    print("Thank you for Visiting ABC Banking System. Please Enter Valid Option")