class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = inf    
        n = len(nums)
        count = [0]*32
        def addtocount(x):
            k=0 
            while k<32:
                if (x>>k)&1==1:
                    count[k] +=1 
                k += 1
        def removefromcount(x):
            k=0
            while k<32:
                if (x>>k)&1!=0:
                    count[k]-=1 
                k += 1
        def value(count):
            ret = 0
            for k in range(32):
                if count[k]!=0:
                    ret +=(1<<k) 
            return ret
        
        j = 0
        for i in range(n):
            addtocount(nums[i])
            if value(count)<k: continue 
            while j<=i and value(count)>=k:
                ret = min(ret, i-j+1)
                removefromcount(nums[j])
                j+=1
        return ret if ret<inf else -1