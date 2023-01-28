#!C:\ms4w\Python\python

# WGS'84 <--> NB Double Stereographic
from pyproj import Proj
p = Proj(init='epsg:2953') # NB Double Stereographic

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print(p.srs)  
print(p(-66.666667, 45.95)) # Fredericton long/lat 
print(p(2487078.6457596286, 7438882.839870726, inverse=True))