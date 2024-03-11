public class Solution {
    public string CustomSortString(string order, string s) {
        Dictionary<char,int> count = new();
        foreach(var ch in s) {
            if (!count.ContainsKey(ch)) {
                count[ch] = 0;
            }
            count[ch] += 1;
        }

        List<char> ans = new();
        foreach (var ch in order) {
            if (count.ContainsKey(ch)) {
                for (int i=0;i<count[ch];i++)
                    ans.Add(ch);
                count.Remove(ch);
            }
        }

        foreach (var ch in count.Keys) {
            for (int i=0;i<count[ch];i++) {
                ans.Add(ch);
            }
        }

        return new string(ans.ToArray());
    }
}