class Persona:

    def __init__(self, first_name: str, last_name: str) -> None:
        
        name: bool = False
        surname: bool = False

        if type(first_name) == str:

            self.first_name = first_name
            name = True

        else:

            self.first_name = None
            print(f"Il nome inserito non è una stringa!")
            

        if type(last_name) == str:

            self.last_name = last_name
            surname = True
            
        else:

            self.last_name = None
            print(f"Il cognome inserito non è una stringa!")

        if name and surname:

            self.age = 0

        else:

            self.age = None

    def setName(self, first_name: str):

        if type(first_name) == str:

            self.first_name = first_name

        else:

            return(f"Il nome inserito non è una stringa!")

    def setLastName(self, last_name: str):

        if type(last_name) == str:

            self.last_name = last_name

        else:

            return(f"Il cognome inserito non è una stringa!")

    def setAge(self, age: int):

        if type(age) == int:

            self.age = age

        else:
        
            return(f"L'età inserita non è un intero!")

    def getName(self):

        return self.first_name

    def getLastName(self):

        return self.last_name

    def getAge(self):

        return self.age
    
    def greet(self):

        print(f'Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!')