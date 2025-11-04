class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        temp = [0]*(n+1)
        ret = 0
        for i in range(m):
            # get histogram
            for j in range(n):
                if matrix[i][j] == '0':
                    temp[j] = 0
                else:
                    temp[j] += 1
            # solve largiest rectangle problem
            # print(f'i={i}, temp={temp}')
            stack = []
            for k in range(n+1):
                while stack and temp[stack[-1]] >= temp[k]:
                    top = stack.pop()
                    ret = max(ret, temp[top]*(k-(stack[-1] if stack else -1)-1))
                    # print(f'i={i} => k={k}, top={top}, area={temp[top]*(k-(stack[-1] if stack else -1)-1)}')
                stack.append(k)
        return ret
