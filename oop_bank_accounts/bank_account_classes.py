import uuid
import random


class Account:
    sort_code: int = 40004
    sort_code_display: str = str(sort_code).zfill(6)

    def __init__(self, name: str):
        """
        param self: Refer to the object instance
        param name:str: Store the name of the account holder
        return: The Account object created
        """
        self.account_type = "Basic Account"
        print(f'creating {self.account_type}...')
        self.name = name
        self.account_number = AccountNumberGenerator().account_number
        self.balance = 0.00
        print(f'{self.account_type} created for {self.name} \n')

    def __str__(self):
        """
        The __str__ function is called when the object is converted to a string.
        It returns a formatted string that includes the name, sort code and account number.
        param self: Refer to the object itself
        return: A string representation of the object
        """
        return f'Name: {self.name} \n' \
               f'  Sort code: {self.sort_code_display} \n' \
               f'  Account number: {self.account_number} \n' \
               f'  Account type: {self.account_type} \n' \
               f'  Current balance: £{self.balance} \n'

    def debit(self, debit_amount: float):
        """
        The debit function takes a float as an argument and adds it to the balance.
        It then prints out the current balance.
        param self: Access the properties of the class
        param debit_amount:float: Pass the amount of money to be debited from the account
        return: The current balance
        """
        transaction_type = "debit"
        if Verification(self, transaction_type, debit_amount).result.is_verified:
            print('Adding money...')
            print(f'Current balance: £{self.balance}')
            self.balance += debit_amount
            print(f'New balance: £{self.balance}\n')

    def credit(self, credit_amount: float):
        """
        The credit function allows the user to add money to their account.
        It takes a float as an argument and adds it to the balance.
        param self: Reference the object that is calling the function
        param credit_amount:float: Determine how much money to add to the account
        return: The result of the verification function
        """
        transaction_type = "credit"
        if Verification(self, transaction_type, credit_amount).result.is_verified:
            print('Withdrawing money...')
            print(f'Current balance: £{self.balance}')
            self.balance -= credit_amount
            print(f'New balance: £{self.balance}\n')


class MinimumBalanceAccount(Account):
    def __init__(self, name: str, minimum_balance: float):
        """
        The __init__ function is called the constructor and is always called when creating an instance of a class.
        It sets up all the variables that are part of that object.
        param self: Refer to the object of the class
        param name:str: Set the name of the account holder
        param minimum_balance:float: Set the minimum balance that must be maintained in this account
        :return: An instance of the class
        """
        super().__init__(name)
        self.account_type = "Minimum Balance Account"
        print(f'configuring account into {self.account_type}...')
        super().debit(minimum_balance)
        self.minimum_balance = minimum_balance
        print(f'{self.account_type} created for {self.name} \n')


class OverdraftAccount(Account):
    def __init__(self, name: str, overdraft_allowance: float):
        """
        The __init__ function is called automatically when a new instance of the class is created.
        It sets up all the attributes that are specific to each instance, such as account_type and overdraft_allowance.
        param self: Refer to the instance of the object itself
        param name:str: Specify the name of the account holder
        param overdraft_allowance:float: Set the overdraft allowance for the account
        return: None
        """
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
        """
        The __init__ function is called when an instance of the class is created.
        It initializes attributes that are specific to each object created from the class.
        param self: Refer to the object instance
        param obj: Account: Determine which type of account to use
        param obj: MinimumBalanceAccount: Check if the account has a minimum balance
        param obj: OverdraftAccount: Check if the account is an overdraft account
        param transaction_type:str: Determine whether the transaction is a credit or debit
        param amount:float: Specify the amount of money to be withdrawn or deposited
        return: A verification result object
        """
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
