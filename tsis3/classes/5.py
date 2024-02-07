class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dmon):
        self.dmon = dmon
        self.balance += self.dmon
        print(f"Your current balance:{self.balance}")
    def withdraw(self,mon):
        self.mon = mon
        enough = True
        self.balance -= self.mon
        if self.balance < 0:
            enough = False
            self.balance += self.mon
            print("You dont have enough money to withdraw!")
        print(f"Your current balance:{self.balance}")
owner = input("Enter owner name: ")
balance = float(input("Enter initial balance: "))  # Assuming balance can be a float
x = Account(owner, balance)
sel = True
while sel == True:
    print("If you want to deposit: -> 1\nIf you want to withdraw: -> 2\nIf you want to exit: -> 3")
    lo = int(input())
    if lo == 1:
        print("How much money do you want to deposit?")
        x.deposit(int(input()))
    elif lo == 2:
        print("How much money do you want to withdraw?")
        x.withdraw(int(input()))
    elif lo == 3:
        sel = False
    else:
        print("please chose 1 , 2 or 3")
        sel = True