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
def hashfunction(dictionary,x,bloom_filter3,num):
	salt = ["opljcmriek","slopwnwggrmb","bemasdhoiqplncb","qzcbuufkasnklzm","qmzhadlmppksj"]
	dictionary[x] = dictionary[x]+salt[num]
	m = hash(dictionary[x])		#get the hash!
	m = m%10000000			#mod it with 10000000 to get something inside 
	bloom_filter3[m] = 1
	return bloom_filter3


#functiont to check if it's a bad password
def check_hash(inputarray,x,bloom_filter,num,total):
	salt = ["opljcmriek","slopwnwggrmb","bemasdhoiqplncb","qzcbuufkasnklzm","qmzhadlmppksj"]
	inputarray[x] = inputarray[x]+salt[num]
	m = hash(inputarray[x])		#get the hash!
	m = m%10000000			#mod it with 10000000 to get something inside 
	if bloom_filter[m] == 1:
		total[num] = 1
	return total


#function to output to output3/5.txt
def output(result,text):
	fo = open(text,"a")		#will create output.txt if it doesn't exist
	fo.write(result+'\n')


def main():

	#read dictionary.txt
	i = file_len(sys.argv[2]);
	dictionary = ["a"]*i;	
	dictionary = readfromfile(sys.argv[2]);


	#create bloom filter w/dictionary.txt
	bloom_filter3 = [0]*10000000;		#bloom filter for hash3
		#created list, initalized zero, of size prime 10000000
	bloom_filter5 = [0]*10000000;		#bloom filter for hash5


	#for loop through dictionary to hash every index into bloom filter3 and 5
	j = len(dictionary)

	#for bloom_filter3
	for x in range(0,j):
		bloom_filter3 = hashfunction(dictionary,x,bloom_filter3,0);
		bloom_filter3 = hashfunction(dictionary,x,bloom_filter3,1);
		bloom_filter3 = hashfunction(dictionary,x,bloom_filter3,2);

	for x in range(0,j):
		bloom_filter5 = hashfunction(dictionary,x,bloom_filter5,0);
		bloom_filter5 = hashfunction(dictionary,x,bloom_filter5,1);
		bloom_filter5 = hashfunction(dictionary,x,bloom_filter5,2);
		bloom_filter5 = hashfunction(dictionary,x,bloom_filter5,3);
		bloom_filter5 = hashfunction(dictionary,x,bloom_filter5,4);
	
	i = file_len(sys.argv[4]);
	inputarray = ["a"]*i;	
	inputarray = readfromfile(sys.argv[4]);

	#for loop through dictionary to hash every index into bloom filter3 and 5
	j = len(inputarray)
	
	for x in range(0,j):
#		print "x is ", x
		total = [0,0,0]
		total = check_hash(inputarray,x,bloom_filter3,0,total);
		total = check_hash(inputarray,x,bloom_filter3,1,total);
		total = check_hash(inputarray,x,bloom_filter3,2,total);
#		print "total is ", total		

		count = 0
		for x in range (0,3):
			if total[x] == 1:
				count = count+1
#		print "count for x is ", count
		if count >= 2:
#			print "maybe"
			output("maybe",sys.argv[6]);
		else:
#			print "no"
			output("no",sys.argv[6]);


	for x in range(0,j):
#		print "x is ", x
		total = [0,0,0,0,0]
		total = check_hash(inputarray,x,bloom_filter5,0,total);
		total = check_hash(inputarray,x,bloom_filter5,1,total);
		total = check_hash(inputarray,x,bloom_filter5,2,total);
		total = check_hash(inputarray,x,bloom_filter5,3,total);
		total = check_hash(inputarray,x,bloom_filter5,4,total);
#		print "the total is ", total		

		count = 0
		for x in range (0,5):
			if total[x] == 1:
				count = count+1
#		print "count is ", count
		if count >= 4:
#			print "maybe"
			output("maybe",sys.argv[7]);
		else:
#			print "no"
			output("no",sys.argv[7]);


		
main()
