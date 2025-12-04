class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s,m,k):
            # longest substring m different chars 
            Map = defaultdict(int)
            j = 0
            ret = 0
            count = 0
            for i in range(len(s)):
                while j<len(s) and len(Map)<=m:
                    Map[s[j]]+=1
                    if Map[s[j]]==k:
                        count += 1
                    j += 1
                    if len(Map)==m and count==m:
                        ret = max(ret, j-i)
                Map[s[i]] -= 1
                if Map[s[i]]==k-1:
                    count -= 1
                if Map[s[i]]==0:
                    del Map[s[i]]
            return ret
        ret = 0
        for m in range(1,27):
            ret = max(ret, helper(s,m,k))
        return ret
