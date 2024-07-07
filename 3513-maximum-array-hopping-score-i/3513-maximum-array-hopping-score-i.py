class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ret,mx=0,0
        for x in nums[:0:-1]:
            if x>mx:
                mx = x 
            ret += mx
            print(f'x={x},mx={mx}, ret={ret}')
        return ret
