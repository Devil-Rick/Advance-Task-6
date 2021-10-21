"""
Task

You are given two integer arrays of size N X M and M X P ( N & M are rows, and P is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers N , M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size ( N + M ) X P.
"""

import numpy as np
N, M, P = map(int, input().split())
w = []
for i in range(N):
    x = list(map(int, input().split()))[:P]
    w.append(x)
for j in range(M):
    y = list(map(int, input().split()))[:P]
    w.append(y)
print(np.array(w))
