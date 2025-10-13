class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int i: nums){
            set.add(i);
        }
        
        
        int max = 0;
        for (int n: nums){
            if (!set.contains(n))
                continue;
        
            set.remove(n);
            int left = n - 1;
            int right = n + 1;
            while (set.contains(left))
                set.remove(left--);
            while (set.contains(right))
                set.remove(right++);
            
            //System.out.format("n=%d,len=%d\n", n, len);
            max = Math.max(max, right - left - 1);
        }
        return max;
    }
}