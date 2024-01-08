class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def diag(x,y):
            return x*x+y*y
        ret = 0
        longestdiag = 0
        for x,y in dimensions:
            d = diag(x,y)
            if longestdiag < d:
                longestdiag = d
                ret = x*y
            elif longestdiag == d:
                ret = max(ret, x*y)
        return ret 