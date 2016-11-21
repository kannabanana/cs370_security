#include "opensslex.h"
#include <stdio.h>
#include <openssl/evp.h>


//PRINT ARRAY
//INPUT: pointer to starting index of array
//OUTPUT: void
void printarray(char * p)
{
	printf("array is %s\n",p);
}



//GENERATE RANDOM ARRAY
//INPUT: length of array
//OUTPUT: array with random values
char *randstring(size_t length) {

	static char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";        
	char *randomString = NULL;
	int n;

	if (length) {
		randomString = malloc(sizeof(char) * (length +1));

		if (randomString) {            
			for (n= 0;n < length;n++) {            
				int key = rand() % (int)(sizeof(charset) -1);
				randomString[n] = charset[key];
			}

			randomString[length] = '\0';
		}
	}
	return randomString;
}




void main(int argc,char *argv[])
{

	time_t t;
	srand((unsigned) time(&t));


	EVP_MD_CTX *mdctx;					//new one w/the value
	const EVP_MD *md;					//the md
	int md_len,i;
	char mess1[] = "Test Message\n";
	unsigned char md_value[EVP_MAX_MD_SIZE];		//char of md value

	OpenSSL_add_all_algorithms();				//need to add this
	if(!argv[1]) {
		printf("Usage: mdtest digestname\n");
		exit(1);
	}


	md = EVP_get_digestbyname(argv[1]);			//get the name


	if(!md) {
		printf("Unknown message digest %s\n", argv[1]);
		exit(1);
	}


	mdctx = EVP_MD_CTX_create();				//create
	
	EVP_DigestInit_ex(mdctx, md, NULL);			//initalize
	EVP_DigestUpdate(mdctx, mess1, strlen(mess1));		//update str1
	EVP_DigestFinal_ex(mdctx, md_value, &md_len);
	EVP_MD_CTX_destroy(mdctx);				//destroy it

	printf("Digest is: ");
	for (i = 0; i < md_len; i++)
		printf("%02x", md_value[i]);
	printf("\n");



	int count = 0;						//starting 
	int flip;
	flip = 1;						//they're different

	size_t len = 10;					//create random string
	char * random_string = NULL;

	while(flip == 1)
{
		random_string = randstring(len);
		printarray(random_string);


		EVP_MD_CTX *mdctx2;					//new one w/the value
		const EVP_MD *md2;					//the md
		unsigned char md_value2[EVP_MAX_MD_SIZE];		//char of md value
		int md_len2;						//len and initialization



		OpenSSL_add_all_algorithms();				//need to add this
		if(!argv[1]) {
			printf("Usage: mdtest digestname\n");
			exit(1);
		}


		md2 = EVP_get_digestbyname(argv[1]);			//get the name

		
		if(!md2) {
			printf("Unknown message digest %s\n", argv[1]);
			exit(1);
		}

		printf ("got md2 value\n");
		mdctx2 = EVP_MD_CTX_create();				//create
		printf ("created\n");
		EVP_DigestInit_ex(mdctx2, md2, NULL);			//initalize
		printf ("init\n");
		EVP_DigestUpdate(mdctx2, random_string, strlen(random_string));		//update str1
		printf ("update\n");
		EVP_DigestFinal_ex(mdctx2, md_value2, &md_len2);
		printf ("final");

		//get first 26 bits of md_value and copy it into 
	
		EVP_MD_CTX_destroy(mdctx2);				//destroy it
		printf("destroy\n");
	

		printf("Digest is: ");
		for (i = 0; i < md_len2; i++)
			printf("%02x", md_value2[i]);
		printf("\n");

		flip = 0;
		for(i = 0;i<2;++i)
		{
			if (flip != 1)
			{
				if(md_value2[i] != md_value[i])
				{
					flip = 1;
				}
			}
		}
		printf("%d\n",count);
		++count;
	}

	

	exit(0);

}
