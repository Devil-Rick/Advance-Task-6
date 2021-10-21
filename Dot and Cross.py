'''
Task

You are given two arrays  A and B . Both have dimensions of N X N.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N .
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.
'''

import numpy as np
m = int(input())
n = np.array([input().split() for _ in range(m)], int)[:m]
q = np.array([input().split() for _ in range(m)], int)[:m]

print(np.dot(n, q))
