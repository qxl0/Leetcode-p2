public class Solution {
    Dictionary<char,List<string>> Map = new Dictionary<char,List<string>>()
        {
            {'2', new List<string>(){"a","b","c"}},
            {'3', new List<string>(){"d","e","f"}},
            {'4', new List<string>(){"g","h","i"}},
            {'5', new List<string>(){"j","k","l"}},
            {'6', new List<string>(){"m","n","o"}},
            {'7', new List<string>(){"p","q", "r","s"}},
            {'8', new List<string>(){"t","u","v"}},
            {'9', new List<string>(){"w","x","y", "z"}}
        };

    List<string> ret = new List<string>();
    public IList<string> LetterCombinations(string digits) {
        if (digits.Length==0) {
            return ret;
        }
        helper(digits, 0, new StringBuilder());
        
        return ret;
    }
    private void helper(string digits, int idx, StringBuilder cur) {
        int n = digits.Length;

        if (idx == n) {
            ret.Add(cur.ToString());
            return;
        }

        foreach (var ch in Map[digits[idx]]) {
            cur.Append(ch);
            helper(digits, idx + 1, cur);
            cur.Remove(cur.Length-1,1);
        }
    }
}