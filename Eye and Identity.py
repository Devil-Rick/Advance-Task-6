"""

Task

Your task is to print an array of size N X M with its main diagonal elements as 0's and 1's everywhere else.


Input Format

A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

Output Format

Print the desired N X M array.
"""

import numpy as np
n, m = map(int, input().split())
np.set_printoptions(sign=' ')
print(np.eye(n, m))
