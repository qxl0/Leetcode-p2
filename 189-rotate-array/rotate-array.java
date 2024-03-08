class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;

        k = k%n;

        List<Integer> temp = new ArrayList<>();
        for (int i=n-k;i<n;i++) {
            temp.add(nums[i]);
        }

        for (int i=0;i<n-k;i++) {
            temp.add(nums[i]);
        }

        System.out.println(temp);
        for (int i=0;i<n;i++) {
            nums[i] = temp.get(i);
        }

    }
}