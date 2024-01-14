class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def checkok(mid):
            # check if mid st all price(num)
            # ithcol 2^(i-1) rows are 1 
            ret = 0
            totalcols = ceil(log(mid+1,2))
            for i in range(totalcols):
                j = i + 1
                # col: j, grpsize:2^j, # of 1 in grp: 2^(j-1)
                if j%x==0:
                    q, r = divmod(mid+1, (pow(2, j)))
                    ret += q*pow(2,j-1) 
                    ret += max(0, r-pow(2,j-1))
            return ret 
        left,right = 1, 10**15+1
        while left<right:
            mid = right-(right-left)//2
            if checkok(mid)<=k:
                left = mid
            else:
                right = mid-1
        return left
        