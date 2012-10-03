#! /usr/bin/env python2

import sys #imports the statements needed for this project
import argparse
import ast
import shlex

parser = argparse.ArgumentParser(description='Process some integers.')#parsing the arguments
parser.add_argument('-f', '--data-file:', dest='add_data', help = "Path to the data file to read at startup")
args = parser.parse_args()

l1 = [];
pID = [];
descrip = [];
footprint = [];
quantity = [];

def readData():
	f = open(sys.argv[2], 'r')
	for line in f:
		line = line.rstrip()
		l1.append(line)
		line = shlex.split(line) 
		pID.append(line[0])
		descrip.append(line[1])
		footprint.append(line[2])
		quantity.append(line[3])

def writeData():
	f1 = open(sys.argv[2], 'w')
	for line in l1:
		f1.write(line+"\n")

if(args.add_data):
	try:
		readData()
		for line1 in sys.stdin:
			if line1.startswith('add'):
				line1 = line1.lstrip("add").strip()
				line1 = line1[1:len(line1)-1]
				line1 = line1 = ast.literal_eval(line1)
				pID.append(line1['PartID'])
				descrip.append(line1['Description'])
				footprint.append(line1['Footprint'])
				quantity.append( line1['Quantity'])
				l1.append(line1['PartID']+"\t"+line1['Description']+"\t\t"+line1['Footprint']+"\t\t"+str(line1['Quantity']))
				writeData()	
			elif line1.startswith('remove'):
				line1 = line1.lstrip("remove").strip()
				pid1 = line1.split("=")
				x = pID.index(pid1[1])
				l1.pop(x)
				pID.pop(x)
				descrip.pop(x)
				footprint.pop(x)
				quantity.pop(x)
				writeData()
			elif line1.startswith('set'):
				line1 = line1.lstrip('set').strip()
				if "where" in line1:
					line1 = line1.split("where")
				elif "for" in line1:
					line1 = line1.split("for")
				type2 = line1[1].split("=")
				x = pID.index(type2[1].strip())
				type1 = line1[0].split("=")
				if(type1[0].strip() == "Footprint"):
					footprint[x] = type1[1].strip();
					l1[x] = pID[x] +"\t"+descrip[x]+"\t\t"+footprint[x]+"\t\t"+ str(quantity[x])
				elif(type1[0].strip() == "Description"):
					descrip[x] = type1[1].strip();
					l1[x] = pID[x] +"\t"+descrip[x]+"\t\t"+footprint[x]+"\t\t"+ str(quantity[x])
				elif(type1[0].strip() == "Quantity"):
					quantity[x] = type1[1].strip();
					l1[x] = pID[x] +"\t"+descrip[x]+"\t\t"+footprint[x]+"\t\t"+ str(quantity[x])
				elif(type1[0].strip() == "PartID"):
					partID[x] = type1[1].strip();
					l1[x] = pID[x] +"\t"+descrip[x]+"\t\t"+footprint[x]+"\t\t"+ str(quantity[x])
				else:
					print "Type you want to change doesnot exist"
				writeData()
			elif line1.startswith("list all"):
				print ""
				if line1.strip() == "list all":
					for line2 in l1:
						print line2
				elif "sort" in line1:
					line1 = line1.lstrip("list all sort by").strip()
					if line1.strip() == "Quantity":
						print "Sort by quantity"
					elif line1.strip() == "Footprint":
						print "Sort by Footprint"
					elif line1.strip() == "Description":
						print "Sort by Description"
					elif line1.strip() == "PartID":
						print "Sort by partID"
					else:
						print "Illegal parameter Passed"

				else:
					line1 = line1.lstrip("list all with").strip()
					line1 = line1.split("=")
					y = []
					count = 0 
					if line1[0].strip() == "Quantity":
						for x in quantity:
							if(x == line1[1].strip()):
								y.append(count)
							count =  count +1
					elif line1[0].strip() == "Footprint":
						for x in footprint:
							if(x == line1[1].strip()):
								y.append(count)
							count = count +1
					elif line1[0].strip() == "Description":
						for x in descrip:
							if(x == line1[1].strip()):
								y.append(count)
							count = count +1
					elif line1[0].strip() == "PartID":
						for x in pID:
							if(x == line1[1].stip()):
								y.append(count)
							count = count +1
					else:
						print "Illegal param provied"
					for x in y:
						print l1[x]	
			else:
				print "Invalid syntax"	
	except ValueError as e: #throw exception if a number/digit is not givent as input
	   print e #print out the exception
	   sys.exit(1)		
