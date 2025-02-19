from volo_commerciale import VoloCommerciale
from volo_charter import VoloCharter

class CompagniaAerea:

    def __init__(self, compagnia: str, costo_biglietto_standard: float) -> None:
        
        self.compagnia: str = compagnia
        self.prezzo: float = costo_biglietto_standard
        self.flotta: list[VoloCommerciale] = []

    def aggiungi_volo(self, volo: VoloCommerciale):

        if volo not in self.flotta:

            self.flotta.append(volo)
            print(f'Il volo {volo.codice} è stato aggiunto alla flotta.')

        else:

            print(f'Il volo {volo.codice} fa gia parte della flotta.')

    def rimuovi_volo(self, volo: VoloCommerciale):

        if volo not in self.flotta:

            print(f'Il volo {volo.codice} non fa parte della flotta.')

        else:

            self.flotta.remove(volo)
            print(f'Il volo {volo.codice} è stato rimosso alla flotta.')

    def mostra_flotta(self):

        if len(self.flotta) < 1:

            print(f'Non sono presenti voli nella flotta.')

        else:

            message: str = f'Ecco a te la lista della flotta della compagnia aerea {self.compagnia}\n'

            for volo in self.flotta:

                message += f'   -{volo.codice}'

            print(message)

    def guadagno(self):

        if len(self.flotta) < 1:

            return 0.00

        soldi: float = 0.00

        for volo in self.flotta:

            posti_eco: int = volo.posti_economica - volo.posti_dis['classe economica']
            posti_bus: int = volo.posti_business - volo.posti_dis['classe business']
            posti_pri: int = volo.posti_prima - volo.posti_dis['classe prima']

            soldi += ((posti_eco * self.prezzo)+(posti_bus * (self.prezzo*2))+(posti_pri * (self.prezzo*3)))

        return round(soldi, 2)
    

if __name__ == "__main__":
    
    volo: VoloCommerciale = VoloCommerciale(codice_volo='aereo1', capacità_max=100)

    volo.prenota_posto(posti=70, classe_servizio='economica')
    volo.prenota_posto(posti=20, classe_servizio='business') 
    volo.prenota_posto(posti=10, classe_servizio='prima')

    volo2: VoloCommerciale = VoloCommerciale(codice_volo='aereo2', capacità_max=853)

    volo2.prenota_posto(posti=364, classe_servizio='economica')
    volo2.prenota_posto(posti=82, classe_servizio='business') 
    volo2.prenota_posto(posti=31, classe_servizio='prima')

    print()

    compagnia: CompagniaAerea = CompagniaAerea(compagnia='Qatar Airways', costo_biglietto_standard=450.00)

    compagnia.rimuovi_volo(volo=volo)
    print()

    compagnia.mostra_flotta()
    print()

    compagnia.aggiungi_volo(volo=volo)
    compagnia.aggiungi_volo(volo=volo)
    print()

    compagnia.aggiungi_volo(volo=volo2)
    print()

    compagnia.mostra_flotta()
    print()

    compagnia.rimuovi_volo(volo=volo)
    print()

    compagnia.mostra_flotta()
    print()

    compagnia.aggiungi_volo(volo=volo)
    print()

    print(f'Guadagno della compagnia {compagnia.compagnia}: {compagnia.guadagno()}')
