import unittest
from aaindex1 import AAindex1 as a1
import random

class AAindex1TestCase(unittest.TestCase):
    def setUp(self):
        self.testA1 = a1()
        
    def test_get_all_aaindex1_data(self):
        result = self.testA1.get_all_aaindex1_number()
        self.assertEqual(result, 566)

    def test01_get_all_aaindex1_names(self):
        result = self.testA1.get_all_aaindex1_names()
        test_data = "alpha-CH chemical shifts (Andersen et al., 1992)"
        self.assertIn(test_data, result)

    def test02_get_all_aaindex1_names(self):
        result = self.testA1.get_all_aaindex1_names()
        test_data = "Scaled side chain hydrophobicity values (Black-Mould, 1991)"
        self.assertIn(test_data, result)
    
    def test01_get_amino_values(self):
        result = self.testA1.get_amino_values()
        test_data = random.choice(list(self.testA1.get_amino_values().keys()))
        self.assertIn(test_data, result)
    
    def test_get_amino_values_list(self):
        # 特徴量が21要素からなるか（[idx, A, L, R, ...]）
        idx = random.randint(0, self.testA1.get_all_aaindex1_number() - 1)
        result = len(self.testA1.get_amino_values_list()[idx])
        test_data = 21
        self.assertEqual(test_data, result)



if __name__ == "__main__":
    unittest.main()