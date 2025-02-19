import unittest

from my_math_library import FractionError, NoneNumDenError, NullDenominatorError, UnsupportedOperationError, PersonalizedMathLibrary

class TestMyLibrary(unittest.TestCase):

    def setUp(self) -> None:
        
        self.message: str = ''

        self.frazione1: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=12, denominatore=4)
        self.frazione2: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=7, denominatore=1)
        self.frazione3: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=8, denominatore=2)
        self.frazione4: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=16, denominatore=7)
        self.frazione5: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=1, denominatore=4)
        self.frazione6: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=1, denominatore=4)
        self.frazione7: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=6, denominatore=24)


    def test_semplifica(self):

        #testa se la funzione semplifica restituisce il numeratore e il denominatore semplificati in modo corretto
        self.assertEqual(first=self.frazione1.semplifica(), second=f'{3.0} {1.0}', msg=f'Error: should return \'3.0 1.0\' not {self.frazione1.semplifica()}')
        
        #testa se la funzione non ha niente da semplificare restituisce il numeratore e il denominatore passati
        self.assertEqual(first=self.frazione2.semplifica(), second=f'{7.0} {1.0}', msg=f'Error: should return \'7.0 1.0\' not {self.frazione1.semplifica()}')

    def test_add_fractions(self):

        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione4), second=f'{148.0} {28.0}', msg=f'Error: should return \'37.0 7.0\' not {self.frazione1.add_fractions(self.frazione4)}') 
        
        #testa che se uno dei due denomitatori è multiplo dell'altro allora il denominatore comune sarà uguale al denominatore multiplo dell'altro
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione3), second=f'{28.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.add_fractions(self.frazione3)}')
        
        #testa che se uno dei due denomitatori è 1 il denominatore comune sarà uguale al denominatore non uguale a 1
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione2), second=f'{40.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.add_fractions(self.frazione2)}')

    def test_sub_fractions(self):

        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione4), second=f'{20.0} {28.0}', msg=f'Error: should return \'37.0 7.0\' not {self.frazione1.sub_fractions(self.frazione4)}') 
        
        #testa che se uno dei due denomitatori è multiplo dell'altro allora il denominatore comune sia uguale al denominatore multiplo dell'altro
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione3), second=f'{-4.0} {4.0}', msg=f'Error: should return \'-4.0 4.0\' not {self.frazione1.sub_fractions(self.frazione3)}')
        
        #testa che se uno dei due denomitatori è 1 il denominatore comune sia uguale al denominatore non uguale a 1
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione2), second=f'{-16.0} {4.0}', msg=f'Error: should return \'-16.0 4.0\' not {self.frazione1.sub_fractions(self.frazione2)}')

    def test_multiply_fractions(self):

        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.multiply_fractions(self.frazione4), second=f'{192.0} {28.0}', msg=f'Error: should return \'192.0 28.0\' not {self.frazione1.sub_fractions(self.frazione4)}') 

    def test_divide_fractions(self):

        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.divide_fractions(self.frazione3), second=f'{24.0} {32.0}', msg=f'Error: should return \'24.0 32.0\' not {self.frazione1.divide_fractions(self.frazione3)}') 

    def test_equal_fractions(self):

        #testa che se vengano passsate due frazioni uguali tra loro venga ritornato True
        self.assertEqual(first=self.frazione5.equal_fractions(self.frazione6), second=True, msg=f'Error: should return \'True\' not {self.frazione5.equal_fractions(self.frazione6)}') 
        #testa che se vengano passsate due frazioni diverse tra loro ma che se semplificate diventano uguali venga ritornato True
        self.assertEqual(first=self.frazione5.equal_fractions(self.frazione7), second=True, msg=f'Error: should return \'True\' not {self.frazione5.equal_fractions(self.frazione6)}') 
        #testa che se vengano passsate due frazioni diverse tra loro venga ritornato False
        self.assertEqual(first=self.frazione5.equal_fractions(self.frazione1), second=False, msg=f'Error: should return \'False\' not {self.frazione5.equal_fractions(self.frazione6)}')

if __name__ == '__main__':
    unittest.main()