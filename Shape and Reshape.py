"""
Task

You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format

A single line of input containing  9 space separated integers.

Output Format

Print the 3X3 NumPy array.
"""

import numpy as np
n = input().split()
x = np.array(n, int).reshape(3, 3)
print(x)
