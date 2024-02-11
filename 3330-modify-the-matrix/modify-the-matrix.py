class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        ans = [[0]*n for _ in range(m)]

        colmax = [max(col) for col in zip(*matrix)]
        # print(colmax)
        for i in range(m):
            for j in range(n):
                ans[i][j] = matrix[i][j] if matrix[i][j]!=-1 else colmax[j]
        
        return ans