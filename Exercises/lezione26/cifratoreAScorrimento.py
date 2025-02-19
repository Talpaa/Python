from codificatore_decodificatore import CodificatoreMessaggio, DecodificatoreMessaggio

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        
        if chiave > 25:
            chiave = (chiave % 25)

        self.chiave: int = chiave
        self.__alfabeto__: list[str] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#0-25

    def __codificaCarattere__(self, char: str)->str:
        
        ind: int = self.__alfabeto__.index(char.upper())
        cn: int = ind + self.chiave

        if cn > 25:

                cn = (cn % 25)-1

        if char.isupper():

            char = self.__alfabeto__[cn]

        else:

            char = self.__alfabeto__[cn].lower()

        return char
    
    def codifica(self, testoInChiaro: str)->str:
        
        testoCodificato: str = ''

        for char in testoInChiaro:
            
            if char.upper() in self.__alfabeto__:
                
                testoCodificato += self.__codificaCarattere__(char)

        return testoCodificato
    
    def __decodificaCarattere__(self, char: str)->str:

        ind: int = self.__alfabeto__.index(char.upper())
        cn: int = ind - self.chiave

        if cn < -26:

            cn *= -1
            cn %= 25 - 1

        if char.isupper():

            char = self.__alfabeto__[cn]

        else:

            char = self.__alfabeto__[cn].lower()

        return char
    
    def decodifica(self, testoCodificato: str)->str:
        
        testoDecodificato: str = ''

        for char in testoCodificato:
            
            if char.upper() in self.__alfabeto__:
                
                testoDecodificato += self.__decodificaCarattere__(char)

        return testoDecodificato
    

if __name__ == "__main__":

    cifrario: CifratoreAScorrimento = CifratoreAScorrimento(chiave= 26)

    testo: str = 'abcdefghijklmnopqrstuvwxyz'
    print(testo)

    print()

    testoCodificato: str = cifrario.codifica(testoInChiaro=testo)
    print(testoCodificato)

    print()

    testoDecifrato: str = cifrario.decodifica(testoCodificato=testoCodificato)
    print(testoDecifrato)