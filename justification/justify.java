import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;
import java.io.File;
import java.util.List;


/**
 * A class that contains static methods that print justified
 * text using dynamic programming optimization. Also
 * contains a main method that takes a file in the directory
 * and prints the justified text in the console.
 */
public class justify {

	public static final int PAGE_WIDTH = 40;

	/**
	 * Reads a file an outputs an ArrayList of the words in the file
	 * in the order they appear. 
	 * @param 	String filename
	 * @return	ArrayList<String> wordList containing the words in the file
	 */
	public static ArrayList<String> readFile(String filename) {

		ArrayList<String> wordList = new ArrayList<String>();
		try {
			Scanner scan = new Scanner(new File(filename));
			
			while(scan.hasNext()) {
				wordList.add(scan.next());
			}
			scan.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		return wordList;
	}

	/**
	 * Justifies the words in the wordList array by minimizing
	 * the "badness" of the line breaks using dynamic programming.
	 * @params ArrayList<String> wordList
	 */
	public static void justification(ArrayList<String> wordList) {
		
		int[] bad = new int[wordList.size() + 1];
		int[] DP = new int[wordList.size()];

		// Initialize the bad array with large values
		for(int j = 0; j < wordList.size(); ++j) {
			bad[j] = Integer.MAX_VALUE;
		}
		
		// set the base case
		bad[wordList.size()] = 0;

		for(int i = wordList.size() - 1; i >= 0; --i) {
			int index;
			int j = i + 1;
			int len = length(i, j, wordList);

			while(j <= wordList.size() && len <= PAGE_WIDTH) {
				if(bad[i] > badness(len) + bad[j]) {
					DP[i] = j;
					bad[i] = badness(len) + bad[j];
				}
				++j;
				len = length(i, j, wordList);
			} // while j is not past the end of the wordList
		} // for all words in the wordList

		// print out the justified text to the console
		int j = 0;
		while(j < wordList.size()) {
			for(int i = j; i < DP[j]; ++i) {
				System.out.print(wordList.get(i) + " ");
			}
			System.out.println();
			j = DP[j];
		}
	}

	/**
	 * Counts the number of characters in a sublist of wordlist,
	 * adding spaces in between words.
	 * @params 	int i = starting index (incluseive)
	 * 			int j = ending index (exclusive)
	 * 			ArrayList<String> wordList = list of words
	 * @return 	length of the sublist
	 */
	public static int length(int i, int j, ArrayList<String> wordList) {
		int len = 0;
		
		// if j is not in the wordList
		if(j > wordList.size()) {
			return Integer.MAX_VALUE;
		}

		// count the number of chars in sublist
		for(int index = i;  index < j; ++index) {
			len += wordList.get(index).length() + 1;
		}
		
		--len; // remove extra space at the end
		
		if(len > PAGE_WIDTH) {
			return Integer.MAX_VALUE;
		}
		return len;
	}

	/**
	 * Calculates the badness of a line break given the
	 * length of the line.
	 * @param int len = length of the line
	 * @return badness of the line break
	 */
	public static int badness(int len) {
		return (int) Math.pow(PAGE_WIDTH - len, 3);
	}
	
	/**
	 * Main function for the static class that takes
	 * a test.txt file and prints justified text to the
	 * console.
	 */
	public static void main(String[] args) {
		ArrayList<String> words = readFile("test.txt");
		justification(words);
	}
}