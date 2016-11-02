#SR Kanna
#Course: Intro to Security
#HW1

#bloom filters in python

import random;
import os;
import sys;
import re;
import hashlib
import md5

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



#hash_function1
def hashfunction(dictionary,x,bloom_filter3,num):
	if num == 0:
		h = hashlib.sha1(dictionary[x])
		h = int(h.hexdigest(),16)
		h = h%10000000
		return h
	elif num ==1:
		h = hashlib.md5(dictionary[x])
		h = int(h.hexdigest(),16)
		h = h%10000000
		return h
	elif num==2:
		h = hashlib.sha224(dictionary[x])
		h = int(h.hexdigest(),16)
		h = h%10000000
		return h
	elif num==3:
		h = hashlib.sha256(dictionary[x])
		h = int(h.hexdigest(),16)
		h = h%10000000
		return h
	else:
		h = hashlib.sha384(dictionary[x])
		h = int(h.hexdigest(),16)
		h = h%10000000
		return h	

#functiont to check if it's a bad password
def check_hash(inputarray,x,bloom_filter,num,total):
	m = hashfunction(inputarray,x,bloom_filter,num)
#	print "check hash m", m, num
	if bloom_filter[m] == 1:
#		print "bloom filter also has a match!", bloom_filter[m]
		total[num] = 1
	return total


#function to output to output3/5.txt
def output(result,text):
	fo = open(text,"a")		#will create output.txt if it doesn't exist
	fo.write(result+'\n')


def main():

	#read dictionary.txt
	i = file_len(sys.argv[2]);
	print "the len of dictionary.txt is ",i
	dictionary = ["a"]*i;	
	dictionary = readfromfile(sys.argv[1]);


	#create bloom filter w/dictionary.txt
	bloom_filter3 = [0]*10000000;		#bloom filter for hash3
		#created list, initalized zero, of size prime 10000000
	bloom_filter5 = [0]*10000000;		#bloom filter for hash5


	#for loop through dictionary to hash every index into bloom filter3 and 5
	j = len(dictionary)

	#for bloom_filter3
	for x in range(0,j):
		h = hashfunction(dictionary,x,bloom_filter3,0);
		bloom_filter3[h] = 1

		h = hashfunction(dictionary,x,bloom_filter3,1);
		bloom_filter3[h] = 1
	
		h = hashfunction(dictionary,x,bloom_filter3,2);
		bloom_filter3[h] = 1


	#bloomfilter5
	for x in range(0,j):	
		h = hashfunction(dictionary,x,bloom_filter5,0);
		bloom_filter5[h] = 1

		h = hashfunction(dictionary,x,bloom_filter5,1);
		bloom_filter5[h] = 1
	
		h = hashfunction(dictionary,x,bloom_filter5,2);
		bloom_filter5[h] = 1


		h = hashfunction(dictionary,x,bloom_filter5,3);
		bloom_filter5[h] = 1
	
		h = hashfunction(dictionary,x,bloom_filter5,4);
		bloom_filter5[h] = 1

	i = file_len(sys.argv[4]);
	inputarray = ["a"]*i;	
	inputarray = readfromfile(sys.argv[4]);


	for x in range(0,i):
		total = [0,0,0]
		total = check_hash(inputarray,x,bloom_filter3,0,total);
		total = check_hash(inputarray,x,bloom_filter3,1,total);
		total = check_hash(inputarray,x,bloom_filter3,2,total);
		print "total is ", total		
	
		count = 0
		for x in range (0,3):
			if total[x] == 1:
				count = count+1
#		print "count for x is ", count
#		if count >= 2:
#			print "maybe"
#			output(total,sys.argv[6]);
#		else:
#			print "no"
#			output(total,sys.argv[7]);
	

main()
