class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        K4(ON(MgH3)2)2F  
        """
        def fill(ans,nam,tmp,cnt):
            cnt = 1 if cnt==0 else cnt
            if len(nam)>0:                        
                ans[nam] += cnt
            else:
                for t in tmp.keys():
                    ans[t] += tmp[t]*cnt
        where = 0
        n = len(formula)
        
        def f(i):
            nonlocal where
            ans = defaultdict(int)
            tmp = defaultdict(int)
            cnt = 0
            nam = ''
            while i < n and formula[i]!=')': 
                if formula[i].isupper() or formula[i] == '(':
                    fill(ans,nam,tmp,cnt)
                    # set 
                    nam = ''
                    cnt = 0
                    tmp.clear()
                    if formula[i].isupper():
                        nam += formula[i]
                        i += 1
                    else:
                        tmp = f(i+1)
                        i = where + 1
                elif formula[i].islower():
                    nam += formula[i]
                    i += 1
                else:
                    cnt = cnt*10+ ord(formula[i])-ord('0')
                    i += 1
            fill(ans,nam,tmp,cnt)
            where = i
            return ans
        res = f(0)        
        output = []
        for k in sorted(res.keys()):
            output.append(k)
            if res[k]>1:
                output.append(str(res[k]))
        return ''.join(output)


            