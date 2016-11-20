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

	/*Values that will not be recycled*/

	int count = 0;						//starting 
	int flip = 0;

	size_t len = 10;					//create random string
	char * random_string = NULL;
	
	while(flip != 1)
	{
		random_string = randstring(len);
		printarray(random_string);
		random_string = NULL;
		++count;
		if (count == 10)
		{
			flip = 1;
		}
	}

	if (flip == 1)
	{	
		printf ("the count is %d\n",count);
	}



	/* Values that will be recycled*/	
	EVP_MD_CTX *mdctx;					//new one w/the value
	const EVP_MD *md;					//the md

	char mess1[] = "Test Message\n";
	char mess2[] = "Hello World\n";
	unsigned char md_value[EVP_MAX_MD_SIZE];		//char of md value
	int md_len, i;						//len and initialization

	printf("origional message 1%s\n",mess1);
	printf("origional message 2%s\n",mess2);
	
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
	EVP_DigestUpdate(mdctx, mess2, strlen(mess2));		
	EVP_DigestFinal_ex(mdctx, md_value, &md_len);
	EVP_MD_CTX_destroy(mdctx);				//destroy it

	printf("Digest is: ");
	for (i = 0; i < md_len; i++)
		printf("%02x", md_value[i]);
	printf("\n");

	exit(0);

}
