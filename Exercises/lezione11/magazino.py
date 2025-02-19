class Prodotto:

    def __init__(self,
                 nome: str,
                 quantità: int) -> None:
        
        self.nome: str = nome
        self.quantità: int = quantità

class Magazzino:

    def __init__(self) -> None:
        
        self.prodotti: list[Prodotto] = []

    def aggiungi_prodotto(self, 
                          prodotto: Prodotto):
        
        if prodotto not in self.prodotti:

            self.prodotti.append(prodotto)
            print(f'{prodotto.nome.title()} è stata/o aggiunta/o in magazzino.\n')

        else:

            print(f'{prodotto.nome.title()} è già presente in magazzino.\n')

    def cerca_prodotto(self, 
                       nome: str) -> Prodotto:

        for prodotto in self.prodotti:

            if prodotto.nome.lower() == nome.lower():

                return prodotto
        print(f'{nome.title()} non è presente in magazzino.\n')    

    def verifica_disponibilità(self,
                               nome: str) -> str:
        
        for prodotto in self.prodotti:

            if prodotto.nome.lower() == nome.lower():

                return f'{prodotto.nome.title()} è presente in magazzino con {prodotto.quantità} unità.\n' 

        return f'{prodotto.nome.title()} non è presente in magazzino.\n'

print()
print()
#Magazino
magazzino: Magazzino = Magazzino()

#Prodotti
colla: Prodotto = Prodotto(nome='Colla', quantità= 2000)

risma: Prodotto = Prodotto(nome='Risma', quantità=10000)

forbice: Prodotto = Prodotto(nome='Forbice', quantità=850)

nastro_adesivo: Prodotto = Prodotto(nome='Nastro Adesivo', quantità=30000)

matita: Prodotto = Prodotto(nome='Matita', quantità=100000)


magazzino.aggiungi_prodotto(colla)
magazzino.aggiungi_prodotto(risma)
magazzino.aggiungi_prodotto(forbice)
magazzino.aggiungi_prodotto(nastro_adesivo)
magazzino.aggiungi_prodotto(matita)

magazzino.aggiungi_prodotto(matita)


magazzino.cerca_prodotto(nome='colla')
magazzino.cerca_prodotto(nome='Penna')

print(magazzino.verifica_disponibilità(nome='Forbice'))
print(magazzino.verifica_disponibilità(nome='Gomma'))


