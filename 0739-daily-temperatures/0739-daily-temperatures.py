class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        nextHigher = [n]*n
        stack = []
        for i in range(n):
            while stack and T[stack[-1]]<T[i]:
                top = stack.pop()
                nextHigher[top] = i
            stack.append(i)
        print(nextHigher)
        ret = [0]*n
        for i in range(n):
            if nextHigher[i]<n:
                ret[i] = nextHigher[i]-i
        return ret