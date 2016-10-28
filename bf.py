#SR Kanna
#Course: Intro to Security
#HW1

#bloom filters in python

import random;
import os;
import sys;
import re;
import hashlib


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
#		print master[x]

	return master

#generates random list of values of size 10
def salt_fun(salt):
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	len = random.randint(0,100)
	for x in range(0,len):
		i = random.randint(0,25)
		salt[x] = alpha[i]	
	return salt



#hash_function1
def hashfunction1(dictionary,x,bloom_filter3):
	salt = "opljcmriek"
	dictionary[x] = dictionary[x]+salt
	m = hash(dictionary[x])		#get the hash!
	m = m%61			#mod it with 61 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3


#hash_function2
def hashfunction2(dictionary,x,bloom_filter3):
	salt = "slopwnwggrmb"
	dictionary[x] = dictionary[x]+salt
	m = hash(dictionary[x])		#get the hash!
	m = m%61			#mod it with 61 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3


#hash_function3
def hashfunction3(dictionary,x,bloom_filter3):
	salt = "cbvmweyuikswazko"
	dictionary[x] = dictionary[x]+salt
	m = hash(dictionary[x])		#get the hash!
	m = m%61			#mod it with 61 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3


#hash_function4
def hashfunction4(dictionary,x,bloom_filter3):
	salt = "kalwncjweiplqwx"
	dictionary[x] = dictionary[x]+salt
	m = hash(dictionary[x])		#get the hash!
	m = m%61			#mod it with 61 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3


#hash_function5
def hashfunction5(dictionary,x,bloom_filter3):
	salt = "xemdjwpqldsaj"
	dictionary[x] = dictionary[x]+salt
	m = hash(dictionary[x])		#get the hash!
	m = m%61			#mod it with 61 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3



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
	for x in range(0,j):
		bloom_filter3 = hashfunction1(dictionary,x,bloom_filter3);
		bloom_filter3 = hashfunction2(dictionary,x,bloom_filter3);
		bloom_filter3 = hashfunction3(dictionary,x,bloom_filter3);

	print bloom_filter3

	for x in range(0,j):
		bloom_filter5 = hashfunction1(dictionary,x,bloom_filter5);
		bloom_filter5 = hashfunction2(dictionary,x,bloom_filter5);
		bloom_filter5 = hashfunction3(dictionary,x,bloom_filter5);
		bloom_filter5 = hashfunction4(dictionary,x,bloom_filter5);
		bloom_filter5 = hashfunction5(dictionary,x,bloom_filter5);
	
	print bloom_filter5

	i = file_len(sys.argv[1]);
	inputfile = ["a"]*i;	
	inputfile = readfromfile(sys.argv[2]);

	check3 = [0]*61;		#bloom filter for hash3
		#created list, initalized zero, of size prime 61
	check5 = [0]*61;		#bloom filter for hash5


	#for loop through dictionary to hash every index into bloom filter3 and 5
	j = len(dictionary)

	#hash each of the input files words with bloom filters
	#see which ones match
		#store to output file

main()
