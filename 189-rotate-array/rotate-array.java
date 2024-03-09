class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        int count = 0;
        int start = 0;

        while (count < n) {
            
            int current = start;
            int current_val = nums[start];

            while (true) {
                int next = (current+k)%n;
                int temp = nums[next];

                // shift current -> next 
                nums[next] = current_val;
                count += 1;

                current = next;
                current_val = temp;

                if (current == start) 
                    break;
            }

            start += 1;
        }
    }
}