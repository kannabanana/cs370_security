#SR Kanna
#Course: Intro to Security
#HW1

#bloom filters in python

import random;
import os;
import sys;
import re;



#returns number of lines in a file
def file_len(fname):
	with open(fname) as f:
		for i,l in enumerate(f):
			pass
	return i+1


#reads a file
def input_listP(text):
	fo = open(text,"r")
	i = file_len(text);

	master = ["a"]*i
	for x in range (0,i):
		master[x] = fo.readline()
		print master[x]

	return master



#hash_function1




#hash_function2



#hash_function3



#hash_function4




#hash_function5




#function to output to output.txt
def output(intersection):
#	print "in output the intersetemption is ", intersection
	fo = open("output.txt","w+")		#will create output.txt if it doesn't exist
	fo.write(str(intersection))


def main():


	input_listP(sys.argv[1]);
	#read input and dictionary.txt
	#create bloom filter with dictionary.txt
	#hash each of the input files words with bloom filters


main()
