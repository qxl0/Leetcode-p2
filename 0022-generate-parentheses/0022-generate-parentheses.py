class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(l,r,path): # count = # of left - # of right
            if l==r==n:
                ret.append(path)
                return
            if l<n:
                dfs(l+1,r, path+'(')
            if l>r:
                dfs(l,r+1, path+ ')')
        dfs(0,0, '')
        return ret