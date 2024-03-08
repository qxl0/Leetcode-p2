class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                
        n = len(nums)
        k %= n
        
        start,count = 0,0
        while count<n:
            current,prev = start,nums[start]
            
            while True:
                next = (current+k)%n
                tmp = nums[next]
                nums[next] = prev 
                prev = tmp
                current = next 
                count += 1
                if start==current:
                    break

            start += 1
        