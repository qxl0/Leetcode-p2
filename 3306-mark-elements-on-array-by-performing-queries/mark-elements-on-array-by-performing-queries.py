class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:        
        n = len(nums)
        ans = []
        q =[(x,i) for i,x in enumerate(nums)]
        heapify(q)
        Map = defaultdict(int)
        for idx, k in queries:
            sm = ans[-1] if ans else sum(nums)
            # mark idx 
            sm_pop = 0
            if idx not in Map:
                sm_pop = nums[idx] 
                Map[idx] = nums[idx]             
            while k and q:                
                x,i = heappop(q)
                if i not in Map:
                    Map[i] = x 
                    k -= 1
                    sm_pop += x 
            ans.append(sm-sm_pop)
        return ans 
