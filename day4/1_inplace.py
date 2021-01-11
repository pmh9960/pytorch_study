from debug_utils import _ns

import torch
import torch.nn as nn

device = torch.device("cuda:0")
a = torch.randn((100, 100, 100), device=device, requires_grad=True)  # 3.8 MiB / 3.8 MiB

# # 1. Normal operation
# a = a + 1  # 3.8 MiB / 7.6 MiB

# # 2. In-place operation
# a += 1  # requires_grad=False인 경우 3.8 MiB / 3.8 MiB & True 인 경우 error
# # ERROR: a leaf Variable that requires grad is being used in an in-place operation.

# a가 더 이상 leaf node가 아니다.
# Leaf node가 아니라면 inplace 연산을 해도 된다. (why?)
a = a * 1

# # Pytorch에서 함수 뒤에 _가 있는 경우는 보통 inplace 연산
# torch.relu_(a)

# # Scenario 1 (Error is occured)
# a = torch.sigmoid(a)
# a += 1 (a = a + 1 : no error)
# a.mean().backward()

# # Scenario 2 (Error is not occured)
# a = torch.relu(a)
# a += 1  # dirty output
# a.mean().backward()

# Scenario 3 (Error is occured)
b = torch.relu(a)
a += 1  # dirty input
b.mean().backward()

print("Good")
