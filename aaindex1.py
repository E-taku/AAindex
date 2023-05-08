from collections import defaultdict
from aaindex import aaindex1
from makeData import MakeDataset

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
        """
        return : [
            [idx, A_val, C_val, ...]
            :
            :
        ]
        """
        values_list = list()
        accession_vals: dict = self.get_amino_values()
        for i, values_dic in enumerate(accession_vals.values()):
            tmp_val_list: list = [i]
            for amino_query in values_dic:
                if amino_query == '-':
                    continue
                tmp_val_list.append(values_dic[amino_query])
            values_list.append(tmp_val_list)
        return values_list

    def get_each_amino_val(self) -> dict:
        each_amino = defaultdict(list)
        accession_vals: dict = self.get_amino_values()
        for values_dic in accession_vals.values():
            for key, amino_val in values_dic.items():
                if key == "-":
                    continue
                each_amino[key].append(amino_val)
        return each_amino
    
    

aa1 = AAindex1()

accession_vals = aa1.get_amino_values()
aa1_names = aa1.get_all_aaindex1_names()
aa1_nums = aa1.get_all_aaindex1_number()

each_amino_score = aa1.get_each_amino_val()

# ↓Neprocでいうとpssm(MakeDatasetForLayer1(MakeDataset):)
amino_values_list = aa1.get_amino_values_list()

seq: str = "MLWQKPTAPEQAPAPARPYQGVRVKEPVKELLRRKRGHASSGAAPAPTAVVLPHQPLATYTTVGPSCLDMEGSVSAVTEEAALCAGWLSQPTPATLQPLAPWTPYTEYVPHEAVSCPYSADMYVQPVCPSYTVVGPSSVLTYASPPLITNVTTRSSATPAVGPPLEGPEHQAPLTYFPWPQPLSTLPTSTLQYQPPAPALPGPQFVQLPISIPEPVLQDMEDPRRAASSLTIDKLLLEEEDSDAYALNHTLSVEGF"
AA1MD = MakeDataset()
make_dummy_seq = AA1MD.make_dummy_seq(15, seq)

window_dataset = AA1MD.make_data_with_window(seq, make_dummy_seq, 15, each_amino_score)
window_dataset_transformation = AA1MD.make_narray_shape_transformation_whole(window_dataset)

print("window_dataset", window_dataset)
print("window_dataset", window_dataset.shape)
print("window_dataset_transformation", window_dataset_transformation)
print("window_dataset_transformation", window_dataset_transformation.shape)