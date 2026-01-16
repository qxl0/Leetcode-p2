class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isparlindrome(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True
        ans = []
        def dfs(i,path):
            if i>=n:
                ans.append(path.copy())
                return
            for j in range(i,n):
                if isparlindrome(s,i,j):
                    dfs(j+1, path+[s[i:j+1]])
        dfs(0,[])
        return ans 