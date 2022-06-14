from bank_account_classes import *


def sample_setup():
    """
    The sample_setup function creates 3 different types of accounts

    return: 3 different accounts as objects
    """
    x = Account("Jia Sheng")
    y = MinimumBalanceAccount("Bess Yu", 100)
    z = OverdraftAccount("Jia Min", 50)

    return [x, y, z]


def sample_transactions():
    """
    The sample_transactions function simulates a day of transactions.
    It creates an account and then calls the debit and credit methods to
    simulate money coming in and going out of the account.

    return: account as objects after sample transactions
    """
    for __ in accounts:
        __.debit(50)
        __.credit(75)
        print(__)
    return accounts


accounts = sample_setup()
accounts = sample_transactions()
