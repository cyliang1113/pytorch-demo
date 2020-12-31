import torch

x = torch.rand(10)
print(x)
print(x.size())

y = torch.rand(10, 2)
print(y)
print(y.size())


z = torch.zeros(10, 2)
print(z)
print(z.size())