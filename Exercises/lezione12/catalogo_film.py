from typing import Any

class MovieCatalog:
    
    def __init__(self) -> None:
        
        self.catalogo: dict[str, list[str]] = {}

    def add_movie(self, director_name: str, movies: list[str]):

        director_name = director_name.title()

        if director_name in self.catalogo:

            for film in movies:

                film = film.title()
                self.catalogo[director_name].append(film)
                print(f'Il film {film} è stato aggiunto alla lista di film del regista {director_name}.\n')

        elif director_name not in self.catalogo:

            self.catalogo[director_name] = []
            
            for film in movies:

                film = film.title()
                self.catalogo[director_name].append(film)


    def remove_movie(self, director_name: str, movie: str):

        director_name = director_name.title()
        movie = movie.title()
        
        if director_name in self.catalogo:

            if movie in self.catalogo[director_name]:

                self.catalogo[director_name].remove(movie)
                print(f'\nIl film {movie} è stato rimosso dalla lista di film del regista {director_name}.')

            if len(self.catalogo[director_name]) == 0:

                self.catalogo.pop(director_name)

                print(f'\nIl regista {director_name} è stato rimosso dal catalogo perchè non aveva più film.')
        
        else:
            print(f'\nIl film {movie} non è stato rimosso perchè il regista {director_name} non è presente nel catalogo.')


    def list_directors(self):

        i: int = 0

        print(f'\nEcco a te la lista di tutti i registi presenti nel catalogo:')

        for regista in self.catalogo:

            i += 1
            print(f'{i}) {regista.title()};')

    def get_movies_by_director(self, director_name: str):

        flag: bool = True

        for regista in self.catalogo:

            if regista.title() == director_name.title():
                i: int = 0
                print(f'\nEcco la lista di film del regista {director_name.title()} disponibili nel catalogo:')

                for film in self.catalogo[regista]:

                    i += 1
                    print(f'{i}) {film.title()};')

                flag = False

        if flag:
            print(f'\nIl regista {director_name.title()} non è presente nel catalogo.')

    def search_movies_by_title(self, title: str)->Any:

        trovati: dict[str, list[str]]= {}

        for regista in self.catalogo:

            for film in self.catalogo[regista]:

                if (title.lower() in film.lower())and\
                    (regista not in trovati):
                    
                    trovati[regista] = []
                    trovati[regista].append(film.title())

                elif(title.title() in film.title())and\
                    (film.title() not in trovati[regista])and\
                    (regista in trovati):

                    trovati[regista].append(film.title())

        if len(trovati) > 0:

            for regista in trovati:
                print(f'\nI film del regista {regista} che contengono la parola \'{title.lower()}\' sono:')
                i: int = 0
                for film in trovati[regista]:
                    i += 1

                    print(f'{i}) {film};')

            return trovati
        
        else:

            return f'Nessun film presente nel catalogo ha la parola \'{title.lower()}\'.\n'



print()

catalogo: MovieCatalog = MovieCatalog()

catalogo.add_movie(director_name='Steven Spielberg', movies=['Ready Player One', 'Jurassic Park', 'Indiana Jones e il Regno del Teschio di Cristallo'])
catalogo.add_movie(director_name='Quentin Tarantino', movies=['Pulp Fiction', 'Kill Bill: Volume 1', 'Kill Bill: Volume 2', 'C\'era una volta a Hollywood'])
catalogo.add_movie(director_name='Guillermo Del Toro', movies=['PINOCCHIO', 'Hellboy'])
catalogo.add_movie(director_name='Mel Brooks', movies=['Frankenstein Junior', 'Mezzogiorno e mezzo di fuoco', 'Balle spaziali'])
catalogo.add_movie(director_name='Martin Scorsese', movies=[])
catalogo.add_movie(director_name='Martin Scorsese', movies=[])


catalogo.get_movies_by_director(director_name = 'Steven SPIELBERG')
catalogo.remove_movie(director_name='Steven SPIELBERG', movie='Indiana Jones e il Regno del Teschio di Cristallo')
catalogo.get_movies_by_director(director_name = 'Steven SPIELBERG')


catalogo.list_directors()
catalogo.remove_movie(director_name='Martin Scorsese', movie='')
catalogo.list_directors()
catalogo.remove_movie(director_name='Martin Scorsese', movie='')

catalogo.search_movies_by_title(title='kill')

catalogo.search_movies_by_title(title='io')