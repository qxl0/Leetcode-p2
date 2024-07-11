class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ret = 0
        for op in logs:
            if op=='./': continue
            elif op=='../': 
                ret -=1
                ret = max(ret,0)
            else:
                ret +=1
        return max(ret,0)