class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> count = new HashMap<>();
        for (var x : nums2) {
            count.put(x, count.getOrDefault(x, 0)+1);
        }

        ArrayList<Integer> ret = new ArrayList<>();
        for (var x: nums1) {
            if (!count.containsKey(x))
                continue;
            ret.add(x);
            count.put(x, count.get(x)-1);
            if (count.get(x) == 0) {
                count.remove(x);
            }
        }

        return ret.stream().mapToInt(x -> x).toArray();
    }
}