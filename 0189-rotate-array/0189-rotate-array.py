class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        cnt = 0
        start = 0
        while cnt < n:          
            current = start
            current_val = nums[current]

            while (True):
                next = (current+k)%n
                temp = nums[next]

                nums[next] = current_val
                cnt += 1

                current = next
                current_val = temp

                if current == start: 
                    break
            start += 1


            

