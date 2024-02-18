public class Solution {
    public int CountPrefixSuffixPairs(string[] words) {
        int ret =0;
        for (int i=0;i<words.Length;i++) {
            for (int j=i+1; j<words.Length; j++) {
                if (isPrefixAndSuffix(words[i], words[j]))
                    ret += 1;
            }
        }

        return ret;
    }

    private bool isPrefixAndSuffix(string str1, string str2) {
        // str1 is both prefix and suffix of str2
        return str2.IndexOf(str1)==0 && str2.LastIndexOf(str1)==str2.Length-str1.Length;
    }
}