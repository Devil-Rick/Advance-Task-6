'''
Task

You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)

Input Format

The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array .

Output Format

Print the result of each operation in the given order under Task.
'''

import numpy as np
n, m = map(int, input().split())
A = np.array([input().split() for i in range(n)], int)[:m]
B = np.array([input().split() for i in range(n)], int)[:m]
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A % B)
print(A**B)
