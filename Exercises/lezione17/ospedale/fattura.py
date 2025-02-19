from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, doctor: Dottore) -> None:
        
        if (type(doctor) == Dottore)and(doctor.isAValidDoctor()):
            self.patients: list[Paziente] = []
            self.doctor = doctor
            self.fatture = len(self.patients)
            self.salary = 0

        else:

            self.patients = None
            self.doctor = None
            self.salary = None
            self.fatture = None
            print(f"Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):

        if (type(self.doctor.getParcel()) == float)and(type(self.fatture) == int): # type: ignore
            
            self.fatture = len(self.patients)
            self.salary = self.fatture * self.doctor.getParcel()
            return self.salary

        elif (self.doctor.getParcel() == None)and(self.fatture == None): # type: ignore

            print(f'Il dottore non ha settato un valore per la parcella!')
            print(f'Il dottore non ha pazienti')

        elif (self.doctor.getParcel() == None): 

            print(f'Il dottore non ha settato un valore per la parcella!')

        elif (self.fatture == None):

            print(f'Il dottore non ha pazienti')

        return None

    def getFatture(self):

        if type(self.patients) == list[Paziente]:

            self.fatture = len(self.patients)

            return self.fatture
        
        else:

            return None
        
    def addPatient(self, patient: Paziente):

        if type(patient) == Paziente:

            if self.patients == None:

                self.patients = []

            self.patients.append(patient)
            self.getFatture()
            self.getSalary()
            print(f'Alla lista del Dottor {self.doctor.last_name} è stato aggiunto il paziente {patient.id_code}') #type: ignore

        else:

            print('Il paziente non può essere aggiunto!')

    def removePatient(self, id_patient: str):

        controllo: bool = False

        if type(self.patients) == list[Paziente]:

            for patient in self.patients:

                if patient.getIdCode() == id_patient:

                    self.patients.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    controllo = True

        if controllo:

            print(f'Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {id_patient}') #type: ignore



