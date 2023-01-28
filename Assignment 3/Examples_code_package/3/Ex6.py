#!C:\ms4w\Python\python

#Read input points from file, do conversion, save in another file

import sys
import pyproj
import csv

#definition of a function
def proj_conversion(input_filename, output_filename):
  
  infile = open(input_filename, 'r')
  csv_f = csv.reader(infile)
 
  outfile = open(output_filename, 'w')

  p = pyproj.Proj(init='epsg:3857')

  print ("Content-Type: text/plain;charset=utf-8")
  print()  # must have a free line here

  for row in csv_f:
    x1 = float(row[0])
    y1 = float(row[1]) 
    (x2, y2) = p(x1,y1)
    print("%.2f,%.2f --> %.2f,%.2f" % (x1,y1,x2,y2))
    
    outfile.write("%.2f,%.2f\n" % (x2,y2))
  
  infile.close()
  outfile.close()

def main():
  f1 = "./points.csv"
  f2 = "./p.csv"
  proj_conversion(f1,f2) 

if __name__ == '__main__':
  main()
