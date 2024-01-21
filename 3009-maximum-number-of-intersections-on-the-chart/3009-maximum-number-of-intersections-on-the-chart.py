class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        # sweep line question. however, the following pt is at 0.5 
        # [0,1,0,1,0]: 4
        # so we enlarge all values to 2 times 
        dc = {v:2*i for i,v in enumerate(sorted(set(y)))}
        y = [dc[v] for v in y]

        diff = defaultdict(int)
        n = len(y)
        for i in range(1,n):
            # y[i-1], y[i]
            s = y[i-1]
            if i==n-1:
                e = y[i]
            else: # i < n-1
                if y[i]>y[i-1]:
                    e = y[i]-1
                else: # y[i]<y[i-1]
                    e = y[i]+1
            diff[min(s,e)]+=1
            diff[max(s,e)+1]-=1

        ret = 0
        level = 0
        for k in sorted(diff):
            x = diff[k]
            level += x
            ret = max(ret, level)
        return ret 