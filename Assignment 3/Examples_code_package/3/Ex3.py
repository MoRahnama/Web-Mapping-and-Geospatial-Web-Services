#!C:\ms4w\Python\python

#Polynomials

from numpy import poly1d
p = poly1d([3,4,5])

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print(p)
print(p*p)
print(p.integ(k=6))
print(p.deriv())
print(p([4]))
print(p([4,5]))
