class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        if n<3: 
            return n
        Map = defaultdict(list)
        
        for i in range(n):
            Map[s[i]].append(i)
        # a: 0,2,3
        ret = 0
        for c,lst in Map.items():
            if len(lst)>=3:
                ret += (1 if len(lst)%2 ==1 else 2 )
            else:
                ret += len(lst)
        return ret