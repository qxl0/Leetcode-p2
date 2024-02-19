public class Solution {
    public int LongestCommonPrefix(int[] arr1, int[] arr2) {
        Dictionary<int, int> Map = new Dictionary<int, int>();

        // preprocess
        foreach (var x in arr1) {
            AddPrefixToMap(x, Map);
        }

        // check 
        int ret = 0;
        foreach (var x in arr2) {
            int y = x;
            while (y>0) {
                if (Map.ContainsKey(y)){
                    ret = Math.Max(ret, y.ToString().Length);
                    break;
                }
                y = y/10;
            }
        }
        
        return ret;
    }

    private void AddPrefixToMap(int x, Dictionary<int,int> Map) {
        while (x>0) {
            if (!Map.ContainsKey(x)) {
                Map[x] = 0;
            }
            Map[x] += 1;
            x = x/10;
        }
    }
}