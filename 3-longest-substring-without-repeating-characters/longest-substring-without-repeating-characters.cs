public static class DictionaryExtensions
{
    public static TValue GetOrDefault<TKey, TValue>(this Dictionary<TKey, TValue> dict, TKey key, TValue defaultValue = default)
    {
        return dict.TryGetValue(key, out TValue value) ? value : defaultValue;
    }
}
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        Dictionary<char,int> Map = new();
        int n = s.Length;
        int ans = 0;
        int i=0;
        for (int j=0;j<n;j++) {
            var x = s[j];
            if (!Map.ContainsKey(x)) Map[x] = 0;
            Map[x] += 1;

            // now 
            while (i<n && Map[x]>1) {
                Map[s[i]] -= 1;
                if (Map[s[i]] == 0) {
                    Map.Remove(s[i]);
                }
                i += 1;
            }

            // update ans
            ans = Math.Max(ans, j-i+1);
        }

        return ans;
    }
}