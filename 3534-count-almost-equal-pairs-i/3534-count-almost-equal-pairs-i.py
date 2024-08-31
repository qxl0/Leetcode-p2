class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def almostequal(x,y):
            if x==y: return True
            xstr,ystr=str(x),str(y)
            m,n = len(xstr),len(ystr)
            if m>=n:
                ystr = ystr.zfill(m)
                countx = Counter(xstr)
                county = Counter(ystr)
            else:
                return almostequal(y, x)
            if countx!=county:
                return False
            diff=0
            for i in range(m):
                if xstr[i]!=ystr[i]:
                    diff += 1
            return diff<=2

        ret = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if almostequal(nums[i],nums[j]):
                    ret += 1
                    print(f'{nums[i]}, {nums[j]}')
        return ret 