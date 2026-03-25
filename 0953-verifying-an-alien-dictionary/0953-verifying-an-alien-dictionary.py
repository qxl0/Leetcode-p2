class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        Order = {c:i for i,c in enumerate(order)}
        def lessthan(w1,w2):
            i,j=0,0
            while i<len(w1) and j<len(w2):
                if Order[w1[i]]>Order[w2[j]]:
                    return False
                elif Order[w1[i]]<Order[w2[j]]:
                    return True
                else:
                    i += 1
                    j += 1
            if i<len(w1):
                return False
            return True

        for w1,w2 in zip(words, words[1:]):
            if not lessthan(w1,w2):
                return False
        return True