import torch

device = torch.device("cuda:0")

a = torch.randn((100, 100, 100), device=device, requires_grad=True)
a = a * 1


def silu(tensor):
    """
    Memory 사용량 : 3 * tensor
    1. tensor
    2. sigmoid
    3. *
    """
    return tensor * torch.sigmoid(tensor)


def silu_inplace(tensor):
    return tensor * torch.sigmoid_(tensor)


def silu_inplace_fix(tensor):
    """
    silu 함수보다 메모리 사용량이 적다.
    
    Memory 사용량 : 3 * tensor
    1. tensor
    2. result
    """
    result = tensor.clone()
    torch.sigmoid_(tensor)
    tensor *= result
    return tensor


# silu(a)
# silu_inplace_fix(a)

# backward에서 Error도 안뜸. 그런데 forward에서 silu와 silu_inplace의 값이 다르다.
# (Debug console에서 찍어볼 것)
silu_inplace(a).mean().backward()

print("Good")
