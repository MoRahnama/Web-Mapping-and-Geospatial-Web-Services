#!C:\ms4w\Python\python

# from a location, calculate another one 10km NW 

import pyproj
lng = 30
lat = 45
angle = 315  # degrees
dist = 10000 # metres
geod = pyproj.Geod(ellps='clrk66')

lng2,lat2,invangle = geod.fwd(lng,lat,angle,dist)

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print("%.8f, %.8f is 10km NW of %.4f, %.4f" % (lat2, lng2, lat,lng))

#GRS80  
#list of ellipsoids: https://jswhit.github.io/pyproj/pyproj.Geod-class.html

import pyproj
lng = 30
lat = 45
angle = 315  # degrees
dist = 10000 # metres
geod1 = pyproj.Geod(ellps='GRS80')
geod2 = pyproj.Geod(ellps='clrk66')
geod3 = pyproj.Geod(ellps='sphere')

lng1,lat1,invangle = geod1.fwd(lng,lat,angle,dist)
lng2,lat2,invangle = geod2.fwd(lng,lat,angle,dist)
lng3,lat3,invangle = geod3.fwd(lng,lat,angle,dist)

print("GRS 80  : %.8f, %.8f is 10km NW of %.4f, %.4f" % (lat1, lng1, lat,lng))
print("CLARK 66: %.8f, %.8f " % (lat2, lng2))
print("SPHERE  : %.8f, %.8f " % (lat3, lng3))

  

