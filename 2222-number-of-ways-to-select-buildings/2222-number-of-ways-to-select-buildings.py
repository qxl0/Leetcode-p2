class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        loop through s, if s[i]=='0', ret += 1's count on left * 1's count on right
        """
        total_0,total_1 = s.count('0'),s.count('1')
        n = len(s)
        ret = 0
        
        left_0,left_1 = 0,0
        for ch in s:
            if ch=='0':
                ret += left_1*(total_1-left_1)
            else:
                ret += left_0*(total_0-left_0)
            left_0 += (ch=='0')
            left_1 += (ch=='1')
        return ret
            