def is_float(num):

    try:
        float(num)
        return True
    
    except ValueError:

        risposta: bool = False

        if num.isdigit():

            risposta = True

        return risposta
    

class Fence:
    
    #-area
    #-temperatura
    #-habitat
    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str) -> None:
        
        while (not(is_float(area)))or(area <= 0):

            print(f'\nL\'area del recinto inserita non è valida')

            area = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

        else:
            self.area: float = float(area)

        while not(is_float(temperature)):

            print(f'\nLa temperatura del recinto inserita non è valida')

            temperature = input(f'Per favore inserisci un valore numerico:     ')

        else:
            self.temperature: float = float(temperature)

        self.habitat: str = habitat
        self.remaining_area: float = area
        self.fauna: list = []

    def __str__(self) -> str:

        message: str = f'\nFence(Area = {round(self.area, 3)} metri quadrati, '\
            f'Area rimasta = {round(self.remaining_area, 3)} metri quadrati, '\
                f'Temperatura: {round(self.remaining_area, 3)} metri quadrati, '\
                    f'Habitat = {self.habitat})\n'\
                        f'Animali nel recinto:\n'
        for animal in self.fauna:

            message += f'\n{animal}'
        
        return message

class Animal:

    #-nome
    #-specie
    #-età
    #-altezza
    #-larghezza
    #-habitat
    #-vita = round(100*(1/età), 3), non è una percentuale
    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 widht: float,
                 preferred_habitat: str,
                 belong_fence: Fence = '') -> None:
        
        self.name: str = name
        self.species: str = species

        while (type(age) != int)or(age <= 0):
            
            print(f'\nL\'età dell\'animale inserita non è valida')

            age = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

            if age.isdigit():

                age = int(age)
        else:
            self.age: int = age

        while (not(is_float(height)))or(height <= 0):

            print(f'\nL\'altezza dell\'animale inserita non è valida')

            height = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

        else:
            self.height: float = float(height)


        while (not(is_float(widht)))or(widht <= 0):

            print(f'\nLa larghezza dell\'animale inserita non è valida')

            widht = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

        else:
            self.widht: float = float(widht)
            
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100*(1/self.age), 3)

        self.belong_fence: Fence = belong_fence

    def __str__(self) -> str:
        
        return f'\nAnimal(Nome:  {self.name}, '\
            +f'Specie: {self.species}, '\
                +f'Età: {self.age}, '\
                    +f'Altezza: {self.height}, '\
                        +f'Larghezza: {self.widht}, '\
                            +f'Habitat: {self.preferred_habitat}, '\
                                +f'Salute: {self.health})\n'



class ZooKeeper:
    
    #-nome
    #-cognome
    #-id
    def __init__(self,
                 name: str,
                 surname: str,
                 id: str) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id

    


    """Consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
    L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
    ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale."""
    def add_animal(self, 
                   animal: Animal, 
                   fence: Fence):
        
        occupied_space: float = round((animal.height * animal.widht), 3)

        if (occupied_space <= fence.remaining_area)and(animal.preferred_habitat == fence.habitat):
            
            fence.fauna.append(animal)

            fence.remaining_area -= occupied_space

            animal.belong_fence = fence

        elif(animal.preferred_habitat != fence.habitat):

            print(f'L\'animale che stai provando ad inserire non è adatto all\'habitat di questo recinto\n' )

        elif (occupied_space > fence.area):

            print(f'L\'animale che stai provando ad inserire è più grande dell\'area rimasta nel recinto\n' )

    """Consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
    L'animale viene allontanato dal suo recinto. 
    L'area del recinto viene ripristinata dello spazio che l'animale rimosso occupava."""
    def remove_animal(self, 
                      animal: Animal, 
                      fence: Fence):
        
        if animal in fence.fauna:

            occupied_space: float = round((animal.height * animal.widht), 3)

            fence.remaining_area += occupied_space
            fence.fauna.remove(animal)

        else:

            print(f'L\'animale che stai provando a rimuovere non è presente in questo recinto\n')

    """Consente al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    Ogni volta che un animale viene nutrito, la sua salute(health) incrementa di 1% rispetto alla sua salute corrente, 
    e le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
    L'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo."""
    def feed(self, 
             animal: Animal):
        
        if animal in animal.belong_fence.fauna:
            increased_height: float = round((animal.height + ((animal.height/100)*2)), 3)
            increased_width: float = round((animal.widht + ((animal.widht/100)*2)), 3)

            dim_re: float = round((animal.belong_fence.remaining_area + (animal.height * animal.widht)), 3)

            increased_animal: float = round((increased_height * increased_width), 3)

            if dim_re >= increased_animal:

                animal.height = increased_height
                animal.widht = increased_width
                animal.health = round((animal.health + (animal.health/100)), 3)

                print(f'L\'animale è stato nutrito\n')

            else:

                print(f'Non puoi nutrire l\'animale scelto perchè una volta nutrito non entrerebbe più nel recinto\n')

        else:

            print(f'L\'animale che vuoi nutrire non è in questo recinto\n')

    """Consente al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
    Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""
    def clean(self, 
              fence: Fence)->float:
        
        time: float = 0.0

        #dimensione area occupata
        #area_occupata: float = fence.area - fence.remaining_area

        #percentuale area occupata
        area_occupata: float = round((fence.area - fence.remaining_area), 3)

        if fence.remaining_area > 0.0:

            time = area_occupata / fence.remaining_area

            return round(time, 3)
        
        else:

            return area_occupata
    
    def __str__(self) -> str:
        
        messaggio: str = f'\nZookeeper(Nome = {self.name}, Cognome = {self.surname}, ID = {self.id}) \n'
        
        return messaggio

class Zoo:
    
    #-recinzioni
    #-guardiani dello zoo
    def __init__(self,
                 fence: list[Fence] = [],
                 zookeeper: list[ZooKeeper] = []) -> None:
        
        self.fence: list[Fence] = fence
        self.zookeeper: list[ZooKeeper] = zookeeper

    def describe_zoo(self):
        
        messaggio: str = f'\nZoo:\n'

        for i in self.zookeeper:

            messaggio += f'{i}\n'

        for j in self.fence:

            messaggio += f'{j}\n'

        return messaggio
    

zk1: ZooKeeper = ZooKeeper('a', 'b', '4144')
zk2: ZooKeeper = ZooKeeper('c', 'd', '4145')

f1: Fence = Fence(1000, 10, 'a')

f2: Fence = Fence(2353, 82, 'f')

a1: Animal =  Animal('a', 'a', 1, 12.52, 14, 'a')
a2: Animal =  Animal('b', 'b', 1, 12.52, 14, 'a')

a3: Animal =  Animal('c', 'd', 1, 12.52, 14, 'f')
a4: Animal =  Animal('c', 'd', 1, 12.52, 14, 'f')

zk1.add_animal(animal=a1, fence=f1)
zk1.add_animal(animal=a2, fence=f1)

zk1.add_animal(animal=a3, fence=f2)
zk1.add_animal(animal=a4, fence=f2)

recinti: list[Fence] = [f1,f2]


guardiani: list[ZooKeeper] = [zk1, zk2]

zoo1: Zoo = Zoo(recinti, guardiani)

print(zoo1.describe_zoo())