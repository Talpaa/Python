from volo import Volo

class VoloCharter(Volo):

    def __init__(self, codice_volo: str, capacità_max: int, prezzo_charter: float) -> None:
        super().__init__(codice_volo, capacità_max)

        self.codice: str = codice_volo
        self.capacità: str = capacità_max
        self.prezzo: float = prezzo_charter
        self.posti_dis: int = capacità_max

    def posti_disponibili(self):
        return self.posti_dis

    def prenota_posto(self):
        
        if self.posti_dis > 0:

            self.posti_dis = 0
            print(f'il volo charter {self.codice} è stato prenotato completamente per un prezzo di {round(self.prezzo, 2)}.')

        else:

            print(f'il volo charter {self.codice} è gia stato prenotato completamente.')


if __name__ == "__main__":
    
    volo: VoloCharter = VoloCharter(codice_volo='cgwevuh', capacità_max=100, prezzo_charter=20000.00)

    print(f'Posti disponibili: {volo.posti_disponibili()}')
    print()
    
    volo.prenota_posto()
    print(f'Posti disponibili: {volo.posti_disponibili()}')
    print()

    volo.prenota_posto()