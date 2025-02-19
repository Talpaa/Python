from volo import Volo

class VoloCommerciale(Volo):

    def __init__(self, codice_volo: str, capacità_max: int) -> None:
        super().__init__(codice_volo, capacità_max)

        self.codice: str = codice_volo
        self.capacità: str = capacità_max

        cap: int = self.capacità//100

        self.posti_economica: int = cap * 70
        self.posti_business: int = cap * 20
        self.posti_prima: int = (self.capacità - (self.posti_economica + self.posti_business))

        self.posti_dis: dict[str: int] = {'posti disponibili': self.capacità, 'classe economica': self.posti_economica, 'classe business': self.posti_business, 'classe prima': self.posti_prima}

    def posti_disponibili(self):

        return self.posti_dis
    
    def prenota_posto(self, posti: int, classe_servizio: str):
        
        if self.posti_dis['posti disponibili'] > 0:

            controllo: bool = False

            if (self.posti_dis['classe economica'] >= posti)and(classe_servizio == 'economica'):

                self.posti_dis['classe economica'] -= posti

                if posti > 1:
                    print(f'Sono stati riservati {posti} posti per la classe economica del volo {self.codice}')

                else:
                    print(f'È stato riservato 1 posto per la classe economica del volo {self.codice}')

                controllo = True


            elif (self.posti_dis['classe business'] >= posti)and(classe_servizio == 'business'):

                self.posti_dis['classe business'] -= posti

                if posti > 1:
                    print(f'Sono stati riservati {posti} posti per la classe business del volo {self.codice}')

                else:
                    print(f'È stato riservato 1 posto per la classe business del volo {self.codice}')

                controllo = True

            elif (self.posti_dis['classe prima'] >= posti)and(classe_servizio == 'prima'):

                self.posti_dis['classe prima'] -= posti

                if posti > 1:
                    print(f'Sono stati riservati {posti} posti per la prima classe del volo {self.codice}')

                else:
                    print(f'È stato riservato 1 posto per la prima classe del volo {self.codice}')

                controllo = True

            else:

                if not((classe_servizio == 'economica')or(classe_servizio == 'business')or(classe_servizio == 'prima')):
                    
                    print(f'ERRORE: Non è presente nessuna classe {classe_servizio}')

                elif classe_servizio == 'prima':

                    print(f'Non ci sono abbastanza posti in prima classe.')

                else:

                    print(f'Non ci sono abbastanza posti nella classe {classe_servizio}.')

            if controllo:

                self.posti_dis['posti disponibili'] -= posti
            
        else:

            print(f'Il volo è al completo non è possibile prenotare altri posti.')


if __name__ == "__main__":
    
    volo: VoloCommerciale = VoloCommerciale(codice_volo='hgsj', capacità_max=100)

    print(volo.posti_disponibili())     
    print()

    volo.prenota_posto(posti=70, classe_servizio='miao')
    print(volo.posti_disponibili())
    print()

    volo.prenota_posto(posti=70, classe_servizio='economica')
    print(volo.posti_disponibili())
    print()

    volo.prenota_posto(posti=20, classe_servizio='business') 
    print(volo.posti_disponibili())
    print()

    volo.prenota_posto(posti=900, classe_servizio='economica')       
    volo.prenota_posto(posti=900, classe_servizio='business')       
    volo.prenota_posto(posti=900, classe_servizio='prima')       
    print(volo.posti_disponibili())
    print()

    volo.prenota_posto(posti=10, classe_servizio='prima')  
    print(volo.posti_disponibili())
    print()

    volo.prenota_posto(posti=70, classe_servizio='economica')

