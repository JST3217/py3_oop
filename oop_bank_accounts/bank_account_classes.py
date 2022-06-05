import uuid
import random


class Account:
    sort_code: int = 40004
    sort_code_display: str = str(sort_code).zfill(6)

    def __init__(self, name: str):
        self.account_type = "Basic Account"
        print(f'creating {self.account_type}...')
        self.name = name
        self.account_number = AccountNumberGenerator().account_number
        self.balance = 0.00
        print(f'{self.account_type} created for {self.name} \n')

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'  Sort code: {self.sort_code_display} \n' \
               f'  Account number: {self.account_number} \n' \
               f'  Account type: {self.account_type} \n' \
               f'  Current balance: £{self.balance} \n'

    def debit(self, debit_amount: float):
        transaction_type = "debit"
        if Verification(self, transaction_type, debit_amount).result.is_verified:
            print('Adding money...')
            print(f'Current balance: £{self.balance}')
            self.balance += debit_amount
            print(f'New balance: £{self.balance}\n')

    def credit(self, credit_amount: float):
        transaction_type = "credit"
        if Verification(self, transaction_type, credit_amount).result.is_verified:
            print('Withdrawing money...')
            print(f'Current balance: £{self.balance}')
            self.balance -= credit_amount
            print(f'New balance: £{self.balance}\n')


class MinimumBalanceAccount(Account):
    def __init__(self, name: str, minimum_balance: float):
        super().__init__(name)
        self.account_type = "Minimum Balance Account"
        print(f'configuring account into {self.account_type}...')
        super().debit(minimum_balance)
        self.minimum_balance = minimum_balance
        print(f'{self.account_type} created for {self.name} \n')


class OverdraftAccount(Account):
    def __init__(self, name: str, overdraft_allowance: float):
        super().__init__(name)
        self.account_type = "Overdraft Account"
        print(f'configuring account into {self.account_type}...')
        self.overdraft_allowance = overdraft_allowance
        print(f'{self.account_type} created for {self.name} \n')


class AccountNumberGenerator:
    def __init__(self):
        randomiser = random.randint(0, 25)
        self.account_number = str(int(uuid.uuid4()))[randomiser:randomiser + 8]  # Generate unique account numbers


class Results:
    def __init__(self, message: str):
        self.message = message
        self.is_verified = None


class VerificationFailed(Results):
    def __init__(self, message: str):
        super().__init__(message)
        self.is_verified = False


class VerificationPassed(Results):
    def __init__(self, message: str):
        super().__init__(message)
        self.is_verified = True


class Verification:
    def __init__(self, obj: (Account, MinimumBalanceAccount, OverdraftAccount), transaction_type: str, amount: float):
        print(f'Verifying {transaction_type} request...')
        self.result = None

        if not isinstance(amount, (int, float)):
            self.result = VerificationFailed('   invalid format input \n')

        elif amount < 0:
            self.result = VerificationFailed('   invalid sign input \n')

        elif transaction_type == "credit":
            if isinstance(obj, MinimumBalanceAccount) and (obj.balance - amount < obj.minimum_balance):
                self.result = VerificationFailed('   withdrawal exceed minimum balance threshold\n')

            elif isinstance(obj, OverdraftAccount) and (obj.balance - amount < -obj.overdraft_allowance):
                self.result = VerificationFailed('   withdrawal exceed overdraft allowance\n')

            elif type(obj) != OverdraftAccount and (obj.balance - amount) < 0:
                self.result = VerificationFailed('   insufficient funds\n')

        if self.result is None:
            self.result = VerificationPassed('request verified...')

        print(f'{self.result.message}')
