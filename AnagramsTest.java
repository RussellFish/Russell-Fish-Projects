/**
 * Russell Fish
 * I pledge my honor that I have abided by the stevens honor cody stystem
 */
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

public class AnagramsTest {

    @Test
    public void testAddWord() {
        Anagrams a = new Anagrams();

        // Test adding single var
        String var = "test";
        a.addWord(var);
        ArrayList<String> tester = a.anagramTable.get(a.myHashCode(var));
        assertNotNull(tester);
        assertEquals(1, tester.size());
        assertTrue(tester.contains(var));

        // Test adding multiple anagrams
        String[] anagramWords = {"list", "silt", "slit", "tils"};
        for (String w : anagramWords) {
            a.addWord(w);
        }
        tester = a.anagramTable.get(a.myHashCode(anagramWords[0]));
        assertNotNull(tester);
        assertEquals(anagramWords.length, tester.size());
        for (String w : anagramWords) {
            assertTrue(tester.contains(w));
        }
    }



}
