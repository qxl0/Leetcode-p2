class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            cur = a
            while stack and stack[-1]>0 and cur<0:
                top = stack.pop()
                if abs(top)>abs(cur):
                    cur = top
                elif abs(top)==abs(cur):
                    cur = 0
            if cur:
                stack.append(cur)
        return stack