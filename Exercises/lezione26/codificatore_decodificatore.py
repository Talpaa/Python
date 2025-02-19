from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro: str):
        pass


class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato: str):
        pass


