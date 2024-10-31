class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        for i,a in enumerate(nums):
            if a%2==0:
                continue
            # xx OR (xx+1) == a
            for x in range(1001):
                if (x | (x + 1)) == a:
                    ans[i] = x
                    break
        return ans