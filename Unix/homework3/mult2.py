#!/usr/bin/python2
import sys #imports the statements needed for this project
import argparse
import fileinput

def isNumber(s):
	try:
        	float(s) # for int, long and float
	except ValueError:
		return False;
	return True;
product = 1.0
parser = argparse.ArgumentParser(description='Process some integers.')#parsing the arguments
parser.add_argument("File",nargs = '*')
parser.add_argument('--ignore-blank', dest='ignore_blank', action = 'store_true')
parser.add_argument('--ignore-non-numeric', dest = 'ignore_non_numeric', action = 'store_true')


args = parser.parse_args()
try: # if wrong input
	if(len(sys.argv) == 1):#if not argument is given 
		for line in iter(sys.stdin.readline,''):
			if line != "\n": 
				product = product * float(line)
			else:
				print product
				product = 1.0
		print product
	elif(args.ignore_blank and not args.ignore_non_numeric):# if argument is ignore_blank
		files = sys.argv[2:]
		for line in fileinput.input(files):
			if line != "\n":
				product = product * float(line)
		print product
	elif(args.ignore_non_numeric and not args.ignore_blank):#if argument is ignore_non_numeric
		files = sys.argv[2:]
		for line in fileinput.input(files):
			if isNumber(line):
				product = product * float(line)
		print product
	elif(args.ignore_non_numeric and args.ignore_blank):# if more ignore_blank and ignore_non_numeric called
		files = sys.argv[3:]
		for line in fileinput.input(files):
			if line != "\n" and isNumber(line):
				product = product *float(line)
		print product
	else: # if one file are more are passed
		for line in fileinput.input():
	    		if line != "\n":
				product = product * float(line)
			else:
				print product
				product = 1.0
		print product
except ValueError as e:
	print e
	sys.exit(1)






