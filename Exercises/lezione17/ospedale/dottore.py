from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)

        if type(specialization) == str:

            self.specialization = specialization

        else:

            self.specialization = None

        if type(parcel) == float or type(parcel) == int:

            self.parcel = float(parcel)

        else: 
            self.parcel = None

    def setSpecialization(self, specialization: str):

        if type(specialization) == str:

            self.specialization = specialization

        else:

            return f'La specializzazione inserita non è una stringa!'

    def setParcel(self, parcel: float):

        if type(parcel) == float or type(parcel) == int:

            self.parcel = float(parcel)

        else:

            return f'Il valore della parcella non è un float!'

    def getSpecialization(self):

        return self.specialization

    def getParcel(self):

        return self.parcel
    
    def isAValidDoctor(self):
        
        if type(self.getAge()) == int:

            if self.getAge() >= 30:

                return(f"Doctor {self.getName()} {self.getLastName()} is valid!")
                
        return(f"Doctor {self.getName()} {self.getLastName()} is not valid!")
    
    def doctorGreet(self):

        self.greet()

        print(f'Sono un medico {self.getSpecialization()}')

