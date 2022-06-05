from bank_account_classes import *

x = Account("Jia Sheng")
y = MinimumBalanceAccount("Bess Yu", 100)
z = OverdraftAccount("Jia Min", 50)

accounts = [x, y, z]
for __ in accounts:
    __.debit(50)
    __.credit(75)
    print(__)
