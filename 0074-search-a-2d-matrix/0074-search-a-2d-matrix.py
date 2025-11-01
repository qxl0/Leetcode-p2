class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        m,n = len(A), len(A[0])
        l,r = 0, m*n-1
        while l<r:
            mid=l+(r-l)//2
            i,j = mid//n, mid%n
            if A[i][j] == target:
                return True
            elif A[i][j]<target:
                l = mid+1
            else:
                r = mid-1
        if A[l//n][l%n]==target:
            return True
        else:
            return False