# ECE 2524 Homework 2 Problem 2 <Siddartha Tondapu>
import sys
if len(sys.argv) == 2:
	print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
	f = open(sys.argv[1], 'r')
	for line in f:
		x = line.split()
		if x[3] == "Blacksburg":
			print x[4]+", "+x[1]+", "+x[0]+", "+x[2]
else:
	print "Enough inputs are not given."

