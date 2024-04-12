class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        n = len(height)
        stack = []
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                top = stack.pop()
                if stack:
                    H = max(0,min(height[stack[-1]], height[i]) - height[top])
                    W = i-stack[-1]-1
                    ret += H*W    
            stack.append(i)  
        return ret  
