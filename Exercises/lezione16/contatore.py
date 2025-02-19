class Contatore:

    def __init__(self) -> None:
        
        self.contatore: int = 0

    def set_zero(self):

        self.contatore = 0

    def add1(self):

        self.contatore += 1

    def sub1(self):

        if self.contatore >= 1:

            self.contatore -= 1
        else:
            print(f'Non è possibile eseguire la sottrazione')

    def get(self)->int:

        return self.contatore
    
    def mostra(self):

        print(f'Conteggio attuale: {self.get()}')


print()
print()
print()


 	

c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.set_zero()
c.mostra()