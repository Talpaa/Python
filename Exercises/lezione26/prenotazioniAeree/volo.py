from abc import ABC, abstractmethod

class Volo(ABC):

    def __init__(self, codice_volo: str, capacità_max: int) -> None:
        super().__init__()

        self.prenotazioni: int = 0

    @abstractmethod
    def posti_disponibili(self):
        pass
    
    @abstractmethod
    def prenota_posto(self):
        pass

    