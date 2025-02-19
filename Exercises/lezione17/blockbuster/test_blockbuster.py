import unittest

from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class testFiml(unittest.TestCase):

    def setUp(self) -> None:
        
        self.film1: Azione = Azione(id= 6384794, title= 'film1')
        self.film2: Azione = Azione(id= 2542525, title= 'film2')
        self.film3: Azione = Azione(id= 2342424, title= 'film3')
        self.film4: Azione = Azione(id= 7356462, title= 'film4')
        self.film5: Azione = Azione(id= 6593749, title= 'film5')
        self.film6: Commedia = Commedia(id= 7230745, title= 'film6')
        self.film7: Commedia = Commedia(id= 6307578, title= 'film7')
        self.film8: Commedia = Commedia(id= 6398564, title= 'film8')
        self.film9: Commedia = Commedia(id= 9678878, title= 'film9')
        self.film10: Drama = Drama(id= 6548473, title= 'film10')
        self.film11: Drama = Drama(id= 2856792, title= 'film11')


        lista_film: list[Azione, Commedia, Drama] = [self.film1, self.film2, self.film3, self.film4, self.film5, 
                                                     self.film6, self.film7, self.film8, self.film9, self.film10]
        
        self.noleggio: Noleggio = Noleggio(film_list= lista_film)

    #Testare la Disponibilità di un Film (isAvaible)
    def test_isAvailble(self):

        #test per verificare che un film disponibile ritorni True.
        self.assertEqual(first=self.noleggio.isAvaible(film= self.film1),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che un film disponibile ritorni False.
        self.assertEqual(first=self.noleggio.isAvaible(film= self.film11),second=False,msg= f'Error: shoul return \'False\' not \'{self.noleggio.isAvaible(film= self.film11)}\'')

    #Testare il Noleggio di un Film (rentAMovie)
    #Testare il Noleggio di un Film Non Disponibile
    def test_rentAMovie(self):

        #test per verificare che un film disponibile possa essere noleggiato correttamente.
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film1, id_client=123456789),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che il film non sia più disponibile.
        self.assertEqual(first=self.noleggio.isAvaible(film= self.film1),second=False,msg= f'Error: shoul return \'False\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.
        self.assertEqual(first=(123456789 in self.noleggio.rented_film),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che non sia possibile noleggiare lo stesso film con un altro cliente.
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film1, id_client=987654321),second=False,msg= f'Error: shoul return \'False\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')

    #Testare la Restituzione di un Film (giveBack)
    def test_giveBack(self):

        #test per verificare che sia possibile noleggiare e restituire un film.
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film1, id_client=123456789),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        self.assertEqual(first=self.noleggio.giveBack(film= self.film1, id_client=123456789, giorni_affitto= 7),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che il film restituito sia nuovamente disponibile.
        self.assertEqual(first=self.noleggio.isAvaible(film= self.film1),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.
        self.assertEqual(first=(self.film1 in self.noleggio.rented_film[123456789]),second=False,msg= f'Error: shoul return \'False\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')

    #Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo)
    def test_calcolaPenaleRitardo(self):

        #test per verificare il calcolo della penale di ritardo per film di diversi generi (azione).
        self.assertEqual(first=self.film1.calcolaPenaleRitardo(giorni_affitto= 7),second=21.0,msg= f'Error: shoul return \'21.0\' not \'{self.film1.calcolaPenaleRitardo(giorni_affitto= 7)}\'')
        #test per verificare il calcolo della penale di ritardo per film di diversi generi (commedia).
        self.assertEqual(first=self.film6.calcolaPenaleRitardo(giorni_affitto= 7),second=17.5,msg= f'Error: shoul return \'17.5\' not \'{self.film1.calcolaPenaleRitardo(giorni_affitto= 7)}\'')
        #test per verificare il calcolo della penale di ritardo per film di diversi generi (dramma).
        self.assertEqual(first=self.film10.calcolaPenaleRitardo(giorni_affitto= 7),second=14.0,msg= f'Error: shoul return \'14.0\' not \'{self.film1.calcolaPenaleRitardo(giorni_affitto= 7)}\'')

    #Testare la Stampa dei Film Disponibili (printMovies)
    def test_printMovies(self):

        message: str = '(film1 - Azione) - (film2 - Azione) - (film3 - Azione) - (film4 - Azione) - (film5 - Azione)'\
                    +f'- (film6 - Commedia) - (film7 - Commedia) - (film8 - Commedia) - (film9 - Commedia) - (film10 - Drama) -'
        
        #test per verificare che la lista dei film disponibili contenga i titoli corretti.
        self.assertEqual(first=self.noleggio.printMovies(),second=message,msg= f'Error: shoul return \'{message}\' not \'{self.noleggio.printMovies()}\'')

    #Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies)
    def test_printMovies(self):

        lista: list[Azione, Commedia, Drama] = [self.film1, self.film6, self.film10]

        #Noleggiare uno o più film per un cliente.
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film1, id_client=123456789),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film6, id_client=123456789),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        self.assertEqual(first=self.noleggio.rentAMovie(film= self.film10, id_client=123456789),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        #test per verificare che la stampa dei film noleggiati contenga i titoli corretti.
        self.assertEqual(first=self.noleggio.printRentMovies(clientID= 123456789),second=lista,msg= f'Error: shoul return \'{lista}\' not \'{self.noleggio.printRentMovies(clientID= 123456789)}\'')


if __name__ == '__main__':
    unittest.main()