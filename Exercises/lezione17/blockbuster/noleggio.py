from movie_genre import Azione, Commedia, Drama

class Noleggio:

    def __init__(self, film_list: list[Azione | Commedia | Drama]) -> None:
        
        self.film_list: list[Azione, Commedia, Drama] = film_list #lista film disponibili all'acquisto
        self.rented_film: dict[int: list[Azione, Commedia, Drama]] = {}

    def isAvaible(self, film: Azione | Commedia | Drama):

        if film in self.film_list:

            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        
        else:

            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film: Azione | Commedia | Drama, id_client: int):

        if self.isAvaible(film):

            self.film_list.remove(film)

            if id_client in self.rented_film:

                self.rented_film[id_client].append(film)

            else:

                self.rented_film[id_client] = [film]

            print(f'Il cliente {id_client} ha noleggiato {film.getTitle()}!')
            return True

        else:

            print(f'Il cliente {id_client} non ha potuto noleggiare {film.getTitle()}!')
            return False

    def giveBack(self,film: Azione | Commedia | Drama, id_client: int, giorni_affitto: int):

        if id_client in self.rented_film:

            if film in self.rented_film[id_client]:

                self.rented_film[id_client].remove(film)
                self.film_list.append(film)

                print(f"Cliente: {id_client}! La penale da pagare per il film {film.getTitle()} e' di {film.calcolaPenaleRitardo(giorni_affitto)} euro!")
                return True
            
            return False
        
    def printMovies(self):

        message: str = ''

        if self.film_list:

            for film in self.film_list:

                message += f'({film.getTitle()} - {film.getGenere()}) - '

        else:

            message = f'Non ci sono film disponibili per il noleggio'

        return message
    
    def printRentMovies(self, clientID: int): 
            
        message: str = ''

        if clientID in self.rented_film:

            if self.rented_film[clientID]:

                lista: list[Azione, Commedia, Drama] = [film for film in self.rented_film[clientID]]

                return lista

            else:

                message = f'Non ci sono film noleggiati dal cliente: {clientID}'

        else:

            message = f'Non esiste nessun cliente con id: {clientID}'

        return message