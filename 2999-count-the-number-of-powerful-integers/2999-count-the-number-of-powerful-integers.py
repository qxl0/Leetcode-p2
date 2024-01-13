class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def helper(x,s):
            # return num of power integers not greater than x
            # s is suffix all PI counted
            xstr = str(x)
            n = len(xstr)-len(s)
            if n<0: return 0
            if n==0: return int(x>=int(s))
            
            ret = 0
            for i in range(n):
                if int(xstr[i])<=limit:
                    ret += int(xstr[i])*pow((limit+1),n-1-i)                    
                else:  # >= limit
                    ret += (limit+1)*pow(limit+1, n-1-i)
                    break
            else:
                ret += int(s<=xstr[n:])
            return ret 
            
        return helper(finish,s)-helper(start-1,s)