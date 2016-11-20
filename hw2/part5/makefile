all:	encdec.c

	gcc -I/usr/local/ssl/include/ -L/usr/local/ssl/lib/ -o enc encdec.c -lcrypto -ldl 
	./enc
