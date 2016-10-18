all:
	javac bloom_filter.java
	java bloom_filter

clean:
	rm -f *.class
