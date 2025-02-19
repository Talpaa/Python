class Animal:
    # - name
    # - zampe
    # - occhi
    # - coda
    # - zanne

    def __init__(self,name: str, zampe: int, occhi: int, coda: bool, zanne: bool) -> None:
        
        self.name = name
        self.zampe = zampe
        self.occhi = occhi
        self.coda = coda
        self.zanne = zanne

    def __str__(self) -> str:
        
        if (self.coda == True)and(self.zanne == True):
        
            return f"{self.name.upper()}: \nha {self.zampe} zampe, ha {self.occhi} occhi ed ha sia zanne che coda"
        
        elif (self.coda == True)and(self.zanne == False):

            return f"{self.name.upper}: \nha {self.zampe} zampe, ha {self.occhi} occhi ed ha la coda"

        elif (self.coda == False)and(self.zanne == True):

            return f"{self.name.upper}: \nha {self.zampe} zampe, ha {self.occhi} occhi ed ha le zanne"

        else:

            return f"{self.name.upper}: \nha {self.zampe} zampe, ha {self.occhi} occhi ed non ha ne zanne ne coda"
        

animali: list[Animal] = [Animal("formica",6,2,False,True),
                         Animal("elefante",4,2,True,True),
                         Animal("gatto",4,2,True,False),
                         Animal("rana",4,2,False,False)]

for i in animali:

    print(i)