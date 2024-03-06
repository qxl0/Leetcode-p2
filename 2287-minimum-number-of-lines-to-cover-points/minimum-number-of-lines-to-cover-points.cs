public class Solution {
    public int MinimumLines(int[][] points) {
        int n = points.Length;
        int[] dp = new int[(1<<n)]; // dp[i]: min lines to contain all pts represented by state i
        Array.Fill(dp, int.MaxValue/2); 

        for (int state=1;state<(1<<n);state++) {
            if (formALine(state, points) || totalSetbits(state)<=2) {
                dp[state] = 1;
            }
        }
        for (int state = 1; state<(1<<n); state++) {
            for (int substate = state; substate>0; substate=((substate-1)&state)) {
                dp[state] = Math.Min(dp[state], dp[substate]+dp[state-substate]);
            }
        }

        return dp[(1<<n)-1];
    }

    private bool formALine(int state, int[][] points) {
        List<int> temp = new();
        for (int i=0;i<points.Length;i++) {
            if (((state>>i)&1)==1) {
                temp.Add(i);
            }
        }

        if (temp.Count<=2)
            return true;

        for (int i=2;i<temp.Count;i++) {
            int a=temp[0],b=temp[1],c=temp[i];
            int ax=points[a][0],ay=points[a][1];
            int bx=points[b][0],by=points[b][1];
            int cx=points[c][0],cy=points[c][1];
            if ((by-ay)*(cx-ax)!=(cy-ay)*(bx-ax)) {
                return false;
            }
        }
        return true;
    }

    private bool isNthBitSet(int x, int n) {
        return (x&(1<<n))!=0;
    }

    private int totalSetbits(int x) {
        int ret = 0;
        for (int i=0;i<32;i++) {
            if (isNthBitSet(x, i)) {
                ret += 1;
            }
        }
        return ret;
    }
}