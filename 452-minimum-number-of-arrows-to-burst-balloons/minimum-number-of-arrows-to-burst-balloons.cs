public class Solution {
    public int FindMinArrowShots(int[][] points) {
        // sort by end points
        Array.Sort(points, (x,y)=>x[1].CompareTo(y[1]));
        int ret = 1;
        int last = points[0][1];
        foreach (var point in points) {
            int end = point[1];
            int start = point[0];
            if (start>last) {
                ret += 1;
                last = end;
            }
        }

        return ret;
    }
}