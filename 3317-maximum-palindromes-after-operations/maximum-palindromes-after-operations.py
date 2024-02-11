class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:        
        counter = Counter()
        for word in words:            
            counter.update(word)
        total = sum(freq//2 for _,freq in counter.items())
        # now 
        ret = 0
        n = len(words)
        for word in sorted(words, key=lambda x: len(x)):
            m = len(word)//2
            if total>=m:
                total -= m
                ret += 1
        return ret 
