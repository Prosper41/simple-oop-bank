from bank_accounts import *

Prosper = BankAccount(2000, "Prosper")
Asaa = BankAccount(2700, "Asaa") 

Prosper.getBalance()
Asaa.getBalance()


Prosper.deposit(19000)
Prosper.deposit(190.982)

Prosper.withdraw(122)
Prosper.transfer(2000000, Asaa)

Prosper.transfer(200, Asaa)

King = InterestRewardAcct(1000, 'King')
King.getBalance()
King.deposit(100)

King.transfer(100, Asaa)

Rich = SavingsAcct(1000, 'Rich')
Rich.getBalance()
Rich.deposit(100)
Rich.transfer(10, Prosper)