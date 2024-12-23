class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl,pl = list(s),list(p)
        def isMatch(lst, pst, i, j):
            # return True if lst[i..] matches pst[j..]
            if i>=len(sl):
                if j>=len(pl):
                    return True
                else:
                    return j+1<len(pl) and pl[j+1]=='*' and isMatch(sl,pl,i,j+2)
            elif j>=len(pl):
                return False
            else: # i,j, both left 
                if j+1==len(pl) or pl[j+1]!='*':
                    return (sl[i]==pl[j] or pl[j]=='.') and isMatch(sl,pl,i+1,j+1)
                else:
                    ret1 = (sl[i]==pl[j] or pl[j]=='.') and isMatch(sl,pl,i+1,j)
                    ret2 = isMatch(sl,pl,i,j+2)
                    return ret1 or ret2                    
        return isMatch(sl,pl,0,0)