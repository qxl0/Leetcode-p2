# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        n = len(pattern)
        def process(pattern):
            n = len(pattern)
            lps = [0]*n
            for i in range(1,n):
                j = lps[i-1]
                while j>0 and pattern[i]!=pattern[j]:
                    j = lps[j-1]
                lps[i] = j + (pattern[i]==pattern[j])
            return lps
        lps = process(pattern)

        i,j = 0,0
        cur = stream.next()
        while i<n:
            if cur == pattern[i]:
                i += 1
                cur = stream.next()
                j += 1
            else:
                if i==0:
                    cur = stream.next()
                    j += 1
                else:
                    i = lps[i-1]
            if i==n:return j-n
        return 0

