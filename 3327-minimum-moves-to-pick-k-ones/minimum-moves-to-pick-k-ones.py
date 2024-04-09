class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        nums = [i for i in range(len(nums)) if nums[i]==1]
        n = len(nums)
        presum = list(accumulate(nums, initial=0))
        ret = inf 
        for m in range(max(0,k-maxChanges), min(k, max(0,k-maxChanges)+3)+1):
            for i in range(n-m+1):
                cur = presum[i+m]-presum[i+m-m//2]-(presum[i+m//2]-presum[i])
                ret = min(ret, cur+(k-m)*2)
        return ret 