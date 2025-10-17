class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()        
        def ksum(nums, k, target):
            n = len(nums)
            if k == 2:
                return twosum(nums, target)
            ans = []
            for i in range(n):
                if i-1>=0 and nums[i]==nums[i-1]:
                    continue
                for ret in ksum(nums[i+1:], k-1, target-nums[i]):
                    ans.append(ret+[nums[i]])
            return ans
        def twosum(nums, target):
            n = len(nums)
            l, r = 0, n-1
            ret = []
            while l<r:
                total = nums[l]+nums[r]
                if total > target or r+1<n and nums[r] == nums[r+1]:
                    r -= 1
                elif total < target or l-1>=0 and nums[l]==nums[l-1]:
                    l += 1
                else:
                    ret.append([nums[l], nums[r]])                    
                    l += 1
                    r -= 1
            return ret
        return ksum(nums, 4, target)