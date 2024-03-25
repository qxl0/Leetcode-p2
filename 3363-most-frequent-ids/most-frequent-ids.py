class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:        
        count = Counter()
        q = []
        ans = []
        for i,f in zip(nums,freq):
            count[i]+=f
            heappush(q,(-count[i], i))
            while count[q[0][1]]!=-q[0][0]:
                heappop(q)
            ans.append(-q[0][0])
        return ans 