# Bài 1
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        # Lấy giá trị lớn nhất để ổn định số học
        x_max = torch.max(x, dim=0, keepdim=True).values
        x_exp = torch.exp(x - x_max)  # Trừ giá trị lớn nhất trước khi tính exp
        partition = x_exp.sum(dim=0, keepdim=True)  # Tổng của các giá trị exp
        return x_exp / partition


# Test the Softmax class
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
assert round(output[-1].item(), 2) == 0.67
print(output)  # Expected: tensor([0.0900, 0.2447, 0.6652])

# Test the SoftmaxStable class
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
assert round(output_stable[-1].item(), 2) == 0.67
print(output_stable)  # Expected: tensor([0.0900, 0.2447, 0.6652])
