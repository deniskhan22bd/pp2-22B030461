class Account:
    owner = None
    balance = None

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("Now is {}".format(self.balance))
    
    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
            print("Left {}".format(self.balance))
        else:
            print("Error you have only {}".format(self.balance))

x1 = Account("Denis", 10000)
x2 = Account("Luna", 50000)

x1.withdraw(100)
x1.deposit(10005)
x2.withdraw(500000)

