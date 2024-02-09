class Solution {
    public boolean closeStrings(String word1, String word2) {
        Set<Character> set1 = new HashSet<>();
        Set<Character> set2 = new HashSet<>();

        for (var ch : word1.toCharArray()) 
            set1.add(ch);
        for (var ch: word2.toCharArray())
            set2.add(ch);
        
        if (!set1.equals(set2))
            return false;
        
        // now we know they contain the same chars
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();

        for (var ch: word1.toCharArray()){
            map1.put(ch, map1.getOrDefault(ch, 0) + 1);            
        }

        for (var ch: word2.toCharArray()){
            map2.put(ch, map2.getOrDefault(ch, 0) + 1);            
        }

        // now check map1.values() should equal to map2.values()
        List<Integer> val1lst = new ArrayList<>(map1.values());
        Collections.sort(val1lst);
        List<Integer> val2lst = new ArrayList<>(map2.values());
        Collections.sort(val2lst);
        boolean isClose =  val1lst.equals(val2lst);
        return isClose;
    }
}