class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD=10**9+7
        if multiplier==1:
            return nums
            
        arr = [(x,i) for i,x in enumerate((nums))]
        # sorted 
        heapify(arr)

        mx = max(nums)

        while k and arr[0][0]*multiplier<=mx:
            k -= 1
            x,i = heappop(arr)
            nums[i] = x*multiplier
            heappush(arr, (nums[i],i))
        times = k//len(nums)
        rem = k%len(nums)

        res = [0]*len(nums)

        first = pow(multiplier, times, MOD)
        second = pow(multiplier, times+1, MOD)

        while arr:
            x,i = heappop(arr)

            val = second if rem > 0 else first
            rem -= 1
            val *= x
            val %= MOD

            res[i] = val
        
        return res


        
        return nums