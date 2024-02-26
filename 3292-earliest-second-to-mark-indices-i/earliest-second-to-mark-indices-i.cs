public class Solution {
    int n,m;
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        n = nums.Length;
        m = changeIndices.Length;
        int[] nums2 = new int[n+1];
        Array.Copy(nums,0, nums2, 1, n);        
                
        int left = 1, right = m+1;
        while (left<right) {
            int mid = left+(right-left)/2;
            if (checkok(mid, nums2, changeIndices)) 
                right = mid;
            else 
                left = mid+1;
        }
        return left==m+1?-1:left;
    }

    private bool checkok(int mid, int[] nums, int[] changes) {
        // check if mid is enough to mark all in nums2[1:n]
        Dictionary<int,int> last = new();
        for (int i=0;i<mid;i++) {
            last[changes[i]] = i;
        }
        if (last.Count != n) 
            return false;
        int cnt = 0;
        for (int i=0;i<mid;i++) {
            // if it's last time we visit i
            if (i==last[changes[i]]) {
                if (cnt<nums[changes[i]]) return false;
                else cnt -= nums[changes[i]];
            }
            else 
                cnt += 1;
        }
        return true;
    }
}