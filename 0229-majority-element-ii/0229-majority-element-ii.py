class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1,c2 = 0,0
        x1,x2 = None, None
        for x in nums:
            if x1 == x:
                c1 += 1
            elif x2 == x:
                c2 += 1
            elif c1 == 0:
                c1 = 1
                x1 = x
            elif c2 == 0:
                c2 = 1
                x2 = x
            else:
                c1 -= 1
                c2 -= 1
        ret = []
        if nums.count(x1) > n//3:
            ret.append(x1)
        if nums.count(x2) > n//3:
            ret.append(x2)
        return ret
            

