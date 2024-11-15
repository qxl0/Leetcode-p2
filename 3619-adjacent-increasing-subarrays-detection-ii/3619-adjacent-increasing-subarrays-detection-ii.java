import java.util.stream.IntStream;

class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int size = nums.size();
        List<Integer> suff = IntStream.range(0, size)
                            .mapToObj(i -> 1)
                            .collect(Collectors.toList());
        for (int i=size-2;i>=0;i--) {
            if (nums.get(i)<nums.get(i+1)) {
                suff.set(i, suff.get(i+1) + 1);
            }
        }

        int result = binarySearch(nums, suff);
        return result;        
    }

    private int binarySearch(List<Integer> nums, List<Integer> suff) {
        int left = 1, right = nums.size()/2;
        int res = 0;
        while (left<=right) {
            int mid = left + (right-left)/2;
            if (f(mid, suff, nums)) {
                res = mid;
                left = mid + 1;
            }
            else {
                right = mid -1;
            }
        }

        return res;
    }

    private boolean f(int mid, List<Integer> suff, List<Integer> nums) {
        int i = 0;
        while (i <= (nums.size()-2*mid)) {
            if (suff.get(i)>=mid && suff.get(i+mid)>=mid) {
                return true;
            }
            i += 1;
        }
        return false;
    }
}