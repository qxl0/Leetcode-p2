class Solution:
    def generateTag(self, caption: str) -> str:
        def removenonalpha(x):
            ret = ''
            for char in x:
                if char.isalpha():
                    ret += char
            return ret
        lst = list(filter(lambda x: len(x)>0, caption.split(" ")))
        # print(lst)
        if len(lst)<=0:
            return '#'
        res = ['#', lst[0].lower()]
        l = 1+len(lst[0])
        for w in lst[1:]:
            if l>=100:
                break
            # 
            w = removenonalpha(w)
            tmp = w[0].upper() + (w[1:].lower() if len(w)>1 else '')
            res.append(tmp)
            l += len(tmp)
        ret = "".join(res)
        if len(ret) > 100:
            ret = ret[:100]
        return ret



        
            