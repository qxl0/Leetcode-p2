class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> ret = new ArrayList<>();
        ret.add(new ArrayList<Integer>());
        ret.add(new ArrayList<Integer>());
        Set<Integer> set1 = new HashSet<>();
        
        for (int i=0; i<nums1.length; i++)
            set1.add(nums1[i]);
        
        Set<Integer> set2 = new HashSet<>();
        for (int i=0; i<nums2.length; i++)
            set2.add(nums2[i]);
        
        for (var ele : set1) {
            if (!set2.contains(ele))
                ret.get(0).add(ele);            
        }
        
        for (var ele: set2) {
            if (!set1.contains(ele))
                ret.get(1).add(ele);
        }
        
        return ret;
        
    }
}