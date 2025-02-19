class Persona:

    def __init__(self, 
                 nome: str,
                 cognome: str, 
                 data_di_nascita: str,
                 genere: str,
                 codice_fiscale: str) -> None:
        
        self._nome: str = nome
        self.cognome: str = cognome
        self.data_di_nascita: int = data_di_nascita
        self.genere: str = genere
        self.codice_fiscale: str = codice_fiscale

    def calcola_età(self):
        
        return 10
    
    def __eq__(self, value: object) -> bool:
        
        
        return value.codice_fiscale == self.codice_fiscale
    
    def get_nome(self)->str:

        return self._nome.upper()
    
    def set_nome(self, nome: str)->None:

        self._nome = nome.lower()
    
    def __str__(self) -> str:
        
        return f'Nome: {self._nome} \nCognome: {self.cognome}'

persona_1: Persona = Persona(nome = 'Flavio',
                             cognome = 'Giorgi',
                             data_di_nascita = '24/12/94',
                             genere = 'Maschio',
                             codice_fiscale = 'FGHDUS56I35I567U')


class Dipendente(Persona):

    def __init__(self, nome: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str,
                 codice_fiscale: str,
                 ore_lavorate: int) -> None:
        
        super().__init__(nome, cognome, data_di_nascita, genere, codice_fiscale)

        self.ore_lavorate: int = ore_lavorate

    def calcola_stipendio(self)->float:

        return 500.00
    
    def __str__(self) -> str:
        return super().__str__()
    
class Professore(Dipendente):

    def __init__(self, 
                 nome: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str,
                 codice_fiscale: str, 
                 ore_lavorate: int,
                 materia_insegnata: str,
                 ore_di_lezione: int) -> None:
        
        super().__init__(nome, cognome, data_di_nascita, genere, codice_fiscale, ore_lavorate)

        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione

    def __str__(self) -> str:
        return super().__str__()

dipendente_1: Dipendente = Dipendente(nome = 'Flavio',
                             cognome = 'Giorgi',
                             data_di_nascita = '24/12/94',
                             genere = 'Maschio',
                             codice_fiscale = 'FGHDUS56I35I567U',
                             ore_lavorate = 500)

print(persona_1.calcola_età())

print(dipendente_1._nome)

print(dipendente_1.ore_lavorate)

print(dipendente_1.calcola_età())

print(dipendente_1.calcola_stipendio())


professore_1: Professore = Professore(nome = 'Flavio',
                             cognome = 'Giorgi',
                             data_di_nascita = '24/12/94',
                             genere = 'Maschio',
                             codice_fiscale = 'FGHDUS56I35I567U',
                             ore_lavorate = 500,
                             materia_insegnata = 'Storia',
                             ore_di_lezione = 1000)

professore_2: Professore = Professore(nome = 'Mario',
                             cognome = 'Rossi',
                             data_di_nascita = '12/08/00',
                             genere = 'Maschio',
                             codice_fiscale = 'MRRSS56I35I567U',
                             ore_lavorate = 500,
                             materia_insegnata = 'Matematica',
                             ore_di_lezione = 1000)


print(professore_1.ore_di_lezione)

print(f'\nPROFESSORE \n{professore_1}')

print(professore_1 == professore_1)

print(professore_1 == professore_2)