#Sistema di Prenotazione Cinema

#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
#Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

class Film:
    
    def __init__(self, 
                 titolo: str, 
                 durata: str) -> None:
        
        self.titolo: str = titolo
        self.durata: str = durata

class Sala:
    
    def __init__(self, 
                 id: str,
                 film: Film,
                 posti_totali: int) -> None:
        
        self.id: str = id
        self.film: Film = film
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = 0
        self.posti_rimasti: int = posti_totali
    
    def prenota_posti(self, 
                      num_posti: int)-> str: 

        if self.posti_rimasti >= num_posti:

            self.posti_rimasti -= num_posti

            if num_posti == 1:
                return f'Il posto è stato prenotato.\n'
            
            else:
                return f'I {num_posti} posti sono stati prenotati.\n'

        else:

            if num_posti == 1:
                return f'Il posto non è disponibile.\n'
            
            else:
                return f'non sono disponibili {num_posti} posti.\n'
            
        
    def posti_disponibili(self)-> int:
            
        return self.posti_totali    

    

class Cinema:

    def __init__(self, 
                 nome: str) -> None:
        
        self.nome: str = nome
        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala: Sala):
        
        if sala in self.sale:

            print('La sala che stai provando ad inserire è gia presente.\n')

        else:

            self.sale.append(sala)
            print('La sala è stata aggiunta.\n')



    def prenota_film(self, 
                     titolo_film: str, 
                     num_posti: int)-> str:

        for sala in self.sale:

            if titolo_film.lower() == sala.film.titolo.lower():

                return f'{sala.prenota_posti(num_posti)}'


        return f'Il film non è presente in nessuna sala.\n'

        

#cinema
adriano: Cinema = Cinema(nome='Cinema Adriano')

#Film
fight_club: Film = Film(titolo='Fight Club', durata='2h 12m')

pulp_fiction: Film = Film(titolo='Pulp Fiction', durata='2h 34m')

il_cavaliere_oscuro: Film = Film(titolo='Il Cavaliere Oscuro',  durata='2h 32m')

non_è_un_paese_per_vecchi: Film = Film(titolo='Non è un paese per vecchi', durata='2h 2m')

nightcrawler: Film = Film(titolo='Nightcrawler', durata='1h 57m')


#Sale
sala_1: Sala = Sala(id='001', film=fight_club, posti_totali= 250)

sala_2: Sala = Sala(id='002', film=pulp_fiction, posti_totali= 250)

sala_3: Sala = Sala(id='003', film=il_cavaliere_oscuro, posti_totali= 250)

sala_4: Sala = Sala(id='004', film=non_è_un_paese_per_vecchi, posti_totali= 250)

sala_5: Sala = Sala(id='005', film=nightcrawler, posti_totali= 250)


adriano.aggiungi_sala(sala_1)
adriano.aggiungi_sala(sala_2)
adriano.aggiungi_sala(sala_3)
adriano.aggiungi_sala(sala_4)
adriano.aggiungi_sala(sala_5)

adriano.aggiungi_sala(sala_5)


print(adriano.prenota_film(titolo_film='Fight Club', num_posti= 10))

print(adriano.prenota_film(titolo_film='Fight Club', num_posti= 240))

print(adriano.prenota_film(titolo_film='Fight Club', num_posti= 2))

print(adriano.prenota_film(titolo_film='Fight Club', num_posti= 1))