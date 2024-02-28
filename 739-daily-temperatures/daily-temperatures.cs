public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        int[] nextLarger = new int[n];
        Array.Fill(nextLarger, n);

        Stack<int> stack = new();
        for (int i=0;i<n;i++) {
            while (stack.Count>0 && temperatures[stack.Peek()]<temperatures[i]) {
                int top = stack.Pop();
                nextLarger[top] = i;
            }
            stack.Push(i);
        }

        int[] ans = new int[n];
        for (int i=0;i<n;i++) {
            if (nextLarger[i]!=n)
                ans[i] = nextLarger[i]-i;
            else
                ans[i] = 0;
        }

        return ans;
    }
}