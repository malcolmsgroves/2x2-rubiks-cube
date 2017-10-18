import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;
import java.io.File;
import java.util.List;

public class justify {


	public static final int PAGE_WIDTH = 40;

	public static ArrayList<String> readPuzzle(String filename) {

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

	public static void justification(ArrayList<String> wordList) {
		int[] bad = new int[wordList.size() + 1];
		int[] DP = new int[wordList.size()];

		for(int j = 0; j < wordList.size(); ++j) {
			bad[j] = Integer.MAX_VALUE;
		}
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
			}
		}

		int j = 0;
		while(j < wordList.size()) {
			for(int i = j; i < DP[j]; ++i) {

				System.out.print(wordList.get(i) + " ");
			}
			System.out.println();
			j = DP[j];
		}
	}

	public static int length(int i, int j, ArrayList<String> wordList) {
		int len = 0;
		if(j > wordList.size()) {
			return Integer.MAX_VALUE;
		}

		for(int index = i;  index < j; ++index) {
			len += wordList.get(index).length() + 1;
		}
		--len;
		if(len > PAGE_WIDTH) {
			return Integer.MAX_VALUE;
		}
		return len;
	}

	public static int badness(int len) {
		return (int) Math.pow(PAGE_WIDTH - len, 3);
	}
	
	public static void main(String[] args) {
		ArrayList<String> words = readPuzzle("test.txt");
		justification(words);
	}
}