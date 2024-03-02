/** 
 * Definition of commonSetBits API (defined in the parent class Problem).
 * int CommonSetBits(int num);
 */

public class Solution : Problem {
    public int FindNumber() {
        int n = 0;

        for (int i=0;i<32;i++) {
            if (CommonSetBits(1<<i)==1) {
                n += 1<<i;
            }
        }

        return n;
    }
}