#!C:\ms4w\Python\python

import numpy as np

# pass parameter from form
import cgi
form = cgi.FieldStorage()
dim_x =  int(form.getvalue('matrix_dim_x'))
dim_y =  int(form.getvalue('matrix_dim_y'))

d = np.random.random((dim_x,dim_y)) # Create an array filled with random values

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print(dim_x, dim_y)
print(d) 
