class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        j = 0
        ans = 0
        for i,ch in enumerate(s):
            window[ch] += 1
            while i-j+1 - max(window.values()) > k:
                window[s[j]] -= 1
                j += 1

            ans = max(ans, i-j+1)
        return ans

