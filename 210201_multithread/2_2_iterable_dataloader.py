import torch
from torch.utils.data import DataLoader, IterableDataset, get_worker_info


class MyIterableDataset_Naive(IterableDataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for sample in self._data:
            # yield : return과 같이 값을 반환하지만 한 번 반환한 값은 두 번째에는 무시.
            yield sample
        return


class MyIterableDataset_1(IterableDataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for idx, sample in enumerate(self._data):
            if idx % get_worker_info().num_workers != get_worker_info().id:
                continue
            yield sample
        return


class MyIterableDataset_2(IterableDataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        worker_info = get_worker_info()
        data = self._data[worker_info.id :: worker_info.num_workers]
        for sample in data:
            yield sample
        return


def worker_init_fn(worker_id):
    worker_info = get_worker_info()
    worker_info.dataset._data = worker_info.dataset._data[
        worker_id :: worker_info.num_workers
    ]


if __name__ == "__main__":
    data = list(range(100))
    iter_dataset = MyIterableDataset_Naive(data)
    iter_loader = DataLoader(
        iter_dataset, batch_size=4, num_workers=3, worker_init_fn=worker_init_fn
    )
    """
    Note:
    1. Iterable dataset의 경우 shuffle=True로 킬 수 없어서 따로 만들어줘야 한다.
    2. Iterable dataset의 num_workers=0,1은 잘 작동하지만, num_workers=2인 경우는?
    이 때 모든 batch가 두 번씩 출력된다.
    (WHY?) Iterable data는 index를 나눠줄 수 없어, 각각의 loader에 모든 index가 들어간다.
    3. MyIterableDataset_1, MyIterableDataset_2처럼 짠다고 하면 중복의 문제는 해결.
    4. 이 때의 문제점은 loader가 각 epoch마다 data index를 나눠줘야 한다.
    => ** MyIterableDataset_Naive를 쓰되 workder_init_fn 사용. **
    """

    for epoch in range(3):
        for batch in iter_loader:
            print(batch)
