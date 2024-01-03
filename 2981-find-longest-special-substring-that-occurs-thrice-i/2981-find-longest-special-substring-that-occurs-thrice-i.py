class Solution:
    def maximumLength(self, s: str) -> int:
        def hassinglechar(ss):
            count = Counter(ss)
            return len(count)==1
        n =len(s)
        count = Counter()
        for i in range(n):            
            for j in range(i,n):
                count[s[i:j+1]]+=1
        lst = count.most_common()
        ret = -1
        for ss,freq in lst:
            if not hassinglechar(ss): continue
            if freq>=3:
                ret = max(ret, len(ss))
                # print(f'ss={ss},freq={freq}')
        return ret 
                
                
                
                
                
        
        