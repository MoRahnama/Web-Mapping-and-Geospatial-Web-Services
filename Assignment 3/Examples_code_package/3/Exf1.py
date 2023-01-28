#!C:\ms4w\Python\python

import numpy as np

# pass parameter from form
import cgi
form = cgi.FieldStorage()
dim =  int(form.getvalue('matrix_dim'))

d = np.random.random((dim,dim)) # Create an array filled with random values

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print(dim)
print(type(dim))
print(d) 
