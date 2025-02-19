class Elettrodomestico:

    def __init__(self, marca: str, modello: str, potenza: int) -> None:
        
        self.marca: str = marca
        self.modello: str = modello
        self.potenza: int = potenza

    def descrivi_elettrodomestico(self):

        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W')


class Frigorifero(Elettrodomestico):

    def __init__(self, marca: str, modello: str, potenza: int, capacità: int) -> None:
        super().__init__(marca, modello, potenza)

        self.capacità: int = capacità

    def descrivi_elettrodomestico(self):
        
        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L')


class Lavatrice(Elettrodomestico):

    def __init__(self, marca: str, modello: str, potenza: int, carico_max: int) -> None:
        super().__init__(marca, modello, potenza)

        self.carico_max: int = carico_max

    def descrivi_elettrodomestico(self):
        
        print(f'Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg')
