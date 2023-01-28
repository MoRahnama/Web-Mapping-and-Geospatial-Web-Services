#!C:\ms4w\Python\python

import numpy as np
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print('MATRIX A')
print(A)
print('MATRIX B')
print(B)
print('MARTIX A+B')
print(A+B)
print('MATRIX A-B')
print(A-B)
print('MATRIX A*B')
print(A*B)             # elementwise product
print('MATRIX AxB')
print(A.dot(B))        # matrix product
print('MATRIX AxB')
print(np.dot(A,B))     # another matrix product
