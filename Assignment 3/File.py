#!C:\ms4w\Python\python
import cgi, os, cgitb;
cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['fileToUpload']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('./tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print ("""\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))

#Open and Read the file - count #rows and compute the avg lat and lng of the cities.
fin = open('./tmp/' + fn, 'r')
count=0
minlat=180.
minlng=180.
maxlat=-180.
maxlng=-180.
sumlat=0.
sumlng=0.
print('Input data')
print ("""<br>""") # New line
for line in fin:
   print(line)
   print ("""<br>""")
   count = count+1
   
   # Splits at ',' word[0] will be the place name; word[1] the lng; and word[2] the lat
   word = line.split(',')
   sumlat += float(word[2])
   sumlng += float(word[1])
   if minlat > float(word[2]):
      minlat = float(word[2])
   if minlng > float(word[1]):
      minlng = float(word[1])
   if maxlat < float(word[2]):
      maxlat = float(word[2])
   if maxlng < float(word[1]):
      maxlng = float(word[1])

print ("""<br>""")
print("Centroid of the populated places using the \"(Xmax + Xmin)/2, (Ymax + Ymin)/2\" formula:")
print ("""<br>""")
print("Longitude = %6.2f" % ((maxlng+minlng)/2))
print ("""<br>""")
print("Latitude = %6.2f" % ((maxlat+minlat)/2))
print ("""<br>""")
print ("""<br>""")
print("Centroid of the populated places using the \"Gx = (x1 + x2 +... + xk) / k , Gy = (y1 + y2 +... + yk) / k\" formula:")
print ("""<br>""")
print("Longitude = %6.2f" % (sumlng/count))
print ("""<br>""")
print("Latitude = %6.2f" % (sumlat/count))
print ("""<br>""")
fin.close()