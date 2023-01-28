#!C:\ms4w\Python\python

# pass parameter from form
import cgi, cgitb
form = cgi.FieldStorage()
Latitude = form.getvalue('Latitude')
Longitude  = form.getvalue('Longitude')
API = "http://api.geonames.org/findNearbyPlaceName?lat=%s&lng=%s&username=marahnama" % (Latitude, Longitude)
if form.getvalue('MaxRows'):
   MaxRows = form.getvalue('MaxRows')
   API += "&maxRows=%s" % MaxRows
if form.getvalue('Radius'):
   Radius = form.getvalue('Radius')
   API += "&radius=%s" % Radius
if form.getvalue('Style'):
   Style = form.getvalue('Style')
   API += "&style=%s" % Style
if form.getvalue('Cities'):
   Cities = form.getvalue('Cities')
   API += "&cities=%s" % Cities
if form.getvalue('Lang'):
   Lang = form.getvalue('Lang')
   API += "&lang=%s" % Lang
if form.getvalue('LocalCountry'):
   LocalCountry = form.getvalue('LocalCountry')
   API += "&localCountry=%s" % LocalCountry

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>GeoNames Service: Find nearby populated place / reverse geocoding</title>")
print ("</head>")
print ("<body>")
print ("<h2> The result:</h2>")
print ("<a href=\"%s\">%s</a>" % (API, API))
print ("</body>")
print ("</html>")
