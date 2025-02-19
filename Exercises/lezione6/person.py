#esercizo 1
class Person:

    # - name
    # - surname
    # - age

    def __init__(self, name: str, age: int) -> None:
        
        self.name = name

        self.age = age




alice = Person("Alice W.", 45)

bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:

    print(alice.name)

else:

    print(bob.name)

persons: list[Person] = [alice, bob,
                         Person("Luca Verdi", 27),
                         Person("Francesco Totti", 52),
                         Person("Mario Rossi", 84)]

youngest: Person = alice

for person in persons:

    if person.age < youngest.age:

        youngest = person


print(youngest.name)