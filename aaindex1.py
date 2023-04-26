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
        accession_vals: dict = defaultdict(dict)
        for accession in self.all_aaindex1_data:
            accession_vals[accession] = self.all_aaindex1_data[accession]['values']
        return accession_vals
    
    def get_amino_values_list(self) -> list:
        values_list = list()
        accession_vals: dict = self.get_amino_values()
        for acc, values_dic in accession_vals.items():
            tmp_val_list: list = [acc]
            for amino_query in values_dic:
                if amino_query == '-':
                    continue
                tmp_val_list.append(values_dic[amino_query])
            values_list.append(tmp_val_list)
        return values_list
    
    

aa1 = AAindex1()
# print(aa1.get_all_aaindex1_names())

accession_vals = aa1.get_amino_values()
for k, v in accession_vals.items():
    print(k, v)

aa1_names = aa1.get_all_aaindex1_names()
# print(aa1_names)
aa1_nums = aa1.get_all_aaindex1_number()
# print(aa1_nums)

amino_values_list = aa1.get_amino_values_list()
print(amino_values_list)
print(len(amino_values_list))
# print(aa1.all_aaindex1_data)