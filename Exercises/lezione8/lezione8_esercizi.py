#specie age
#

class Animal:

    def __init__(self, 
                 species: str,
                 age: str) -> None:
        
        self.species: str = species
        self.age: str = age

    def __str__(self) -> str:
        
        return f'(Specie: {self.species}, Età: {self.age})'



class Rabbit(Animal):

    def __init__(self, 
                 species: str, 
                 age: str) -> None:
        super().__init__(species, age)


class Cat(Animal):

    def __init__(self, 
                 species: str, 
                 age: str,
                 name: str) -> None:
        super().__init__(species, age)
        self.name: str = name

    def speak(self)->str:

        return 'Miao'


class Person(Animal):

    def __init__(self, 
                 species: str, 
                 age: str,
                 name: str,
                 surname: str,
                 cf: str) -> None:
        super().__init__(species, age)

        self.name: str = name
        self.surname: str = surname
        self.cf: str = cf

    def speak(self)-> str:

        return f'Ciao mi chiamo {self.name} {self.surname} e ho {self.age} anni'

    def __str__(self) -> str:

        return f'{self.name.capitalize()} {self.surname.capitalize()}(cf = {self.cf})'\
            + f'{super().__str__()}'
    
    

p1 = Person(name='Mario', surname='Rossi', cf='bella', age='22', species='Homo Sapiens')
a1 = Animal(species='Balena Balana', age='25')
c1 = Cat(name='Garfield', age='15', species='gatto')

print(p1)
print(a1)
print(c1)


print(p1.speak())

print(c1.speak())
    

        