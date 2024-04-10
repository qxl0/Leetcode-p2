class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        def minusone(nums):
            return [x-1 for x in nums]
        ret = 0
        while tickets[k]>0:
            if tickets[k]>1:
                ret +=sum(1 for x in tickets if x>0)
            else:
                ret += sum(1 for x in tickets[:k+1] if x>0)
            tickets = minusone(tickets)
            print(f'ret={ret}, {tickets}')
        return ret 

