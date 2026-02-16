class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        def getTotal(s):
            count = 0
            tobeRemoved = 0
            for i in range(n):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    if count > 0:
                        count -= 1
                    else:
                        tobeRemoved += 1
                        count = 0
            # at the end count should be 0
            tobeRemoved += count
            return tobeRemoved
        totalLen = n - getTotal(s)
        ans = []
        def dfs(cur, path, count):
            if count < 0 or len(path)>totalLen:
                return
            if cur >= n:
                if len(path)==totalLen and count == 0:
                    ans.append(path)            
                return
            # remove or not remove
            ch = s[cur]
            if ch == '(':
                newcount = count + 1
            elif ch == ')':
                newcount = count - 1
            else:
                newcount = count
            dfs(cur+1, path + ch , newcount)
            # remove
            if ch == '(' or ch == ')':
                if len(path)==0 or ch != path[-1]:
                    dfs(cur+1, path, count)
        dfs(0,'',0)
        return ans
            
