"""
Task

You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of N  and M.
The next  lines contains N the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten
"""

import numpy as np
N, M = map(int, input().split())
l = []
for i in range(N):
    n = list(map(int, input().split()))[:M]
    l.append(n)
x = np.array(l)
print(np.transpose(x))
print(x.flatten())
