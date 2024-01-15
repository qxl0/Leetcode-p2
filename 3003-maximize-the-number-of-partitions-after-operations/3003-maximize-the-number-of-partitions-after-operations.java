class Solution {
    int k;
    String s;    
    HashMap<Long,Integer> dp;
    public int maxPartitionsAfterOperations(String s, int k) {
        this.k = k;
        this.s = s;
        this.dp = new HashMap<>();
        return dfs(0, 0, true)+1;
    }
    private int dfs(int idx, int mask,boolean canchange) {
        // return: max number of partitions s[0:idx]
        
        long key = ((long)idx<<27|((long)mask<<1)|(canchange?1:0));
        if (dp.containsKey(key))            
            return dp.get(key);
        if (idx == s.length())
            return 0;
        int newmask = mask | (1<<(s.charAt(idx)-'a'));
        int ret = 0;
        if (Integer.bitCount(newmask)>k) {
            ret = 1 + dfs(idx + 1, (1<<(s.charAt(idx)-'a')),canchange);
        }
        else {
            ret = dfs(idx + 1, newmask,canchange);
        }

        if (canchange) {
            for (int i = 0; i<26; i++) {
                newmask = mask | (1<<i);
                if (Integer.bitCount(newmask)>k) {
                    ret = Math.max(ret, 1 + dfs(idx + 1, (1<<i), false));
                }
                else {
                    ret = Math.max(ret, dfs(idx + 1, newmask,false));
                }
            }
        }
        dp.put(key, ret);
        return ret;
    }
}