class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = inf 
        count = [0]*32
        n = len(nums)
        def addtocount(x):
            i=0
            while i<32:
                if (x>>i)&1==1:
                    count[i]+= 1
                i += 1
        def removefromcount(x):
            i=0
            while i<32:
                if (x>>i)&1==1:
                    count[i]-= 1
                i += 1
        def getvalue(count):
            ret = 0
            for i in range(32):
                if count[i]!=0:
                    ret += 1<<i    
            return ret 
        
        i  = 0
        for j in range(n):
            addtocount(nums[j])
            if getvalue(count)<k:continue  
            while i<=j and getvalue(count)>=k:
                ret = min(ret, j-i+1)
                removefromcount(nums[i])
                i += 1
            
        return ret if ret<inf else -1