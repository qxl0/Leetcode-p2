public class Solution {
    public bool IsPossibleToSplit(int[] nums) {
        Dictionary<int,int> count = new();
        foreach (var x in nums) {
            if (!count.ContainsKey(x)) {
                count[x] = 0;
            }
            count[x] += 1;

            if (count[x]>2){
                return false;
            }
        }
        return true;
    }
}