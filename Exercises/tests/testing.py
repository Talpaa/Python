import unittest

from ..ripasso.ripasso import Calc #import relativo(al file in cui mi trovo)

#from ripasso.ripasso import Calc

class TestCalculation(unittest.TestCase):

    def setUp(self):
        
        self.calculation = Calc(8, 2)

    def test_sum(self):

        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong')


if __name__ == '__main__':
    unittest.main()