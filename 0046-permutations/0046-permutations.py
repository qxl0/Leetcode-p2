class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        def dfs(arr):
            if len(arr)==1:
                return [[arr[0]]]
            ret = []
            for i in range(len(arr)):
                x = arr[i]
                for perm in dfs(arr[:i]+arr[i+1:]):
                    ret.append(perm+[x])
                # print(f'i={i},x={x}, ret={ret}')
            return ret
        return dfs(nums)
        
# 1,2,3 ->
# loop through nums:
# iteration 1, 1 -> [2,3], -> append 1 to the results
#           2, 2 -> [1,3], -> append 2 to the results
#           3, 