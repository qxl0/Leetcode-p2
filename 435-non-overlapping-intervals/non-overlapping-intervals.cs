public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        Array.Sort(intervals, (a,b)=>a[1].CompareTo(b[1]));

        int last = int.MinValue;
        int ans = 0;

        foreach (var row in intervals) {
            int start = row[0];
            int end = row[1];

            if (last<=start) {
                last = end;
            } else {
                ans += 1;
            }
        }

        return ans;
    }
}