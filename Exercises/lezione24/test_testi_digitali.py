import unittest

from testi_digitali import Documento, Email, File

class TestMyLibrary(unittest.TestCase):

    def setUp(self) -> None:
        
        self.documento: Documento = Documento(testo='Ciao')
        self.email: Email = Email(testo='Ciao Bob, possiamo incontrarci domani?', mittente='alice@example.com', destinatario='bob@example.com', titolo='Incontro')
        self.file: File = File()

    def test_getTesto_documento(self):

        self.assertEqual(first=self.documento.getTesto(), second='Ciao', msg=f'Error: should return \'Ciao\' not {self.documento.getTesto()}')

    def test_setTesto_documento(self):

        self.assertEqual(first=self.documento.getTesto(), second='Ciao', msg=f'Error: should return \'Ciao\' not {self.documento.getTesto()}')
        self.assertEqual(first=self.documento.setTesto(testo='Addio'), second=None, msg=f'Error: should return \'None\' not {self.documento.getTesto()}')
        self.assertEqual(first=self.documento.getTesto(), second='Addio', msg=f'Error: should return \'Addio\' not {self.documento.getTesto()}')

    def test_isInText_documento(self):

        self.assertEqual(first=self.documento.isInText(parola_chiave='z'), second=False, msg=f'Error: should return \'False\' not True')
        self.assertEqual(first=self.documento.isInText(parola_chiave='a'), second=True, msg=f'Error: should return \'True\' not False')


    def test_getTesto_email(self):

        self.assertEqual(first=self.email.getTesto(), second='Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?', msg=f'Error: should return:\n\'Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?\'\nnot {self.email.getTesto()}')

    def test_writeToFile_email(self):

        self.assertEqual(first=self.email.writeToFile(nome_file='email2'), second=None, msg=f'Error: should return \'None\' not {self.email.getTesto()}')

        with open('lezione24/email/email2.txt', 'r') as email:

            self.assertEqual(first=email.read(), second='Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?', msg=f'Error: should return:\n\'Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?\'\nnot {self.email.getTesto()}')

    def test_isInText_email(self):

        self.assertEqual(first=self.email.isInText(parola_chiave='animale'), second=False, msg=f'Error: should return \'False\' not True')
        self.assertEqual(first=self.email.isInText(parola_chiave='incontrarci'), second=True, msg=f'Error: should return \'True\' not False')


    def test_getTesto_file(self):

        self.assertEqual(first=self.file.getTesto(), second='Percorso: lezione24/documenti/documento.txt\nContenuto: Questo e\' il contenuto del file.', msg=f'Error: should return:\n\'Percorso: lezione24/documenti/documento.txt\nContenuto: Questo e\' il contenuto del file.\'\nnot {self.file.getTesto()}')

    def test_isInText_file(self):

        self.assertEqual(first=self.file.isInText(parola_chiave='animale'), second=False, msg=f'Error: should return \'False\' not True')
        self.assertEqual(first=self.file.isInText(parola_chiave='contenuto'), second=True, msg=f'Error: should return \'True\' not False')

if __name__ == '__main__':
    unittest.main()

        #self.assertEqual(first=self., second=, msg=f'Error: should return \'    \' not {self.}')
