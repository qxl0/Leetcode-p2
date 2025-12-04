class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)
        n = len(s)
        if min(count.values())>=k:
            return n
        if max(count.values())<k:
            return 0
        ret = 0
        for i in range(n):
            if count[s[i]]<k:
                continue
            j = i
            while j<n and count[s[j]]>=k:
                j += 1
            ret = max(ret, self.longestSubstring(s[i:j],k))
        return ret