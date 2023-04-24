from collections import defaultdict
from aaindex import aaindex1

class AAindex1:
    def __init__(self):
        self.all_aaindex1_data: dict = self.get_all_aaindex1_data()
        
    def get_all_aaindex1_names(self) -> list:
        aa1_names = aaindex1.record_names()
        return aa1_names

    def get_all_aaindex1_number(self) -> int:
        aa1_nums = aaindex1.num_records()
        return aa1_nums
    
    def get_all_aaindex1_data(self) -> dict:
        return aaindex1.parse_aaindex()
    
    def get_amino_values(self) -> dict:
        accession_val: dict = defaultdict(dict)
        for accession in self.all_aaindex1_data:
            accession_val[accession] = self.all_aaindex1_data[accession]['values']
        return accession_val

aa1 = AAindex1()
print(aa1.get_all_aaindex1_names())

accession_val = aa1.get_amino_values()
for k, v in accession_val.items():
    print(k, v)

aa1_names = aa1.get_all_aaindex1_names()
print(aa1_names)
aa1_nums = aa1.get_all_aaindex1_number()
print(aa1_nums)
