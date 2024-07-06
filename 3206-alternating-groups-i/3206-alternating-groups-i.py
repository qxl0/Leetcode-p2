class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ret = 0
        for i in range(n):
            if i==0:
                if colors[0]!=colors[n-1] and colors[0]!=colors[1]:
                    ret += 1
                continue
            if i==n-1:
                if colors[n-1]!=colors[0] and colors[n-1]!=colors[n-2]:
                    ret += 1
                continue
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                ret += 1
        return ret
