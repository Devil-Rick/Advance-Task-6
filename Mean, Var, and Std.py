'''
Task

You are given a 2-D array of size N X M.
Your task is to find:

1. The mean along axis 1
2. The var along axis 0
3. The std along axis None

Input Format

The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

First, print the mean.
Second, print the var.
Third, print the std.

'''

import numpy as np
n, m = map(int, input().split())
x = np.array([input().split() for _ in range(n)], int)[:m]
print(np.mean(x, axis=1))
print(np.var(x, axis=0))
print(round(np.std(x), 11))
