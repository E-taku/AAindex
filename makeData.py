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
            # print("idx1", idx, "idx+window", idx+window)
            for idx2 in dummy_seq[idx:idx+window]:
                amino_name = amino_seq[idx2]
                # print(amino_seq[idx2], idx)
                # print("amino_name", amino_name)
                each_site.append(each_amino_score[amino_name])
            # print("each_site: ",len(each_site))
            dataset.append(each_site)
            # print(len(dataset))
        # return dataset
        return np.array(dataset, np.float64)
        

    
    def make_narray_shape_transformation_whole(self,pssm_n):
        """
        Args:
            pssm_n (_numpy.ndarray_): pssm with window size n
            data_no (_list_): idx of list
            
        Returns:
            dataset _numpy.ndarray_: Convert to 393*315 dimensions
        """
        return np.reshape(pssm_n, (len(pssm_n), (len(pssm_n[0])*len(pssm_n[0][0]))))
    
        # dataset = []
        # for idx in range(len(pssm_n)):
        #     print(pssm_n[idx])
        #     print(len(pssm_n[idx]))
        #     tmp_dataset = []
        #     for idx2 in range(len(pssm_n[idx])):
        #         print(pssm_n[idx][idx2])
        #         print(len(pssm_n[idx][idx2]))
        #         tmp_dataset.append(pssm_n[idx][idx2])
        #     print(len(tmp_dataset))
        #     dataset.append(tmp_dataset)
        # dataset = np.array(dataset, np.float32)
        # return dataset    
            
            
        #     pssm_dimension_1 = np.array(pssm_n[idx][0].flatten(),np.float32)
        #     dataset.append(pssm_dimension_1)
        # return np.array(dataset,np.float32)