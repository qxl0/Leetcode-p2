class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        t = 0
        n = 1
        while n < k:
            n *= 2
            t += 1
        # when done, n >= k, 
        shift = 0
        def helper(cur, k, n):
            nonlocal shift
            if cur < 0:
                return
            if k > n//2:
                if operations[cur] == 0:
                    k -= n//2
                else:
                    k -= n//2
                    shift += 1
            helper(cur-1, k, n//2)
        if t > 0:
            helper(t-1, k, n)
        return chr(ord('a') + shift%26)
