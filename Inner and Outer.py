"""
Task

You are given two arrays: A and B .
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array A .
The second line contains the space separated elements of array B .

Output Format

First, print the inner product.
Second, print the outer product.

Sample Input
"""


import numpy as np
A, B = [np.array([input().split()], int) for _ in range(2)]
print(np.inner(A, B)[0][0], np.outer(A, B), sep="\n")
