#!C:\ms4w\Python\python

import sqlite3, cgi, cgitb
form = cgi.FieldStorage()
conn = sqlite3.connect('canvec_220313_332517.gpkg')
minValue = form.getvalue('minValue')
maxValue  = form.getvalue('maxValue')

print ("Content-Type: text/plain;charset=utf-8")
print()  # must have a free line here

print ("Opened database successfully")

sqlq = "SELECT COUNT(*) FROM road_segment_1 WHERE speed_restriction > %s AND speed_restriction < %s" % (minValue, maxValue)
print("QUERY: " + sqlq)

try:
   cursor = conn.execute(sqlq)
   for row in cursor:
      print(row)
except:
    print("Wrong query")
    
conn.close()