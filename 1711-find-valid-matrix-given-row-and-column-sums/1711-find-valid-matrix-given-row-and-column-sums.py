class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum),len(colSum)
        ans = [[0]*n for _ in range(m)]

        for i in range(m):
            ans[i][0] = rowSum[i]
        colsum = sum(rowSum)
        for j in range(n):  
            newcolsum = 0          
            if colsum>colSum[j]:
                # -> j+1
                i = 0
                while i<m and colsum-rowSum[i]>colSum[j]:
                    colsum -= rowSum[i]
                    ans[i][j] = 0
                    ans[i][j+1] = rowSum[i]
                    newcolsum += ans[i][j+1]
                    i += 1
                # now, colsum - rowSum[i] <= colSum[j]
                if j+1<n:                  
                    ans[i][j+1] += colsum - colSum[j]
                    newcolsum += colsum - colSum[j]
                ans[i][j] -= colsum - colSum[j]
            colsum = newcolsum
        return ans
