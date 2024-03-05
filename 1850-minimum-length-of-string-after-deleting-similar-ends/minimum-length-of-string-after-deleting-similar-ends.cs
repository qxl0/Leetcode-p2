public class Solution {
    public int MinimumLength(string s) {
        LinkedList<char> slst = new LinkedList<char>(s.ToCharArray());
        int n = s.Length;

        while (slst.Count > 1)
        {
            char cur = slst.First.Value;
            if (cur != slst.Last.Value)
                break;
            while (cur == slst.First.Value && cur == slst.Last.Value)
            {
                slst.RemoveFirst();
                if (slst == null || slst.Count == 0)
                    return 0;
            }
            while (cur == slst.Last.Value)
            {
                slst.RemoveLast();
                if (slst == null || slst.Count == 0)
                    return 0;
            }
        }

        return slst.Count;
    }
}