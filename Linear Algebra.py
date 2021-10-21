'''
Task

You are given a square matrix A with dimensions N X M. Your task is to find the determinant. 

Input Format

The first line contains the integer N.
The next N lines contains the N space separated elements of array A .

Output Format

Print the determinant of A .
'''

import numpy
print(round(numpy.linalg.det(numpy.array(
    [list(map(float, input().split())) for _ in range(int(input()))])), 2))
