from codificatore_decodificatore import CodificatoreMessaggio, DecodificatoreMessaggio

#se come chiave dai la metà della lunghezza della frase da decifrare + 1 la frase decifrata sarà uguale alla frase di partenza

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        
        self.chiave: int = chiave

    def __mixa_stringa__(self, stringa: str):

        count: int = 0
        stringa_mixata: str = ''
        lunstringa: int = len(stringa)
        con: bool = False

        if lunstringa%2 == 1:

            count = (lunstringa//2) +1
            lunstringa += 1
            con= True

        else:

            count = lunstringa//2
        
        for x in range(lunstringa//2):

            if (con)and(x+count+1) > len(stringa):

                stringa_mixata += stringa[x]
                return stringa_mixata
            
            stringa_mixata += stringa[x] + stringa[x+count]

        return stringa_mixata
    
    def codifica(self, testoInChiaro: str):
        
        testoCodificato: str = testoInChiaro

        for _ in range(self.chiave):

            testoCodificato = self.__mixa_stringa__(testoCodificato)

        return testoCodificato
    
    def __ordina_stringa__(self, stringa: str):

        stringa_ordinata: str = ''
        countP: int = 0
        countD: int = 1

        while countP < len(stringa):

            stringa_ordinata += stringa[countP]

            countP +=2

        while countD < len(stringa):

            stringa_ordinata += stringa[countD]

            countD += 2

        return stringa_ordinata
        
    
    def decodifica(self, testoCodificato: str):
        
        testoInChiaro: str = testoCodificato

        for _ in range(self.chiave):

            testoInChiaro = self.__ordina_stringa__(testoInChiaro)

        return testoInChiaro


if __name__ == "__main__":

    cifrario: CifratoreACombinazione = CifratoreACombinazione(chiave= 120)

    stringa: str = 'abcdefghijklmnopqrstuvwxyz'

    print(stringa)
    print()

    stringa_mixata: str = cifrario.codifica(testoInChiaro=stringa)

    print(stringa_mixata)
    print()

    stringa = cifrario.decodifica(testoCodificato=stringa_mixata)

    print(stringa)