from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, id_code: str) -> None:
        super().__init__(first_name, last_name)

        if type(id_code) == str:

            self.id_code = id_code

        else:

            self.id_code = None

    def setIdCode(self, id_code: str):

        if type(id_code) == str:

            self.id_code = id_code

        else:

            print(f'L\'id code inserito non è una stringa!')

    def getIdCode(self):

        return self.id_code
    
    def patientInfo(self):

        print(f'Paziente: {self.getName()} {self.getLastName()}\n'\
              +f'ID: {self.getIdCode()}')