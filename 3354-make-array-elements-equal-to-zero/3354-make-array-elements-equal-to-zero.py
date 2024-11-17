class Solution:
    def countValidSelections(self, nums: List[int]) -> int:        
        n = len(nums)
        def isvalid(arr, start,dir):
            # simulate 
            cur = start 
            while cur>=0 and cur<n:
                if dir=='left':
                    while cur>=0 and cur<n and arr[cur]==0:
                        cur -= 1
                else:
                    while cur<n and cur>=0 and arr[cur]==0:
                        cur += 1
                # when stop, nums[cur]!=0
                if cur<0 or cur>=n:
                    if sum(arr)==0:
                        return 1
                    return 0
                arr[cur]-=1
                dir = 'right' if dir=='left' else 'left'
                cur = cur + 1 if dir == 'right' else cur -1 
            return 0
        def valid(arr, start):
            # return 0, 1, 2     
            arr = nums.copy()       
            ret = isvalid(arr, start,'left')
            arr = nums.copy()
            ret += isvalid(arr, start,'right')
            return ret
        pos = [i for i in range(n) if nums[i]==0]
        ret = 0
        for start in pos:            
            ret += valid(nums, start)
        return ret