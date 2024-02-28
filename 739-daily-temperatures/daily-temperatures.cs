public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        int[] nextLarger = new int[n];
        Array.Fill(nextLarger, n);
        int[] ans = new int[n];
        Array.Fill(ans, 0);
        Stack<int> stack = new();
        for (int i=0;i<n;i++) {
            while (stack.Count>0 && temperatures[stack.Peek()]<temperatures[i]) {
                int top = stack.Pop();
                ans[top] = i-top;
            }
            stack.Push(i);
        }

        return ans;
    }
}