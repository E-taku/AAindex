from collections import defaultdict
from aaindex import aaindex1
from makeData import MakeDataset
import numpy as np


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
        if len(each_amino["X"]) == 0:
            each_amino["X"] = [0 for _ in range(len(each_amino["M"]))]
        # windowを折り返さずに０埋めする
        each_amino["-"] = [0 for _ in range(len(each_amino["M"]))]
        return each_amino
    
    def get_feature_value_from_seqList(self, windowSeqList, each_amino_val):
        print(len(windowSeqList))
        amino_features = []
        for residue in windowSeqList:
            amino_features.append(each_amino_val[residue])
        return amino_features
    
    def get_all_aminoFeatures(self, seq_list, AA1MD):
        all_amino_features = []
        for seq in seq_list:
            window_seqList = AA1MD.get_window_seqList(15, seq)
            amino_features = self.get_feature_value_from_seqList(window_seqList, each_amino_score)
            all_amino_features.append(amino_features)
        all_amino_features = np.array(all_amino_features)
        return all_amino_features


aa1 = AAindex1()

accession_vals = aa1.get_amino_values()
aa1_names = aa1.get_all_aaindex1_names()
aa1_nums = aa1.get_all_aaindex1_number()

each_amino_score = aa1.get_each_amino_val()
print("each_amino_score",each_amino_score)

# ↓Neprocでいうとpssm(MakeDatasetForLayer1(MakeDataset):)
amino_values_list = aa1.get_amino_values_list()


seq =  "MXTSNEWSSMTSNEWSSMEW"
seq2 =  "MXTSNEWSSMTSNEWSSMEW"
seq = [seq, seq2]


AA1MD = MakeDataset()

all_amino_features = aa1.get_all_aminoFeatures(seq, AA1MD)
print(all_amino_features.shape)
exit()

make_dummy_seq = AA1MD.make_dummy_seq(15, seq)
print(make_dummy_seq)
print(len(make_dummy_seq))

window_dataset = AA1MD.make_data_with_window(seq, make_dummy_seq, 15, each_amino_score)
print("seq", len(seq))
print("window_dataset", len(window_dataset))
print("window_dataset", len(window_dataset[1]))

window_dataset_transformation = AA1MD.make_narray_shape_transformation_whole(window_dataset)
print("window_dataset_transformation", window_dataset_transformation)
print("window_dataset_transformation", window_dataset_transformation.shape)