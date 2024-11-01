class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def take1(x):
            s = list(bin(x)[2:])
            i = len(s)-1
            while i>=0 and s[i]=='1':
                i -= 1
            if i+1<len(s):            
                s[i+1] = '0'
            return int(''.join(s),2)
                
        n = len(nums)
        ans = [-1]*n
        for i in range(n):
            x = nums[i]
            if x%2==0:
                continue
            # x is odd 
            # 1000111 -> 100011
            ans[i] = take1(x)
        return ans
