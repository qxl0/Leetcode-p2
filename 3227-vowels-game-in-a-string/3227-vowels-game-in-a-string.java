class Solution {
    public boolean doesAliceWin(String s) {
        Set<Character> vowels = Set.of('a','e','i','o','u');

        int countofvowels=0;
        for (var ch : s.toCharArray()) {
            countofvowels += vowels.contains(ch) ? 1:0;
        }
        if (countofvowels==0)
            return false;
        else if (countofvowels%2==1)
            return true;
        else {
            return true;
        }
        
    }
}