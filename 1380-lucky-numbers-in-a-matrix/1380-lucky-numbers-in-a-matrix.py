class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        def islucky(i,j):
            # min -> i, max in j
            for k in range(n):
                if k==j: continue 
                if matrix[i][k]<matrix[i][j]:
                    return False 
            for k in range(m):
                if k==i: continue
                if matrix[k][j]>matrix[i][j]:
                    return False 
            return True 
        return [matrix[i][j] for i in range(m) for j in range(n) if islucky(i,j)]