/*
 *
 *HW1
 *Intro to Security
 */

//headers for java
import java.io.File;
import Java.io.filereader;
import java.io.IOException;


//class bloom_filter
public class bloom_filter{

	//FIELDS

	
	//METHODS

	//class function
	public bloom_filter(){

	}


	//read from file
	public String readFile(String filename)
	{
		String content = null;
		File file = new File(filename); //for ex foo.txt
		FileReader reader = null;
		try {
			reader = new FileReader(file);
			char[] chars = new char[(int) file.length()];
			reader.read(chars);
			content = new String(chars);
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(reader !=null){reader.close();}
		}
		return content;
	}



	//read input and dictionary.txt
	//create bloom filter with dictionary.txt
	//hash each of the input files words with bloom filters


	//output text
	public output(){

	}

	//main
	public static void main(String [] args){
		

		new bloom_filter();
	}

}
