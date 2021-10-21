'''
Task

You are given a 2-D array with dimensions N X M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

Compute the sum along axis 0. Then, print the product of that sum.
'''

import numpy as np
n, m = map(int, input().split())
x = np.array([input().split() for _ in range(n)], int)[:m]
print(np.prod(np.sum(x, axis=0)))
