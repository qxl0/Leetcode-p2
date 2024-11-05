class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        def xsum(i):
            # i, ..., i+k-1  --> k 
            count = Counter(nums[i:i+k])
            lst = count.most_common()
            ans = 0
            lst.sort(key=lambda x:(-x[1],-x[0]))
            for i in range(min(x, len(lst))):
                ans += lst[i][0]*lst[i][1]
            return ans


        ans = []
        for i in range(n-k+1):
            # i, i+k+1, 
            ans.append(xsum(i))
        return ans