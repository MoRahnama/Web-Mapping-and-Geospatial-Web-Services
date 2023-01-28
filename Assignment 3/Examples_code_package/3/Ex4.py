#!C:\ms4w\Python\python

# WGS84 --> Web Mercator
import pyproj
p = pyproj.Proj(init='epsg:3857')
(x1, y1) = (-66.666667, 45.95)
(x2, y2) = p(x1,y1)

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print("WGS84: %9.3f %11.3f" % (x1,y1))
print("Web Mercator: %9.3f %11.3f" % (x2,y2))


