class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        if (n<=k) {
            return "0";
        }

        Stack<Character> stack = new Stack<>();
        for (var x : num.toCharArray()) {
            while (k>0 && !stack.isEmpty() && stack.peek()>x) {
                stack.pop();
                k -= 1;
            }

            stack.push(x);
        }

        while (k>0) {
            stack.pop();
            k -= 1;
        }
        String[] ret = new String[stack.size()];
        int i = 0;
        for (var ch: stack) {
            ret[i++] = ch.toString();
        }
        
        String ans = String.join("", ret).replaceAll("^0+","");
        if (ans.isEmpty())
            return "0";
        return ans;

    }
}