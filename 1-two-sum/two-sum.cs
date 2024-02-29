public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int n = nums.Length;
        Dictionary<int,int> Map = new();
        List<int> ans = new();
        for (int i=0;i<n;i++) {
            if (Map.ContainsKey(target-nums[i])) {                
                ans.Add(i);
                ans.Add(Map[target-nums[i]]);
                return ans.ToArray();
            }
            if (!Map.ContainsKey(nums[i]))
                Map.Add(nums[i], i);
        }

        return ans.ToArray();
    }
}