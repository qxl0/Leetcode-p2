class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        where = 0
        def f(i):
            nonlocal where
            ans = defaultdict(int)
            nam = ''
            cnt = 0
            pre = defaultdict(int)

            while i<n and formula[i]!=')':
                if formula[i].isupper() or formula[i]=='(':
                    fill(ans, nam,pre,cnt)
                    nam = ''
                    pre.clear()
                    cnt = 0
                    if formula[i].isupper():
                        nam += formula[i]
                        i += 1
                    else:
                        pre = f(i+1)
                        i = where + 1
                elif formula[i].isdigit():
                    cnt = cnt*10 + ord(formula[i])-ord('0')
                    i += 1
                else:
                    nam += formula[i]
                    i += 1
            fill(ans, nam, pre, cnt)
            where = i
            return ans
        def fill(ans, nam, tmp, cnt):
            cnt = 1 if cnt == 0 else cnt
            if len(nam)>0:
                ans[nam] += cnt
            elif len(tmp)>0:
                for k in tmp.keys():
                    ans[k] = ans[k] + tmp[k]*cnt
        ans = f(0)
        ret = ''
        for k in sorted(ans.keys()):
            ret += k 
            if ans[k]>1:
                ret += str(ans[k])
        return ret


                