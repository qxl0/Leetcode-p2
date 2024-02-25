public class Solution {
    public int MinFlips(int a, int b, int c) {
        int ret = 0;

        int i = 0;
        int len = (int)Math.Log(Math.Pow(10,9), 2);
        while (i < len+1)
        {
            if (((c >> i) & 1) == 1)
            {
                if (((a >> i) & 1) == 0 && ((b >> i) & 1) == 0)
                {
                    ret += 1;
                    Console.WriteLine($"i={i}, 1");
                }
            }
            else
            {
                if (((a >> i) & 1) == 1)
                {
                    // Console.WriteLine($"i={i}, 1");
                    ret += 1;
                }           
                if  (((b >> i) & 1) == 1) {
                    ret += 1;
                }         
            }
            i += 1;
        }

        return ret;
    }
}