class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int a : asteroids) {
            int cur = a;
            while (!stack.isEmpty() && stack.peek()>0 && cur<0)
                if (Math.abs(cur)>stack.peek())
                    stack.pop();
                else if (Math.abs(cur)<stack.peek())
                    cur = 0;
                else {
                    cur = 0;
                    stack.pop();
                }
                    
            // check 
            if (cur != 0)
                stack.push(cur);
        }
        int[] ret = new int[stack.size()];
        for (int i=ret.length-1;i>=0;i--) {
            ret[i] = stack.pop();
        }
        return ret;
    }
}