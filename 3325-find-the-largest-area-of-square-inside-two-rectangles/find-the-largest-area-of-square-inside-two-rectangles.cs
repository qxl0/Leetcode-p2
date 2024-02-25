public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long ret = 0;
        // var zipped = bottomLeft.Zip(topRight, (p1,p2)=>(p1,p2));
        // zipped.OrderBy()
        for (int i=0;i<bottomLeft.Length;i++) {
            for (int j=i+1;j<bottomLeft.Length;j++) {
                // i, j
                int ni=i;
                int nj=j;
                if (bottomLeft[ni][0]>bottomLeft[nj][0] || 
                    bottomLeft[ni][0]==bottomLeft[nj][0] && topRight[ni][1]>topRight[nj][1]){
                    int tmp = nj;
                    nj = ni;
                    ni = tmp;
                }
                int x1 = bottomLeft[ni][0];
                int y1 = bottomLeft[ni][1];
                int x2 = topRight[ni][0];
                int y2 = topRight[ni][1];

                int u1 = bottomLeft[nj][0];
                int v1 = bottomLeft[nj][1];
                int u2 = topRight[nj][0];
                int v2 = topRight[nj][1];

                if (u1>=x2 || v1>=y2) continue;

                long new_x = Math.Min(x2, u2)-Math.Max(x1,u1);
                long new_y = Math.Min(y2, v2)-Math.Max(y1,v1);

                // Console.WriteLine($"{i},{j}, new_x={new_x}, new_y={new_y}");
                if (new_x<0 || new_y<0) continue;
                if (new_x!=new_y) {
                    ret = Math.Max(ret, Math.Min(new_x,new_y)*Math.Min(new_x,new_y));
                } 
                else {                    
                    ret = Math.Max(ret, new_x*new_y);
                }
                
            }
        }

        return ret;
    }
}