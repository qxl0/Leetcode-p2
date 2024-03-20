class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        """
        x x x x x x x x x x , k, maxChanges=3
                
        """        
        # [0, 1, 5, 6, 9]  k=3 maxChanges=1 
        numstr = "".join(map(str, nums))
        if "111" in numstr:
            maxC = 3 
        elif "11" in numstr:
            maxC = 2
        elif "1" in numstr:
            maxC = 1
        else:
            maxC = 0
        
        if maxC>k: maxC = k 
        if maxChanges>=k-maxC:
            return max(0,maxC-1) + 2*(k-maxC) 
        
        k -= maxChanges
        res = maxChanges*2 

        A = [i for i in range(len(nums)) if nums[i]==1]
        mid = k//2
        left = 0
        cur = mn = sum(abs(i-A[mid]) for i in A[:k])
        for right in range(k, len(A)):
            # use O(1) to calculate cur when mid -> mid+1 by
            # [left+1, ... mid, mid+1, ... right]
            cur -= A[mid]-A[left]
            left += 1
            cur += A[right]-A[mid+1]
            cur += ((mid+1-left)-(right-(mid+1)))*(A[mid+1]-A[mid])
            mn = min(mn, cur)
            mid +=1 
        return res+mn
        

        