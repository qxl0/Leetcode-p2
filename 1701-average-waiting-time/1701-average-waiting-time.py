class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:        
        n = len(customers)        
        ret = customers[0][1]
        cur = customers[0][0]+customers[0][1]
        for b,w in customers[1:]:
            cur = max(b, cur) + w
            ret += cur-b
        return ret/n
