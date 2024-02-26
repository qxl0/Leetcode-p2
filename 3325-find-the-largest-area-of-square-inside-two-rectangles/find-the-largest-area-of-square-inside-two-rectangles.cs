public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long ret = 0;
        for (int i=0;i<bottomLeft.Length;i++) {
            for (int j=i+1;j<topRight.Length;j++) {
                long minx = Math.Max(bottomLeft[i][0], bottomLeft[j][0]);
                long maxx = Math.Min(topRight[i][0], topRight[j][0]);
                long miny = Math.Max(bottomLeft[i][1], bottomLeft[j][1]);
                long maxy = Math.Min(topRight[i][1], topRight[j][1]);

                if (minx<maxx && miny<maxy) {
                    long s = Math.Min(maxx-minx, maxy-miny);
                    ret = Math.Max(ret, s*s);
                }
            }
        }
        return ret;
    }
}