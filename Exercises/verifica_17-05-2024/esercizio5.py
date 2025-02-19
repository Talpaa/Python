class Account:
    
    def __init__(self,
                 account_id: str,
                 balance: float = 0) -> None:
        
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float):
        
        self.balance += amount

    def get_balance(self):
        
        return f'{self.balance}'

class Bank:
    
    def __init__(self,
                 accounts: dict[str, Account] = {}) -> None:
        
        self.accounts: dict[str, Account] = accounts.copy()

    def create_account(self, account_id: str, amount: float = 0):
        
        if account_id in self.accounts:

            raise ValueError(f'Account with this ID already exists')
        else:
            self.accounts[account_id] = amount
            return Account(account_id, amount)

    def deposit(self, account_id, amount):

        self.accounts[account_id] += amount

    def get_balance(self, account_id):

        if account_id in self.accounts:
            
            return self.accounts[account_id]
        
        else: 

            raise ValueError(f'Account not found')

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())#Output 0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))#Output 100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))#Output 200

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

#Output Account with this ID already exists


bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)

#Output account not found