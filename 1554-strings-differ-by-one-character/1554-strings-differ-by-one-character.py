class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        base = 26
        n = len(dict)
        hset = []
        for word in dict:
            h = 0
            for ch in word:
                h = h*base+ord(ch)-ord('a')
            hset.append(h)
        # 
        m = len(dict[0])
        power = 1
        for j in range(m-1,-1,-1):
            # process 
            Map = set()
            for i in range(n):
                newhash = hset[i] - (ord(dict[i][j])-ord('a'))*(power)
                if newhash in Map:
                    return True
                Map.add(newhash)
            power *= base
        return False