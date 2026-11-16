import os
import pandas as pd
import torch.utils.data
from PIL import Image

class MirFlickr25kDataset(torch.utils.data.Dataset):

    def __init__(self, split, missing_type, missing_rate, **kwargs):
        super().__init__()
        dataframe = pd.read_pickle(os.path.join('dataset', 'mirflickr25k', f'{split}.pkl'))
        if missing_type == 'Image' or missing_type == 'Text':
            missing_table = pd.read_pickle('dataset/missing_table/single/mirflickr25k/missing_table.pkl')
        elif missing_type == 'Both':
            missing_table = pd.read_pickle('dataset/missing_table/both/mirflickr25k/missing_table.pkl')
        dataframe = pd.merge(dataframe, missing_table, on='item_id')
        self.missing_type = missing_type
        self.id_list = dataframe['item_id'].tolist()
        self.text_list = dataframe['text'].tolist()
        self.label_list = dataframe['label'].tolist()
        self.missing_mask_list = dataframe[f'missing_mask_{int(10 * missing_rate)}'].tolist()
        self.q_i_list = dataframe['q_i'].tolist()
        self.q_t_list = dataframe['q_t'].tolist()

    def __getitem__(self, index):
        text = self.text_list[index]
        image = Image.open(os.path.join(os.environ.get('CSR_MIRFLICKR_ROOT', 'dataset/mirflickr25k/raw'), 'imgs', 'mirflickr', f'im{int(self.id_list[index]) + 1}.jpg')).convert('RGB')
        if self.missing_type in ('Text', 'Both') and self.missing_mask_list[index] == 0:
            text = 'I love deep learning' * 1024
        return {'image': image, 'text': text, 'label': self.label_list[index], 'missing_mask': self.missing_mask_list[index], 'q_i': self.q_i_list[index], 'q_t': self.q_t_list[index]}

    def __len__(self):
        return len(self.text_list)
