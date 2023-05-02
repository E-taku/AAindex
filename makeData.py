import numpy as np

class MakeDataset(object):
    def make_dummy_seq(self, window, q_list):
        """
        q_list : list
        window : window size 

        return :
            li : list of idx
        """
        li = []
        for idx in range(0, int(window/2)):
            li.append(idx)
        for idx in range(len(q_list)):
            li.append(idx)
        for idx in range(len(q_list) - int(window/2), len(q_list)):
            li.append(idx)
        return li
    
    def make_data_with_window(self, amino_seq, dummy_seq, window, each_amino_score):
        dataset = []
        for idx in range(len(amino_seq)):  # index of amino_seq
            each_site = list()
            for idx2 in dummy_seq[idx:idx+window]:
                amino_name = amino_seq[idx2]
                each_site.append(each_amino_score[amino_name])
            dataset.append(each_site)
        return np.array(dataset, np.float32)
    