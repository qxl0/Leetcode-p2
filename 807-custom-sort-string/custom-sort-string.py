class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []
        for ch in order:
            if ch in count:
                ans.append(ch*count[ch])
                del count[ch]
        for ch in count:
            ans.append(ch*count[ch])
        return "".join(ans)