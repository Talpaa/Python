#Simulazione: La tartaruga e la lepre
from abc import ABC, abstractmethod
from random import randint

class AbcConcorrente(ABC):#da fare astratta

    def __init__(self) -> None:
        
        self.casella: int = 0
        self.passo: int = 0
        self.energia = 100

    @abstractmethod
    def spostamento(self, meteo: bool):

        pass



class Tartaruga(AbcConcorrente):

    def __init__(self) -> None:
        super().__init__()

    def spostamento(self, meteo: bool):

        self.passo = randint(1,10)
        flag_t: bool = True

        if (self.passo <= 5)and(self.energia >= 5):

            self.casella += 3
            self.energia -= 5

        elif (self.passo <= 8)and(self.energia >= 3):

            self.casella += 1
            self.energia -= 3

        elif (self.passo <= 10)and(self.energia >= 10):

            self.casella -= 6
            self.energia -= 10
        else:
            flag_t = False
            self.energia += 10

        if (meteo)and(flag_t):
            self.casella += -1

        if self.energia < 0:
            self.energia = 0

        elif self.energia > 100:         
            self.energia = 100

        if self.casella < 0:
            self.casella = 0


class Lepre(AbcConcorrente):

    def __init__(self) -> None:
        super().__init__()

    def spostamento(self, meteo: bool):

        self.passo = randint(1,10)
        flag_l: bool = True

        #Grande balzo
        if  (self.passo <= 2)and(self.energia >= 15):

            self.casella += 9
            self.energia -= 15

        # Grande scivolata
        elif (self.passo <= 3)and(self.energia >= 20):

            self.casella -= 12
            self.energia -= 20

        # Piccolo balzo
        elif (self.passo <= 6)and(self.energia >= 5):

            self.casella += 1
            self.energia -= 5
        #Piccola scivolata
        elif (self.passo <= 8)and(self.energia >= 8):

            self.casella -= 2 
            self.energia -= 8

        #Riposo
        elif(self.passo <= 10):

            flag_l: bool = False

            self.energia += 10


        if (meteo)and(flag_l):
            self.casella += -1

        if self.energia < 0:
            self.energia = 0

        elif self.energia > 100: 
            self.energia = 100

        if self.casella < 0:
            self.casella = 0

class Percorso:

    def __init__(self) -> None:
        
        self.caselle: list[str] = []
        self.meteo: bool = True #se è True c'è pioggia, se è False c'è il sole
        self.ostacoli: dict[int, int] = {14: 3, 29: 5, 44: 7}
        self.bonus: dict[int, int] = {9: 3, 24: 5, 49: 10}

    def add_element(self):

        self.caselle = ['-' for _ in range(70)]

        for key in self.bonus:

            self.caselle.pop(key)
            self.caselle.insert(key, 'bonus')

        for key in self.ostacoli:

            self.caselle.pop(key)
            self.caselle.insert(key, 'trap')

    def gara(self, tartaruga: Tartaruga, lepre: Lepre):

        tartaruga.spostamento(percorso.meteo)
        lepre.spostamento(percorso.meteo)

    #controllo se uno dei due concorrenti sia finito sulla casella con un malus o con un bonus 
        if tartaruga.casella in self.ostacoli:

            tartaruga.casella -= self.ostacoli[tartaruga.casella]

        elif tartaruga.casella in self.ostacoli:

            tartaruga.casella += self.ostacoli[tartaruga.casella]

        if lepre.casella in self.ostacoli:

            lepre.casella -= self.ostacoli[lepre.casella]

        elif tartaruga.casella in self.ostacoli:

            lepre.casella += self.ostacoli[lepre.casella]
        
        posizione_t: int = tartaruga.casella
        if posizione_t > 69:
            posizione_t = 69
            
        posizione_l: int = lepre.casella
        if posizione_l > 69:
            posizione_l = 69

        self.add_element()

        if (tartaruga.casella == lepre.casella):

            if self.caselle[posizione_t] == '-':
                self.caselle[posizione_t ] = 'OUCH!!!'

            elif self.caselle[posizione_t -1] == '-':
                self.caselle[posizione_t -1] = 'OUCH!!!'

            elif self.caselle[posizione_t +1] == '-':
                self.caselle[posizione_t +1] = 'OUCH!!!'

        else:
        
            if self.caselle[posizione_t] == '-':

                    self.caselle[posizione_t] = 'T'

            elif self.caselle[posizione_t-1] == '-':

                    self.caselle[posizione_t-1] = 'T'

            elif self.caselle[posizione_t+1] == '-':

                    self.caselle[posizione_t+1] = 'T'     


            if self.caselle[posizione_l] == '-':
                
                    self.caselle[posizione_l] = 'L'

            elif self.caselle[posizione_l-1] == '-':
                
                    self.caselle[posizione_l-1] = 'L'

            elif self.caselle[posizione_l+1] == '-':
                
                    self.caselle[posizione_l+1] = 'L'

            
print(f'BANG !!!!! AND THEY\'RE OFF !!!!!')    

tartaruga: Tartaruga = Tartaruga()

lepre: Lepre = Lepre()

percorso: Percorso = Percorso()

percorso.add_element()

count: int = 0

message: str = ''

while (tartaruga.casella < 69)and(lepre.casella < 69):

    if (count % 10) == 0:

        percorso.meteo = not(percorso.meteo)

    count += 1

    percorso.gara(tartaruga, lepre)


    for i in percorso.caselle:

        message = message + f'{i} '

    #print(f'Lepre: {lepre.casella}, {lepre.energia}\nTartaruga: {tartaruga.casella}, {tartaruga.energia}')
    print(f'{message}\n')
    message = ''



if (tartaruga.casella >= 69)and(lepre.casella >= 69):

    print(f"IT'S A TIE.")

elif tartaruga.casella >= 69:

    print(f"TORTOISE WINS! || VAY!!!")

else:

    print(f'"HARE WINS || YUCH!!!"')
