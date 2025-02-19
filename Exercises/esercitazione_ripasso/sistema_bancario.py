class Account:

    def __init__(self, account_id: str, balance: float = 0.0) -> None:
        
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float)->None:

        self.balance += amount

    def get_balance(self):

        return self.balance
    

class Bank:

    def __init__(self) -> None:
        
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id):

        if account_id not in self.accounts:
        
            account: Account = Account(account_id=account_id, balance=0.0)

            self.accounts[account_id] = account

            return account
        
        else:

            print(f'Account with this ID already exists')

    def deposit(self, account_id: str, amount: float):

        if account_id in self.accounts:

            self.accounts[account_id].deposit(amount=amount)

    def get_balance(self, account_id: str):

        if account_id in self.accounts:

            return self.accounts[account_id].get_balance()
        
        else:

            print(f'Account not found')
        

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())