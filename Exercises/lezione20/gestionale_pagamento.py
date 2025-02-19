class Pagamento:

    def __init__(self) -> None:
        
        self.__importo: float = 0.00

    def set_importo(self, importo: float)->None:

        self.__importo = importo

    def get_importo(self):

        return self.__importo
    
    def dettagliPagamento(self)->str:

        return f"Importo del pagamento: {round(number=self.get_importo(), ndigits= 2)}€"
    
class PagamentoContanti(Pagamento):

    def __init__(self, importo: float) -> None:
        
        self.__importo: float = importo

    def set_importo(self, importo: float) -> None:
        
        self.__importo = importo

    def get_importo(self):
        
        return self.__importo 

    def inPezziDa(self):

        importo: float = float(self.get_importo())

        pezzi: dict[float, int]  = {500.00: 0, 200.00: 0, 100.00: 0, 50.00: 0, 20.00: 0, 10: 0, 5: 0, 2.00: 0, 1.00: 0, 0.50: 0, 0.20: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        
        message: str = f'{round(self.get_importo(), 2)}€ da pagare in contanti con:\n'

        for taglio in pezzi:

            if (importo // taglio) > 0:

                pezzi[taglio] = int(importo // taglio)

                importo -= taglio * pezzi[taglio]

        for taglio in pezzi:

            if pezzi[taglio] > 0:

                if taglio >= 5.00:

                    if pezzi[taglio] == 1:

                        message += f'1 banconota da {taglio}€\n'

                    else:

                        message += f'{pezzi[taglio]} banconote da {taglio}€\n'

                else:

                    if pezzi[taglio] == 1:

                        message += f'1 moneta da {taglio}€\n'

                    else:

                        message += f'{pezzi[taglio]} monete da {taglio}€\n'

        return message



    def dettagliPagamento(self) -> str:
        
        message: str = f'pagamento in contanti di: {round(number=self.get_importo(), ndigits= 2)}€'\
                      +f'{self.inPezziDa()}'
        
        return message
    

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo: float, nome: str, cognome: str, mese_scadenda: str, anno_scadenza: str, numero_carta: int) -> None:
        
        self.__importo: float = importo

        self.nome: str = nome
        self.cognome: str = cognome
        self.data_scadenza: str = f'{mese_scadenda}/{anno_scadenza}'
        self.numero_carta: str = str(numero_carta)

    def set_importo(self, importo: float) -> None:
        
        self.__importo = importo

    def get_importo(self):
        
        return self.__importo 

    def dettagliPagamento(self) -> str:
        
        return f'Pagamento di: {round(number=self.get_importo(), ndigits= 2)}€ effettuato con la carta di credito\n'\
                +f'Nome sulla carta: {self.nome} {self.cognome}\n'\
                +f'Data di scadenza: {self.data_scadenza}\n'\
                +f'Numero della carta: {self.numero_carta}\n'
    


pagamento1: PagamentoContanti = PagamentoContanti(150.00)
pagamento2: PagamentoContanti = PagamentoContanti(95.25)

pagamento3: PagamentoCartaDiCredito = PagamentoCartaDiCredito(importo=200.00, nome='Mario', cognome='Rossi', mese_scadenda= '11', anno_scadenza= '99', numero_carta=1234567890123456)
pagamento4: PagamentoCartaDiCredito = PagamentoCartaDiCredito(importo=500.00, nome='Luigi', cognome='Bianchi', mese_scadenda= '01', anno_scadenza= '25', numero_carta=6543210987654321)

print(pagamento1.dettagliPagamento())
print(pagamento2.dettagliPagamento())
print(pagamento3.dettagliPagamento())
print(pagamento4.dettagliPagamento())
