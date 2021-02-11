import torch
import torch.nn as nn
import torch.autograd.profiler as profiler

device = torch.device("cuda:0")


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )

        self.fc = nn.Sequential(nn.Linear(2048, 512), nn.ReLU(), nn.Linear(512, 10))

    def forward(self, input_tensor):
        output = self.seq(input_tensor)
        return self.fc(output.flatten(start_dim=1))


if __name__ == "__main__":
    # 실제로 상용화 할 때는 profiling은 굉장한 속도 저하.
    with profiler.profile(use_cuda=True) as prof:
        with profiler.record_function("initialize"):
            input_image = torch.rand((4, 1, 64, 64))
            model = Model()
            model.to(device)

        # Model에 처음 데이터가 들어가면 memory 할당을 진행해주는데 이 과정이 오래걸림.
        with profiler.record_function("model first input"):
            input_image = input_image.to(device)
            output = model(input_image)
            torch.cuda.synchronize()

        with profiler.record_function("infer"):
            # * 2. Synchronize는 최대한 덜해라.
            # * 언제 Synchronize가 일어나는가? : device간 데이터를 옮길 때.
            # input_image = torch.rand((4, 1, 64, 64))
            # input_image = input_image.to(device) # to를 사용하여 sync가 일어남.

            # 해당 device에서 바로 생성
            input_image = torch.rand((4, 1, 64, 64), device=device)

            output = model(input_image)
            loss = output.mean()  # loss가 아니지만 대충.

        print(loss.item())

    print(prof.export_chrome_trace("at_least_sync.trace"))
