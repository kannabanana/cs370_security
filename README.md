Compiling: make (this will run the makefile)
	   make clean (remove output3.txt and output5.txt)

Answer to Questions:

1. What hash function did you choose and why (cryptographic or non-cryptographic)? What is the output range of the hash functions? What is the size of the bloom filter in each case?

	
I used one of python’s built in functions, hash, to hash. Hash is not cryptographic. To generate 5 different hash functions, I created a salt function to append a given password before hashing. The salting strings are put into an array of size 5. Indices 0-2 are chosen for ouput3.txt, and indices 0-4 is chosen for output5.txt. Dictionary.txt has approximately 600,000 passwords.  I mod my hashing function after salting with the size of the bloom filter, which is 10 million, so the output range is between zero to ten million-1. The size of the the bloom-fitler is 10 million. 


2. How long does it take for your bloom filter to check 1 password in each case? Why does one perform better than others?

	I used linux's time command to check a password with three hashes and five hashes. I ran each test three times and got the average. With hashing with three hash functions, I got 5.27s as the average for 1 password. For five hash functions, I have approximately 5.33s as the average time for one password. Because you are running through five hashes, this is going to be slower compared to three hashes. 

3. What is the probability of False positives in your bloom filter in each case? What is the probability of false negatives in your bloom filter?

	I treated the white spaces in the dictionary.txt and sample_input.txt file as seperate passwords if one had whitespaces and the other did not, since there were repeated passwords. For example, comparing sample_input and dictionary.txt line numbers 1,7,9,11,12,13,14,15,16 and 18 are not dictionary.txt (including my spacing policy), but 2,3,4,5,6,8,10 and 17 is a direct match for dictionary.txt. The probability of false negatives is zero, since the bloom filter will always correctly identify passwords against dictionary.txt. The false positive rate can be calculated using fp = (1-[1-1/m]^kn)^k. This yields .0049 or .5% chance with three hashes and .0013 or .1% chance with five hashes. I do not have any false negatives or false positives in output3.txt or output5.txt.


4. How can you reduce the rate of false positives?
		
False positives are passwords that aren’t bad passwords but bloom filter will claim they match a bad password from dictionary.txt. A few options exist to reduce the false positive rate. By knowing the desired false positive rate, you can plug into a formula to get an optimal size of the bloom filter and number of hash functions to include. For example, m = - (nlnp)/(ln2)^2 is the formula to decide the size of the array, where n is the expected number of items, and p is the probability. Furthermore, k = -(m/n (ln2)) determines the number of hashes to use, where m is the size of the array, and n expected number of items.
