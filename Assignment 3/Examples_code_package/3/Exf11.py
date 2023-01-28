#!C:\ms4w\Python\python
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

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
sumlat=0.
sumlng=0.
print('Input data')
print ("""<br>""") # New line
for line in fin:
   print(line)
   print ("""<br>""")
   count = count+1
   # Splits at ',' word[0] will be the city name; word[1] the lat; and word[2] the lng
   word = line.split(',')
   sumlat += float(word[1])
   sumlng += float(word[2])
print ("""<br>""")
print('...Number of cities: ', count)
print ("""<br>""")
print("AVG lat = %6.2f" % (sumlat/count))
print ("""<br>""")
print("AVG lng = %6.2f" % (sumlng/count))
fin.close()