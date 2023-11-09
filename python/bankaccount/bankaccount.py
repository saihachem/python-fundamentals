class BankAccount:
    accounts=[]
    
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if(self.balance-amount) >= 0:
            self.balance-=amount
        else:
            print("insufficient funds: charging a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self
        

    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings= BankAccount (.05,1000)
checkings= BankAccount (.02,5000)

savings.deposit(50).deposit(100).deposit(200).withdraw(1000).yield_interest().display_account_info()
checkings.deposit(200).deposit(400).withdraw(40).withdraw(20).withdraw(80).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_accounts()

        