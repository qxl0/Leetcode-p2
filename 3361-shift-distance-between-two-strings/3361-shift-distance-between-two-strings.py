class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:        
        total_next,total_prev = sum(nextCost),sum(previousCost)
        nextsum = list(accumulate(nextCost))
        prevsum = list(accumulate(previousCost))
        def nextmove(c1,c2):
            # calcu cost c1->c2 use nextCost
            i = ord(c1)-ord('a')
            j = ord(c2)-ord('a')            
            ret = None
            if i==j:return 0
            if i<j:
                ret= nextsum[j-1]-(nextsum[i-1] if i>0 else 0)
            else:
                p = nextsum[i-1]-(nextsum[j-1] if j>0 else 0)
                ret = total_next-p
            # print(f'->{c1},{c2}: {ret}')
            return ret
        def prevmove(c1,c2):
            # calcu cost c1->c2 use nextCost
            i = ord(c1)-ord('a')
            j = ord(c2)-ord('a')
            ret = None
            if i==j:return 0
            if i>j:
                ret= prevsum[i]-(prevsum[j] if j>=0 else 0)
            else:
                p = prevsum[j]-(prevsum[i] if i>=0 else 0)
                ret = total_prev-p
            # print(f'->Prev, {c1},{c2}: {ret}')
            return ret
        ret = 0
        for sch,tch in zip(s,t):
            ret += min(nextmove(sch,tch), prevmove(sch,tch))
        return ret

