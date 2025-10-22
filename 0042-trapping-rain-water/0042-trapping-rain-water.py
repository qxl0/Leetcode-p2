class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        ans = 0
        l, r = 0, n-1
        max_l, max_r = h[l], h[r]
        while l<r:
            if max_l < max_r:
                ans += max_l-h[l]
                max_l = max(max_l, h[l+1])
                l += 1
            else:
                ans += max_r-h[r]
                max_r = max(max_r, h[r-1])
                r -= 1
        return ans