public class Solution {
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        // convert to 0-indexed 
        int n = changeIndices.Length;
        for (int i=0;i<n;i++) {
            changeIndices[i] -= 1;
        }

        // binary search 
        int l=1,r = n;
        while (l<r) {
            int mid = l+(r-l)/2;

            if (checkok(mid, nums,changeIndices))
                r = mid;
            else
                l = mid+1;                
        }
        return checkok(l, nums,changeIndices) ? l: -1;
    }

    private bool checkok(int mid, int[] nums, int[] changeIndices) {
        int m = nums.Length;
        int[] last = new int[m];
        Array.Fill(last, -1);
        for (int i=0;i<mid;i++) {
            last[changeIndices[i]] = i;
        }

        // check if 
        
        for (int i=0;i<m;i++) {            
            if (last[i] == -1) 
                return false;
        }

        int count = 0;
        for (int i=0;i<mid;i++) {
            int idx = changeIndices[i];
            if (i!=last[idx]) {
                count += 1;
            }
            else {
                // have to mark
                count -= nums[idx];
                if (count<0) return false;
            }
        }

        return true;
    }
}