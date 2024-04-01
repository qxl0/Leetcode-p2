class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        sums = [ x+y for x,y in points]
        diffs = [x-y for x,y in points]

        i,j = -1,-1 
        issum = False 
        n = len(points)
        mxsum,mnsum = max(sums),min(sums) 
        mxdiff,mndiff = max(diffs),min(diffs)
        if mxsum-mnsum>mxdiff-mndiff:
            # find i,j     
            isum = True 
            for k in range(n):
                if sums[k]==mxsum: i = k 
                if sums[k]==mnsum: j = k 
        else:
            for k in range(n):
                if diffs[k]==mxdiff: i=k
                if diffs[k]==mndiff: j=k
        print(f'i={i},j={j}')
        # calculate if removing i
        ret = max(mxsum-mnsum, mxdiff-mndiff)        
        mxsum = max(x for k,x in enumerate(sums) if k!=i)
        mnsum = min(x for k,x in enumerate(sums) if k!=i)
        mxdiff = max(x for k,x in enumerate(diffs) if k!=i)
        mndiff = min(x for k,x in enumerate(diffs) if k!=i)
        ret = min(ret, max(mxsum-mnsum, mxdiff-mndiff))
        
        mnsum = min(x for k,x in enumerate(sums) if k!=j)
        mxsum = max(x for k,x in enumerate(sums) if k!=j)
        mndiff = min(x for k,x in enumerate(diffs) if k!=j)
        mxdiff = max(x for k,x in enumerate(diffs) if k!=j)
        ret = min(ret, max(mxsum-mnsum, mxdiff-mndiff))

        return ret 
