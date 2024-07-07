class Solution:
    def validStrings(self, n: int) -> List[str]:
        ret = []
        def dfs(i,cur):
            if i==n:
                ret.append(cur)
                return 
            
            dfs(i+1, cur+'1')
            if not cur or cur[-1]=='1':
                dfs(i+1,cur+'0')
            
                
        dfs(0,'')
        return ret 