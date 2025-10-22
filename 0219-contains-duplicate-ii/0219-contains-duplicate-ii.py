class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # i-k, i+k
        Set = Counter(nums[:k])
        if n <= k:
            return len(Set)<len(nums)
        for i in range(k, n):
            Set[nums[i]]+=1
            if i - k > 0:
                Set[nums[i-k-1]] -= 1
                if Set[nums[i-k-1]] == 0:
                    del Set[nums[i-k-1]]
            # check
            if len(Set) < k + 1:
                return True
        return False