class Libro:

    def __init__(self,
                 titolo: str,
                 autore: str) -> None:
        
        self.titolo: str = titolo
        self.autore: str = autore
        self.status_disponibilita = True
        pass

class Biblioteca:

    def __init__(self) -> None:
        
        self.libri: list[Libro] = []

    def aggiungi_libro(self, libro: Libro):
        
        if libro not in self.libri:

            self.libri.append(libro)
            print(f'Il libro è stato aggiunto nella biblioteca.\n')

        else:

            print(f'Il libro è già presente nella biblioteca.\n')

    def presta_libro(self, titolo: str)->str:
        
        for libro in self.libri:

            if libro.titolo.lower() == titolo.lower():

                if libro.status_disponibilita:

                    libro.status_disponibilita = False
                    return f'Il libro {titolo.title()} è stato prestato.\n'

                else:

                    return f'Il libro {titolo.title()} è già stato preso in prestito.\n'
                
        return f'Il libro {titolo.title()} non è presente in biblioteca.\n'

    def restituisci_libro(self, titolo: str):
        
        for libro in self.libri:

            if libro.titolo.lower() == titolo.lower():

                if not(libro.status_disponibilita):

                    libro.status_disponibilita = True
                    return f'Il libro {titolo.title()} è stato riportato.\n'

                else:

                    return f'Il libro {titolo.title()} è già stato riportato.\n'
                
        return f'Il libro {titolo.title()} non è presente in biblioteca.\n'

    def mostra_libri_disponibili(self):

        i: int = 0
        print(f'Libri disponibilio al prestito:\n')
        
        for libro in self.libri:

            if libro.status_disponibilita:
                i += 1

                print(f'{i}) {libro.titolo};\n')    

#biblioteca
biblioteca: Biblioteca = Biblioteca()

#libri
il_codice_da_vinci: Libro = Libro(titolo='Il Codice da Vinci', autore='Dan Brown')

harry_potter_e_la_pietra_filosofale: Libro = Libro(titolo='Harry Potter e la Pietra Filosofale', autore='J. K. Rowling')

lo_hobbit: Libro = Libro(titolo='Lo Hobbit', autore='J.R.R. Tolkien')

#L'alchimista, di Paulo Coelho 

#inserimento libri dentro la biblioteca
biblioteca.aggiungi_libro(il_codice_da_vinci)
biblioteca.aggiungi_libro(harry_potter_e_la_pietra_filosofale)
biblioteca.aggiungi_libro(lo_hobbit)

biblioteca.aggiungi_libro(lo_hobbit)

biblioteca.mostra_libri_disponibili()

print(biblioteca.presta_libro(titolo='lo hobbit'))
print(biblioteca.presta_libro(titolo='lo hobbit'))

biblioteca.mostra_libri_disponibili()


print(biblioteca.restituisci_libro(titolo='lo hobbit'))
print(biblioteca.restituisci_libro(titolo='lo hobbit'))

biblioteca.mostra_libri_disponibili()