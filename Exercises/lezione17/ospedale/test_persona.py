import unittest

from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class testPersona(unittest.TestCase):

    def setUp(self) -> None:
        
        self.persona = Persona(first_name=12,last_name=True)

    def test_Initialisation(self):
        
        self.persona.setName(first_name='Mario')
        self.persona.setLastName(last_name='Rossi')
        self.persona.setAge(age=24)
        
        self.assertEqual(self.persona.getName(), 'Mario', f'Error: should return \'Mario\' not \'{self.persona.getName()}\'')
        self.assertEqual(self.persona.getLastName(), 'Rossi', f'Error: should return \'Rossi\' not \'{self.persona.getLastName()}\'')
        self.assertEqual(self.persona.getAge(), 24, f'Error: should return \'24\' not \'{self.persona.getAge()}\'')

    def test_Initialisation_None(self):

        self.assertEqual(self.persona.getName(), None, f'Error: should return \'None\' not \'{self.persona.getName()}\'')
        self.assertEqual(self.persona.getLastName(), None, f'Error: should return \'None\' not \'{self.persona.getLastName()}\'')
        self.assertEqual(self.persona.getAge(), None, f'Error: should return \'None\' not \'{self.persona.getAge()}\'')

    def test_set(self):

        self.persona.setName(first_name=1)
        self.persona.setLastName(last_name=2)
        self.persona.setAge(age='ds')
         
        self.assertEqual(self.persona.getName(), None, f'Error: should return \'None\' not \'{self.persona.getName()}\'')
        self.assertEqual(self.persona.getLastName(), None, f'Error: should return \'None\' not \'{self.persona.getLastName()}\'')
        self.assertEqual(self.persona.getAge(), None, f'Error: should return \'None\' not \'{self.persona.getAge()}\'')


class testDottore(unittest.TestCase):
     
    def setUp(self) -> None:
          
        self.dottore = Dottore(first_name=12, last_name=True, specialization=34, parcel='t')
        self.dottore1 = Dottore(first_name='b', last_name='a', specialization='', parcel=1.23)
        self.dottore2 = Dottore(first_name='c', last_name='e', specialization='', parcel=2.34)
        self.dottore3 = Dottore(first_name='d', last_name='i', specialization='', parcel=3.45)


    def test_Initialisation(self):
        
        self.dottore.setName(first_name='Mario')
        self.dottore.setLastName(last_name='Rossi')
        self.dottore.setAge(age=24)
        self.dottore.setSpecialization(specialization='Neurologo')
        self.dottore.setParcel(parcel=538.76)
        
        self.assertEqual(self.dottore.getName(), 'Mario', f'Error: should return \'Mario\' not \'{self.dottore.getName()}\'')
        self.assertEqual(self.dottore.getLastName(), 'Rossi', f'Error: should return \'Rossi\' not \'{self.dottore.getLastName()}\'')
        self.assertEqual(self.dottore.getAge(), 24, f'Error: should return \'24\' not \'{self.dottore.getAge()}\'')
        self.assertEqual(self.dottore.getSpecialization(), 'Neurologo', f'Error: should return \'Neurologo\' not \'{self.dottore.getSpecialization()}\'')
        self.assertEqual(self.dottore.getParcel(), 538.76, f'Error: should return \'538.76\' not \'{self.dottore.getParcel()}\'')

    def test_Initialisation_None(self):

        self.assertEqual(self.dottore.getName(), None, f'Error: should return \'None\' not \'{self.dottore.getName()}\'')
        self.assertEqual(self.dottore.getLastName(), None, f'Error: should return \'None\' not \'{self.dottore.getLastName()}\'')
        self.assertEqual(self.dottore.getAge(), None, f'Error: should return \'None\' not \'{self.dottore.getAge()}\'')
        self.assertEqual(self.dottore.getSpecialization(), None, f'Error: should return \'None\' not \'{self.dottore.getSpecialization()}\'')
        self.assertEqual(self.dottore.getParcel(), None, f'Error: should return \'None\' not \'{self.dottore.getParcel()}\'')

    def test_set(self):

        self.dottore.setName(first_name=1)
        self.dottore.setLastName(last_name=2)
        self.dottore.setAge(age='f')
        self.dottore.setSpecialization(specialization=3)
        self.dottore.setParcel(parcel='t')
         
        self.assertEqual(self.dottore.getName(), None, f'Error: should return \'None\' not \'{self.dottore.getName()}\'')
        self.assertEqual(self.dottore.getLastName(), None, f'Error: should return \'None\' not \'{self.dottore.getLastName()}\'')
        self.assertEqual(self.dottore.getAge(), None, f'Error: should return \'None\' not \'{self.dottore.getAge()}\'')
        self.assertEqual(self.dottore.getSpecialization(), None, f'Error: should return \'None\' not \'{self.dottore.getSpecialization()}\'')
        self.assertEqual(self.dottore.getParcel(), None, f'Error: should return \'None\' not \'{self.dottore.getParcel()}\'')

    def test_isAValidDoctor(self):

        self.assertEqual(self.dottore1.getAge(), 0, f'Error: should return 0 not \'{self.dottore1.getAge()}\'')
        self.assertEqual(self.dottore2.getAge(), 0, f'Error: should return 0 not \'{self.dottore2.getAge()}\'')
        self.assertEqual(self.dottore3.getAge(), 0, f'Error: should return 0 not \'{self.dottore3.getAge()}\'')


        self.dottore1.setAge(age=18)
        self.dottore2.setAge(age=30)
        self.dottore3.setAge(age=45)

        self.assertEqual(self.dottore1.isAValidDoctor(), 'Doctor b a is not valid!', f'Error: should return 0 not \'{self.dottore1.isAValidDoctor()}\'')
        self.assertEqual(self.dottore2.isAValidDoctor(), 'Doctor c e is valid!', f'Error: should return 0 not \'{self.dottore2.isAValidDoctor()}\'')
        self.assertEqual(self.dottore3.isAValidDoctor(), 'Doctor d i is valid!', f'Error: should return 0 not \'{self.dottore3.isAValidDoctor()}\'')
    

class testPaziente(unittest.TestCase):

    def setUp(self) -> None:
        
        self.paziente = Paziente(first_name=12,last_name=True, id_code=23.4)

    def test_Initialisation(self):
        
        self.paziente.setName(first_name='Francesco')
        self.paziente.setLastName(last_name='Totti')
        self.paziente.setIdCode(id_code='1CAP')
        
        self.assertEqual(self.paziente.getName(), 'Francesco', f'Error: should return \'Francesco\' not \'{self.paziente.getName()}\'')
        self.assertEqual(self.paziente.getLastName(), 'Totti', f'Error: should return \'Totti\' not \'{self.paziente.getLastName()}\'')
        self.assertEqual(self.paziente.getIdCode(), '1CAP', f'Error: should return \'1CAP\' not \'{self.paziente.getIdCode()}\'')

    def test_Initialisation_None(self):

        self.assertEqual(self.paziente.getName(), None, f'Error: should return \'None\' not \'{self.paziente.getName()}\'')
        self.assertEqual(self.paziente.getLastName(), None, f'Error: should return \'None\' not \'{self.paziente.getLastName()}\'')
        self.assertEqual(self.paziente.getIdCode(), None, f'Error: should return \'None\' not {self.paziente.getIdCode()}')


class testFattura(unittest.TestCase):

    def setUp(self) -> None:
        
        self.dottore = Dottore(first_name='Claudio', last_name='Pieraccioni', specialization='Neurologo', parcel=538.76)
        self.paziente = Paziente(first_name='Francesco', last_name='Totti', id_code='1CAP')
        self.paziente1 = Paziente(first_name='Mario', last_name='Mario', id_code='JAHU')
        self.paziente2 = Paziente(first_name='Luigi', last_name='Mario', id_code='WAHA')
        self.fattura = Fattura(doctor= self.dottore)

    def test_fattura(self):

        patients=[self.paziente, self.paziente1, self.paziente2]

        self.assertEqual(self.fattura.getSalary(), 0.0, f'Error: should return \'None\' not {self.fattura.getSalary()}')

        for patient in patients:

            self.fattura.addPatient(patient)

        self.assertEqual(self.fattura.getSalary(), 1616.28, f'Error: should return \'1616.28\' not {self.fattura.getSalary()}')
        


if __name__ == '__main__':
    unittest.main()