class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        S = Counter()
        n = len(s)
        j = 0
        ans = s+"#"
        for i in range(n):            
            S[s[i]] += 1
            while j <n and S >= T:
                if len(ans)>len(s[j:i+1]):
                    ans = s[j:i+1]
                S[s[j]] -= 1
                if S[s[j]] == 0:
                    del S[s[j]]
                j += 1
        return ans if len(ans)<n+1 else ""