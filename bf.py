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
def readfromfile(text):
	fo = open(text,"r")
	i = file_len(text);

	master = ["a"]*i
	for x in range (0,i):
		master[x] = fo.readline()
		print master[x]

	return master



#hash_function1
def hashfunction1(dictionary[x],bloom_filter3):
	#loop through function add ascii value, divide by number of len of 
	return bloom_filter3



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

	#read dictionary.txt
	i = file_len(sys.argv[1]);
	dictionary = ["a"]*i;	
	dictionary = readfromfile(sys.argv[1]);


	#create bloom filter w/dictionary.txt
	bloom_filter3 = [0]*61;		#bloom filter for hash3
		#created list, initalized zero, of size prime 61
	bloom_filter5 = [0]*61;		#bloom filter for hash5


	#for loop through dictionary to hash every index into bloom filter3 and 5
	j = len(dictionary)

	#for bloom_filter3
	for x in range(0,len):
		bloom_filter3 = hashfunction1(dictionary[x],bloom_filter3);
		bloom_filter3 = hashfunction2(dictionary[x],bloom_filter3);
		bloom_filter3 = hashfunction3(dictionary[x],bloom_filter3);

	
	#hashfunction4
	#hashfunction5
	
	#hash each of the input files words with bloom filters
	#see which ones match
		#store to output file

main()
