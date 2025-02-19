class Media:
    
    def __init__(self) -> None:
        
        self.title: str = ''
        self.reviews: list[int] = []

    def set_title(self, title: str):
        
        self.title = title

    def get_title(self)->str:
        
        return self.title

    def aggiungi_valutazione(self, voto: int):
        
        if (voto > 0)and(voto < 6):
        
            self.reviews.append(voto)

        else:

            print(f'Voto non valido.')

    def get_media(self)->float:
        
        sum: int = 0

        for voto in self.reviews:

            sum += voto

        media: float = sum / len(self.reviews)

        return media

    def get_rate(self):

        media: float = self.get_media()
        message: str = ''
        
        if media <= 1.5:

            message = f'Terribile'
        
        elif media <= 2.5:

            message = f'Brutto'
        
        elif media <= 3.5:

            message = f'Normale'      

        elif media <= 4.5:

            message = f'Bello'
        
        elif media <= 5:

            message = f'Grandioso'
        
        return message


    def rate_percentage(self, voto: int)->float:
        
        count: int = 0

        for num in self.reviews:

            if voto == num:

                count += 1

        uno_per: float = len(self.reviews) / 100.00

        percentuale: float = count / uno_per

        return percentuale

    def recensione(self)->str:
        
        message: str =\
              f'Titolo del Film: {self.get_title()}\n'\
             +f'Voto Medio: {self.get_media()}\n'\
             +f'Giudizio: {self.get_rate()}\n'\
             +f'Terribile: {self.rate_percentage(1)}%\n'\
             +f'Brutto: {self.rate_percentage(2)}%\n'\
             +f'Normale: {self.rate_percentage(3)}%\n'\
             +f'Bello: {self.rate_percentage(4)}%\n'\
             +f'Grandioso: {self.rate_percentage(5)}%\n'
        
        return message
    


print()
print()

libro: Media = Media()
libro.set_title(title='Moby Dick')
libro.aggiungi_valutazione(1)
libro.aggiungi_valutazione(2)
libro.aggiungi_valutazione(3)
libro.aggiungi_valutazione(3)
libro.aggiungi_valutazione(3)
libro.aggiungi_valutazione(4)
libro.aggiungi_valutazione(4)
libro.aggiungi_valutazione(4)
libro.aggiungi_valutazione(5)
libro.aggiungi_valutazione(5)

print(libro.recensione())


film: Media = Media()
film.set_title(title='Albakiara')
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(1)
film.aggiungi_valutazione(2)
film.aggiungi_valutazione(2)
film.aggiungi_valutazione(2)
film.aggiungi_valutazione(3)

print(film.recensione())
