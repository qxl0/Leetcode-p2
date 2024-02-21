public class Solution {
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.Length;
        int[] ans = new int[n];
        Array.Sort(potions);

        for (int i=0;i<n;i++) {
            ans[i] = find(spells[i], potions, success);
        }
        return ans;
    }

    private int find(int spell, int[] potions, long success) {
        int left = 0, right = potions.Length-1;
        while (left<=right) {
            int mid=left+(right-left)/2;
            long product = (long)spell * potions[mid];
            if (product >= success) {
                right = mid-1;
            } 
            else {
                left = mid+1;
            }
        }
        return (int)(potions.Length-left);
    }
}