/*
SR Kanna
CS370 - HW2 - Part V
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/evp.h>

#define DICTIONARY "words_dict.txt"


//ORIGIONAL VALUES
char input[] = "This is a top secret.";
char cipherinput[] = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9";
unsigned char initialvec[16] = { 0 } ;



//get the hex
int hex_fun(unsigned char *buf, int length, FILE *OF)
{
    unsigned char buffer[1024]="";
    unsigned char *pbuffer = buffer;
	char x='\n';
	int i;
	for ( i = 0; i < length; i++ )
	{
		fprintf(OF,"%02x",buf[i]);
		sprintf(pbuffer, "%02x", buf[i]);
		pbuffer +=2;
	}
	fprintf(OF,"%c",x);

    if(!strcmp(buffer, cipherinput))
    	return 1;
	return 0;
}




int main()
{
	char thekey[1024];
	FILE *letters, *OF;

	unsigned char outbuf[1024 + EVP_MAX_BLOCK_LENGTH];
	int outlen, tmplen, i;
	EVP_CIPHER_CTX ctx;

	letters = fopen(DICTIONARY, "r");
	OF = fopen("ciphertext.txt", "w+"); //file to store ciphers
	if( thekey < 0 || OF < 0 )
	{
		perror ("Cannot open file");
		exit(1);
	}



	
	EVP_CIPHER_CTX_init(&ctx);
	while ( fgets(thekey,16, letters) )
	{
		if(strlen(thekey)>=16)
			continue;

		for(i=strlen(thekey)-1;i<16;i++) //if thekey is less than 16 than pad with spaces
				thekey[i]=' ';
		thekey[i] = '\0';

	    EVP_EncryptInit_ex(&ctx, EVP_aes_128_cbc(), NULL, thekey, initialvec);

		if(!EVP_EncryptUpdate(&ctx, outbuf, &outlen, input, strlen(input)))
		{
			EVP_CIPHER_CTX_cleanup(&ctx);
			return 0;
		}
		if(!EVP_EncryptFinal_ex(&ctx, outbuf + outlen, &tmplen))
		{
			EVP_CIPHER_CTX_cleanup(&ctx);
			return 0;
		}
		outlen += tmplen;
        
		if(hex_fun(outbuf, outlen, OF)) //convert raw cipher to hex value
		{
			printf("Key : %s\n",thekey);
			break;
		}
	}

	fclose(letters);
	fclose(OF);

	return 1;
}


