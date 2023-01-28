#!C:\ms4w\Python\python

#Compute location of intermediate points along the geodesic line

from pyproj import Geod
g = Geod(ellps='clrk66') # Use Clarke 1966 ellipsoid.
# specify the lat/lons of Boston and Portland.
boston_lat = 42.+(15./60.); boston_lon = -71.-(7./60.)
portland_lat = 45.+(31./60.); portland_lon = -123.-(41./60.)
# find ten equally spaced points along the geodesic between Boston and Portland.
lonlats = g.npts(boston_lon,boston_lat,portland_lon,portland_lat,10)

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

for lon,lat in lonlats: 
   print('%6.3f  %7.3f' % (lat, lon))


