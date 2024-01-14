class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n,len_a,len_b = len(s),len(a),len(b)
        aidx = []        
        for i in range(n-len_a+1):
            if a == s[i:i+len_a]:
                aidx.append(i)
        bidx = []        
        for i in range(n-len_b+1):
            if b == s[i:i+len_b]:
                bidx.append(i)
        res = set()
        if len(aidx) == 0 or len(bidx)==0: return []
        bi = 0
        for idx in aidx:
            if idx > bidx[bi]:
                if idx-bidx[bi]<=k:
                    res.add(idx)
                    continue
                # increase bi
                while bi<len(bidx) and idx-bidx[bi]>k:
                    bi += 1
                # when stop 
                if bi==len(bidx): 
                    return res 
                if abs(idx-bidx[bi])<=k: # now bidx[bi]>idx, maybe too large 
                    res.add(idx)
            else: # idx < bidex[bi]
                if bidx[bi]-idx<=k:
                    res.add(idx)                    
                # wait for idx 
        return sorted(list(res))
            
                
        