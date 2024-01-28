class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        Set<String> fset = new HashSet<>();
        for (var fw: forbidden)
            fset.add(fw);
        
        int ret = 0, left = 0;
        
        for (int i=0;i<word.length();i++) {
            for (int j = Math.max(i-10, left); j<=i; j++) {
                if (fset.contains(word.substring(j, i+1)))
                    left = j+1;
            };
            
            ret = Math.max(ret, i-left+1);                    
        }
        return ret;
    }
}