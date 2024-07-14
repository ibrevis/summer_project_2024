import torch
import numpy as np
from time import sleep, time

device = 'cpu'

A = torch.rand((20000,20000),device=device)
B = torch.rand((20000,20000),device=device)

t0 = time()
for i in range(20):
    torch.matmul(A,B)
    print(i)
    #sleep(2)
print((time() - t0)/60,' [min]')  



