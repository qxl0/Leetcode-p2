public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        int count = s.Count(c=>c=='1');
        char[] charArr = s.ToCharArray();
        
        // 
        Array.Sort(charArr, (x,y)=>y-x);

        // 
        int n = charArr.Length;
        if (charArr[n-1]!='1') {
            int i=n-2;
            while (i>=0 && charArr[i]!='1') {
                i -= 1;
            }

            // when stop == '1'.
            if (i>=0) {
                // swap
                charArr[i]='0';
                charArr[n-1]='1';
            }
        }
        
        return new string(charArr);
    }
}