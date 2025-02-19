from film import Film

class Azione(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = 'Azione'
        self.__penale: float = 3.00

    def getGenere(self)->str:
        
        return f'{self.__genere}'
    
    def getPenale(self)->float:

        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_affitto: int)->float:

        return self.getPenale() * giorni_affitto



class Commedia(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = 'Commedia'
        self.__penale: float = 2.50

    def getGenere(self)->str:
        
        return f'{self.__genere}'
    
    def getPenale(self)->float:

        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_affitto: int)->float:

        return self.getPenale() * giorni_affitto

class Drama(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = 'Drama'
        self.__penale: float = 2.00

    def getGenere(self)->str:
        
        return f'{self.__genere}'
    
    def getPenale(self)->float:

        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_affitto: int)->float:

        return self.getPenale() * giorni_affitto