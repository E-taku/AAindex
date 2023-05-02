import unittest
from aaindex1 import AAindex1 as a1
from makeData import MakeDataset as md
import random

class AAindex1TestCase(unittest.TestCase):
    def setUp(self):
        self.testMd = md()
        self.seq: str = "MLWQKPTAPEQAPAPARPYQGVRVKEPVKELLRRKRGHASSGAAPAPTAVVLPHQPLATYTTVGPSCLDMEGSVSAVTEEAALCAGWLSQPTPATLQPLAPWTPYTEYVPHEAVSCPYSADMYVQPVCPSYTVVGPSSVLTYASPPLITNVTTRSSATPAVGPPLEGPEHQAPLTYFPWPQPLSTLPTSTLQYQPPAPALPGPQFVQLPISIPEPVLQDMEDPRRAASSLTIDKLLLEEEDSDAYALNHTLSVEGF"
        
    def test_get_dummy_seq(self):
        window_size = 15
        seq_size = len(self.seq)
        result = len(self.testMd.make_dummy_seq(window_size, self.seq))
        test_data = seq_size + window_size - 1
        self.assertEqual(result, test_data)

if __name__ == "__main__":
    unittest.main()