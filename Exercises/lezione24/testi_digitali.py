class Documento:

    def __init__(self, testo: str) -> None:
        
        self.testo: str = testo

    def setTesto(self, testo: str):

        self.testo = testo

    def getTesto(self)->str:

        return self.testo
    
    def isInText(self, parola_chiave: str)->bool:

        if parola_chiave in self.getTesto():

            return True
        
        return False
    

class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)

        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo

    def setMittente(self, mittente: str):

        self.mittente = mittente

    def setDestinatario(self, destinatario: str):

        self.destinatario = destinatario

    def setTitolo(self, titolo: str):

        self.titolo = titolo

    def getMittente(self):

        return self.mittente
    
    def getDestinatario(self):

        return self.destinatario
    
    def getTitolo(self):

        return self.titolo
    
    def getTesto(self) -> str:
        
        return f'Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}'
        
    def writeToFile(self, nome_file: str):

        with open(f'lezione24/email/{nome_file}.txt', 'w') as email:

            email.write(self.getTesto())

class File(Documento):

    def __init__(self) -> None:

        self.percorso: str = f'lezione24/documenti/documento.txt'
        testo: str = ''

        super().__init__(testo)

    def leggiTestoDaFile(self):

        with open('lezione24/documenti/documento.txt', 'r') as documento:

            return documento.read()

    def getTesto(self) -> str:
        
        return f'Percorso: {self.percorso}\nContenuto: {self.leggiTestoDaFile()}'
    

if __name__ == "__main__":

    email: Email = Email(testo='Ciao Bob, possiamo incontrarci domani?', mittente='alice@example.com', destinatario='bob@example.com', titolo='Incontro')

    file: File = File()

    print()
    print(email.getTesto())

    print()
    print(file.getTesto())

    print()
    email.writeToFile(nome_file='email1')

    print()
    print(email.isInText(parola_chiave='incontrarci'))

    print()
    print(file.isInText(parola_chiave='percorso'))