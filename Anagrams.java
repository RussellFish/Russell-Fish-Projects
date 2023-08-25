/**
 * Russell Fish
 * I pledge my honor that I have abided by the stevens honor cody stystem
 */

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


public class Anagrams {
    final Integer[] primes =
            {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97, 101};
    Map<Character,Integer> letterTable;
    Map<Long,ArrayList<String>> anagramTable;
    /**
     * This is a private helper method that initializes
     * the letterTable map with the corresponding
     * primes for each lowercase letter of the alphabet.
     */
    private void buildLetterTable() {
        letterTable = new HashMap<Character, Integer>();
        letterTable.put('a', 2);
        letterTable.put('b', 3);
        letterTable.put('c', 5);
        letterTable.put('d', 7);
        letterTable.put('e', 11);
        letterTable.put('f', 13);
        letterTable.put('g', 17);
        letterTable.put('h', 19);
        letterTable.put('i', 23);
        letterTable.put('j', 29);
        letterTable.put('k', 31);
        letterTable.put('l', 37);
        letterTable.put('m', 41);
        letterTable.put('n', 43);
        letterTable.put('o', 47);
        letterTable.put('p', 53);
        letterTable.put('q', 59);
        letterTable.put('r', 61);
        letterTable.put('s', 67);
        letterTable.put('t', 71);
        letterTable.put('u', 73);
        letterTable.put('v', 79);
        letterTable.put('w', 83);
        letterTable.put('x', 89);
        letterTable.put('y', 97);
        letterTable.put('z', 101);
    }


    Anagrams() {
        buildLetterTable();
        anagramTable = new HashMap<Long,ArrayList<String>>();
    }

    /**
     * This is the constructor of the Anagrams class.
     * It calls the buildLetterTable method to initialize the letterTable map
     * and initializes the anagramTable map.
     *
     */
    public void addWord(String s) {
        long hashCode = myHashCode(s);
        ArrayList<String> anagram = anagramTable.get(hashCode);
        if (anagram == null) {
            anagram = new ArrayList<String>();
            anagramTable.put(hashCode, anagram);
        }
        anagram.add(s);
    }


    public long myHashCode(String s) throws IllegalArgumentException {
        if (s.isEmpty()) {
            throw new IllegalArgumentException("String cannot be empty.");
        }

        long hashVar = 1;
        for (char c : s.toCharArray()) {
            int isPrime = letterTable.get(Character.toLowerCase(c));
            hashVar *= isPrime;
        }
        return hashVar;
    }


    public void processFile(String s) throws IOException {
        FileInputStream fstream = new FileInputStream(s);
        BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
        String strLine;
        while ((strLine = br.readLine()) != null)   {
            this.addWord(strLine);
        }
        br.close();
    }

    /**
     * This method returns the list of entries in the anagramTable map with the largest number of anagrams.
     * @return
     */
    public ArrayList<Map.Entry<Long, ArrayList<String>>> getMaxEntries() {
        ArrayList<Map.Entry<Long, ArrayList<String>>> maxEntries = new ArrayList<>();
        int maximumAnagramSize = 0;

        for (Map.Entry<Long, ArrayList<String>> entry : anagramTable.entrySet()) {
            ArrayList<String> anagrams = entry.getValue();
            if (anagrams.size() > maximumAnagramSize) {
                maximumAnagramSize = anagrams.size();
                maxEntries.clear();
                maxEntries.add(entry);
            } else if (anagrams.size() == maximumAnagramSize) {
                maxEntries.add(entry);
            }
        }

        return maxEntries;
    }


    public static void main(String[] args) {
        Anagrams a = new Anagrams();

        final long startTime = System.nanoTime();
        try {
            a.processFile("words_alpha.txt");
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        ArrayList<Map.Entry<Long,ArrayList<String>>> maxEntries = a.getMaxEntries();
        final long estimatedTime = System.nanoTime() - startTime;
        final double seconds = ((double) estimatedTime/1000000000);
        System.out.println("Time: "+ seconds);
        System.out.println("List of max anagrams: "+ maxEntries);
    }
}
