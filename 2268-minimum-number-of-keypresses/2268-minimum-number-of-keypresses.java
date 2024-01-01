class Solution {
    public int minimumKeypresses(String s) {
        int ret = 0;
        Map<Character, Integer> charToInt = new HashMap<>();
        for (var ch : s.toCharArray()) {
            charToInt.put(ch, charToInt.getOrDefault(ch, 0) + 1);
        }

        // sort based on frequency
        List<Map.Entry<Character,Integer>> lst = new ArrayList<>(charToInt.entrySet());
        Collections.sort(lst, new Comparator<Map.Entry<Character,Integer>>(){
            @Override
            public int compare(Map.Entry<Character,Integer> o1, Map.Entry<Character,Integer> o2) {
                return o2.getValue() - (o1.getValue());
            }
        });

        // loop through lst
        int i = 0;
        for (var item : lst){
            int freq = item.getValue();
            ret += freq*(1 + Math.floor(i/9));
            i += 1;
        }

        return ret;
    }
}