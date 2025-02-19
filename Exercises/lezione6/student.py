#esercizio 2
class Student:

    # - name
    # - age
    # - gender
    # - study program
    def __init__(self, name: str, age: int, gender: str, study_program: str) -> None:
        
        self.name = name
        self.age = age
        self.gender = gender
        self.study_program = study_program

    def __str__(self) -> str:
        
        return f"Il nome dello studente è {self.name} ha {self.age} anni il suo gender è {self.gender} e il suo percorso di studi è {self.study_program}"  
print('\n\n\n')
students: list[Student] = [Student("Mario Rossi", 24, "Male", "Fullstack"),
                           Student("Francesco Verdi", 19, "Male", "Cloud"),
                           Student("Sofia Proietti", 35, "Female", "Cyber Security")
                           ]

for i in students:

    print(i)