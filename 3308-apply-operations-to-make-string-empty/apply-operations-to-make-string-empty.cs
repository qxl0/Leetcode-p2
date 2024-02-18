public class Solution {
    public string LastNonEmptyString(string s) {
        Dictionary<char, int> Map = new Dictionary<char,int>();

        int mx = 0;
        for (int i=0;i<s.Length;i++) {
            if (!Map.ContainsKey(s[i])) {
                Map[s[i]] = 0;
            }
            Map[s[i]] += 1;

            mx = Math.Max(mx, Map[s[i]]);
        }

        StringBuilder ret = new StringBuilder();
        for (int i=s.Length-1;i>=0;i--) {
            if (Map[s[i]] == mx && !ret.ToString().Contains(s[i]))
                ret.Insert(0,s[i]);
        }

        return ret.ToString();
    }
}