class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialamount, accName):
        self.balance = initialamount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${
              self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance ${self.balance:.2f} ")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.\nAccount '{
              self.name}' balance ${self.balance:.2f} ")
        self.getBalance()

    def viablieTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${
                    self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viablieTransaction(amount)
            self.balance = self.balance - amount
            print('withdraw completed.')
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transfer...🚀')
            self.viablieTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✔️\n\n***********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌')
            {error}

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.055)
        print("\nDeposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialamount, accName):
        super().__init__(initialamount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viablieTransaction(amount+self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")


