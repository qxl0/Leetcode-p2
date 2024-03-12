public class Solution {
    public string LargestPalindromic(string num) {
        Dictionary<char,int> Map = new();
        foreach (var ch in num){
            if (!Map.ContainsKey(ch)) {
                Map[ch] = 0;
            }
            Map[ch] += 1;
        }

        List<char> ans = new();
        char middle='\0';
        foreach (var key in Map.Keys) {
            int freq = Map[key];
            AddToAns(ans, key, freq/2);            
            if (freq%2==1 && middle<key) {
                middle = key;
            }
        }
        
        
        ans.Sort((x,y)=>y-x);
        string ret = string.Join("", ans.ToArray());
        ret = ret.TrimStart('0');
        ans.Reverse();
        string rev = string.Join("", ans);
        if (ret.Length>0)
            if (middle!='\0')
                return ret + middle +rev;
            else 
                return ret + rev;
        else 
            if (middle=='\0')
                return "0";
            return middle.ToString();

    }

    private void AddToAns(List<char> ans, char ch, int x) {        
        while (x>0) {
            ans.Add(ch);
            x -= 1;
        }
    }
}