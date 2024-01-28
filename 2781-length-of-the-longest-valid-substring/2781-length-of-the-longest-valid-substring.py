from sortedcontainers import SortedDict
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int: 
        fset = set()
        def slide(word,length,Map):
            n = len(word)
            code = 0
            for i,ch in enumerate(word):
                if i>=length:
                    code &= (1<<(5*(length-1)))-1 # 0000011....1 
                code = (code<<5) + ord(ch)-ord('a')+1
                if i>=length-1:
                    if code in fset:
                        if i-length+1 not in Map:
                            Map[i-length+1] = []
                        Map[i-length+1].append(i)            
        
        for fword in forbidden:
            # get its code and stored set 
            code = 0
            for ch in fword:
                code <<=5
                code += ord(ch)-ord('a')+1
            fset.add(code)
        # scan word to check (i,i+l) is in fset
        Map = SortedDict()
        for l in range(1,11):
            slide(word,l,Map)
        
        # <---
        n = len(word)
        ret = 0
        rightBound = n
        for i in range(n-1,-1,-1):
            if i in Map:
                for j in Map[i]:
                    rightBound = min(rightBound, j)
            ret = max(ret, rightBound-i)
        return ret