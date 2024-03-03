public class Solution {
    public int[] ResultArray(int[] nums) {
        List<int> arr1 = new(), arr2 = new();

         arr1.Add(nums[0]);
         arr2.Add(nums[1]);
         int i1=0,i2=0;

        for (int i=2;i<nums.Length;i++) {
            if (arr1[i1]>arr2[i2]) {
                arr1.Add(nums[i]);
                i1 += 1;                
            } else {
                arr2.Add(nums[i]);
                i2 += 1;
            }
        }

        arr1.AddRange(arr2);

        return arr1.ToArray();
    }
}