class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int) -> None:
        
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def descrivi_veicolo(self):

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    

class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, porte: int) -> None:
        super().__init__(marca, modello, anno)

        self.porte: int = porte

    def descrivi_veicolo(self):
        
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.porte}")
    

class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:
        super().__init__(marca, modello, anno)

        self.tipo: str = tipo

    def descrivi_veicolo(self):

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
    

	
veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto