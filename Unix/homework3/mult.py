#!/usr/bin/python2
import sys #imports the statements needed for this project
import argparse

product = 1 #set product intially to 1
parser = argparse.ArgumentParser(description='Process some integers.')#parsing the arguments
args = parser.parse_args()
try:
	for line in iter(sys.stdin.readline,''):#read line from terminal
		if line != "\n": # if line is not null
			product = product * float(line)#find the product by multiplying to the product and setting it equal to product
		else:# if line is null
			print int(product)#print the product out
			product = 1#set product to 1
	print int(product)#if no more inputs given, display the product

except ValueError as e: #throw exception if a number/digit is not givent as input
   print e #print out the exception
   sys.exit(1)




