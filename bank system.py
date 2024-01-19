
from random import randint
# create an account holder class
# create an account number generator using random and randint

class AccountHolder:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
    
    def __str__(self):
        return "Name: " + self.name + "\nID: " + self.id + "\nAddress: " + self.address
    
    
        
class BankAccount:
    def __init__(self, accountHolder:AccountHolder, balance= None):
        self.accountHolder = accountHolder
        if balance == None:
            self.balance = 0
        else:
            self.balance = balance
        self.accountNumber = self.accountNumberGenerator()
        self.save_details()
    
    def __str__(self):
        return str(self.accountHolder) + "\nAccount Number: " + self.accountNumber + "\nBalance: R" + str(float(self.balance))
    
    def accountNumberGenerator(self):
        characters = "0123456789"
        number = ""
        for i in range(3):
            number+= characters[randint(0, 9)]
        for i in range(5):
            number+= characters[randint(5, len(characters) - 1)]
        for i in range(2):
            number+= characters[randint(0, 4)]
        return number
    
    def save_details(self):
        with open("database.txt", "a+") as f:
            f.write(self.__str__() + "\n")
            f.write("--------------------------" + "\n")
            
    def deposit(self, amount):
        self.balance += float(amount)
        print(f"deposited R{amount} into account")
        self.updateBalance()
    
    def getID(self):
        return self.accountHolder.id

    def getName(self):
        return self.accountHolder.name
        
    def withdraw(self, amount):
        if self.balance <= 0 or self.balance <= float(amount):
            print("Unable to withdraw. Balance is too low")
        else:
            self.balance -= float(amount)
            print(f"withdrew R{amount} from account")
            self.updateBalance()
            
    def updateBalance(self):
        with open("database.txt", "r") as f:
            contents = f.read()
            accounts = contents.split("--------------------------\n")
        with open("database.txt", "w") as f:    
            accounts_to_write = []
            for account in accounts:
                if self.accountNumber in account:
                    accounts_to_write.append(account[:(account.find("Balance: R") + 10)] + str(self.balance) + "\n")
                else:    
                    accounts_to_write.append(account)
            f.write("--------------------------\n".join(accounts_to_write))
                                
                    
def main():
    bank_accounts = []
    print("Welcome to the Totally Ethical Bank System.")
    while True:
        mode = input(f"Create account(A)\nQuit(Q)\nList accounts(ls)\nLogin(E): \n").lower().strip()
        if mode == "a":
            input_name = input('Enter name: ')            
            input_id = input('Enter id: ')            
            input_address= input('Enter address: ')
            bankAccount = BankAccount(AccountHolder(input_name, input_id, input_address))
            bank_accounts.append(bankAccount)
        elif mode == "q":
            with open("database.txt", "w") as f:
                f.write("")
            print("Thank you for using the system")
            break
        elif mode == "ls":
            if len(bank_accounts) > 0:
                print()
                for account in bank_accounts:
                    print(str(account) + "\n")
            else:
                print("No accounts")
        elif mode == "e":
            input_id = input("Enter id to login into your account: ")
            for account in bank_accounts:
                if account.getID() == input_id:
                    print(f"Welcome back {account.getName()}! \nAvailable Options: \ndeposit \'amount\' \nwithdraw \'amount\'")
                    print()
                    while True:
                        transactionType = input().lower().strip().split(" ")
                        if transactionType[0] == "deposit":
                            account.deposit(transactionType[1])
                            transactAgain = input("Would you like to transact again: ").lower()
                            if transactAgain == "y":
                                continue
                            else:   
                                break                
                        elif transactionType[0] == "withdraw":
                            account.withdraw(transactionType[1])
                            transactAgain = input("Would you like to transact again: ").lower()
                            if transactAgain == "y":
                                continue
                            else:   
                                break    
                        elif transactionType[0] == "help":   
                            print("Available actions: \ndeposit \'amount\' \nwithdraw \'amount\'")     
                        else:
                            print("Invalid input!The available actions are \'deposit\' or \'withdraw\'. Otherwise enter \'help\'")
                    break
        else:
            continue                    
    
    
main()