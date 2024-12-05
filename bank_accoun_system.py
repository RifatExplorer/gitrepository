class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited.New balance is:{self.balance} ")

    def withdrawls(self,amount):
        if self.balance < amount:
            print(f"Insufficiant funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaing balance :{self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Courrent Balance: {self.balance}")

name =input('Enter Account Holder Name: ')
account =BankAccount(name)

print(" ")
print("***************************")
print("If you want to Diposit please enter  D :")
print("If you want to withdraw please enter W :")
print("If you want to cheack your current balance please enter CB :")
print("****************************")
print(" ")

while True:
    a = input("How can i help you today? ")
    if a == 'D':
        amount = int(input("Enter amount to diposit: "))
        account.deposit(amount)
    elif a == 'W':
        amount = int(input("Enter ammount to withdraw: "))
        account.withdrawls(amount)
    elif a == 'CB':
        account.display_balance()
    else:
        break

print("Thanks! Stay with us")
print(" ")
    
        