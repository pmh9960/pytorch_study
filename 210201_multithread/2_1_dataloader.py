import torch
from torch.utils.data import Dataset, DataLoader

torch.manual_seed(1234)


class MyDataset(Dataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


if __name__ == "__main__":
    data = list(range(100))
    dataset = MyDataset(data)
    loader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=0)
    # num_workers=0,1,2 어떤 것으로 돌려도 shuffle된 결과는 같다.

    for batch in loader:
        print(batch)
