import unittest
from Generaldistribution import Distribution


class TestDistributionClass(unittest.TestCase):
    def setUp(self):
        self.Distribution = Distribution(25, 2)

    def test_initialization(self): 
        self.assertEqual(self.Distribution.mean, 25, 'incorrect mean')
        self.assertEqual(self.Distribution.stdev, 2, 'incorrect standard deviation')

    def test_pdf(self):
        self.assertEqual(round(self.Distribution.pdf(25), 5), 0.19947,
         'pdf function does not give expected result') 

    def test_meancalculation(self):
        self.Distribution.read_data_file('numbers.txt', True)
        self.assertEqual(self.Distribution.calculate_mean(),\
         sum(self.Distribution.data) / float(len(self.Distribution.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.Distribution.read_data_file('numbers.txt', True)
        self.assertEqual(round(self.Distribution.stdev, 2), 92.87, 'sample standard deviation incorrect')
        self.Distribution.read_data_file('numbers.txt', False)
        self.assertEqual(round(self.Distribution.stdev, 2), 88.55, 'population standard deviation incorrect')
                
    
if __name__ == '__main__':
    unittest.main()