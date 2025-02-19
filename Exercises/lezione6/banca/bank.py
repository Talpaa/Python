from typing import Any

class ContoBancario:

    total_account: int = 0
    definizione: str = 'Classe<ContoBancario>'

    def __init__(self, iban: int, saldo: float, nome: str) -> None:
        
        self.iban: int = iban
        self.saldo: float = saldo
        self.none: str = nome

        ContoBancario.total_account +=1

    def deposito(self, importo: float):

        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è {self.saldo}')

    def prelievo(self, importo: float):
        self.saldo += importo
        print(f'{importo} prelevato. Il nuovo saldo è {self.saldo}')

    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_account}')

    @classmethod
    def get_type(cls):
        print(f'Type: {cls.definizione}')

    @staticmethod
    def valida_account(iban: Any):
        if isinstance(iban, int)and(len(str(iban)) == 10):
            print('iban valido')
            return True
        
        else:
            print('iban non valido')
            return False
        
account1 = ContoBancario(1234567890, 0, 'Alice')
account2 = ContoBancario(9876543210, 1000, 'Bob')

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(150)

ContoBancario.get_total_accounts()

ContoBancario.get_type()

account3 = ContoBancario(9876543210, 0, 'Bob')

ContoBancario.get_total_accounts()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account('12345ABCD')