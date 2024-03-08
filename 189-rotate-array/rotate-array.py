class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        start = 0
        while count<n:
            cur,cur_v = start, nums[start]
            while True:
                nxt = (cur+k)%n
                tmp = nums[nxt]
                nums[nxt] = cur_v
                count += 1
                cur,cur_v = nxt,tmp
                if (cur==start):
                    break
            start += 1

                
