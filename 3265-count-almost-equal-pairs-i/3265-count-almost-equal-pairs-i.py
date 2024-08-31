class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def almostequal(x,y):
            if x==y: return True
            m,n = len(str(x)),len(str(y))
            if m<n:
                return almostequal(y, x)
            # m > n
            xl = list(str(x))
            for i in range(m):
                for j in range(i+1,m):
                    xl[i],xl[j]=xl[j],xl[i]
                    if int(''.join(xl))==y:
                        return True
                    xl[i],xl[j]=xl[j],xl[i]
            return False


        ret = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if almostequal(nums[i],nums[j]):
                    ret += 1
                    print(f'{nums[i]}, {nums[j]}')
        return ret 