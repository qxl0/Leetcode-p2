class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        ret = 0
        for _,freq in count.items():
            if freq<3:
                ret += freq
            else:
                ret += 1 if freq%2==1 else 2
        return ret