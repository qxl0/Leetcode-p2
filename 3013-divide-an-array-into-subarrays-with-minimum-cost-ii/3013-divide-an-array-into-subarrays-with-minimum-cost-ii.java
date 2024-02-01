class Solution {
    public long minimumCost(int[] nums, int k, int dist) {
        // windows size: dist+1
        // look for k-1 smallest element in window
        int n = nums.length;
        TreeSet<Integer> using = new TreeSet<>((a,b) -> nums[a]==nums[b] ? a-b : nums[a]-nums[b]);
        TreeSet<Integer> waiting = new TreeSet<>((a,b) -> nums[a]==nums[b] ? a-b : nums[a]-nums[b]);
        
        long res = Long.MAX_VALUE, curSum = 0l;
        
        // Add dist+1 to using
        for (int i=1;i<=dist+1;i++)
        {
            using.add(i);
            curSum += nums[i];
        }
        
        // only k-1 is needed, so move larger element to waiting
        while (using.size()>k-1){
            int i = using.pollLast();
            curSum -= nums[i];
            waiting.add(i);
        }
        
        res = Math.min(res, curSum);
        
        for (int i=1;i+dist+1<n;i++) {
            // check i 
            
            waiting.add(i+dist+1);
            
            // window: i, ... i+dist+1
            // remove i
            if (using.contains(i)) {
                curSum -= nums[i];
                using.remove(i);
                
                int j = waiting.pollFirst();
                curSum += nums[j];
                using.add(j);
            } else {
                // i is not in using
                waiting.remove(i);
                
                // compare 
                int u = using.last();
                int v = waiting.first();
                if (nums[u]>nums[v]) {
                    curSum -= nums[u];
                    using.remove(u);
                    waiting.add(u);
                    
                    curSum += nums[v];
                    waiting.remove(v);
                    using.add(v);
                }
            }
            
            res = Math.min(res, curSum);
        }
        return res+nums[0];
    }
}