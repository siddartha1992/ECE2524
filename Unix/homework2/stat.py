# ECE 2524 Homework 2 Problem 3 <Siddartha Tondapu>
import sys
if len(sys.argv) == 2:
	print "ACCOUNT SUMMARY"
	f = open(sys.argv[1], 'r')

	name = []
	price = []

	for line in f:
		x = line.split()
		name.append(x[1])
		price.append(float(x[2]))
	
	print "Total amount owed = ", sum(price)
	print "Average amount owed = ", sum(price)/len(price)
	print "Maximum amount owed = ", max(price)," by ",name[price.index(max(price))]
	print "Minimum amount owed = ", min(price)," by ",name[price.index(min(price))] 
else:
	print "Enough inputs are not given."

 
