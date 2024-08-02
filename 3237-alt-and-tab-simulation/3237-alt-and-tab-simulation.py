class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        Map1 = {val:i for i,val in enumerate(windows)}
        Map2 = {i:val for i,val in enumerate(windows)}

        idx = -1
        for v in queries:  
            i = Map1[v]          
            del Map1[v]
            Map1[v] = idx

            del Map2[i]
            Map2[idx] = v

            idx -= 1
            
        n = len(windows)
        ret = []
        poslst = sorted(Map1.values())

        for idx in poslst:
            ret.append(Map2[idx])
        
        return ret
            



