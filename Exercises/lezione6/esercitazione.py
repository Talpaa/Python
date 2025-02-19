from abc import ABC, abstractmethod 

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):

        pass

    @abstractmethod
    def movimento(self,t: int):

        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome: str = nome
        self.velocita: float = 10.0 #m/s

    def verso(self):     
        print('Bau!')
    
    def movimento(self, t: int):
        print(f'Il cane percorre in {t} secondi {self.velocita * t} metri')
    
class Gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome: str = nome
        self.velocita: float = 15.0 #m/s

    def verso(self):   
        print('Miao!') 
    
    def movimento(self, t: int):  
        print(f'Il gatto percorre in {t} secondi {self.velocita * t} metri')

cane_1: Cane = Cane(nome='Pinco')
cane_1.verso()
cane_1.movimento(60)
print()
gatto_1: Gatto = Gatto(nome='pallino')
gatto_1.verso()
gatto_1.movimento(60)