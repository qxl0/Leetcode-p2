

import static java.lang.Math.max;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> count = new HashMap<>();

        for (var n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        Integer ret = 0;
        Integer maxFreq = 0;

        for (var item : count.entrySet()) {
            Integer n = item.getKey();
            Integer freq = item.getValue();

            if (freq>maxFreq) {
                maxFreq = freq;
                ret = n;
            }
        }

        return ret;
    }
}