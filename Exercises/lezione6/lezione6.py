class Person:

    # - name
    # - surname
    # - age

    def __init__(self, name: str, surname: str, age: int) -> None:
        
        self.name = name

        self.surname = surname

        self.age = age

        self.hobbies: set[str] = set()

    def add_hobbies(self, hobbies: list[str]):

        self.hobbies.update(hobbies)

    def add_hobby(self, hobby: str):

        self.hobbies.add(hobby)

    def remove_hobby(self, hobby: str):

        if hobby in self.hobbies:
            self.hobbies.remove(hobby)

    def __str__(self)->str:

        #ogni volta che chiamo un oggetto per printarlo in automatico mi stamperà questo
        return f"\n\nNome = {self.name}; \nCognome = {self.surname}; \nEtà = {self.age}; \nhobbies = {self.hobbies}"

persona = Person("Mario","Rossi", 24) #Person.__init__("Mario", "Rossi", 24)
print(persona)

persona.age = 22
print(f"\nEtà = {persona.age}")


"""name: str = input("\nInserisci il tuo nome: ")
surname: str = input("Inserisci il tuo cognome: ")
age: int = int(input("Inserisci la tua età: "))

user = Person(name, surname, age)
print(user)
print(persona)


avg_age: float = (persona.age + user.age) / 2
print(f"L'età media è :{avg_age}")"""


persons: list[Person]= [Person("Mario", "Rossi", 22),
                       Person("Francesco", "Totti", 52),
                       Person("Mario", "Rossi", 84)]


avg_age = 0

for person in persons:

    avg_age += person.age

avg_age /= len(persons)
print(f"L'età media è :{avg_age}")

persona.add_hobby("Basket")

persona.add_hobby("Rugby")

print(persona)

persona.remove_hobby("Basket")

print(persona)

persona.add_hobbies(["a","b","c"])

print(persona)
