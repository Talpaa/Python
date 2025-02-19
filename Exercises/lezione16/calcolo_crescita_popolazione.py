from abc import ABC, abstractmethod

class Specie(ABC):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    @abstractmethod
    def cresci(self):
        #Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
        
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita/100))

    @abstractmethod
    def anni_per_superare(self, specie: 'Specie')->int:

        anni_passati: int = 0

        while (self.popolazione <= specie.popolazione)and(anni_passati <= 1000): 

            anni_passati += 1

            self.cresci()
            specie.cresci()
        
        if anni_passati <= 1000:
            return anni_passati
        
        else:

            return f'{self.nome} non supererà mai {specie.nome}'
    
    @abstractmethod
    def getDensita(self, area_kmq: float)->int:
        
        anni_passati: int = 0

        while(self.popolazione / area_kmq) < 1:

            anni_passati += 1
            self.cresci()
        
        
        return anni_passati
    
class BufaloKlingon(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float, nome: str = 'Bufalo Klingon') -> None:
        super().__init__(nome, popolazione, tasso_crescita)

        self.nome = nome

    def cresci(self):
        return super().cresci()
    
    def anni_per_superare(self, specie: Specie) -> int:
        return super().anni_per_superare(specie)
    
    def getDensita(self, area_kmq: float) -> int:
        return super().getDensita(area_kmq)

class Elefante(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float, nome: str = 'Elefante') -> None:
        super().__init__(nome, popolazione, tasso_crescita)

        self.nome = nome

    def cresci(self):
        return super().cresci()
    
    def anni_per_superare(self, specie: Specie) -> int:
        return super().anni_per_superare(specie)
    
    def getDensita(self, area_kmq: float) -> int:
        return super().getDensita(area_kmq)

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")